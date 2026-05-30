"""compute_stats.py — точные статистики факторного эксперимента (44 прогона, 9 стендов).

Цель:
  1. Распарсить 44 markdown-файла с результатами тестовых прогонов.
  2. Сагрегировать в DataFrame stand × run × task → (Pass@1, Completeness, Время, Статус).
  3. Вычислить:
     - Pass@1 mean ± Wilson 95% CI для каждого стенда.
     - Completeness mean.
     - TimeToSuccess (mean по успешным прогонам).
     - p-значения по 5 гипотезам (Wilcoxon signed-rank).
     - Cohen's d по формуле для пропорций (Cohen 1988): d = 2·arcsin(√p1) − 2·arcsin(√p0).
     - Cohen's d на каждом шаге waterfall ablation.
  4. Сохранить:
     - JSON: multiagent/tools/stats_output.json
     - Markdown: multiagent/tools/stats_report.md
"""
from __future__ import annotations

import json
import math
import os
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import numpy as np
import pandas as pd
from scipy import stats as scstats

# --- Конфигурация ----------------------------------------------------------

# Пути определяются относительно расположения скрипта (docs/technical/),
# без привязки к абсолютному пути конкретной машины.
DOCS_ROOT = Path(__file__).resolve().parents[1]          # .../docs
DATA_DIR = DOCS_ROOT / "experiment" / "test_results"
OUT_DIR = Path(__file__).resolve().parent                # docs/technical
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Базовые таблицы (§1–4) пишутся в *.generated.* — итоговые stats_report.md и
# stats_output.json дополнены вручную (робастность, ARR, стратификация) и не
# перезаписываются автоматическим прогоном.
JSON_OUT = OUT_DIR / "stats_output.generated.json"
MD_OUT = OUT_DIR / "stats_report.generated.md"

STAND_CONFIG = {
    "A": {"agent": "single", "rag": "3-shot", "graph": "off", "model": "Haiku 4.5"},
    "B": {"agent": "multi", "rag": "0-shot", "graph": "off", "model": "Haiku 4.5"},
    "C": {"agent": "multi", "rag": "3-shot", "graph": "off", "model": "Haiku 4.5"},
    "D": {"agent": "multi", "rag": "5-shot", "graph": "off", "model": "Haiku 4.5"},
    "E": {"agent": "multi", "rag": "5-shot", "graph": "on",  "model": "Haiku 4.5"},
    "F": {"agent": "multi", "rag": "3-shot", "graph": "off", "model": "Ollama 14b"},
    "G": {"agent": "multi", "rag": "0-shot", "graph": "on",  "model": "Haiku 4.5"},
    "H": {"agent": "multi", "rag": "0-shot", "graph": "on",  "model": "Ollama 14b"},
    "I": {"agent": "multi", "rag": "3-shot", "graph": "on",  "model": "Haiku 4.5"},
}

# --- Парсинг ---------------------------------------------------------------

TEST_HEADER_RE = re.compile(r"^## Тест (\d+)\.\s*(.*?)\s*$", re.MULTILINE)


def parse_completeness(value: str) -> Optional[float]:
    """Парсит '1/3 (33%)' → 1/3 = 0.3333."""
    m = re.search(r"(\d+)\s*/\s*(\d+)", value)
    if not m:
        return None
    num, den = int(m.group(1)), int(m.group(2))
    if den == 0:
        return None
    return num / den


def parse_int(value: str) -> Optional[int]:
    m = re.search(r"\d+", value)
    return int(m.group(0)) if m else None


