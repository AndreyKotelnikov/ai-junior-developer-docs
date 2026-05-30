# Детальная архитектура — семь функциональных колонок

**Назначение**: дать полную детализацию компонентов системы AI Junior Developer по семи функциональным колонкам — с указанием конкретных агентов, эндпоинтов, моделей и потоков данных через 12 стадий пайплайна.

**Связанные документы**:
- [`PROJECT_ARCHITECTURE.md`](PROJECT_ARCHITECTURE.md) — высокоуровневая архитектура: 4 микросервиса.
- [`decisions/`](decisions/README.md) — 8 Architecture Decision Records.
- [`components/ui.md`](components/ui.md) — описание веб-интерфейса.

Документ раскрывает архитектуру из **4 микросервисов** и **11 функциональных блоков**, сгруппированных в 7 функциональных колонок. Развёртывание — 15 контейнеров Docker Compose.

---

## 1. Семь функциональных колонок

| # | Колонка | Микросервис(ы) | Функциональные блоки |
|:-:|---|---|---|
| 1 | Веб-интерфейс | `ui` | блок 1 |
| 2 | RAG-сервис | `rag-service` | блок 2 (+ блок 6 deprecated) |
| 3 | Мультиагентная система | `multiagent` | блок 3 |
| 4 | Программные компоненты | `multiagent` | блок 7 |
| 5 | Roslyn-граф и .NET-приложение | `roslyn-graph`, `dotnet-app` | блоки 4, 5 |
| 6 | Аудит и инфраструктура | `postgres`, `multiagent` | блоки 8, 9, 10 |
| 7 | LLM-движок | внешний (Anthropic) или `ollama` | блок 11 |

---

## 2. Колонка 1 — Веб-интерфейс

| Параметр | Значение |
|---|---|
| Микросервис | `ui` — React 18 + TypeScript + Vite + Nginx 1.25, порт 8501 |
| Назначение | ввод требования, выбор LLM-режима, мониторинг 16 этапов в реальном времени, просмотр diff и метрик |
| Каналы | обратный прокси `/api/* → multiagent:8000`; WebSocket `/ws/progress/{task_id}` |
| Страницы | `Agents`, `History`, `Patterns`, `Compliance`, `Onboard` |

Детали — [`components/ui.md`](components/ui.md).

---

## 3. Колонка 2 — RAG-сервис

| Параметр | Значение |
|---|---|
| Микросервис | `rag-service` — Python 3.11 + FastAPI + E5-multilingual + rank-bm25, порт 8100 |
| Назначение | классификация типа задачи (Zero-Retrain Router); гибридный поиск по корпусу 1 154 пар MR-diff |
| Поиск | E5-multilingual + BM25 + RRF + Cross-Encoder; MRR = 0,765 |
| Блок 6 (deprecated 13.04.2026) | исторический шестистадийный конвейер Pattern Extraction на SetFit-классификаторе (1,1 ГБ) |

---

## 4. Колонка 3 — Мультиагентная система

| Параметр | Значение |
|---|---|
| Микросервис | `multiagent` — Python 3.11 + FastAPI, порт 8000 |
| Назначение | оркестрация 7 актуальных агентов через LangGraph-DAG; точка входа `POST /api/tasks` |
| Изоляция состояния | per-task `RunContext` (dataclass + `ContextVar` PEP 567) |
| Агенты | Orchestrator, RoslynExplorer, Slim Coder, Coder расширенный, FixAgent, Tester исследовательский, ExplainerAgent (всего 9 ролей в таблице, 7 в production-цепочке) |

Детали по агентам — см. раздел «Мультиагентная система».

---

## 5. Колонка 4 — Программные компоненты

