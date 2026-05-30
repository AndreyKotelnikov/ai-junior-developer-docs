"""compute_h3_mixed.py — корректная инференция для H3 через mixed-effects модель.

Цель: устранить методологическую уязвимость one-sample Wilcoxon на стеке 45 разностей
(псевдо-репликация: 45 разностей сняты на одной выборке из 15 задач × 3 RAG-уровня —
кластеризованы по задаче).

Используется линейная mixed-effects модель с random intercept на задаче:
    Δ ~ 1 + C(rag_level) + (1 | task_id)
- intercept: средний эффект графа по 45 (task, RAG)-конфигурациям;
- C(rag_level): фиксированный эффект уровня RAG (контролирует, что разные RAG дают разные средние);
- (1 | task_id): random intercept на задаче (учитывает корреляцию разностей одной задачи).

Выход — итоговые числа гипотезы H3:
- intercept_estimate (средний эффект графа в долях, ≈ 0,1056)
- intercept_p_value
- ICC по задаче
- эффективное n с учётом design-effect для кластеров размера 3

Опирается на ту же инфраструктуру парсинга, что и compute_stats.py.
"""
from __future__ import annotations

import math
import re
from pathlib import Path
from typing import Dict, List, Optional

import numpy as np
import pandas as pd
from scipy import stats as scstats

try:
    import statsmodels.formula.api as smf
    import statsmodels.api as sm
    HAS_STATSMODELS = True
except ImportError:
    HAS_STATSMODELS = False

ROOT = Path(r"E:/DS/JD Разработка/jd-claude")
DATA_DIR = ROOT / "docs" / "experiment" / "test_results"

PAIRS = [("B", "G", 0), ("C", "I", 3), ("D", "E", 5)]
RELEVANT_STANDS = {"B", "C", "D", "G", "I", "E"}

TEST_HEADER_RE = re.compile(r"^## Тест (\d+)\.\s*(.*?)\s*$", re.MULTILINE)


# --- Парсинг (упрощённая версия из compute_stats.py) -----------------------

def parse_completeness(value: str) -> Optional[float]:
    m = re.search(r"(\d+)\s*/\s*(\d+)", value)
    if not m:
        return None
    num, den = int(m.group(1)), int(m.group(2))
    if den == 0:
        return None
    return num / den


def parse_test_block(block: str) -> Dict[str, Optional[float]]:
    out: Dict[str, Optional[float]] = {"completeness": None}

    def find_value(label: str) -> Optional[str]:
        pattern = rf"\|\s*{re.escape(label)}\s*\|\s*([^|\n]+?)\s*\|"
        m = re.search(pattern, block)
        return m.group(1).strip() if m else None

    comp_raw = find_value("Completeness")
    if comp_raw is not None:
        out["completeness"] = parse_completeness(comp_raw)
    return out


def parse_file(path: Path) -> List[Dict]:
    text = path.read_text(encoding="utf-8")
    matches = list(TEST_HEADER_RE.finditer(text))
    rows: List[Dict] = []
    for i, m in enumerate(matches):
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        block = text[start:end]
        cut = block.find("## Итоги прогона")
        if cut > 0:
            block = block[:cut]
        test_num = int(m.group(1))
        data = parse_test_block(block)
        data["test_num"] = test_num
        rows.append(data)
    return rows


def load_completeness_data() -> pd.DataFrame:
    files = sorted(DATA_DIR.glob("stand-*.md"))
    rows: List[Dict] = []
    for f in files:
        m = re.match(r"stand-([A-Z])-run-(\d+)\.md", f.name)
        if not m:
            continue
        stand, run = m.group(1), int(m.group(2))
        if stand not in RELEVANT_STANDS:
            continue
        for r in parse_file(f):
            if r["completeness"] is None:
                continue
            rows.append({
                "stand": stand,
                "run": run,
                "test_num": r["test_num"],
                "completeness": r["completeness"],
            })
    return pd.DataFrame(rows)