def parse_test_block(block: str) -> Dict[str, Optional[float]]:
    """Парсит одиночный блок теста, возвращает dict с метриками."""
    out: Dict[str, Optional[float]] = {
        "task_id": None,
        "status": None,
        "pass1": None,
        "time_sec": None,
        "completeness": None,
    }

    def find_value(label: str) -> Optional[str]:
        # Строка вида "| <label> | <value> |"
        pattern = rf"\|\s*{re.escape(label)}\s*\|\s*([^|\n]+?)\s*\|"
        m = re.search(pattern, block)
        return m.group(1).strip() if m else None

    out["task_id"] = find_value("task_id")

    status_raw = find_value("Статус")
    out["status"] = status_raw

    pass_raw = find_value("Pass@1")
    if pass_raw is not None:
        out["pass1"] = parse_int(pass_raw)

    time_raw = find_value("Время")
    if time_raw is not None:
        # формат "330 сек"
        out["time_sec"] = parse_int(time_raw)

    comp_raw = find_value("Completeness")
    if comp_raw is not None:
        out["completeness"] = parse_completeness(comp_raw)

    return out


def parse_file(path: Path) -> List[Dict]:
    """Парсит один файл стенда → список dict per test."""
    text = path.read_text(encoding="utf-8")

    # Разрезаем по заголовкам тестов
    matches = list(TEST_HEADER_RE.finditer(text))
    rows: List[Dict] = []
    for i, m in enumerate(matches):
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        block = text[start:end]
        # Прерываем на строке "## Итоги прогона"
        cut = block.find("## Итоги прогона")
        if cut > 0:
            block = block[:cut]

        test_num = int(m.group(1))
        test_name = m.group(2).strip()
        data = parse_test_block(block)
        data["test_num"] = test_num
        data["test_name"] = test_name
        rows.append(data)
    return rows


def load_all_data() -> pd.DataFrame:
    files = sorted(DATA_DIR.glob("stand-*.md"))
    rows: List[Dict] = []
    for f in files:
        m = re.match(r"stand-([A-Z])-run-(\d+)\.md", f.name)
        if not m:
            continue
        stand, run = m.group(1), int(m.group(2))
        for r in parse_file(f):
            rows.append({
                "stand": stand,
                "run": run,
                **r,
            })
    df = pd.DataFrame(rows)
    return df


# --- Статистики ------------------------------------------------------------

def wilson_ci(successes: int, n: int, z: float = 1.96) -> Tuple[float, float, float]:
    """Wilson 95% CI для пропорции."""
    if n == 0:
        return (0.0, 0.0, 0.0)
    p = successes / n
    denom = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / denom
    half = (z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))) / denom
    return (p, centre - half, centre + half)


def bootstrap_arr_ci(df: pd.DataFrame, stand: str, n_boot: int = 10000,
                     seed: int = 42) -> Dict:
    """ARR = mean(b·c) и 95% bootstrap-ДИ по наблюдениям стенда.

    b — признак успешной сборки (pass1 ∈ {0,1}); c — Completeness прогона
    (доля ∈ [0,1]). Доверительный интервал получен percentile-bootstrap по
    наблюдениям стенда (по умолчанию 10 000 ресэмплов, RNG seed = 42).
    Метод корректнее интервала Уилсона: ARR — среднее произведения, а не
    биномиальная доля.
    """
    sub = df[df["stand"] == stand].dropna(subset=["pass1", "completeness"])
    bc = (sub["pass1"].astype(float) * sub["completeness"].astype(float)).to_numpy()
    n = len(bc)
    if n == 0:
        return {"stand": stand, "n": 0, "arr": None, "ci_low": None, "ci_high": None}
    rng = np.random.default_rng(seed)
    boots = np.empty(n_boot)
    for i in range(n_boot):
        boots[i] = rng.choice(bc, size=n, replace=True).mean()
    lo, hi = np.percentile(boots, [2.5, 97.5])
    return {
        "stand": stand,
        "n": int(n),
        "arr": float(bc.mean() * 100),
        "ci_low": float(lo * 100),
        "ci_high": float(hi * 100),
    }


def cohen_d_proportions(p1: float, p0: float) -> float:
    """d = 2·arcsin(√p1) − 2·arcsin(√p0). Cohen 1988."""
    return 2 * math.asin(math.sqrt(p1)) - 2 * math.asin(math.sqrt(p0))


