# Документация проекта AI Junior Developer

**Назначение папки `docs/`** — техническая база знаний проекта **AI Junior Developer**: архитектура системы, описания подсистем, конкурентный анализ, материалы факторного эксперимента, нормативные документы и описания пользовательского интерфейса. Папка собирает в одном месте все полные технические артефакты, по которым можно независимо проверить и воспроизвести результаты проекта.

**Цель этого файла** — дать читателю быстро сориентироваться: понять верхнеуровневую структуру `docs/` и за один-два перехода найти нужный документ.

---

## 1. О системе в двух абзацах

**AI Junior Developer** — корпоративный AI-инструмент автоматической доработки .NET-приложений (ASP.NET Core + Entity Framework Core) по бизнес-требованиям на естественном русском языке. Система ориентирована на регулируемый on-premise-сегмент российского рынка (банки, госсектор, субъекты КИИ) с учётом 152-ФЗ, 187-ФЗ и Приказов ФСТЭК № 235 и № 239.

Технически система состоит из четырёх микросервисов и трёх хранилищ; мультиагентный конвейер преобразует бизнес-требование в проверенный на сборку diff с пост-объяснением. Качество кодогенерации проверено факторным экспериментом (9 стендов × 5 повторов × 15 задач = 675 наблюдений).

---

## 2. Верхнеуровневая архитектура

```
┌─────────────────────────────────────────────────────────────┐
│  UI (React + TypeScript)         — веб-интерфейс, 5 страниц   │
└───────────────────────────┬─────────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────────┐
│  multiagent (FastAPI + Python)   — оркестрация агентов        │
│  ├── roslyn-graph (.NET 9)       — семантический анализ C#    │
│  ├── rag-service (Python)        — гибридный поиск примеров   │
│  └── audit-layer (pipeline_audit)— compliance-журналирование  │
└───────────────────────────┬─────────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────────┐
│  dotnet-app/src                  — целевой проект клиента     │
└───────────────────────────────────────────────────────────────┘

Хранилища и инфраструктура:
  PostgreSQL + pgvector  — журнал pipeline_audit, контекст проектов
  Qdrant                 — векторная база корпуса примеров
  Ollama                 — локальный LLM-движок (air-gapped режим)
```