# --- Построение 45 (task, RAG)-разностей ------------------------------------

def build_delta_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """Для каждой задачи и каждой RAG-пары вычисляем разность Completeness(graph_on) - Completeness(graph_off),
    усреднённую по 5 повторам.

    Выход: DataFrame с колонками (task_id, rag_level, delta), длина 45.
    """
    # Среднее по 5 повторам для каждого (stand, task)
    avg = df.groupby(["stand", "test_num"])["completeness"].mean().reset_index()
    avg_pivot = avg.pivot(index="test_num", columns="stand", values="completeness")

    rows: List[Dict] = []
    for stand_off, stand_on, rag in PAIRS:
        if stand_off not in avg_pivot.columns or stand_on not in avg_pivot.columns:
            print(f"WARN: пара {stand_off}→{stand_on} (RAG={rag}) пропущена — нет данных")
            continue
        for task_num in avg_pivot.index:
            off_val = avg_pivot.loc[task_num, stand_off]
            on_val = avg_pivot.loc[task_num, stand_on]
            if pd.isna(off_val) or pd.isna(on_val):
                continue
            rows.append({
                "task_id": int(task_num),
                "rag_level": int(rag),
                "delta": float(on_val - off_val),
            })
    return pd.DataFrame(rows)


# --- ICC из mixed-effects модели --------------------------------------------

def fit_mixed_model(delta_df: pd.DataFrame) -> Dict[str, float]:
    """Подгонка mixed-effects: Δ ~ 1 + C(rag_level) + (1 | task_id)."""
    if not HAS_STATSMODELS:
        return {"error": "statsmodels не установлен; запустить `pip install statsmodels`"}

    # Модель: фиксированные эффекты — intercept + RAG dummies; random intercept по task_id
    model = smf.mixedlm("delta ~ 1 + C(rag_level)", delta_df, groups=delta_df["task_id"])
    try:
        result = model.fit(reml=False, method="lbfgs")
    except Exception as exc:
        return {"error": f"fit failed: {exc}"}

    # Извлекаем intercept (средний эффект графа при базовой категории RAG=0)
    intercept = float(result.fe_params["Intercept"])
    intercept_se = float(result.bse_fe["Intercept"])
    # p-value для intercept (двусторонний z-тест)
    z_stat = intercept / intercept_se
    intercept_pval = 2 * (1 - scstats.norm.cdf(abs(z_stat)))

    # Variance components
    var_random = float(result.cov_re.iloc[0, 0])  # дисперсия random intercept
    var_residual = float(result.scale)  # остаточная дисперсия
    icc = var_random / (var_random + var_residual) if (var_random + var_residual) > 0 else 0.0

    # Average effect across RAG levels (marginal mean of intercept + C(rag) effects)
    # Базовая категория RAG=0; добавляем эффекты для RAG=3 и RAG=5
    intercept_3 = intercept + (float(result.fe_params.get("C(rag_level)[T.3]", 0.0)))
    intercept_5 = intercept + (float(result.fe_params.get("C(rag_level)[T.5]", 0.0)))
    avg_effect_across_rag = (intercept + intercept_3 + intercept_5) / 3

    # Effective n при design-effect для кластеров размера m=3 (3 разности на задачу):
    # design_effect = 1 + (m - 1) * ICC; effective_n = n_total / design_effect
    n_total = len(delta_df)
    m = 3  # размер кластера
    design_effect = 1 + (m - 1) * icc
    effective_n = n_total / design_effect

    return {
        "intercept_estimate": intercept,
        "intercept_se": intercept_se,
        "intercept_p_value": intercept_pval,
        "intercept_z": z_stat,
        "avg_effect_across_rag": avg_effect_across_rag,
        "var_random_task": var_random,
        "var_residual": var_residual,
        "icc_task": icc,
        "n_total": n_total,
        "cluster_size_m": m,
        "design_effect": design_effect,
        "effective_n": effective_n,
        "convergence": result.converged if hasattr(result, "converged") else "unknown",
        "summary": str(result.summary()),
    }