def aggregate_per_task(df: pd.DataFrame, stand: str, metric: str) -> pd.Series:
    """Среднее по 5 (или 4) повторам для каждой из 15 задач — возвращает Series длиной 15."""
    sub = df[df["stand"] == stand]
    return sub.groupby("test_num")[metric].mean()


def wilcoxon_paired(x: pd.Series, y: pd.Series) -> Tuple[float, float, str]:
    """Возвращает (statistic, p_value, method_note).

    Если все разности нулевые — возвращаем p=1.0, statistic=0.
    """
    x_vals = x.values.astype(float)
    y_vals = y.values.astype(float)
    diff = y_vals - x_vals
    if np.allclose(diff, 0):
        return (0.0, 1.0, "all_zero_diffs")
    try:
        # zsplit лучше для тай-эффектов; pratt тоже допустимо
        res = scstats.wilcoxon(x_vals, y_vals, zero_method="wilcox", correction=False, alternative="two-sided", method="auto")
        return (float(res.statistic), float(res.pvalue), "scipy.wilcoxon(zero_method=wilcox)")
    except ValueError as exc:
        return (float("nan"), float("nan"), f"error: {exc}")


def stand_summary(df: pd.DataFrame, stand: str) -> Dict:
    """Сводка по стенду: метрики Pass@1, Wilson CI, Completeness, TimeToSuccess,
    σ Pass@1 (по 5 повторам, ddof=1) и FSR (доля наблюдений с pass1=1 ∧ completeness=0).

    Все метрики определены в notes/metrics_methodology.md.
    """
    sub = df[df["stand"] == stand]
    n_total = len(sub)
    pass_total = int(sub["pass1"].sum())
    p_mean, lo, hi = wilson_ci(pass_total, n_total)
    comp_mean = float(sub["completeness"].mean()) if n_total else None
    success_subset = sub[sub["pass1"] == 1]
    time_to_succ = float(success_subset["time_sec"].mean()) if len(success_subset) else None
    n_runs = sub["run"].nunique()
    n_tasks = sub["test_num"].nunique()
    # σ Pass@1 (per-run, ddof=1) — выборочное стандартное отклонение по 5 повторам.
    # Для каждого run i вычисляем долю успехов, затем std по 5 значениям.
    if n_runs > 1:
        per_run_pass = sub.groupby("run")["pass1"].mean()
        sigma_pass1 = float(per_run_pass.std(ddof=1))
    else:
        sigma_pass1 = float("nan")
    # FSR (False Success Rate) — строгое определение:
    # доля наблюдений, где pass1=1 (build OK) И completeness=0 (ни один файл из F_required не изменён).
    # Семантика: «формальный успех при полном промахе по адресации».
    if n_total > 0:
        false_success_strict = sub[(sub["pass1"] == 1) & (sub["completeness"] == 0)]
        fsr = len(false_success_strict) / n_total
    else:
        fsr = float("nan")
    return {
        "stand": stand,
        "n_observations": n_total,
        "n_runs": int(n_runs),
        "n_tasks": int(n_tasks),
        "pass1_count": pass_total,
        "pass1_mean": p_mean,
        "wilson_ci_low": lo,
        "wilson_ci_high": hi,
        "completeness_mean": comp_mean,
        "time_to_success_mean": time_to_succ,
        "sigma_pass1_per_run": sigma_pass1,
        "fsr": fsr,
    }


# --- Гипотезы --------------------------------------------------------------

def compute_hypothesis_pair(df: pd.DataFrame, stand_a: str, stand_b: str, metric: str = "pass1") -> Dict:
    """Сравнение пары стендов: aggregate per task → wilcoxon + Cohen's d."""
    x = aggregate_per_task(df, stand_a, metric)
    y = aggregate_per_task(df, stand_b, metric)
    common = x.index.intersection(y.index)
    x = x.loc[common]
    y = y.loc[common]
    stat, p, note = wilcoxon_paired(x, y)
    p_a = float(x.mean())
    p_b = float(y.mean())
    d = cohen_d_proportions(p_b, p_a)
    return {
        "from": stand_a,
        "to": stand_b,
        "metric": metric,
        "n_pairs": int(len(common)),
        "mean_from": p_a,
        "mean_to": p_b,
        "delta": p_b - p_a,
        "wilcoxon_statistic": stat,
        "p_value": p,
        "method": f"Wilcoxon paired on {len(common)} tasks (mean per task across runs); {note}",
        "cohens_d": d,
    }