Подробное описание каждого блока — в разделе [`architecture/`](#-architecture--архитектура-системы).

---

## 3. Карта папки `docs/`

Папка разбита на **7 тематических разделов**.

| Раздел | Отвечает на вопрос | Для кого |
|---|---|---|
| 🏗️ [`architecture/`](#-architecture--архитектура-системы) | Как устроена система? | Разработчики, архитекторы, эксперты |
| ⚙️ [`technical/`](#-technical--технические-артефакты-подсистем) | Что конкретно делает подсистема X и как считались метрики? | Разработчики ядра, интеграторы, рецензенты |
| 🥊 [`competitors/`](#-competitors--конкурентный-анализ) | Чем проект отличается от конкурентов? | Аналитики, эксперты, инвесторы |
| 🧪 [`experiment/`](#-experiment--материалы-факторного-эксперимента) | Как проверялись гипотезы и каковы результаты? | Рецензенты, исследователи |
| 🖼️ [`screenshots/`](#-screenshots--описания-экранов-интерфейса) | Что и как показано в интерфейсе? | UX-аналитики, заказчики |
| 📋 [`compliance/`](#-compliance--нормативное-соответствие) | Как соответствовать российскому регулированию? | Compliance-офицер, юрист |
| 📜 [`evolution/`](#-evolution--планы-развития) | Куда проект движется дальше? | Команда, инвестор |

---

## 4. Детальное содержимое разделов

### 🏗️ `architecture/` — архитектура системы

Как устроена система целиком и каждый её компонент.

| Файл | Содержание |
|---|---|
| [`PROJECT_ARCHITECTURE.md`](architecture/PROJECT_ARCHITECTURE.md) | Архитектура целевого .NET-решения: структура папок, ключевые точки доработки, примеры из кода |
| [`detailed-architecture.md`](architecture/detailed-architecture.md) | Детальная схема архитектуры: 4 микросервиса; единый конвейер из **8 фаз = 12 стадий журнала = 16 этапов UI** (одна и та же логика на разных уровнях детализации) |
| [`ui_README.md`](architecture/ui_README.md) | Полное руководство по веб-интерфейсу: 5 страниц, 16 этапов пайплайна (UI-детализация тех же 8 фаз), WebSocket-протокол |
| [`components/ui.md`](architecture/components/ui.md) | Краткая компонентная карточка UI (полное руководство — `ui_README.md`) |
| [`codebase_complexity_summary.md`](architecture/codebase_complexity_summary.md) | Сводка сложности кодовой базы `dotnet-app` (1 559 файлов, 253 сущности EF Core) |
| [`pattern_extraction_README.md`](architecture/pattern_extraction_README.md) | Описание исторического конвейера извлечения паттернов из корпуса MR-diff |
| [`decisions/`](architecture/decisions/) | Каталог архитектурных решений: 8 файлов `ADR-001 … ADR-008` + `README.md`-оглавление (контекст и обоснование) |

### ⚙️ `technical/` — технические артефакты подсистем

Спецификации подсистем, методология эксперимента, расчётные скрипты, литература и пользовательские сценарии.

**Спецификации подсистем**

| Файл | Содержание |
|---|---|
| [`roslyn-graph-endpoints.md`](technical/roslyn-graph-endpoints.md) | Справочник ~50 эндпоинтов сервиса `roslyn-graph` в 14 категориях |
| [`programmatic-transformers.md`](technical/programmatic-transformers.md) | 10 детерминированных AST-трансформеров: параметры и примеры |
| [`ast_transformers_registry_full.md`](technical/ast_transformers_registry_full.md) | Реестр 10 AST-трансформеров и тестовое покрытие |
| [`visary_framework_conventions_full.md`](technical/visary_framework_conventions_full.md) | Полный каталог неявных конвенций корпоративного фреймворка |

**Методология факторного эксперимента**

| Файл | Содержание |
|---|---|
| [`metrics_methodology.md`](technical/metrics_methodology.md) | Единая методология расчёта метрик (формулы, параметры, пороги, мощность) |
| [`statistical_minimum.md`](technical/statistical_minimum.md) | Статистический минимум для читателя без подготовки (8 концептов) |
| [`glossary_statistics_metrics.md`](technical/glossary_statistics_metrics.md) | Глоссарий статистических и метрических терминов |
| [`triangulation_framework.md`](technical/triangulation_framework.md) | Соответствие гипотез методам и триангуляционный фреймворк вердиктов |
| [`robustness_methodology.md`](technical/robustness_methodology.md) | Робастность вторичных гипотез H2b/H4 (TOST, bootstrap, стратификация) |
| [`validity_threats.md`](technical/validity_threats.md) | Угрозы валидности (Cook & Campbell) и применённые митигации |
| [`completeness_ceiling.md`](technical/completeness_ceiling.md) | Проверка теоретического потолка Completeness (= 100 %) |
| [`run_protocol.md`](technical/run_protocol.md) | Протокол одного прогона эксперимента (9 шагов) |
| [`artifact_trace.md`](technical/artifact_trace.md) | Принципы трассировки артефактов «артефакт → шаг → результат» |

**Расчётные артефакты (скрипты и данные)**

| Файл | Содержание |
|---|---|
| [`compute_stats.py`](technical/compute_stats.py) | Расчёт основных статистик (Wilcoxon, Wilson, Cohen's d, ARR-bootstrap) |
| [`compute_power.py`](technical/compute_power.py) | Анализ статистической мощности (Монте-Карло) |
| [`compute_h3_mixed.py`](technical/compute_h3_mixed.py) | Mixed-effects-анализ гипотезы H3 |
| [`compute_robustness_stats.py`](technical/compute_robustness_stats.py) | Робастность H2b/H4 (TOST + bootstrap) |
| [`stats_report.md`](technical/stats_report.md) · [`stats_output.json`](technical/stats_output.json) · [`stats_output_robustness.json`](technical/stats_output_robustness.json) | Готовые статистики (отчёт + машиночитаемые сводки) |

**Литература и заимствования**

| Файл | Содержание |
|---|---|
| [`borrowed_patterns_full.md`](technical/borrowed_patterns_full.md) | Реестр заимствованных паттернов и авторская адаптация |
| [`neurosymbolic_literature_chain_full.md`](technical/neurosymbolic_literature_chain_full.md) | Цепочка литературы по нейросимвольной интеграции |
| [`ollama_model_research_full.md`](technical/ollama_model_research_full.md) | Сравнительный анализ 8 кандидатов локальных LLM |

**Сценарии и эксплуатация**

| Файл | Содержание |
|---|---|
| [`scenario_a_business_user_full.md`](technical/scenario_a_business_user_full.md) · [`scenario_b_compliance_officer_full.md`](technical/scenario_b_compliance_officer_full.md) · [`scenario_c_onboarding_admin_full.md`](technical/scenario_c_onboarding_admin_full.md) | Полные описания 3 пользовательских сценариев (А, Б, В) |
| [`cli_replay_manual.md`](technical/cli_replay_manual.md) | Мануал CLI побайтового воспроизведения прогонов |
| [`stand_h_hardware_full.md`](technical/stand_h_hardware_full.md) | Аппаратная конфигурация air-gapped-стенда H |
| [`improvement_tasks_full.md`](technical/improvement_tasks_full.md) | Полные карточки 15 производственных задач плана улучшений |

### 🥊 `competitors/` — конкурентный анализ

Позиционирование проекта относительно конкурентов и внешних бейзлайнов.

| Файл | Содержание |
|---|---|
| [`research_gap_matrix.md`](competitors/research_gap_matrix.md) | Расширенная Research Gap Matrix: 45 систем × 7 структурных характеристик |
| [`GigaCode_Enterprise_on_premise.md`](competitors/GigaCode_Enterprise_on_premise.md) | Профиль ближайшего российского конкурента — GigaCode Enterprise on-premise |
| [`gigacode_vs_aijd_full.md`](competitors/gigacode_vs_aijd_full.md) | Развёрнутое сопоставление AI Junior Developer и GigaCode |
| [`external_baselines_comparison_full.md`](competitors/external_baselines_comparison_full.md) | Сравнение с внешними бейзлайнами: методология ARR, 16 строк, 32 источника |

### 🧪 `experiment/` — материалы факторного эксперимента

Тестовые задания, конфигурации стендов и сырые результаты прогонов.

| Файл / папка | Содержание |
|---|---|
| [`0.1_tests.md`](experiment/0.1_tests.md) | 15 тестовых заданий `modify_entity` со стратификацией и эталонными F_required |
| [`task_type_selection.md`](experiment/task_type_selection.md) | Обоснование выбора типа задач `modify_entity` (26 % корпуса) |
| [`design_rationale.md`](experiment/design_rationale.md) | Обоснование отбора 9 из 12 multi-конфигураций стендов |
| [`rag_corpus.md`](experiment/rag_corpus.md) | Паспорт корпуса для RAG (1 154 пары MR-diff, индексация, гибридный поиск) |
| [`hyp-run-tests.py`](experiment/hyp-run-tests.py) | Скрипт прогона тестовых заданий по стендам |
| [`stand_configs/`](experiment/stand_configs/) | 9 Docker Compose-конфигураций стендов A–I факторного эксперимента + `README.md` с описанием технического каркаса и параметров инференса |
| [`test_results/`](experiment/test_results/) | 45 файлов сырых результатов прогонов (`stand-{A–I}-run-{1–5}.md`) — полная сетка 675 наблюдений |

### 🖼️ `screenshots/` — описания экранов интерфейса

Восемь подробных описаний ключевых экранов веб-интерфейса:

| Файл | Экран |
|---|---|
| [`ui_main_agents.md`](screenshots/ui_main_agents.md) | Главная страница `Agents` (завершённый прогон add_entity, 4/4 подзадач) |
| [`ui_build_tab.md`](screenshots/ui_build_tab.md) | Вкладка «Сборка» и блок `TaskExplanation` |
| [`ui_compliance.md`](screenshots/ui_compliance.md) | Страница `/compliance`: журнал аудита и воспроизведение |
| [`ui_onboarding.md`](screenshots/ui_onboarding.md) | Мастер онбординга нового проекта |
| [`ui_settings.md`](screenshots/ui_settings.md) | Панель настроек запуска |
| [`ui_approval_gate.md`](screenshots/ui_approval_gate.md) | Шлюз утверждения `ApprovalGate` |
| [`ui_dag.md`](screenshots/ui_dag.md) | DAG-визуализация плана подзадач |
| [`ui_demo_mode.md`](screenshots/ui_demo_mode.md) | Демо-режим (8 шаблонов задач) |

### 📋 `compliance/` — нормативное соответствие

| Файл | Содержание |
|---|---|
| [`compliance-matrix.md`](compliance/compliance-matrix.md) | Матрица нормативного соответствия: 13 требований (152-ФЗ, 187-ФЗ, Приказы ФСТЭК № 235/239, Указ № 490) с механизмом и статусом; сертификация ФСТЭК — задача R15 |
| [`categorisation_act.md`](compliance/categorisation_act.md) | Акт категорирования объекта КИИ (III категория, 187-ФЗ ст. 7) |

### 📜 `evolution/` — планы развития

| Файл | Содержание |
|---|---|
| [`milestones/2026-Q3-future.md`](evolution/milestones/2026-Q3-future.md) | Эволюционный roadmap проекта на Q3 2026 и далее |

---

## 5. Быстрый старт по роли читателя

**🏗️ Разработчик системы**
→ [`architecture/PROJECT_ARCHITECTURE.md`](architecture/PROJECT_ARCHITECTURE.md) → [`architecture/detailed-architecture.md`](architecture/detailed-architecture.md) → [`architecture/decisions/README.md`](architecture/decisions/README.md) → [`technical/`](#-technical--технические-артефакты-подсистем)

**🧪 Рецензент / исследователь (проверка результатов)**
→ [`experiment/0.1_tests.md`](experiment/0.1_tests.md) → [`experiment/test_results/`](experiment/test_results/) → [`technical/metrics_methodology.md`](technical/metrics_methodology.md) → [`technical/stats_report.md`](technical/stats_report.md)

**🥊 Аналитик / эксперт (позиционирование)**
→ [`competitors/research_gap_matrix.md`](competitors/research_gap_matrix.md) → [`competitors/gigacode_vs_aijd_full.md`](competitors/gigacode_vs_aijd_full.md) → [`competitors/external_baselines_comparison_full.md`](competitors/external_baselines_comparison_full.md)

**📋 Compliance-офицер**
→ [`compliance/categorisation_act.md`](compliance/categorisation_act.md) → [`technical/cli_replay_manual.md`](technical/cli_replay_manual.md) → [`technical/scenario_b_compliance_officer_full.md`](technical/scenario_b_compliance_officer_full.md)

**🤝 Заказчик / UX-аналитик**
→ [`architecture/ui_README.md`](architecture/ui_README.md) → [`screenshots/`](#-screenshots--описания-экранов-интерфейса) → [`technical/scenario_a_business_user_full.md`](technical/scenario_a_business_user_full.md)