# --- Cluster bootstrap (валидация mixed-model) ------------------------------

def cluster_bootstrap(delta_df: pd.DataFrame, n_boot: int = 10_000, seed: int = 42) -> Dict[str, float]:
    """Cluster-bootstrap по задачам: пересэмплируем задачи (с возвратом), для каждой
    включаем все 3 разности. Даёт непараметрический 95% CI на средний эффект.
    """
    rng = np.random.default_rng(seed)
    tasks = delta_df["task_id"].unique()
    n_tasks = len(tasks)
    boot_means = np.empty(n_boot, dtype=float)

    # Группируем разности по задаче для быстрого пересэмплинга
    deltas_by_task = {t: delta_df.loc[delta_df["task_id"] == t, "delta"].values for t in tasks}

    for i in range(n_boot):
        sample_tasks = rng.choice(tasks, size=n_tasks, replace=True)
        sample = np.concatenate([deltas_by_task[t] for t in sample_tasks])
        boot_means[i] = sample.mean()

    return {
        "boot_mean": float(np.mean(boot_means)),
        "boot_ci_low": float(np.quantile(boot_means, 0.025)),
        "boot_ci_high": float(np.quantile(boot_means, 0.975)),
        "boot_p_one_sided": float(np.mean(boot_means <= 0)),  # P(effect <= 0) под H0
    }


# --- Fisher's combined p-value (вспомогательная проверка) -------------------

def fisher_combined_p(delta_df: pd.DataFrame) -> Dict[str, float]:
    """Три раздельных one-sample Wilcoxon (по 15 разностей каждый), Fisher's method для объединения p-значений.

    Альтернатива mixed-model: проверяет ту же содержательную нулевую гипотезу.
    """
    p_values = []
    pair_results = []
    for rag_level in [0, 3, 5]:
        sub = delta_df.loc[delta_df["rag_level"] == rag_level, "delta"].values
        if len(sub) == 0:
            continue
        if np.allclose(sub, 0):
            p = 1.0
        else:
            res = scstats.wilcoxon(sub, zero_method="wilcox", alternative="two-sided")
            p = float(res.pvalue)
        p_values.append(p)
        pair_results.append({
            "rag_level": rag_level,
            "n": len(sub),
            "mean_delta": float(np.mean(sub)),
            "median_delta": float(np.median(sub)),
            "wilcoxon_p": p,
        })
    # Fisher's combined: X^2 = -2 * sum(ln(p_i)), df = 2k
    chi2_stat = -2 * sum(math.log(p) for p in p_values if p > 0)
    df = 2 * len(p_values)
    combined_p = 1 - scstats.chi2.cdf(chi2_stat, df)
    return {
        "individual_pair_results": pair_results,
        "fisher_chi2": chi2_stat,
        "fisher_df": df,
        "fisher_combined_p": float(combined_p),
    }


# --- Главное -----------------------------------------------------------------