def compute_h2b_interaction(df: pd.DataFrame) -> Dict:
    """H2b — интерактивный эффект RAG × Graph.

    Способ 1: G→E (multi+0shot+graph → multi+5shot+graph) — добавление RAG к graph-стенду.
    Это «RAG в условиях graph».
    Способ 2: контраст разностей: (E-G) − (D-B). Если он положительный и значимый — есть синергия.
    Возвращаем оба, основной отчёт строится по контрасту разностей.
    """
    # G→E (RAG в graph)
    pair_GE = compute_hypothesis_pair(df, "G", "E", "pass1")
    # B→D (RAG без graph)
    pair_BD = compute_hypothesis_pair(df, "B", "D", "pass1")
    # Контраст: per-task ΔRAG_with_graph − ΔRAG_without_graph
    e = aggregate_per_task(df, "E", "pass1")
    g = aggregate_per_task(df, "G", "pass1")
    d_ = aggregate_per_task(df, "D", "pass1")
    b = aggregate_per_task(df, "B", "pass1")
    common = e.index.intersection(g.index).intersection(d_.index).intersection(b.index)
    contrast = (e.loc[common] - g.loc[common]) - (d_.loc[common] - b.loc[common])
    # one-sample wilcoxon контраста против нуля
    if np.allclose(contrast.values, 0):
        stat, p, note = 0.0, 1.0, "all_zero_diffs"
    else:
        try:
            res = scstats.wilcoxon(contrast.values, zero_method="wilcox", correction=False, alternative="two-sided", method="auto")
            stat, p, note = float(res.statistic), float(res.pvalue), "scipy.wilcoxon(one-sample on contrast)"
        except ValueError as exc:
            stat, p, note = float("nan"), float("nan"), f"error: {exc}"
    contrast_mean = float(contrast.mean())
    # Cohen's d по эффекту контраста: используем стандартный одновыборочный d=mean/std
    if contrast.std(ddof=1) > 0:
        d_one_sample = contrast_mean / contrast.std(ddof=1)
    else:
        d_one_sample = float("nan")
    # Дополнительно — d_h по пропорциям для метода 1 (G→E)
    return {
        "approach": "Contrast of differences: (E-G) - (D-B), one-sample Wilcoxon",
        "n_pairs": int(len(common)),
        "contrast_mean": contrast_mean,
        "wilcoxon_statistic": stat,
        "p_value": p,
        "method": note,
        "cohens_d_one_sample": d_one_sample,
        "supplementary_GE": pair_GE,
        "supplementary_BD": pair_BD,
    }


