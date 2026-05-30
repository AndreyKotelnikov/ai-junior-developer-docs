"""compute_robustness_stats.py — расчёт робастности вторичных гипотез H2b и H4
факторного эксперимента. Работает на тех же 675 наблюдениях (45 файлов
docs/experiment/test_results/stand-{A-I}-run-{1-5}.md).

Источники методов:
  TOST          — Schuirmann, 1987; Lakens, 2017
  Bayes factor  — Kass & Raftery, 1995; Wagenmakers, 2007;
                  формула JZS — Rouder et al., 2009
  Bootstrap     — Efron & Tibshirani, 1993
  Sign test     — Conover, 1999, гл. 3

Запуск:  python docs/technical/compute_robustness_stats.py
Выход:   docs/technical/stats_output_robustness.json
"""

import json
import re
import math
from pathlib import Path

import numpy as np
from scipy import stats
from scipy.integrate import quad

# --- Параметры (pre-registered) -------------------------------------------
ALPHA = 0.05
TOST_BOUND = 0.75          # порог эквивалентности H4 (паритет ≥ 75 %)
H2B_THRESHOLD = 5.0        # порог +5 п.п. для H2b
N_BOOTSTRAP = 10_000
RNG_SEED = 42
CAUCHY_R = 0.5             # масштаб приора Cauchy(0; 0,5) для Bayes factor

STANDS = list("ABCDEFGHI")
RUNS = [1, 2, 3, 4, 5]
N_TASKS = 15
RESULTS_DIR = Path(__file__).resolve().parents[1] / "experiment" / "test_results"
OUT_PATH = Path(__file__).resolve().parent / "stats_output_robustness.json"

# Страты сложности: тесты 1–5 простые, 6–10 средние, 11–15 сложные
STRATA = {"simple": range(1, 6), "medium": range(6, 11), "complex": range(11, 16)}

# --- Парсинг файлов прогонов ----------------------------------------------
ROW_RE = re.compile(
    r"^\|\s*(\d{1,2})\s*\|[^|]*\|[^|]*\|\s*([A-Za-z_]+)\s*\|"
    r"\s*([01])\s*\|\s*(\d+)\s*/\s*(\d+)",
)


def parse_run_file(path: Path):
    """Возвращает dict {task_no: {'pass1': int, 'completeness': float}} по сводной таблице."""
    tasks = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        m = ROW_RE.match(line.strip())
        if m:
            no = int(m.group(1))
            pass1 = int(m.group(3))
            num, den = int(m.group(4)), int(m.group(5))
            comp = (num / den) if den else 0.0
            if 1 <= no <= N_TASKS:
                tasks[no] = {"pass1": pass1, "completeness": comp}
    if len(tasks) != N_TASKS:
        raise ValueError(f"{path.name}: найдено {len(tasks)} задач вместо {N_TASKS}")
    return tasks


def load_all():
    """data[stand][task_no] = список из 5 значений pass1 (и completeness)."""
    data = {}
    for st in STANDS:
        pass1 = {t: [] for t in range(1, N_TASKS + 1)}
        comp = {t: [] for t in range(1, N_TASKS + 1)}
        for r in RUNS:
            f = RESULTS_DIR / f"stand-{st}-run-{r}.md"
            tasks = parse_run_file(f)
            for t in range(1, N_TASKS + 1):
                pass1[t].append(tasks[t]["pass1"])
                comp[t].append(tasks[t]["completeness"])
        data[st] = {"pass1": pass1, "completeness": comp}
    return data


def per_task_mean(data, stand, metric="pass1"):
    """Среднее значение метрики по 5 повторам — массив из 15 значений."""
    d = data[stand][metric]
    return np.array([np.mean(d[t]) for t in range(1, N_TASKS + 1)])


# --- Bayes factor (JZS, Rouder et al. 2009) -------------------------------
def jzs_bf10(t, n, r=CAUCHY_R):
    """BF10 для одновыборочного t-теста при приоре Cauchy(0; r) на эффект-сайз."""
    nu = n - 1

    def integrand(g):
        # плотность Inverse-Gamma(1/2, 1/2) для вспомогательной переменной g
        ig = g ** (-1.5) * math.exp(-1.0 / (2.0 * g)) / math.sqrt(2.0 * math.pi)
        a = 1.0 + n * g * r * r
        like = a ** (-0.5) * (1.0 + t * t / (a * nu)) ** (-(nu + 1) / 2.0)
        return like * ig

    m1, _ = quad(integrand, 0, np.inf, limit=200)
    m0 = (1.0 + t * t / nu) ** (-(nu + 1) / 2.0)
    return m1 / m0