def main() -> None:
    print(f"Загрузка данных из {DATA_DIR}...")
    df = load_completeness_data()
    print(f"Загружено {len(df)} строк (Completeness) по стендам {sorted(df['stand'].unique())}")

    delta_df = build_delta_dataframe(df)
    print(f"Построено {len(delta_df)} (task, RAG)-разностей (ожидается 45 = 3 RAG × 15 задач)")
    print(f"  Распределение по RAG: {delta_df['rag_level'].value_counts().to_dict()}")
    print(f"  Распределение по задачам: {len(delta_df['task_id'].unique())} уникальных задач")
    print()

    print("=" * 70)
    print("MIXED-EFFECTS MODEL: Δ ~ 1 + C(rag_level) + (1 | task_id)")
    print("=" * 70)
    mm = fit_mixed_model(delta_df)
    if "error" in mm:
        print(f"ОШИБКА: {mm['error']}")
    else:
        print(f"Intercept (средний эффект графа при RAG=0): {mm['intercept_estimate']*100:+.2f} п.п.")
        print(f"Intercept SE: {mm['intercept_se']*100:.2f} п.п.")
        print(f"Intercept z-stat: {mm['intercept_z']:.4f}")
        print(f"Intercept p-value (two-sided): {mm['intercept_p_value']:.6f}")
        print(f"Средний эффект графа по 3 RAG-уровням: {mm['avg_effect_across_rag']*100:+.2f} п.п.")
        print(f"Variance random intercept (task): {mm['var_random_task']:.6f}")
        print(f"Variance residual: {mm['var_residual']:.6f}")
        print(f"ICC по задаче: {mm['icc_task']:.4f}")
        print(f"N total: {mm['n_total']}")
        print(f"Cluster size (m): {mm['cluster_size_m']}")
        print(f"Design effect: {mm['design_effect']:.4f}")
        print(f"Effective N: {mm['effective_n']:.2f}")
        print(f"Convergence: {mm['convergence']}")
        print()
        # Полный summary statsmodels — для аудита
        print("--- statsmodels summary ---")
        print(mm["summary"])

    print()
    print("=" * 70)
    print("CLUSTER-BOOTSTRAP (10 000 ресэмплов по задачам)")
    print("=" * 70)
    cb = cluster_bootstrap(delta_df, n_boot=10_000, seed=42)
    print(f"Bootstrap mean Δ: {cb['boot_mean']*100:+.2f} п.п.")
    print(f"95% CI: [{cb['boot_ci_low']*100:+.2f}, {cb['boot_ci_high']*100:+.2f}] п.п.")
    print(f"P(Δ ≤ 0) под нулевой гипотезой: {cb['boot_p_one_sided']:.4f}")

    print()
    print("=" * 70)
    print("FISHER'S COMBINED P-VALUE (3 раздельных Wilcoxon × Fisher)")
    print("=" * 70)
    fc = fisher_combined_p(delta_df)
    for r in fc["individual_pair_results"]:
        print(f"  RAG={r['rag_level']}: n={r['n']}, mean Δ={r['mean_delta']*100:+.2f} п.п., median={r['median_delta']*100:+.2f}, Wilcoxon p={r['wilcoxon_p']:.6f}")
    print(f"Fisher chi² = {fc['fisher_chi2']:.4f}, df={fc['fisher_df']}, combined p = {fc['fisher_combined_p']:.6f}")

    print()
    print("=" * 70)
    print("SUMMARY — итоговые числа гипотезы H3")
    print("=" * 70)
    if "error" not in mm:
        print(f"""
Mixed-effects модель `Δ ~ 1 + C(rag) + (1 | task_id)`:
  - средняя оценка эффекта графа: {mm['avg_effect_across_rag']*100:+.2f} п.п.
    (95% CI mixed: [{(mm['avg_effect_across_rag'] - 1.96*mm['intercept_se'])*100:+.2f}, {(mm['avg_effect_across_rag'] + 1.96*mm['intercept_se'])*100:+.2f}] п.п. — приближённый)
  - p-value для intercept: {mm['intercept_p_value']:.6f}
  - ICC по задаче: {mm['icc_task']:.3f}
  - эффективное n: {mm['effective_n']:.0f} (из 45 при design effect {mm['design_effect']:.2f})

Cluster-bootstrap (10 000 ресэмплов по задачам):
  - средний Δ: {cb['boot_mean']*100:+.2f} п.п.
  - 95% CI: [{cb['boot_ci_low']*100:+.2f}, {cb['boot_ci_high']*100:+.2f}] п.п.
  - P(Δ ≤ 0): {cb['boot_p_one_sided']:.4f}

Fisher's combined p (3 раздельных Wilcoxon): {fc['fisher_combined_p']:.6f}
""")


if __name__ == "__main__":
    main()