def compute_h3_avg(df: pd.DataFrame) -> Dict:
    """H3 — среднее по 3 парам B→G, C→I, D→E по Completeness."""
    pairs = [("B", "G"), ("C", "I"), ("D", "E")]
    rows = []
    deltas_per_task: List[pd.Series] = []
    for a, b in pairs:
        x = aggregate_per_task(df, a, "completeness")
        y = aggregate_per_task(df, b, "completeness")
        common = x.index.intersection(y.index)
        deltas_per_task.append(y.loc[common] - x.loc[common])
        rows.append({
            "from": a, "to": b,
            "mean_from": float(x.loc[common].mean()),
            "mean_to": float(y.loc[common].mean()),
            "delta": float((y.loc[common] - x.loc[common]).mean()),
        })
    # Объединяем все 45 разностей (3 пары × 15 задач) в одну выборку для wilcoxon
    combined = pd.concat(deltas_per_task, ignore_index=True)
    if np.allclose(combined.values, 0):
        stat, p, note = 0.0, 1.0, "all_zero_diffs"
    else:
        try:
            res = scstats.wilcoxon(combined.values, zero_method="wilcox", correction=False, alternative="two-sided", method="auto")
            stat, p, note = float(res.statistic), float(res.pvalue), "scipy.wilcoxon(one-sample on stacked deltas)"
        except ValueError as exc:
            stat, p, note = float("nan"), float("nan"), f"error: {exc}"
    avg_delta = float(combined.mean())
    # Cohen's d_h по средним пропорциям completeness (приближение): между средним «до» и «после»
    p_before = float(np.mean([r["mean_from"] for r in rows]))
    p_after = float(np.mean([r["mean_to"] for r in rows]))
    p_before_clamped = max(min(p_before, 1.0), 0.0)
    p_after_clamped = max(min(p_after, 1.0), 0.0)
    d_h = cohen_d_proportions(p_after_clamped, p_before_clamped)
    # Cohen's d_z по контрасту (one-sample): mean/std
    if combined.std(ddof=1) > 0:
        d_one_sample = float(combined.mean() / combined.std(ddof=1))
    else:
        d_one_sample = float("nan")
    return {
        "pairs": rows,
        "n_combined_deltas": int(len(combined)),
        "avg_delta": avg_delta,
        "wilcoxon_statistic": stat,
        "p_value": p,
        "method": note,
        "cohens_d_h_proportion": d_h,
        "cohens_d_z_one_sample": d_one_sample,
        "mean_completeness_before": p_before,
        "mean_completeness_after": p_after,
    }


def compute_h4_parity(df: pd.DataFrame) -> Dict:
    """H4 — паритет on-prem: Pass@1(H) / Pass@1(G).

    Stand H = 4 прогона × 15 задач (max). Для wilcoxon парим по задачам (mean per task).
    """
    h_summary = stand_summary(df, "H")
    g_summary = stand_summary(df, "G")
    p_h = h_summary["pass1_mean"]
    p_g = g_summary["pass1_mean"]
    parity = p_h / p_g if p_g > 0 else float("inf")
    pair = compute_hypothesis_pair(df, "G", "H", "pass1")
    return {
        "stand_H": h_summary,
        "stand_G": g_summary,
        "parity_ratio": parity,
        "delta_pp": (p_h - p_g) * 100,
        "wilcoxon_statistic": pair["wilcoxon_statistic"],
        "p_value": pair["p_value"],
        "cohens_d_h": pair["cohens_d"],
        "method": pair["method"],
    }


# --- Waterfall ablation ----------------------------------------------------

WATERFALL_STEPS = [
    ("A", "B", "+ multi (отказ от single-agent)"),
    ("B", "D", "+ RAG (5-shot к multi+0-shot)"),
    ("D", "E", "+ graph (к multi+RAG)"),
    ("B", "G", "+ graph (к multi+0-shot)"),
    ("G", "E", "+ RAG (к multi+graph)"),
]


def compute_waterfall(df: pd.DataFrame) -> List[Dict]:
    out: List[Dict] = []
    for a, b, label in WATERFALL_STEPS:
        pair = compute_hypothesis_pair(df, a, b, "pass1")
        pair["label"] = label
        out.append(pair)
    return out


# --- Сборка отчёта ---------------------------------------------------------

def fmt_p(p: float) -> str:
    if p is None or (isinstance(p, float) and (math.isnan(p) or math.isinf(p))):
        return "nan"
    if p < 0.0001:
        return f"p = {p:.4e}".replace("e-0", "×10⁻").replace("e-", "×10⁻")
    if p < 0.001:
        return f"p = {p:.5f}"
    return f"p = {p:.4f}"