def bf_label(bf):
    if bf >= 100:
        return "решающее (decisive)"
    if bf >= 30:
        return "очень сильное (very strong)"
    if bf >= 10:
        return "сильное (strong)"
    if bf >= 3:
        return "умеренное (moderate)"
    if bf >= 1:
        return "слабое (anecdotal)"
    return "в пользу H0"


# --- Основной расчёт ------------------------------------------------------
def main():
    rng = np.random.default_rng(RNG_SEED)
    data = load_all()

    B = per_task_mean(data, "B")
    D = per_task_mean(data, "D")
    E = per_task_mean(data, "E")
    G = per_task_mean(data, "G")
    H = per_task_mean(data, "H")
    G_comp = per_task_mean(data, "G", "completeness")
    H_comp = per_task_mean(data, "H", "completeness")

    # ========== H2b: эффект взаимодействия RAG × граф ==========
    # Контраст per task: (E - D) - (G - B) = E + B - D - G
    contrast = (E - D) - (G - B)
    inter_point = float(np.mean(contrast)) * 100  # в п.п.

    # 1) Wilcoxon one-sample
    try:
        w_stat, w_p = stats.wilcoxon(contrast)
    except ValueError:
        w_stat, w_p = float("nan"), 1.0

    # 2) Знаковый тест направления (односторонний)
    k_pos = int(np.sum(contrast > 0))
    n_nonzero = int(np.sum(contrast != 0))
    sign_p = stats.binomtest(k_pos, n_nonzero, 0.5, alternative="greater").pvalue \
        if n_nonzero > 0 else 1.0

    # 3) Bayes factor (one-sample t на контрасте)
    sd_c = np.std(contrast, ddof=1)
    t_c = float(np.mean(contrast) / (sd_c / math.sqrt(N_TASKS))) if sd_c > 0 else 0.0
    bf_h2b = jzs_bf10(t_c, N_TASKS)

    # 4) Bootstrap-CI на interaction
    boot_inter = np.array([
        np.mean(contrast[rng.integers(0, N_TASKS, N_TASKS)]) * 100
        for _ in range(N_BOOTSTRAP)
    ])
    inter_ci = (float(np.percentile(boot_inter, 2.5)),
                float(np.percentile(boot_inter, 97.5)))
    # bootstrap-вероятности превышения порогов (для H2b)
    p_inter_above_0 = float(np.mean(boot_inter > 0))
    p_inter_above_5 = float(np.mean(boot_inter > H2B_THRESHOLD))

    # 5) Стратификация
    h2b_strata = {}
    for name, rng_idx in STRATA.items():
        idx = [i - 1 for i in rng_idx]
        m = float(np.mean(contrast[idx])) * 100
        h2b_strata[name] = {"mean_pp": round(m, 2),
                            "sign": "+" if m > 0 else ("-" if m < 0 else "0")}
    n_pos_strata = sum(1 for s in h2b_strata.values() if s["sign"] == "+")

    # margin-of-safety
    sigma_c = sd_c * 100
    margin = inter_point - H2B_THRESHOLD

    # ========== H4: паритет on-prem / cloud ==========
    parity_point = float(np.mean(H) / np.mean(G))

    # TOST: bootstrap одностороннего 95 % ДИ на отношение паритета
    boot_ratio = []
    for _ in range(N_BOOTSTRAP):
        idx = rng.integers(0, N_TASKS, N_TASKS)
        mg = np.mean(G[idx])
        mh = np.mean(H[idx])
        if mg > 0:
            boot_ratio.append(mh / mg)
    boot_ratio = np.array(boot_ratio)
    tost_lower = float(np.percentile(boot_ratio, 5))   # одностор. 95 % нижняя граница
    ci_two_sided = (float(np.percentile(boot_ratio, 2.5)),
                    float(np.percentile(boot_ratio, 97.5)))
    tost_verdict = "equivalent" if tost_lower > TOST_BOUND else "not_equivalent"
    # bootstrap-вероятность превышения порога паритета и установленная нижняя граница
    p_parity_above_75 = float(np.mean(boot_ratio >= TOST_BOUND))
    # формально установленный (через одностор. 95 % ДИ) уровень non-inferiority.
    # Округление ВНИЗ (floor), а не к ближайшему: установленная граница θ
    # корректна только при tost_lower > θ. round() мог бы округлить вверх
    # (0,6575 → 0,66) и дать θ ВЫШЕ нижней границы ДИ — ложное утверждение.
    established_bound = math.floor(tost_lower * 100) / 100

    # Bayes factor для H4 (paired t-тест G vs H = one-sample на разностях)
    diff_gh = G - H
    sd_d = np.std(diff_gh, ddof=1)
    t_d = float(np.mean(diff_gh) / (sd_d / math.sqrt(N_TASKS))) if sd_d > 0 else 0.0
    bf_h4 = jzs_bf10(t_d, N_TASKS)

    # Стратификация паритета H4
    h4_strata = {}
    for name, rng_idx in STRATA.items():
        idx = [i - 1 for i in rng_idx]
        mg = np.mean(G[idx]); mh = np.mean(H[idx])
        par = float(mh / mg) if mg > 0 else 0.0
        h4_strata[name] = round(par, 4)
    n_above_strata = sum(1 for v in h4_strata.values() if v > TOST_BOUND)

    # Триангуляция трёх метрик
    triang = {
        "pass1_parity": round(parity_point, 4),
        "completeness_parity": round(float(np.mean(H_comp) / np.mean(G_comp)), 4),
    }

    # ========== Сборка JSON ==========
    out = {
        "_meta": {
            "n_observations": 675,
            "source": "docs/experiment/test_results/stand-{A-I}-run-{1-5}.md",
            "rng_seed": RNG_SEED,
            "n_bootstrap": N_BOOTSTRAP,
            "cauchy_prior_r": CAUCHY_R,
            "script": "docs/technical/compute_robustness_stats.py",
        },
        "h2b": {
            "interaction_pp": round(inter_point, 2),
            "wilcoxon": {"statistic": round(float(w_stat), 4), "p": round(float(w_p), 4)},
            "sign_test": {"k_positive": k_pos, "n_nonzero": n_nonzero,
                          "n": N_TASKS, "p_one_sided": round(float(sign_p), 4)},
            "bayes_factor_10": round(float(bf_h2b), 3),
            "bayes_factor_label": bf_label(bf_h2b),
            "bootstrap_ci_95": {"lower": round(inter_ci[0], 2),
                                "upper": round(inter_ci[1], 2),
                                "threshold": H2B_THRESHOLD},
            "bootstrap_prob": {"p_interaction_gt_0": round(p_inter_above_0, 3),
                               "p_interaction_gt_5": round(p_inter_above_5, 3)},
            "stratification": h2b_strata,
            "n_positive_strata": n_pos_strata,
            "margin_of_safety": {"point_estimate_pp": round(inter_point, 2),
                                 "threshold_pp": H2B_THRESHOLD,
                                 "delta_pp": round(margin, 2),
                                 "sigma_pp": round(sigma_c, 2),
                                 "delta_in_sigma": round(margin / sigma_c, 2) if sigma_c else None},
        },
        "h4": {
            "pass1_parity": round(parity_point, 4),
            "tost": {"ci_lower_one_sided_95": round(tost_lower, 4),
                     "threshold": TOST_BOUND,
                     "verdict": tost_verdict,
                     "established_noninferiority_bound": established_bound,
                     "p_parity_ge_threshold": round(p_parity_above_75, 3),
                     "method": f"bootstrap_approximation_n{N_BOOTSTRAP}"},
            "bootstrap_ci_95_two_sided": {"lower": round(ci_two_sided[0], 4),
                                          "upper": round(ci_two_sided[1], 4)},
            "bayes_factor_10": round(float(bf_h4), 3),
            "bayes_factor_label": bf_label(bf_h4),
            "triangulation": triang,
            "stratification": h4_strata,
            "n_strata_above_threshold": n_above_strata,
        },
    }

    OUT_PATH.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(out, ensure_ascii=False, indent=2))
    print(f"\nЗаписано в {OUT_PATH}")


if __name__ == "__main__":
    main()