| Параметр | Значение |
|---|---|
| Микросервис | `multiagent` (блок 7) |
| AST-трансформеры | 10 детерминированных трансформеров типовых EF Core-операций |
| ProgrammaticFixer | 5 классов CS-ошибок (CS0246, CS0117, CS1061, CS0535, CS0738); ~ 60 % ошибок без LLM |
| Покрытие | на эталонной задаче «модификация сущности» — 12 из 13 подзадач (~ 92 %) без LLM |

Детали — [`../technical/programmatic-transformers.md`](../technical/programmatic-transformers.md).

---

## 6. Колонка 5 — Roslyn-граф и .NET-приложение

| Параметр | Значение |
|---|---|
| `roslyn-graph` | .NET 9 + Microsoft.CodeAnalysis + LibGit2Sharp 0.30.0 + ASP.NET Core 9 Minimal API, порт 8300 |
| Граф зависимостей | 4 типа рёбер: CALLS, INHERITS, USES_TYPE, COCHANGES |
| Эндпоинты | ~ 50 эндпоинтов в 14 функциональных категориях |
| `dotnet-app` | ASP.NET Core 3.1 + EF Core; 1 559 файлов, 253 сущности EF Core, фреймворк Visary |

Полный реестр эндпоинтов Roslyn-графа описан в технической документации проекта.

---

## 7. Колонка 6 — Аудит и инфраструктура

| Блок | Компонент | Назначение |
|:-:|---|---|
| 8 | Слой compliance-аудита | append-only `pipeline_audit` (17 столбцов в 4 группах); REVOKE на DML; SHA-256; OpenTimestamps; CLI `multiagent_replay` |
| 9 | Инфраструктура LLM-вызовов | Serial-Ollama Scheduler + ModelRouter + KVCacheManager; Slim Coder |
| 10 | Конвенции проекта | `project_conventions.json` (5 Pydantic-схем + JSON Schema 2020-12); auto-discovery 5 фокус-детекторами |

Детали по слою аудита — [`../technical/artifact_trace.md`](../technical/artifact_trace.md).

---

## 8. Колонка 7 — LLM-движок

| Режим | Модели |
|---|---|
| Облачный (Anthropic) | Claude Haiku 4.5 (`claude-haiku-4-5-20251001`, 200 K контекст, prompt caching) / Sonnet 4.5 через OpenRouter API |
| Локальный air-gapped (Ollama) | `qwen3:14b` (Orchestrator); `qwen2.5-coder:14b` (Coder, FixAgent, Explorer, Tester); `qwen2.5:3b` (ExplainerAgent) |

---

## 9. Двенадцать стадий пайплайна

Восемь укрупнённых фаз пайплайна на уровне технической реализации разворачиваются в 12 стадий:

| Фаза | Стадии |
|---|---|
| Phase 0 | классификация операции (`_classify_operation`, Zero-Retrain Router); построение пакета задачи (`_build_task_pack`) |
| Phase 1 | планирование Orchestrator |
| Phase 2 | три подфазы Roslyn-навигации: Localization → Signature extraction → Anchors |
| Phase 3 | кодирование Coder (приоритет ProgrammaticTransformer) |
| Phase 3.5 | инкрементальная семантическая валидация Roslyn |
| Fix-loop | ProgrammaticFixer → LLM FixAgent |
| Phase 4 | финальная сборка `dotnet build` |
| Phase 5 | пост-объяснение ExplainerAgent |

На каждом LLM-вызове параллельно срабатывает sidecar-журналирование в `pipeline_audit`. На стороне UI пайплайн представлен как 16 этапов.

---

## 10. Поддерживающие хранилища

| Хранилище | Порт | Назначение |
|---|:-:|---|
| PostgreSQL + pgvector 0.8 | 5432 | `pipeline_audit` (append-only) + контекст проектов |
| PostgreSQL + PostGIS | 5433 | база данных `dotnet-app` |
| Qdrant | 6333 / 6334 | векторная БД корпуса MR-diff |
| Ollama | 11434 / 11435 | локальный LLM-движок для air-gapped-режима |