def main() -> int:
    df = load_all_data()
    if df.empty:
        print("ERROR: no data parsed", file=sys.stderr)
        return 1

    # Убедимся, что все pass1/completeness/time_sec — числа
    df["pass1"] = pd.to_numeric(df["pass1"], errors="coerce")
    df["completeness"] = pd.to_numeric(df["completeness"], errors="coerce")
    df["time_sec"] = pd.to_numeric(df["time_sec"], errors="coerce")

    # 1. Сводка по стендам
    summaries = [stand_summary(df, s) for s in sorted(STAND_CONFIG.keys())]

    # 2. Гипотезы
    h1 = compute_hypothesis_pair(df, "A", "C", "pass1")
    h2a = compute_hypothesis_pair(df, "B", "D", "pass1")
    h2b = compute_h2b_interaction(df)
    h3 = compute_h3_avg(df)
    h4 = compute_h4_parity(df)

    waterfall = compute_waterfall(df)

    output = {
        "data_shape": list(df.shape),
        "n_files_parsed": int(df["stand"].count() / df["test_num"].nunique() if df["test_num"].nunique() else 0),
        "stands": summaries,
        "hypotheses": {
            "H1_multiagent_A_to_C": h1,
            "H2a_RAG_isolation_B_to_D": h2a,
            "H2b_RAG_x_Graph_interaction": h2b,
            "H3_graph_co_change_avg": h3,
            "H4_on_prem_parity": h4,
        },
        "waterfall_ablation": waterfall,
    }

    JSON_OUT.write_text(json.dumps(output, indent=2, ensure_ascii=False, default=str), encoding="utf-8")

    # Markdown report
    lines: List[str] = []
    lines.append("# Точные статистики факторного эксперимента\n")
    n_files = len(sorted(DATA_DIR.glob("stand-*.md")))
    lines.append(f"_Источник_: `docs/experiment/test_results/` — {n_files} файлов × 15 тестов (полная сетка 9 стендов × 5 повторов).\n")
    lines.append(f"_DataFrame shape_: {df.shape[0]} строк × {df.shape[1]} столбцов.\n\n")

    lines.append("## 1. Сводка по стендам\n")
    lines.append("| Стенд | Конфигурация | n | Pass@1 | Wilson 95% CI | Completeness | TimeToSuccess | σ Pass@1 (per-run, ddof=1) | FSR (pass1=1 ∧ comp=0) |\n")
    lines.append("|:-:|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|\n")
    for s in summaries:
        cfg = STAND_CONFIG[s["stand"]]
        cfg_str = f"{cfg['agent']} • {cfg['rag']} • graph={cfg['graph']} • {cfg['model']}"
        ci_str = f"[{s['wilson_ci_low']*100:.2f}%; {s['wilson_ci_high']*100:.2f}%]"
        comp = f"{s['completeness_mean']*100:.2f}%" if s["completeness_mean"] is not None else "—"
        tts = f"{s['time_to_success_mean']:.1f} с" if s["time_to_success_mean"] is not None else "—"
        sigma = f"{s['sigma_pass1_per_run']*100:.2f}%" if s.get("sigma_pass1_per_run") is not None and not (isinstance(s["sigma_pass1_per_run"], float) and math.isnan(s["sigma_pass1_per_run"])) else "—"
        fsr = f"{s['fsr']*100:.2f}%" if s.get("fsr") is not None and not (isinstance(s["fsr"], float) and math.isnan(s["fsr"])) else "—"
        lines.append(f"| {s['stand']} | {cfg_str} | {s['n_observations']} | {s['pass1_mean']*100:.2f}% | {ci_str} | {comp} | {tts} | {sigma} | {fsr} |\n")

    lines.append("\n## 2. Гипотезы\n")

    def hyp_row(name: str, h: Dict) -> str:
        delta_pp = h["delta"] * 100
        return f"| {name} | {h['mean_from']*100:.2f}% → {h['mean_to']*100:.2f}% | {delta_pp:+.2f} п.п. | {fmt_p(h['p_value'])} | d = {h['cohens_d']:.4f} |"

    lines.append("| Гипотеза | Pass@1 (от → к) | Δ | p-value (Wilcoxon) | Cohen's d_h |\n")
    lines.append("|---|:-:|:-:|:-:|:-:|\n")
    lines.append(hyp_row("H1 (A→C, multi)", h1) + "\n")
    lines.append(hyp_row("H2a (B→D, RAG)", h2a) + "\n")
    lines.append(f"| H2b (interaction (E−G)−(D−B)) | contrast = {h2b['contrast_mean']*100:+.2f} п.п. | — | {fmt_p(h2b['p_value'])} | d_z = {h2b['cohens_d_one_sample']:.4f} |\n")
    lines.append(f"| H3 (avg of B→G, C→I, D→E by Completeness) | {h3['mean_completeness_before']*100:.2f}% → {h3['mean_completeness_after']*100:.2f}% | {h3['avg_delta']*100:+.2f} п.п. | {fmt_p(h3['p_value'])} | d_h = {h3['cohens_d_h_proportion']:.4f}; d_z = {h3['cohens_d_z_one_sample']:.4f} |\n")
    lines.append(hyp_row("H4 (G→H, on-prem паритет)", {
        "delta": h4["delta_pp"]/100,
        "mean_from": h4["stand_G"]["pass1_mean"],
        "mean_to": h4["stand_H"]["pass1_mean"],
        "p_value": h4["p_value"],
        "cohens_d": h4["cohens_d_h"],
    }) + "\n")
    lines.append(f"\n_Паритет H/G по Pass@1_: {h4['parity_ratio']:.4f} ({h4['parity_ratio']*100:.2f}%).\n")

    lines.append("\n### Подробности по гипотезам\n")

    for name, hh in [("H1", h1), ("H2a", h2a)]:
        lines.append(f"\n**{name}:** Wilcoxon paired по {hh['n_pairs']} задачам (среднее по runs). statistic = {hh['wilcoxon_statistic']:.4f}, {fmt_p(hh['p_value'])}, d_h = {hh['cohens_d']:.4f}. Method: {hh['method']}.\n")
    lines.append(f"\n**H2b:** Контраст разностей `(E−G)−(D−B)` per task, one-sample Wilcoxon vs 0. n = {h2b['n_pairs']}, contrast mean = {h2b['contrast_mean']:.6f} ({h2b['contrast_mean']*100:+.2f} п.п.), statistic = {h2b['wilcoxon_statistic']:.4f}, {fmt_p(h2b['p_value'])}, d_z = {h2b['cohens_d_one_sample']:.4f}. Method: {h2b['method']}.\n")
    lines.append("\nВспомогательно для H2b:\n")
    lines.append(f"- G→E (добавление RAG к graph-стенду): {h2b['supplementary_GE']['mean_from']*100:.2f}% → {h2b['supplementary_GE']['mean_to']*100:.2f}% ({h2b['supplementary_GE']['delta']*100:+.2f} п.п.); {fmt_p(h2b['supplementary_GE']['p_value'])}; d_h = {h2b['supplementary_GE']['cohens_d']:.4f}.\n")
    lines.append(f"- B→D (добавление RAG без graph): {h2b['supplementary_BD']['mean_from']*100:.2f}% → {h2b['supplementary_BD']['mean_to']*100:.2f}% ({h2b['supplementary_BD']['delta']*100:+.2f} п.п.); {fmt_p(h2b['supplementary_BD']['p_value'])}; d_h = {h2b['supplementary_BD']['cohens_d']:.4f}.\n")

    lines.append(f"\n**H3:** среднее по 3 парам (B→G, C→I, D→E) по Completeness; стэк всех {h3['n_combined_deltas']} разностей, one-sample Wilcoxon vs 0. avg Δ = {h3['avg_delta']:.6f} ({h3['avg_delta']*100:+.2f} п.п.), statistic = {h3['wilcoxon_statistic']:.4f}, {fmt_p(h3['p_value'])}, d_h (по средним пропорциям) = {h3['cohens_d_h_proportion']:.4f}, d_z (one-sample) = {h3['cohens_d_z_one_sample']:.4f}.\n")
    for r in h3["pairs"]:
        lines.append(f"  - {r['from']}→{r['to']}: completeness {r['mean_from']*100:.2f}% → {r['mean_to']*100:.2f}% ({r['delta']*100:+.2f} п.п.).\n")

    lines.append(f"\n**H4:** Wilcoxon paired G ↔ H по 15 задачам. Pass@1: G = {h4['stand_G']['pass1_mean']*100:.2f}%, H = {h4['stand_H']['pass1_mean']*100:.2f}%. Δ = {h4['delta_pp']:+.2f} п.п. statistic = {h4['wilcoxon_statistic']:.4f}, {fmt_p(h4['p_value'])}, d_h = {h4['cohens_d_h']:.4f}. Stand H = {h4['stand_H']['n_runs']} прогонов × 15 задач = {h4['stand_H']['n_observations']} наблюдений (полная сетка).\n")

    lines.append("\n## 3. Waterfall ablation (Cohen's d на каждом шаге)\n")
    lines.append("| Шаг | Pass@1 (исходный) | Pass@1 (целевой) | Δ | Cohen's d_h | p-value |\n")
    lines.append("|---|:-:|:-:|:-:|:-:|:-:|\n")
    for w in waterfall:
        lines.append(f"| {w['from']}→{w['to']} ({w['label']}) | {w['mean_from']*100:.2f}% | {w['mean_to']*100:.2f}% | {w['delta']*100:+.2f} п.п. | {w['cohens_d']:.4f} | {fmt_p(w['p_value'])} |\n")

    lines.append("\n## 3a. ARR (mean(b·c)) и 95% bootstrap-ДИ\n")
    lines.append("| Стенд | n | ARR = mean(b·c) | 95% bootstrap-ДИ |\n")
    lines.append("|:-:|:-:|:-:|:-:|\n")
    for s in ("E", "H"):
        ci = bootstrap_arr_ci(df, s)
        if ci["arr"] is not None:
            lines.append(f"| {s} | {ci['n']} | {ci['arr']:.2f}% | [{ci['ci_low']:.2f}%; {ci['ci_high']:.2f}%] |\n")

    lines.append("\n## 4. Методология\n")
    lines.append("- **Wilson 95% CI** для пропорций (`successes/n`); формула Уилсона с z = 1,96.\n")
    lines.append("- **σ Pass@1** — выборочное стандартное отклонение Pass@1 между 5 повторами одного стенда (per-run, ddof = 1): `groupby('run')['pass1'].mean().std(ddof=1)`.\n")
    lines.append("- **FSR (False Success Rate)** — доля наблюдений, где pass1=1 (build OK) И completeness=0 (ни один из эталонных файлов не изменён); строгое определение «формальный успех при полном промахе по адресации».\n")
    lines.append("- **Wilcoxon signed-rank**: парим по 15 задачам — для каждого стенда берём среднее Pass@1 (или Completeness) по всем 5 повторам. Если все разности нулевые, p = 1.\n")
    lines.append("- Используем scipy.stats.wilcoxon с zero_method='wilcox' (нулевые разности отбрасываются), correction=False, alternative='two-sided', method='auto'.\n")
    lines.append("- **Cohen's d_h** для пропорций (Cohen 1988): `d = 2·arcsin(√p₁) − 2·arcsin(√p₀)`.\n")
    lines.append("- **Cohen's d_z** (one-sample) для контраста разностей: `d = mean(diff) / std(diff, ddof=1)`.\n")
    lines.append("- Для **H2b** используется контраст разностей: `(E−G) − (D−B)` per task; нулевая гипотеза — отсутствие синергии RAG×Graph.\n")
    lines.append("- Для **H3** — стек всех разностей по 3 парам (45 наблюдений), one-sample Wilcoxon vs 0.\n")
    lines.append("- Полная методология: `docs/technical/metrics_methodology.md`.\n")

    MD_OUT.write_text("".join(lines), encoding="utf-8")
    print(f"OK. JSON: {JSON_OUT}\nMD:  {MD_OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
