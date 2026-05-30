#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Universal hypothesis test runner for dotnet-multiagent-system.

Solves Windows + Cyrillic + Docker volume mount issues:
 1. JSON with Cyrillic via urllib + json.dumps (no bash/curl)
 2. Uses `python` (not python3) — Windows compatible
 3. shutil instead of rsync for code reset
 4. Deletes CONTENTS of src-X, not the directory itself (Docker volume mount)
 5. shutil instead of git checkout/clean for reset
 6. Python handles Unicode/Cyrillic paths natively
 7. Polls only terminal statuses (success/failed/cancelled)
 8. Foreground execution — no background processes
 9. Validates actual file changes — detects false_success
10. filecmp comparison instead of git diff for metrics
11. flush=True on all prints
12. 60s HTTP timeout for Ollama polling

Usage:
    python scripts/hyp-run-tests.py <stand> <port> <run_number|all> [--timeout 600]

Examples:
    python scripts/hyp-run-tests.py C 8020 1
    python scripts/hyp-run-tests.py C 8020 all --timeout 900
    python scripts/hyp-run-tests.py F 8050 1 --timeout 1800
"""

import argparse
import filecmp
import json
import os
import re
import shutil
import sys
import time
import urllib.request
import urllib.error
from datetime import datetime

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESULTS_DIR = os.path.join(BASE_DIR, "test-stands", "results")

TERMINAL_STATUSES = {"success", "failed", "cancelled"}

DEFAULT_TIMEOUT = 1800  # 30 min (3x from 600)
OLLAMA_DEFAULT_TIMEOUT = 5400  # 90 min (3x from 1800)
DEFAULT_POLL_INTERVAL = 15
HTTP_TIMEOUT = 60
NUM_RUNS = 5

# ---------------------------------------------------------------------------
# Test requirements (Cyrillic strings stored directly in Python)
# ---------------------------------------------------------------------------

REQUIREMENTS = {
    1: (
        "Добавить поля в сущность Portfolio:\n"
        "- **Description**: string (текстовое поле)\n"
        "- **IsActive**: bool (по умолчанию false)"
    ),
    2: (
        "Добавить поля в сущность OrganizationPerson:\n"
        "- **INN**: string (ИНН, максимальная длина 12 символов)\n"
        "- **SNILS**: string (СНИЛС, максимальная длина 14 символов)\n"
        "- **BirthDate**: int? (дата рождения)"
    ),
    3: (
        "Добавить поля в сущность PhotoReportItem:\n"
        "- **SortOrder**: int (порядок сортировки)\n"
        "- **IsMainPhoto**: bool (признак основного фото)"
    ),
    4: (
        "Добавить поля в сущность SubmittedDocumentsTemplate:\n"
        "- **Comment**: string (текстовое поле для комментария)\n"
        "- **SortOrder**: int (порядок сортировки)"
    ),
    5: (
        "Добавить поле в сущность ContractCurrency:\n"
        "- **Confirmation**: Confirmation? (подтверждение)"
    ),
    6: (
        "Добавить поля в сущность ConstructionSection:\n"
        "- **Responsible**: User (ответственный — FK)\n"
        "- **PlannedStartDate**: int? (плановая дата начала)\n"
        "- **PlannedFinishDate**: int? (плановая дата окончания)\n"
        "- **Status**: ApprovalStatus? (статус согласования)\n"
        "- **PlannedBudget**: decimal? (плановый бюджет)"
    ),
    7: (
        "Добавить поля в сущность Experience:\n"
        "- **Region**: Region (регион объекта — FK)\n"
        "- **Town**: Town (город — FK)\n"
        "- **DeveloperCategory**: DeveloperCategory? (категория застройщика — enum)\n"
        "- **ResidentialComplex**: string (название ЖК)"
    ),
    8: (
        "Добавить поля в сущность MediaLink:\n"
        "- **ConstructionSite**: ConstructionSite (объект строительства — FK)\n"
        "- **Author**: User (автор — FK)\n"
        "- **UploadDate**: int? (дата загрузки)\n"
        "- **IsPublic**: bool (публичная ссылка)"
    ),
    9: (
        "Добавить поля в сущность SpecialZone:\n"
        "- **ProjectDoc**: ProjectDoc (ссылка на документ — FK)\n"
        "- **VerifiedBy**: User (кто проверил — FK)\n"
        "- **VerificationDate**: int? (дата проверки)\n"
        "- **IsVerified**: bool (проверено)\n"
        "- **Coordinates**: string (координаты)"
    ),
    10: (
        "Добавить поля в сущность CheckPoint:\n"
        "- **ConstructionSite**: ConstructionSite (объект строительства — FK)\n"
        "- **Priority**: int (приоритет, по умолчанию 0)\n"
        "- **Status**: ApprovalStatus? (статус согласования)\n"
        "- **CompletionPercent**: int? (процент выполнения)"
    ),
    11: (
        "Добавить поля в сущность Notice:\n"
        "- **Tranche**: Tranche (транш — FK)\n"
        "- **ConstructionSection**: ConstructionSection (секция — FK)\n"
        "- **Priority**: int (приоритет, 1–5)\n"
        "- **DueDate**: int? (плановая дата исполнения)\n"
        "- **Resolution**: string (резолюция, текстовое поле)"
    ),
    12: (
        "Добавить поля в сущность EscrowAccount:\n"
        "- **Organization**: Organization (организация — FK)\n"
        "- **ContractNumber**: string (номер договора, максимум 50 символов)\n"
        "- **CreditAgreementDate**: int? (дата кредитного договора)\n"
        "- **Collateral**: decimal? (размер обеспечения)\n"
        "- **CollateralFile**: string (файл обеспечения)"
    ),
    13: (
        "Добавить атрибуты в 10 сущностей:\n"
        "- **IsArchived**: bool (признак архивации, по умолчанию false)\n"
        "- **ArchivedDate**: DateTime? (дата архивации)\n"
        "\n"
        "Сущности для модификации:\n"
        "1. Discussion\n"
        "2. BankPolicy\n"
        "3. Notice\n"
        "4. CheckPoint\n"
        "5. MediaLink\n"
        "6. ProjectAnalog\n"
        "7. TargetProgram\n"
        "8. CheckListItem\n"
        "9. DiscussionProtocol\n"
        "10. BankPolicyItem"
    ),
    14: (
        "Модифицировать связанные сущности:\n"
        "\n"
        "BankPolicy — добавить:\n"
        "- **Status**: ApprovalStatus? (статус)\n"
        "- **Responsible**: User (ответственный — FK)\n"
        "- **DueDate**: int? (срок)\n"
        "- **Comment**: string (комментарий, текстовое поле)\n"
        "\n"
        "BankPolicyItem — добавить:\n"
        "- **Weight**: decimal? (вес критерия)\n"
        "- **Status**: ApprovalStatus? (статус элемента)\n"
        "- **Responsible**: User (ответственный — FK)"
    ),
    15: (
        "Добавить поля в сущность SalesData:\n"
        "- **ConstructionSection**: ConstructionSection (секция — FK)\n"
        "- **CompanyGroup**: CompanyGroup (группа компаний — FK)\n"
        "- **SalesManager**: User (менеджер продаж — FK)\n"
        "- **SalesTarget**: decimal? (план продаж)\n"
        "- **SalesComment**: string (комментарий, текстовое поле)"
    ),
}

# ---------------------------------------------------------------------------
# Required files for completeness metric
# ---------------------------------------------------------------------------

F_REQUIRED = {
    1: ["Data/Entities/Portfolio.cs"],
    2: ["Data/Entities/OrganizationPerson.cs"],
    3: ["Data/Entities/PhotoReport/PhotoReportItem.cs"],
    4: ["Data/Entities/SubmittedDocumentsTemplate.cs"],
    5: ["Data/Entities/ContractCurrency.cs"],
    6: ["Data/Entities/ConstructionSection.cs", "Data/DataConfiguration.cs"],
    7: ["Data/Entities/Experience.cs", "Data/DataConfiguration.cs", "Data/Initializer.cs"],
    8: ["Data/Entities/MediaLink.cs", "Data/DataConfiguration.cs", "Data/Initializer.cs"],
    9: ["Data/Entities/SpecialZone.cs", "Data/DataConfiguration.cs", "Data/Initializer.cs"],
    10: ["Data/Entities/CheckPoint.cs", "Data/DataConfiguration.cs", "Data/Initializer.cs"],
    11: ["Data/Entities/Notice.cs", "Data/DataConfiguration.cs", "Data/Initializer.cs"],
    12: ["Data/Entities/EscrowAccount.cs", "Data/DataConfiguration.cs", "Data/Initializer.cs"],
    13: [
        "Data/Entities/Discussion.cs", "Data/Entities/BankPolicy.cs",
        "Data/Entities/Notice.cs", "Data/Entities/CheckPoint.cs",
        "Data/Entities/MediaLink.cs", "Data/Entities/ProjectAnalog.cs",
        "Data/Entities/TargetProgram.cs", "Data/Entities/CheckListItem.cs",
        "Data/Entities/DiscussionProtocol.cs", "Data/Entities/BankPolicyItem.cs",
    ],
    14: ["Data/Entities/BankPolicy.cs", "Data/Entities/BankPolicyItem.cs", "Data/DataConfiguration.cs"],
    15: ["Data/Entities/SalesData.cs", "Data/DataConfiguration.cs", "Data/Initializer.cs"],
}

# ---------------------------------------------------------------------------
# Test metadata
# ---------------------------------------------------------------------------

TESTS = {
    1: {"name": "Portfolio +2 поля", "complexity": "Простая", "type": "modify_entity"},
    2: {"name": "OrganizationPerson +3 поля", "complexity": "Простая", "type": "modify_entity"},
    3: {"name": "PhotoReportItem +2 поля", "complexity": "Простая", "type": "modify_entity"},
    4: {"name": "SubmittedDocumentsTemplate +2 поля", "complexity": "Простая", "type": "modify_entity"},
    5: {"name": "ContractCurrency +1 enum", "complexity": "Простая", "type": "modify_entity"},
    6: {"name": "ConstructionSection +5 полей", "complexity": "Средняя", "type": "modify_entity"},
    7: {"name": "Experience +4 поля", "complexity": "Средняя", "type": "modify_entity"},
    8: {"name": "MediaLink +4 поля", "complexity": "Средняя", "type": "modify_entity"},
    9: {"name": "SpecialZone +5 полей", "complexity": "Средняя", "type": "modify_entity"},
    10: {"name": "CheckPoint +4 поля", "complexity": "Средняя", "type": "modify_entity"},
    11: {"name": "Notice +5 полей", "complexity": "Сложная", "type": "modify_entity"},
    12: {"name": "EscrowAccount +5 полей", "complexity": "Сложная", "type": "modify_entity"},
    13: {"name": "10 сущностей +2 поля", "complexity": "Сложная", "type": "modify_entity"},  # bulk-вариант: 10 сущностей одним требованием
    14: {"name": "BankPolicy + BankPolicyItem", "complexity": "Сложная", "type": "modify_entity"},
    15: {"name": "SalesData +5 полей", "complexity": "Сложная", "type": "modify_entity"},
}

# ---------------------------------------------------------------------------
# Stand configurations
# ---------------------------------------------------------------------------

STAND_CONFIG = {
    "A": {"agent_mode": "single", "use_rag": True, "rag_top_k": 3, "use_graph": False},
    "B": {"agent_mode": "multi", "use_rag": False, "rag_top_k": 0, "use_graph": False},
    "C": {"agent_mode": "multi", "use_rag": True, "rag_top_k": 3, "use_graph": False},
    "D": {"agent_mode": "multi", "use_rag": True, "rag_top_k": 5, "use_graph": False},
    "E": {"agent_mode": "multi", "use_rag": True, "rag_top_k": 5, "use_graph": True},
    "F": {"agent_mode": "multi", "use_rag": True, "rag_top_k": 3, "use_graph": False},
    "G": {"agent_mode": "multi", "use_rag": False, "rag_top_k": 0, "use_graph": True},
    "H": {"agent_mode": "multi", "use_rag": False, "rag_top_k": 0, "use_graph": True},
    "I": {"agent_mode": "multi", "use_rag": True, "rag_top_k": 3, "use_graph": True},
}

OLLAMA_STANDS = {"F", "H"}

# Phase definitions: which stands belong to which phase
PHASES = {
    1: {"stands": {"A", "B", "C", "D"}, "marker": ".phase1_complete"},
    2: {"stands": {"E", "G"}, "marker": ".phase2_complete"},
    3: {"stands": {"F"}, "marker": ".phase3_complete"},
    4: {"stands": {"H"}, "marker": ".phase4_complete"},
}

# Which phase markers each stand must wait for BEFORE starting tests
PHASE_WAIT = {
    "A": [],                    # Phase 1 — only .infra_ready (handled in session prompt)
    "B": [],
    "C": [],
    "D": [],
    "E": [".phase1_complete"],  # Phase 2 — wait for phase 1
    "G": [".phase1_complete"],
    "F": [".phase2_complete"],  # Phase 3 — wait for phase 2
    "H": [".phase3_complete"],  # Phase 4 — wait for phase 3
}

STAND_DESCRIPTIONS = {
    "A": "Single-agent + RAG(3)",
    "B": "Multi-agent, без RAG, без графа",
    "C": "Multi-agent + RAG(3)",
    "D": "Multi-agent + RAG(5)",
    "E": "Multi-agent + RAG(5) + граф",
    "F": "Multi-agent + RAG(3) + Ollama",
    "G": "Multi-agent + граф (без RAG)",
    "H": "Multi-agent + граф + Ollama (без RAG)",
    "I": "Multi-agent + RAG(3) + граф",
}


# ---------------------------------------------------------------------------
# Utility: print with flush
# ---------------------------------------------------------------------------

def log(msg):
    print(msg, flush=True)


# ---------------------------------------------------------------------------
# reset_stand: delete contents (not directory!) then copy fresh source
# ---------------------------------------------------------------------------

def reset_stand(stand):
    """Reset test-stands/src-{stand} to a fresh copy from dotnet-app/src.

    Deletes contents but NOT the directory itself (Docker volume mount).
    Preserves obj/bin folders to avoid full NuGet restore.
    Fully removes .git to prevent index.lock and object accumulation.
    Uses shutil — no rsync, no rm -rf.
    """
    src_dir = os.path.join(BASE_DIR, "dotnet-app", "src")
    dst_dir = os.path.join(BASE_DIR, "test-stands", "src-" + stand)

    log(f"  Resetting src-{stand} ...")

    if not os.path.isdir(dst_dir):
        log(f"  WARNING: {dst_dir} does not exist, creating it")
        os.makedirs(dst_dir, exist_ok=True)

    # Step 1: Force-remove .git first (prevent index.lock issues)
    git_dir = os.path.join(dst_dir, ".git")
    if os.path.isdir(git_dir):
        # Remove read-only flags on Windows (git objects are read-only)
        def force_remove_readonly(func, path, exc_info):
            os.chmod(path, 0o777)
            func(path)
        try:
            shutil.rmtree(git_dir, onerror=force_remove_readonly)
            log(f"  Cleaned .git directory")
        except Exception as e:
            log(f"  WARNING: could not fully remove .git: {e}")

    # Step 2: delete everything else in dst except obj/bin
    skip = {"obj", "bin", ".git"}
    for item in os.listdir(dst_dir):
        if item in skip:
            continue
        item_path = os.path.join(dst_dir, item)
        try:
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)
            else:
                os.remove(item_path)
        except Exception as e:
            log(f"  WARNING: could not remove {item_path}: {e}")

    # Step 3: copy fresh source (including .git from reference)
    for item in os.listdir(src_dir):
        if item in {"obj", "bin"}:
            continue
        s = os.path.join(src_dir, item)
        d = os.path.join(dst_dir, item)
        try:
            if os.path.isdir(s):
                shutil.copytree(s, d)
            else:
                shutil.copy2(s, d)
        except Exception as e:
            log(f"  WARNING: could not copy {s} -> {d}: {e}")

    log(f"  Reset complete.")


# ---------------------------------------------------------------------------
# send_task: POST via urllib with proper Cyrillic JSON
# ---------------------------------------------------------------------------

def send_task(port, requirement, config):
    """Submit a task to the multiagent API. Returns task_id or None."""
    payload = {
        "requirement": requirement,
        "agent_mode": config["agent_mode"],
        "use_rag": config["use_rag"],
        "rag_top_k": config["rag_top_k"],
        "use_graph": config["use_graph"],
    }
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")

    url = f"http://localhost:{port}/api/tasks"

    for attempt in range(3):
        try:
            req = urllib.request.Request(
                url, data=body,
                headers={"Content-Type": "application/json; charset=utf-8"},
                method="POST",
            )
            resp = urllib.request.urlopen(req, timeout=30)
            data = json.loads(resp.read().decode("utf-8"))
            task_id = data.get("task_id") or data.get("id")
            if task_id:
                log(f"  Task submitted: {task_id}")
                return task_id
            log(f"  WARNING: API returned no task_id: {data}")
            return None
        except Exception as e:
            log(f"  Submit attempt {attempt + 1}/3 failed: {e}")
            if attempt < 2:
                time.sleep(10)

    log("  ERROR: all 3 submit attempts failed")
    return None


# ---------------------------------------------------------------------------
# poll_task: poll until terminal status
# ---------------------------------------------------------------------------

def poll_task(port, task_id, timeout_sec, interval_sec=DEFAULT_POLL_INTERVAL):
    """Poll task status until a terminal status is reached or timeout.

    Terminal statuses: success, failed, cancelled.
    Returns the full API response dict.
    """
    url = f"http://localhost:{port}/api/tasks/{task_id}"
    elapsed = 0
    last_status = ""

    while elapsed < timeout_sec:
        try:
            req = urllib.request.Request(url, method="GET")
            resp = urllib.request.urlopen(req, timeout=HTTP_TIMEOUT)
            data = json.loads(resp.read().decode("utf-8"))
            status = data.get("status", "unknown")

            if status != last_status:
                log(f"  [{elapsed:>4d}s] Status: {status}")
                last_status = status

            if status in TERMINAL_STATUSES:
                return data

        except urllib.error.URLError as e:
            log(f"  [{elapsed:>4d}s] Poll error: {e}")
        except Exception as e:
            log(f"  [{elapsed:>4d}s] Poll error: {e}")

        time.sleep(interval_sec)
        elapsed += interval_sec

    log(f"  TIMEOUT after {timeout_sec}s (last status: {last_status})")
    return {"status": "timeout", "last_status": last_status, "elapsed": timeout_sec}


# ---------------------------------------------------------------------------
# get_changed_files: filecmp comparison (no git diff)
# ---------------------------------------------------------------------------

def _compare_dirs(dcmp, prefix=""):
    """Recursively compare directories, return list of changed relative paths."""
    changed = []
    # Files that differ
    for name in dcmp.diff_files:
        changed.append(os.path.join(prefix, name).replace("\\", "/"))
    # Files only in right (new files created by agent)
    for name in dcmp.right_only:
        right_path = os.path.join(dcmp.right, name)
        if os.path.isdir(right_path):
            # Walk all files in new directory
            for root, _dirs, files in os.walk(right_path):
                for f in files:
                    full = os.path.join(root, f)
                    rel = os.path.relpath(full, dcmp.right).replace("\\", "/")
                    changed.append(os.path.join(prefix, rel).replace("\\", "/"))
        else:
            changed.append(os.path.join(prefix, name).replace("\\", "/"))
    # Recurse into subdirectories
    for sub_name, sub_dcmp in dcmp.subdirs.items():
        changed.extend(_compare_dirs(sub_dcmp, os.path.join(prefix, sub_name)))
    return changed


def get_changed_files(stand):
    """Compare test-stands/src-{stand} against dotnet-app/src using filecmp.

    Ignores obj/bin directories. Returns list of relative paths (forward slashes).
    """
    original = os.path.join(BASE_DIR, "dotnet-app", "src")
    modified = os.path.join(BASE_DIR, "test-stands", "src-" + stand)

    if not os.path.isdir(original) or not os.path.isdir(modified):
        log("  WARNING: source directories not found for comparison")
        return []

    ignore = ["obj", "bin"]
    dcmp = filecmp.dircmp(original, modified, ignore=ignore)
    changed = _compare_dirs(dcmp)
    # Filter to .cs files only
    changed = sorted(set(f for f in changed if f.endswith(".cs")))
    return changed


# ---------------------------------------------------------------------------
# compute_completeness
# ---------------------------------------------------------------------------

def compute_completeness(changed_files, test_num):
    """Compute completeness: intersection of changed_files with F_REQUIRED.

    Returns (matched_count, total_required, percentage, matched_list, required_list).
    """
    required = F_REQUIRED.get(test_num, [])
    total = len(required)
    if total == 0:
        return 0, 0, 0.0, [], []

    matched = []
    for req_path in required:
        # Normalize for comparison
        req_norm = req_path.replace("\\", "/")
        for cf in changed_files:
            cf_norm = cf.replace("\\", "/")
            if cf_norm == req_norm or cf_norm.endswith("/" + req_norm.split("/")[-1]):
                # Also check full path match for deeper paths
                if cf_norm == req_norm or cf_norm.endswith(req_norm):
                    matched.append(req_path)
                    break

    pct = (len(matched) / total * 100) if total > 0 else 0.0
    return len(matched), total, pct, matched, required


# ---------------------------------------------------------------------------
# evaluate_result: detect false success
# ---------------------------------------------------------------------------

def evaluate_result(api_response, changed_files, test_num):
    """Evaluate the test result. Returns (final_status, analysis_text)."""
    status = api_response.get("status", "unknown")
    error = api_response.get("error", "")

    if status == "timeout":
        return "timeout", "Тест завершился по таймауту"

    if status == "cancelled":
        return "cancelled", "Тест был отменён"

    if status in ("failed", "error"):
        return "failed", f"Тест завершился с ошибкой: {error}" if error else "Тест завершился с ошибкой"

    if status == "success":
        if len(changed_files) == 0:
            return "false_success", "API вернул success, но ни один файл не изменён — ложный успех"

        matched, total, pct, _, _ = compute_completeness(changed_files, test_num)
        if matched == total:
            return "success", f"Все {total} ожидаемых файлов изменены"
        else:
            return "success", (
                f"Изменено {matched}/{total} ожидаемых файлов ({pct:.0f}%). "
                f"Изменено всего файлов: {len(changed_files)}"
            )

    return status, f"Неизвестный статус: {status}"


# ---------------------------------------------------------------------------
# Result file I/O
# ---------------------------------------------------------------------------

def _result_file_path(stand, run_num):
    """Return path to result markdown file."""
    os.makedirs(RESULTS_DIR, exist_ok=True)
    return os.path.join(RESULTS_DIR, f"stand-{stand}-run-{run_num}.md")


def write_run_header(result_file, stand, run_num, config):
    """Write header to result file at start of a run."""
    desc = STAND_DESCRIPTIONS.get(stand, stand)
    is_ollama = stand in OLLAMA_STANDS
    model = "qwen2.5-coder:14b" if is_ollama else "Claude Haiku 4.5"
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    header = (
        f"# Прогон: Конфигурация {stand}, повторение {run_num}\n"
        f"\n"
        f"**Дата**: {now}\n"
        f"**Конфигурация**: {stand}: {desc}\n"
        f"**Настройки**: agent_mode={config['agent_mode']}, "
        f"use_rag={config['use_rag']}, rag_top_k={config['rag_top_k']}, "
        f"use_graph={config['use_graph']}\n"
        f"**Модель**: {model}\n"
        f"\n"
        f"---\n\n"
    )

    with open(result_file, "w", encoding="utf-8") as f:
        f.write(header)


def write_test_result(result_file, test_num, result_data):
    """Append a single test result to the markdown file. Called IMMEDIATELY after each test."""
    meta = TESTS[test_num]
    rd = result_data

    # Compute F_missing
    required = F_REQUIRED.get(test_num, [])
    f_actual_list = [f.strip() for f in rd.get("f_actual_str", "").split(",") if f.strip() and f.strip() != "—"]
    f_missing = []
    for req_path in required:
        found = False
        for actual in f_actual_list:
            if actual.replace("\\", "/").endswith(req_path.replace("\\", "/").split("/")[-1]):
                found = True
                break
        if not found:
            f_missing.append(req_path)
    f_missing_str = ", ".join(f_missing) if f_missing else "—"

    section = (
        f"## Тест {test_num}. {meta['name']} ({meta['complexity']})\n"
        f"\n"
        f"### Основные метрики\n"
        f"| Метрика | Значение |\n"
        f"|---------|----------|\n"
        f"| task_id | {rd.get('task_id', '—')} |\n"
        f"| Статус | {rd['status']} |\n"
        f"| Pass@1 | {rd['pass1']} |\n"
        f"| Время | {rd['time_sec']} сек |\n"
        f"| Build итераций | {rd.get('build_iterations', '—')} |\n"
        f"| Completeness | {rd['completeness_str']} |\n"
        f"| Токены (total) | {rd.get('token_total', '—')} |\n"
        f"\n"
        f"### Файлы\n"
        f"| Метрика | Значение |\n"
        f"|---------|----------|\n"
        f"| F_actual | {rd['f_actual_str']} |\n"
        f"| F_required | {rd['f_required_str']} |\n"
        f"| F_missing | {f_missing_str} |\n"
        f"\n"
        f"### RAG контекст\n"
        f"| Метрика | Значение |\n"
        f"|---------|----------|\n"
        f"| task_type | {rd.get('rag_task_type', '—')} (confidence: {rd.get('rag_confidence', '—')}) |\n"
        f"| Примеров загружено | {rd.get('rag_examples_count', '—')} |\n"
        f"| Template | {rd.get('rag_template_name', '—')} |\n"
        f"\n"
        f"### Валидация\n"
        f"| Проверка | Результат |\n"
        f"|----------|----------|\n"
        f"| API status | {rd.get('api_status', '—')} |\n"
        f"| F_actual.length > 0 | {'✅' if f_actual_list else '❌'} ({len(f_actual_list)} файлов) |\n"
        f"| F_actual ∩ F_required > 0 | {'✅' if not f_missing or len(f_missing) < len(required) else '❌'} |\n"
        f"| Итоговый статус | **{rd['status']}** |\n"
        f"\n"
        f"### Анализ\n"
        f"{rd['analysis']}\n"
        f"\n"
        f"---\n\n"
    )

    with open(result_file, "a", encoding="utf-8") as f:
        f.write(section)


def write_run_summary(result_file, results):
    """Write summary table after all 15 tests."""
    total = len(results)
    passed = sum(1 for r in results.values() if r["pass1"] == 1)
    false_success = sum(1 for r in results.values() if r["status"] == "false_success")
    failed = sum(1 for r in results.values() if r["status"] in ("failed", "error"))
    timeouts = sum(1 for r in results.values() if r["status"] == "timeout")
    avg_time = sum(r["time_sec"] for r in results.values()) / max(total, 1)
    total_time = sum(r["time_sec"] for r in results.values())

    # Compute avg completeness
    completeness_values = [r["completeness_pct"] for r in results.values()]
    avg_completeness = sum(completeness_values) / max(len(completeness_values), 1)

    summary = (
        f"\n## Итоги прогона\n"
        f"\n"
        f"| Метрика | Значение |\n"
        f"|---------|----------|\n"
        f"| Всего тестов | {total} |\n"
        f"| Pass@1 | {passed}/{total} ({passed/max(total,1)*100:.0f}%) |\n"
        f"| False success | {false_success} |\n"
        f"| Failed | {failed} |\n"
        f"| Timeout | {timeouts} |\n"
        f"| Avg completeness | {avg_completeness:.1f}% |\n"
        f"| Avg time | {avg_time:.0f} сек |\n"
        f"| Total time | {total_time:.0f} сек ({total_time/60:.1f} мин) |\n"
        f"\n"
        f"### Сводная таблица\n"
        f"\n"
        f"| # | Тест | Сложность | Статус | Pass@1 | Completeness | Время |\n"
        f"|---|------|-----------|--------|--------|--------------|-------|\n"
    )

    for t in range(1, 16):
        if t in results:
            r = results[t]
            meta = TESTS[t]
            summary += (
                f"| {t} | {meta['name']} | {meta['complexity']} | "
                f"{r['status']} | {r['pass1']} | {r['completeness_str']} | "
                f"{r['time_sec']} сек |\n"
            )
        else:
            meta = TESTS[t]
            summary += f"| {t} | {meta['name']} | {meta['complexity']} | — | — | — | — |\n"

    summary += "\n"

    with open(result_file, "a", encoding="utf-8") as f:
        f.write(summary)

    log(f"\nSummary: Pass@1 = {passed}/{total}, Avg completeness = {avg_completeness:.1f}%, "
        f"Total time = {total_time:.0f}s")


# ---------------------------------------------------------------------------
# retest: replace specific test section in existing result file
# ---------------------------------------------------------------------------

def replace_test_in_file(result_file, test_num, new_result_data):
    """Replace a specific test section in an existing result file.

    Finds '## Тест N.' and replaces everything up to the next '---' separator.
    """
    if not os.path.isfile(result_file):
        log(f"  ERROR: {result_file} does not exist, cannot replace test {test_num}")
        return False

    with open(result_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Build the new section text (same format as write_test_result)
    meta = TESTS[test_num]
    rd = new_result_data
    required = F_REQUIRED.get(test_num, [])
    f_actual_list = [x.strip() for x in rd.get("f_actual_str", "").split(",") if x.strip() and x.strip() != "—"]
    f_missing = []
    for req_path in required:
        found = any(a.replace("\\", "/").endswith(req_path.replace("\\", "/").split("/")[-1]) for a in f_actual_list)
        if not found:
            f_missing.append(req_path)
    f_missing_str = ", ".join(f_missing) if f_missing else "—"

    new_section = (
        f"## Тест {test_num}. {meta['name']} ({meta['complexity']})\n"
        f"\n"
        f"### Основные метрики\n"
        f"| Метрика | Значение |\n"
        f"|---------|----------|\n"
        f"| task_id | {rd.get('task_id', '—')} |\n"
        f"| Статус | {rd['status']} |\n"
        f"| Pass@1 | {rd['pass1']} |\n"
        f"| Время | {rd['time_sec']} сек |\n"
        f"| Build итераций | {rd.get('build_iterations', '—')} |\n"
        f"| Completeness | {rd['completeness_str']} |\n"
        f"| Токены (total) | {rd.get('token_total', '—')} |\n"
        f"\n"
        f"### Файлы\n"
        f"| Метрика | Значение |\n"
        f"|---------|----------|\n"
        f"| F_actual | {rd['f_actual_str']} |\n"
        f"| F_required | {rd['f_required_str']} |\n"
        f"| F_missing | {f_missing_str} |\n"
        f"\n"
        f"### RAG контекст\n"
        f"| Метрика | Значение |\n"
        f"|---------|----------|\n"
        f"| task_type | {rd.get('rag_task_type', '—')} (confidence: {rd.get('rag_confidence', '—')}) |\n"
        f"| Примеров загружено | {rd.get('rag_examples_count', '—')} |\n"
        f"| Template | {rd.get('rag_template_name', '—')} |\n"
        f"\n"
        f"### Валидация\n"
        f"| Проверка | Результат |\n"
        f"|----------|----------|\n"
        f"| API status | {rd.get('api_status', '—')} |\n"
        f"| F_actual.length > 0 | {'✅' if f_actual_list else '❌'} ({len(f_actual_list)} файлов) |\n"
        f"| F_actual ∩ F_required > 0 | {'✅' if not f_missing or len(f_missing) < len(required) else '❌'} |\n"
        f"| Итоговый статус | **{rd['status']}** |\n"
        f"\n"
        f"### Анализ\n"
        f"{rd['analysis']}\n"
        f"\n"
        f"---\n"
    )

    # Find and replace the section using regex
    pattern = re.compile(
        rf"## Тест {test_num}\..+?(?=\n## Тест \d+\.|\n## Итоги прогона|\Z)",
        re.DOTALL,
    )
    match = pattern.search(content)
    if not match:
        log(f"  WARNING: Could not find '## Тест {test_num}.' section in {result_file}")
        return False

    content = content[:match.start()] + new_section + "\n" + content[match.end():]

    with open(result_file, "w", encoding="utf-8") as f:
        f.write(content)

    log(f"  Replaced test {test_num} in {result_file}")
    return True


def update_summary_in_file(result_file, stand):
    """Re-read all test sections from the file and rewrite the summary."""
    if not os.path.isfile(result_file):
        return

    with open(result_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Parse all test results from the file
    results = {}
    for test_num in range(1, 16):
        pattern = re.compile(
            rf"## Тест {test_num}\..+?"
            rf"\| Статус \| (.+?) \|.+?"
            rf"\| Pass@1 \| (\d+) \|.+?"
            rf"\| Время \| (\d+) сек \|.+?"
            rf"\| Completeness \| (.+?) \|",
            re.DOTALL,
        )
        m = pattern.search(content)
        if m:
            status = m.group(1).strip()
            pass1 = int(m.group(2))
            time_sec = int(m.group(3))
            compl_str = m.group(4).strip()
            # Parse completeness percentage
            pct_match = re.search(r"\((\d+(?:\.\d+)?)%\)", compl_str)
            compl_pct = float(pct_match.group(1)) if pct_match else 0.0
            results[test_num] = {
                "status": status,
                "pass1": pass1,
                "time_sec": time_sec,
                "completeness_str": compl_str,
                "completeness_pct": compl_pct,
            }

    if not results:
        log(f"  WARNING: Could not parse any test results from {result_file}")
        return

    # Remove old summary
    summary_pattern = re.compile(r"\n## Итоги прогона.*", re.DOTALL)
    content = summary_pattern.sub("", content)

    # Write updated content without summary
    with open(result_file, "w", encoding="utf-8") as f:
        f.write(content)

    # Append new summary
    write_run_summary(result_file, results)
    log(f"  Updated summary in {result_file}: Pass@1 = "
        f"{sum(1 for r in results.values() if r['pass1']==1)}/{len(results)}")


def run_retest(stand, port, retest_list, config, timeout):
    """Run specific tests in specific runs, replacing results in-place.

    retest_list: list of (run_num, test_num) tuples.
    """
    # Group by run_num
    by_run = {}
    for run_num, test_num in retest_list:
        by_run.setdefault(run_num, []).append(test_num)

    for run_num in sorted(by_run.keys()):
        tests = sorted(by_run[run_num])
        result_file = _result_file_path(stand, run_num)

        log(f"\n{'#'*60}")
        log(f"# RETEST: Run {run_num}, tests {tests}")
        log(f"# File: {result_file}")
        log(f"{'#'*60}")

        if not os.path.isfile(result_file):
            log(f"  ERROR: {result_file} does not exist. Cannot retest.")
            continue

        for test_num in tests:
            try:
                result_data = run_single_test(stand, port, test_num, config, timeout)
            except Exception as e:
                log(f"  UNHANDLED ERROR in test {test_num}: {e}")
                result_data = {
                    "status": "error", "pass1": 0, "time_sec": 0,
                    "completeness_str": "0/0 (0%)", "completeness_pct": 0.0,
                    "f_actual_str": "", "f_required_str": ", ".join(F_REQUIRED.get(test_num, [])),
                    "analysis": f"Необработанная ошибка при retest: {e}",
                }

            replace_test_in_file(result_file, test_num, result_data)

        # Update summary for this run
        update_summary_in_file(result_file, stand)

    log(f"\nRetest complete for stand {stand}.")


# ---------------------------------------------------------------------------
# find_resume_point: check existing result file for completed tests
# ---------------------------------------------------------------------------

def find_resume_point(result_file):
    """Check existing result file for completed tests. Returns set of completed test numbers."""
    completed = set()
    if not os.path.isfile(result_file):
        return completed

    try:
        with open(result_file, "r", encoding="utf-8") as f:
            content = f.read()
        # Parse "## Тест N." headers
        for line in content.split("\n"):
            line = line.strip()
            if line.startswith("## Тест "):
                try:
                    # "## Тест 5. ContractCurrency ..."
                    num_str = line.split("## Тест ")[1].split(".")[0].strip()
                    completed.add(int(num_str))
                except (IndexError, ValueError):
                    pass
    except Exception as e:
        log(f"  WARNING: could not parse result file for resume: {e}")

    return completed


# ---------------------------------------------------------------------------
# Ollama mode switching
# ---------------------------------------------------------------------------

def warmup_ollama():
    """Send a warmup request to Ollama to pre-load model into VRAM."""
    log("  Warming up Ollama (loading model into VRAM)...")
    warmup_start = time.time()
    try:
        payload = json.dumps({
            "model": "qwen2.5-coder:14b",
            "prompt": "// Hello world\npublic class Test { }",
            "stream": False,
        }).encode("utf-8")
        req = urllib.request.Request(
            "http://localhost:11435/api/generate",
            data=payload,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        urllib.request.urlopen(req, timeout=600)  # up to 10 min for model load
        log(f"  Warmup done in {time.time() - warmup_start:.0f}s")
    except Exception as e:
        log(f"  Warmup failed ({time.time() - warmup_start:.0f}s): {e}")
        log("  Continuing anyway — first test may be slow.")


def switch_to_ollama(port):
    """Switch LLM mode to ollama for Ollama stands (F, H)."""
    log("  Switching LLM mode to ollama...")
    url = f"http://localhost:{port}/api/llm/config"

    # PUT to switch mode
    payload = json.dumps({"llm_mode": "ollama"}).encode("utf-8")
    try:
        req = urllib.request.Request(
            url, data=payload,
            headers={"Content-Type": "application/json"},
            method="PUT",
        )
        resp = urllib.request.urlopen(req, timeout=30)
        data = json.loads(resp.read().decode("utf-8"))
        log(f"  LLM mode switched: {data}")
    except Exception as e:
        log(f"  ERROR switching LLM mode: {e}")
        return False

    # GET to verify
    try:
        req = urllib.request.Request(url, method="GET")
        resp = urllib.request.urlopen(req, timeout=30)
        data = json.loads(resp.read().decode("utf-8"))
        mode = data.get("llm_mode", "unknown")
        log(f"  Verified LLM mode: {mode}")
    except Exception as e:
        log(f"  ERROR verifying LLM mode: {e}")
        return False

    if mode != "ollama":
        return False

    # Warmup: pre-load model into VRAM
    warmup_ollama()
    return True


# ---------------------------------------------------------------------------
# fetch_extended_metadata: tokens, RAG context from API
# ---------------------------------------------------------------------------

def fetch_extended_metadata(port, task_id):
    """Fetch extended metadata (tokens, RAG context) for a completed task.

    Returns dict with token_total, rag_task_type, rag_confidence,
    rag_examples_count, rag_template_name, build_iterations.
    """
    meta = {
        "token_total": 0,
        "rag_task_type": "—",
        "rag_confidence": 0.0,
        "rag_examples_count": 0,
        "rag_template_name": "—",
        "build_iterations": 0,
    }

    if not task_id:
        return meta

    # 1. Fetch tokens
    try:
        url = f"http://localhost:{port}/api/tasks/{task_id}/tokens"
        req = urllib.request.Request(url, method="GET")
        resp = urllib.request.urlopen(req, timeout=HTTP_TIMEOUT)
        data = json.loads(resp.read().decode("utf-8"))
        meta["token_total"] = data.get("total_tokens", 0) or data.get("total", 0)
    except Exception:
        pass  # Tokens are nice-to-have

    # 2. Fetch task details for RAG context
    try:
        url = f"http://localhost:{port}/api/tasks/{task_id}"
        req = urllib.request.Request(url, method="GET")
        resp = urllib.request.urlopen(req, timeout=HTTP_TIMEOUT)
        data = json.loads(resp.read().decode("utf-8"))

        # RAG context
        rag = data.get("rag_context") or {}
        meta["rag_task_type"] = rag.get("task_type", "—")
        meta["rag_confidence"] = rag.get("confidence", 0.0)
        examples = rag.get("examples") or []
        meta["rag_examples_count"] = len(examples)
        template = rag.get("template") or {}
        meta["rag_template_name"] = template.get("template_name") or template.get("name") or "—"

        # Build iterations (count coder steps)
        steps = data.get("steps") or data.get("pipeline_steps") or []
        meta["build_iterations"] = sum(
            1 for s in steps
            if isinstance(s, dict) and s.get("agent") == "coder"
        )
    except Exception:
        pass  # Best effort

    return meta


# ---------------------------------------------------------------------------
# Phase markers: wait + create
# ---------------------------------------------------------------------------

def _markers_dir():
    """Return path to test-stands/ where markers are stored."""
    return os.path.join(BASE_DIR, "test-stands")


def wait_for_phase_markers(stand):
    """Wait for required phase markers before starting tests.

    E.g., stand E waits for .phase1_complete, stand F waits for .phase2_complete.
    """
    required = PHASE_WAIT.get(stand, [])
    if not required:
        return

    markers_dir = _markers_dir()
    for marker_name in required:
        marker_path = os.path.join(markers_dir, marker_name)
        log(f"Waiting for phase marker {marker_name}...")
        poll_count = 0
        while not os.path.isfile(marker_path):
            time.sleep(30)
            poll_count += 1
            if poll_count % 20 == 0:  # Every 10 min
                log(f"  Still waiting for {marker_name} ({poll_count * 30}s elapsed)...")
        log(f"Phase marker {marker_name} found: {_read_marker(marker_path)}")


def _read_marker(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read().strip()
    except Exception:
        return "(unreadable)"


def create_session_marker(stand):
    """Create .session_X_complete marker after all runs are done."""
    markers_dir = _markers_dir()
    marker_path = os.path.join(markers_dir, f".session_{stand}_complete")
    now = datetime.now().isoformat()
    with open(marker_path, "w", encoding="utf-8") as f:
        f.write(f"{now} Session {stand} completed all {NUM_RUNS} runs\n")
    log(f"Session marker created: .session_{stand}_complete")


def try_create_phase_marker(stand):
    """Check if all stands in this phase are complete.

    If so, create phase marker and stop previous phase stands.
    """
    markers_dir = _markers_dir()

    # Find which phase this stand belongs to
    for phase_num, phase_info in PHASES.items():
        if stand not in phase_info["stands"]:
            continue

        # Check if all stands in this phase have completed
        all_done = True
        for s in phase_info["stands"]:
            session_marker = os.path.join(markers_dir, f".session_{s}_complete")
            if not os.path.isfile(session_marker):
                all_done = False
                break

        if all_done:
            phase_marker = os.path.join(markers_dir, phase_info["marker"])
            if not os.path.isfile(phase_marker):
                now = datetime.now().isoformat()
                with open(phase_marker, "w", encoding="utf-8") as f:
                    f.write(f"{now} Phase {phase_num} completed "
                            f"(stands: {','.join(sorted(phase_info['stands']))})\n")
                log(f"Phase marker created: {phase_info['marker']}")

                # Stop previous phase stands
                _stop_phase_stands(phase_num)

        break  # Found our phase


def _stop_phase_stands(completed_phase_num):
    """Stop docker compose for stands in the completed phase."""
    phase_info = PHASES.get(completed_phase_num)
    if not phase_info:
        return

    log(f"Stopping phase {completed_phase_num} stands: {sorted(phase_info['stands'])}")
    for s in sorted(phase_info["stands"]):
        compose_file = os.path.join(BASE_DIR, f"docker-compose.stand-{s.lower()}.yml")
        if os.path.isfile(compose_file):
            try:
                import subprocess
                subprocess.run(
                    ["docker", "compose", "-f", compose_file, "down"],
                    capture_output=True, timeout=120, cwd=BASE_DIR
                )
                log(f"  Stand {s} stopped")
            except Exception as e:
                log(f"  WARNING: could not stop stand {s}: {e}")


# ---------------------------------------------------------------------------
# run_single_test: full cycle for one test
# ---------------------------------------------------------------------------

def run_single_test(stand, port, test_num, config, timeout):
    """Run a single test: reset -> send -> poll -> collect -> evaluate.

    Returns result_data dict.
    """
    meta = TESTS[test_num]
    requirement = REQUIREMENTS[test_num]

    log(f"\n{'='*60}")
    log(f"Test {test_num}: {meta['name']} ({meta['complexity']})")
    log(f"{'='*60}")

    # Step 1: Reset source
    try:
        reset_stand(stand)
    except Exception as e:
        log(f"  ERROR during reset: {e}")
        return {
            "status": "error",
            "pass1": 0,
            "time_sec": 0,
            "completeness_str": "0/0 (0%)",
            "completeness_pct": 0.0,
            "f_actual_str": "",
            "f_required_str": ", ".join(F_REQUIRED.get(test_num, [])),
            "analysis": f"Ошибка при сбросе исходного кода: {e}",
        }

    # Step 2: Send task
    start_time = time.time()
    task_id = send_task(port, requirement, config)

    if not task_id:
        return {
            "status": "error",
            "pass1": 0,
            "time_sec": 0,
            "completeness_str": "0/0 (0%)",
            "completeness_pct": 0.0,
            "f_actual_str": "",
            "f_required_str": ", ".join(F_REQUIRED.get(test_num, [])),
            "analysis": "Не удалось отправить задачу (3 попытки)",
        }

    # Step 3: Poll until terminal
    api_response = poll_task(port, task_id, timeout)
    elapsed = int(time.time() - start_time)

    # Step 4: Collect changed files
    changed_files = get_changed_files(stand)
    log(f"  Changed files ({len(changed_files)}): {changed_files}")

    # Step 5: Compute completeness
    matched, total, pct, matched_list, required_list = compute_completeness(changed_files, test_num)

    # Step 6: Evaluate
    final_status, analysis = evaluate_result(api_response, changed_files, test_num)
    pass1 = 1 if final_status == "success" else 0

    # Step 7: Fetch extended metadata (tokens, RAG context)
    ext_meta = fetch_extended_metadata(port, task_id)

    result_data = {
        "status": final_status,
        "pass1": pass1,
        "time_sec": elapsed,
        "completeness_str": f"{matched}/{total} ({pct:.0f}%)",
        "completeness_pct": pct,
        "f_actual_str": ", ".join(changed_files) if changed_files else "—",
        "f_required_str": ", ".join(required_list),
        "analysis": analysis,
        "task_id": task_id,
        "api_status": api_response.get("status", "unknown"),
        "api_error": api_response.get("error", ""),
        # Extended metadata
        "token_total": ext_meta["token_total"],
        "build_iterations": ext_meta["build_iterations"],
        "rag_task_type": ext_meta["rag_task_type"],
        "rag_confidence": ext_meta["rag_confidence"],
        "rag_examples_count": ext_meta["rag_examples_count"],
        "rag_template_name": ext_meta["rag_template_name"],
    }

    log(f"  Result: status={final_status}, pass1={pass1}, "
        f"completeness={matched}/{total} ({pct:.0f}%), time={elapsed}s")

    return result_data


# ---------------------------------------------------------------------------
# run_full_pass: 15 tests with resume support
# ---------------------------------------------------------------------------

def run_full_pass(stand, port, run_num, config, timeout):
    """Run all 15 tests for a single pass. Supports resume from interrupted run."""
    result_file = _result_file_path(stand, run_num)
    completed_tests = find_resume_point(result_file)

    if completed_tests:
        log(f"\nResuming run {run_num}: already completed tests {sorted(completed_tests)}")
    else:
        write_run_header(result_file, stand, run_num, config)

    results = {}

    # Load existing results for summary (minimal — just mark as completed)
    for t in completed_tests:
        results[t] = {
            "status": "completed_prev",
            "pass1": -1,  # unknown from previous run
            "time_sec": 0,
            "completeness_str": "—",
            "completeness_pct": 0.0,
        }

    for test_num in range(1, 16):
        if test_num in completed_tests:
            log(f"\nSkipping test {test_num} (already completed in this run)")
            continue

        try:
            result_data = run_single_test(stand, port, test_num, config, timeout)
        except Exception as e:
            log(f"  UNHANDLED ERROR in test {test_num}: {e}")
            result_data = {
                "status": "error",
                "pass1": 0,
                "time_sec": 0,
                "completeness_str": "0/0 (0%)",
                "completeness_pct": 0.0,
                "f_actual_str": "",
                "f_required_str": ", ".join(F_REQUIRED.get(test_num, [])),
                "analysis": f"Необработанная ошибка: {e}",
            }

        # Write immediately after each test
        write_test_result(result_file, test_num, result_data)
        results[test_num] = result_data

        # Ollama: pause between tests to let GPU cool down and release memory
        if stand in OLLAMA_STANDS and test_num < 15:
            log(f"  Ollama cooldown: sleeping 15s...")
            time.sleep(15)
        log(f"  Result written to {result_file}")

    # Write summary (only for non-resumed tests or if all done)
    summary_results = {k: v for k, v in results.items() if v.get("pass1", -1) != -1}
    if summary_results:
        write_run_summary(result_file, summary_results)

    log(f"\nRun {run_num} complete. Results: {result_file}")
    return results


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def _parse_retest_arg(retest_str):
    """Parse --retest argument: '1:12,1:13,5:1-15' → [(1,12),(1,13),(5,1),(5,2),...(5,15)]"""
    result = []
    for part in retest_str.split(","):
        part = part.strip()
        if ":" not in part:
            continue
        run_str, tests_str = part.split(":", 1)
        try:
            run_num = int(run_str)
        except ValueError:
            continue
        if "-" in tests_str:
            lo, hi = tests_str.split("-", 1)
            try:
                for t in range(int(lo), int(hi) + 1):
                    result.append((run_num, t))
            except ValueError:
                continue
        else:
            try:
                result.append((run_num, int(tests_str)))
            except ValueError:
                continue
    return result


def main():
    parser = argparse.ArgumentParser(
        description="Universal hypothesis test runner for dotnet-multiagent-system",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  python scripts/hyp-run-tests.py C 8020 1\n"
            "  python scripts/hyp-run-tests.py C 8020 all --timeout 900\n"
            "  python scripts/hyp-run-tests.py F 8050 1 --timeout 1800\n"
            "  python scripts/hyp-run-tests.py D 8030 1 --retest 1:12,1:13,3:13,5:1-15\n"
        ),
    )
    parser.add_argument("stand", type=str, help="Stand letter (A-H)")
    parser.add_argument("port", type=int, help="Multiagent API port")
    parser.add_argument("run", type=str, help="Run number (1-5) or 'all'")
    parser.add_argument("--timeout", type=int, default=None,
                        help="Timeout per test in seconds (default: 600, Ollama: 1800)")
    parser.add_argument("--retest", type=str, default=None,
                        help="Retest specific tests: 'run:test,...' e.g. '1:12,1:13,5:1-15'")

    args = parser.parse_args()

    stand = args.stand.upper()
    port = args.port

    if stand not in STAND_CONFIG:
        log(f"ERROR: Unknown stand '{stand}'. Valid: {sorted(STAND_CONFIG.keys())}")
        sys.exit(1)

    config = STAND_CONFIG[stand]

    # Determine timeout
    if args.timeout is not None:
        timeout = args.timeout
    elif stand in OLLAMA_STANDS:
        timeout = OLLAMA_DEFAULT_TIMEOUT
    else:
        timeout = DEFAULT_TIMEOUT

    # Determine runs
    if args.run.lower() == "all":
        runs = list(range(1, NUM_RUNS + 1))
    else:
        try:
            run_num = int(args.run)
            if run_num < 1 or run_num > NUM_RUNS:
                log(f"ERROR: run must be 1-{NUM_RUNS} or 'all'")
                sys.exit(1)
            runs = [run_num]
        except ValueError:
            log(f"ERROR: invalid run '{args.run}', expected 1-{NUM_RUNS} or 'all'")
            sys.exit(1)

    desc = STAND_DESCRIPTIONS.get(stand, stand)
    log(f"{'='*60}")
    log(f"Hypothesis Test Runner")
    log(f"Stand: {stand} ({desc})")
    log(f"Port: {port}")
    log(f"Runs: {runs}")
    log(f"Timeout: {timeout}s per test")
    log(f"Config: {config}")
    log(f"{'='*60}")

    # Handle --retest mode
    if args.retest:
        retest_list = _parse_retest_arg(args.retest)
        if not retest_list:
            log("ERROR: could not parse --retest argument")
            sys.exit(1)

        log(f"\nRETEST MODE: {len(retest_list)} tests to re-run")
        for run_num, test_num in retest_list:
            log(f"  Run {run_num}, Test {test_num}")

        # For Ollama stands, switch LLM mode
        if stand in OLLAMA_STANDS:
            log("\nOllama stand detected — switching LLM mode...")
            ok = switch_to_ollama(port)
            if not ok:
                log("WARNING: Failed to switch to Ollama mode.")

        try:
            run_retest(stand, port, retest_list, config, timeout)
        except KeyboardInterrupt:
            log("\n\nInterrupted by user.")
            sys.exit(130)

        log("\nRetest complete.")
        sys.exit(0)

    # Normal mode: wait for phase markers
    wait_for_phase_markers(stand)

    # For Ollama stands, switch LLM mode before starting
    if stand in OLLAMA_STANDS:
        log("\nOllama stand detected — switching LLM mode...")
        ok = switch_to_ollama(port)
        if not ok:
            log("WARNING: Failed to switch to Ollama mode. Continuing anyway.")

    # Run tests
    for run_num in runs:
        log(f"\n{'#'*60}")
        log(f"# RUN {run_num} of {len(runs)}")
        log(f"{'#'*60}")

        try:
            run_full_pass(stand, port, run_num, config, timeout)
        except KeyboardInterrupt:
            log("\n\nInterrupted by user. Results saved up to last completed test.")
            sys.exit(130)
        except Exception as e:
            log(f"\nFATAL ERROR in run {run_num}: {e}")
            # Continue to next run
            continue

    log("\nAll runs complete.")

    # Create session completion marker
    create_session_marker(stand)

    # Try to create phase marker (if all stands in this phase are done)
    try_create_phase_marker(stand)


if __name__ == "__main__":
    main()
