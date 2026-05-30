# UI Service

## Назначение

Веб-интерфейс мультиагентной системы генерации кода **AI Junior Developer**. React SPA. Предоставляет полный цикл работы с задачами:

- ввод бизнес-требования и конфигурацию пайплайна;
- выбор LLM-режима (OpenRouter API / Ollama on-prem);
- мониторинг в реальном времени через WebSocket;
- просмотр плана, кода, сборки и пост-объяснения от ExplainerAgent;
- compliance-аудит (`pipeline_audit`), byte-identical replay и нотаризация;
- онбординг нового .NET-проекта через auto-discovery конвенций;
- управление feature-flags на лету.

## Запуск локально

```bash
cd ui
npm install
npm run dev
```

Открыть `http://localhost:5173`. Бэкенд multiagent должен быть запущен на `http://localhost:8000` (см. `vite.config.ts` для proxy).

## Запуск через Docker

```bash
docker compose up -d ui
```

После старта UI доступен на `http://localhost/` через nginx из `docker-compose.yml`.

## Сборка production

```bash
cd ui
npm run build
```

Результат — статика в `ui/dist/`, обслуживается nginx-стадией Docker-образа.

## Тесты

```bash
cd ui
npm run test
```

## Оглавление

- [Два режима LLM](#два-режима-llm-openrouter-api-vs-ollama)
- [Страницы приложения](#страницы-приложения)
- [Пайплайн выполнения задачи](#пайплайн-выполнения-задачи-от-ввода-до-результата)
- [16 этапов пайплайна](#16-этапов-пайплайна)
- [Компоненты главной страницы](#компоненты-главной-страницы-agents)
- [Шесть вкладок центральной панели](#шесть-вкладок-центральной-панели)
- [TaskExplanation: пост-объяснение от ExplainerAgent](#taskexplanation-пост-объяснение-от-explaineragent)
- [Правая панель метрик](#правая-панель-метрик)
- [Compliance: аудит и replay](#compliance-аудит-и-replay)
- [Onboarding: подключение нового .NET-проекта](#onboarding-подключение-нового-net-проекта)
- [WebSocket](#websocket-реальное-время)
- [State Management](#state-management-zustand)
- [API-клиент](#api-клиент)
- [Сборка и деплой](#сборка-и-деплой)
- [Структура проекта](#структура-проекта)

---

## Два режима LLM: OpenRouter API vs Ollama

Система поддерживает два режима работы с языковыми моделями. Переключение выполняется в панели настроек (`SettingsPanel`) через компонент `LlmModeSwitcher`.

### OpenRouter API (облачный режим)

```
Кнопка: [Cloud] API / OpenRouter    — подсвечивается синим при выборе
```

- **Провайдер**: облачные модели через OpenRouter (Anthropic Claude Haiku 4.5 / Sonnet 4.5, GPT и др.).
- **Настройка**: переменные `OPENAI_API_KEY`, `OPENAI_BASE_URL` на бэкенде.
- **UI отображает**: текущую модель (`llmConfig.global.model`) и endpoint (`api_base`).
- **Переключение**: `PUT /api/llm/config` с `{ llm_mode: "api" }`.
- **Преимущества**: мощные модели, стабильный формат ответов, поддержка больших планов (34+ подзадач).
- **Ограничение**: запрещено для значимых объектов критической информационной инфраструктуры РФ (Указ Президента РФ № 166 от 30.03.2022); в этих сценариях выбирайте Ollama-режим.

### Ollama (локальный air-gapped режим, GPU 24+ ГБ)

```
Кнопка: [HardDrive] Ollama          — подсвечивается зелёным при выборе
```

- **Провайдер**: локальная модель через Ollama API (`http://host.docker.internal:11434`).
- **Рекомендуемые модели** (per-agent routing через `ModelRouter`):
  - Orchestrator: `qwen3:14b` (thinking-mode для декомпозиции).
  - Coder / FixAgent / Explorer / Tester: `qwen2.5-coder:14b`.
  - ExplainerAgent: `qwen2.5:3b` (lightweight для post-hoc summary).
- **Аппаратные требования**: минимум RTX 4090 24 ГБ для 14B моделей (Stand G); 48+ ГБ GPU (A100 / 2× RTX 4090) для 32B (Stand H).
- **OllamaScheduler**: single-worker priority queue с per-agent priority (orchestrator=1 → ... → explainer=7), KV-cache stats, `model_load_events` per-task; устраняет одновременную загрузку моделей в одну GPU.
- **Переключение**: `PUT /api/llm/config` с `{ llm_mode: "ollama" }`.
- **Применимость**: банки, госсектор, субъекты КИИ — где облачные API запрещены или критичен полный контроль над данными.

**Проверки перед переключением на Ollama**:
1. Запрос `GET /api/llm/ollama/status` — проверка доступности.
2. Если `status === 'offline'` → alert: «Ollama недоступен. Запустите контейнер ollama и загрузите модели.»
3. Если `models.length === 0` → alert: «В Ollama нет загруженных моделей. Выполните scripts/pull-ollama-models.ps1»
4. Только если обе проверки пройдены → `PUT /api/llm/config`.

**Индикаторы статуса Ollama** (рядом с кнопкой):

| Статус | Иконка | Текст |
|--------|--------|-------|
| `online` | Зелёная галочка | «{N} моделей» |
| `offline` | Красный крестик | «Недоступен» |
| `error` | Жёлтый треугольник | «Ошибка» |
| `loading` | Спиннер | «Проверка…» |

**Список загруженных моделей** (только в режиме Ollama + online):
- Отображается имя модели (`font-mono`) и размер в ГБ.
- Пример: `qwen2.5-coder:14b   8.7 GB`.

**Ошибка при активном Ollama + offline**:
- Красный баннер: «Ollama недоступен. Проверьте, что контейнер запущен и модели загружены.»

### Влияние режима на пайплайн

| Аспект | API (OpenRouter) | Ollama (локальный) |
|--------|------------------|--------------------|
| Скорость | Зависит от сети + очереди | Зависит от GPU (одна модель в памяти на запрос) |
| Качество планов | Высокое (Claude Haiku 4.5 / Sonnet 4.5) | Среднее (14B параметров) |
| EDIT-блоки | Стабильный формат | qwen2.5-coder:14b — стабильно |
| Стоимость | Платная (отображается в MetricsPanel) | Бесплатно (своё железо) |
| Конфиденциальность | Данные уходят в облако | Полностью air-gapped |
| Compliance с 152-ФЗ / 187-ФЗ для значимых объектов КИИ | ❌ (запрещено Указом № 166) | ✅ |
| Replay byte-identical | ~50 % (стохастичность Claude) | 100 % (Ollama+seed) |
| Промпты | Полные (`ORCHESTRATOR_SYSTEM_PROMPT`) | Сокращённые (`ORCHESTRATOR_OLLAMA_PROMPT`) + per-agent routing |
| Prompt cache | `cache_control: ephemeral` (Anthropic) — поддерживается | KV-cache reuse через `KVCacheManager` (готов, интеграция в Coder отложена) |

---

## Страницы приложения

Навигация через боковое меню (`Sidebar`, файл `src/components/layout/Sidebar.tsx`). Меню сворачивается (60px) / разворачивается (200px).

### 5 страниц + кнопка настроек

| Иконка | Название | Путь | Описание |
|--------|----------|------|----------|
| `Bot` | Agents | `/` | Главная — создание и мониторинг задач |
| `History` | History | `/history` | История выполненных задач с фильтрами |
| `Shapes` | Patterns | `/patterns` | Браузер RAG-паттернов и шаблонов |
| `ShieldCheck` | Compliance | `/compliance`, `/compliance/:runId` | Compliance-аудит, journal `pipeline_audit`, replay |
| `Compass` | Onboard | `/onboarding` | Подключение нового .NET-проекта (auto-discovery конвенций) |
| `Settings` | (Settings) | — slide-over | Кнопка открывает выдвижную панель настроек на странице Agents |

Страницы History, Patterns, Settings, Compliance и Onboarding загружаются лениво (`React.lazy`).

> **Compliance** и **Onboarding** добавлены в рамках задач D3 (Compliance-grade Audit Layer) и C2 (Auto-discovery conventions) плана улучшений `0.5_jd_improve_plan_results.md`.

---

## Пайплайн выполнения задачи (от ввода до результата)

### Полный пользовательский сценарий

```
┌─────────────────────────────────────────────────────────────┐
│ 1. ВВОД ТРЕБОВАНИЯ                                          │
│    Пользователь вводит текст или выбирает шаблон            │
│    Выбирает режим LLM (API / Ollama) в настройках           │
│    Настраивает этапы пайплайна (пресеты или вручную)        │
│    Нажимает [Запустить]                                     │
│                                                             │
│    → POST /api/tasks { requirement, settings, stages, ... } │
│    ← { task_id, status: "pending" }                         │
│    → WebSocket: ws://.../ws/progress/{task_id}              │
│    → Textarea сворачивается, UI переходит в режим монитора  │
└────────────────────────────┬────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────┐
│ 2. ROSLYN-EXPLORER (3 фазы, 0 LLM)                          │
│    Статусы: analyzing → exploring                           │
│                                                             │
│    UI: Explorer пульсирует зелёным в AgentPipeline          │
│    Локализация выполняется ЧЕРЕЗ ROSLYN GRAPH БЕЗ LLM       │
│    (weighted scoring: cochange × 3.0 + RAG × 1.5 +         │
│     graph × 2.0)                                            │
│                                                             │
│    Phase 1: Локализация файлов                              │
│    Phase 2: Извлечение сигнатур                             │
│    Phase 3: Якоря для вставки кода                          │
│                                                             │
│    Fallback на legacy LLM-Explorer при пустом результате    │
│    (feature-flag USE_ROSLYN_EXPLORER=false)                 │
└────────────────────────────┬────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────┐
│ 3. ORCHESTRATOR (план)        Статус: planning              │
│                                                             │
│    UI: авто-переключение на вкладку «План»                  │
│    План загружается через WS (details.plan) или REST        │
│    Каждая subtask содержит поле `why` (для ExplainerAgent)  │
│                                                             │
│    Если approvalRequired=true и autoApprove=false:          │
│    ┌─────────────────────────────────────────────┐          │
│    │ [!] План требует утверждения (N подзадач)   │          │
│    │                                             │          │
│    │ [✓ Утвердить] [✎ Редактировать] [✗ Отклонить]│         │
│    └─────────────────────────────────────────────┘          │
│                                                             │
│    Утвердить → POST /api/tasks/{id}/approve                 │
│    Отклонить → POST /api/tasks/{id}/cancel → cancelled      │
└────────────────────────────┬────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────┐
│ 4. CODER (генерация кода)     Статус: coding                │
│                                                             │
│    UI: авто-переключение на вкладку «Код»                   │
│                                                             │
│    Для каждой подзадачи pipeline пытается ПЕРВЫМ ПРИМЕНИТЬ  │
│    PROGRAMMATIC TRANSFORMER (10 детерминированных функций   │
│    AST→AST):                                                │
│      add_entity_registration, add_associated_entity,        │
│      add_one_to_many, add_owned_collection, add_using,      │
│      add_scalar_property, add_enum_value,                   │
│      register_di_service, register_filter, delete_file      │
│                                                             │
│    WS-событие `programmatic_transformer` отображает 92 %    │
│    типовых subtasks как «Без LLM-вызова, детерминированно». │
│                                                             │
│    Для оставшихся subtasks вызывается Slim Coder (LLM,      │
│    ~2.5K токенов; static (cached) + dynamic split) или      │
│    legacy Coder (custom_system_prompt в fix-loop).          │
│                                                             │
│    WS события file_modified → файлы появляются в CodeTab    │
│    WS события subtask_progress → счётчик «Задача 3/12»      │
└────────────────────────────┬────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────┐
│ 5. ROSLYN-ВАЛИДАЦИЯ (~6 сек)                                │
│    POST /api/diagnostics/semantic                           │
│    Долгоживущий MSBuildWorkspace; быстрее full build (~60c) │
│                                                             │
│    Если ошибки:                                             │
│      - PROGRAMMATIC FIXER пытается исправить 5 кодов CS     │
│        (CS0246, CS0117, CS1061, CS0535, CS0738)             │
│        Levenshtein ≤ 2 для CS0117/CS1061                    │
│        Critical safety: _is_active_subtask_target()         │
│        не даёт удалить ссылку на ещё-не-созданный файл      │
│                                                             │
│      - Что не закрывается → LLM FixAgent                    │
│                                                             │
│    WS-события: programmatic_fix, audit_call, build_result   │
└────────────────────────────┬────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────┐
│ 6. TESTER + DOTNET BUILD                                    │
│    Статусы: building → fixing → building → ...              │
│                                                             │
│    UI: авто-переключение на вкладку «Сборка»                │
│    WS события build_result → строки в BuildTab              │
│                                                             │
│    Попытка 1: ✗ 5 ошибок                                    │
│    Попытка 2: ✗ 2 ошибки (-3)                               │
│    Попытка 3: ✓ 0 ошибок — успех!                           │
│                                                             │
│    График тренда ошибок обновляется в реальном времени      │
│    Максимум 5 попыток сборки                                │
│                                                             │
│    Финальный шаг — `dotnet build` для контроля сборки       │
└────────────────────────────┬────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────┐
│ 7. EXPLAINER (post-hoc объяснение)  Статус: success         │
│                                                             │
│    ExplainerAgent (1 LLM-вызов, ≤400 tokens) формирует      │
│    JSON: { what_done, why, what_to_check[], source }        │
│                                                             │
│    UI: компонент `TaskExplanation` (collapsible)            │
│    показывает 3 секции с иконками:                          │
│      ✓ Что сделано                                          │
│      ◎ Зачем                                                │
│      ☑ Что проверить                                        │
│                                                             │
│    Реализует требования объяснимости:                       │
│      - Концепция развития ИИ в РФ (Указ Президента РФ № 490)│
│      - Принципы доверенного ИИ Альянса в сфере ИИ           │
│      - Приказ ФСТЭК № 235 § II.2 (журналирование действий)  │
└────────────────────────────┬────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────┐
│ 8. РЕЗУЛЬТАТ              Статус: success / failed          │
│                                                             │
│    UI: авто-переключение на вкладку «Лог»                   │
│    Фиксируется finishedAt, рассчитывается длительность      │
│    Токены подгружаются через REST                           │
│    MetricsPanel показывает итог: токены, стоимость, время   │
│                                                             │
│    SIDECAR: каждый LLM-вызов → INSERT в pipeline_audit      │
│    (append-only Postgres + restricted role + SHA-256 хеши)  │
│    run_id = task_id; доступен через страницу /compliance    │
│                                                             │
│    Кнопка [Запустить] заменяется на [Сброс]                 │
│    Textarea разблокируется для нового требования            │
│                                                             │
│    Browser Notification: «Task Complete»                    │
└─────────────────────────────────────────────────────────────┘
```

### 16 этапов пайплайна

Определены в `pipelineStore.ts` (с fallback на клиенте) и `stage_defaults.py` (бэкенд). Тип `StageKey` в `src/types/api.ts`:

| # | Этап | Описание | LLM | Агент / компонент |
|---|------|---------|-----|-------------------|
| 1 | `repo_map_build` | Построение карты классов и методов | Нет | — |
| 2 | `rag_enrichment` | Поиск паттернов в RAG | Нет | — |
| 3 | `read_structure` | Чтение `project_conventions.json` | Нет | — |
| 4 | `explorer_phase1` | Локализация файлов | **Нет** (через RoslynExplorer) | RoslynExplorer |
| 5 | `explorer_phase2` | Извлечение сигнатур | **Нет** | RoslynExplorer |
| 6 | `explorer_phase3` | Anchors для вставки кода | **Нет** | RoslynExplorer |
| 7 | `orchestrator_rag_context` | RAG-контекст для плана | Нет | — |
| 8 | `orchestrator_create_plan` | Генерация плана подзадач (с полем `why`) | Да | Orchestrator |
| 9 | `coding` | Slim Coder для творческих subtasks | Да | Coder |
| 10 | `roslyn_post_validation` | Roslyn-валидация (FK, DataConfig, Initializer) | Нет | Roslyn Graph |
| 11 | `programmatic_patches` | 10 трансформеров AST→AST (92 % subtasks) | **Нет** | ProgrammaticTransformers |
| 12 | `build_and_fix` | `dotnet build` + автоисправление (до 5 попыток) | Часть | Tester + LLM FixAgent |
| 13 | `programmatic_fix` | Фиксер 5 кодов CS-ошибок | **Нет** | ProgrammaticFixer |
| 14 | `unit_tests` | Запуск xUnit-набора T01..T25 — **только в режиме исследовательского эксперимента**; в production-сценарии не выполняется | Нет | — |
| 15 | `explainer` | Пост-объяснение «что / зачем / что проверить» | Да | ExplainerAgent |
| 16 | `run` | Запуск приложения для проверки | Нет | — |

> **Важно про `unit_tests`.** Этап доступен в pipeline-метаданных, но в реальном пользовательском сценарии (доработка кода по бизнес-требованию) **xUnit-набор T01..T25 не запускается**. Этот набор существует исключительно для повышения **достоверности измерений в факторном эксперименте** (9 стендов × 5 повторов × 15 задач = 675 наблюдений). При обычном production-прогоне pipeline завершается шагом `dotnet build` + `explainer`.

### Прогресс этапов (что обновляется на UI)

Бэкенд отправляет `stage_progress` события в основном для `coding`, `programmatic_patches`, `build_and_fix`, `programmatic_fix`. Для остальных этапов UI **выводит** статусы через маппинг `STATUS_TO_COMPLETED_STAGES` в `taskStore.ts`:

```
status=analyzing  → repo_map_build = done
status=exploring  → + rag_enrichment, read_structure, explorer_* = done
status=planning   → + orchestrator_rag_context = done
status=coding     → + orchestrator_create_plan = done
status=building   → + coding, programmatic_patches = done
status=success    → все 16 этапов = done
```

---

## Компоненты главной страницы (Agents)

Страница `AgentsPage` состоит из нескольких вертикальных секций и трёхколоночного рабочего пространства.

### Верхняя секция — ввод требования (`RequirementInput`)

**Textarea**: «Опишите бизнес-требование для доработки .NET приложения…»
- Минимальная высота: 72px, максимальная: 300px, resizable.
- Блокируется во время выполнения задачи (`disabled={isRunning}`).
- Сворачивается автоматически при старте задачи → кнопка разворачивания.

**Бейдж типа задачи**: после RAG-классификации (Zero-Retrain Router) отображается тип (например, `add_entity`, `modify_service`).

**Кнопки** (зависят от состояния):

| Состояние | Кнопки |
|-----------|--------|
| Нет задачи | `[Шаблон]` `[Настройки]` `[Демо]` `[Запустить]` |
| Задача выполняется | `[Настройки]` `[Стоп]` |
| Задача завершена | `[Настройки]` `[Сброс]` |

**Кнопка «Шаблон»** — выпадающий список из 8 категорий:

| Категория | Пример |
|-----------|--------|
| Добавление сущности | CustomerCategory с полями Название, Код, Приоритет, РодительскаяКатегория |
| Доработка сущности | Поля в ConstructionSiteAnalog: ТипАналога, КоэффициентКорректировки и др. |
| Добавление сервиса | NotificationService с методами Send, GetUnread, MarkAsRead |
| Доработка сервиса | CalculationService + RecalculateByPeriod, валидация, логирование |
| Фильтрация и сортировка | Фильтры для ConstructionObject: статус, дата, сортировка, пагинация |
| Исправление бага | BuildingPermit: теряется FK связь с ConstructionObject |
| Импорт/Экспорт | Экспорт ContractPayment в xlsx с заголовками на русском |
| Рефакторинг | DocumentApproval: извлечь Validator, перенести логику в сервис |

**Кнопка «Демо»** — запускает демо-режим с моковыми данными (`demo/demoMode.ts`).

**Кнопка «Запустить»** → `POST /api/tasks`:
```typescript
{
  requirement: "текст",
  project: "dotnet-app",
  use_rag: true,
  add_ef_migrations: false,
  rag_top_k: 3,
  rag_issue_iids: [123, 456] | null,
  use_patterns_only: false,
  agent_mode: "multi",   // или "single" — для Stand A baseline
  use_graph: true,       // RoslynExplorer + Roslyn-валидация
  stages: {
    "repo_map_build":      { enabled: true, custom_prompt: "" },
    "rag_enrichment":      { enabled: true, custom_prompt: "" },
    ...
  }
}
```

**Кнопка «Стоп»** → `POST /api/tasks/{taskId}/cancel` → статус `cancelled`.

**Кнопка «Сброс»** → `store.reset()` → очистка состояния, сохранение настроек.

### Панель настроек (`SettingsPanel`)

Выдвижная панель справа (400px, slide-over), вызывается кнопкой шестерёнки в Sidebar.

**Секции панели**:

#### 1. Режим LLM (`LlmModeSwitcher`)
Две кнопки-переключателя: `[API OpenRouter]` / `[Ollama]` + информация о текущей модели и статусе Ollama (см. секцию [Два режима LLM](#два-режима-llm-openrouter-api-vs-ollama)).

#### 2. Пресеты

Четыре кнопки быстрого конфигурирования пайплайна:

| Пресет | Описание | Отключённые этапы |
|--------|---------|-------------------|
| **Полный** | Все этапы включены | — |
| **Быстрый** | Без RAG и Roslyn | `rag_enrichment`, `orchestrator_rag_context`, `roslyn_post_validation` |
| **Только план** | Остановка после планирования | `coding`, `programmatic_patches`, `roslyn_post_validation`, `build_and_fix`, `programmatic_fix`, `explainer`, `run` |
| **Только код** | Без сборки и запуска | `build_and_fix`, `programmatic_fix`, `run` |

#### 3. Этапы пайплайна

Список из 16 этапов, каждый с:
- **Toggle switch** (вкл/выкл) — индиго при включении.
- **Метка «LLM»** (фиолетовый бейдж) — для этапов с LLM-вызовами.
- **Метка «Programmatic»** — для этапов с детерминированной логикой (transformers / fixer / RoslynExplorer).
- **Textarea кастомного промпта** — только для LLM-этапов, когда они включены.

#### 4. RAG настройки

| Настройка | Тип | По умолчанию | Описание |
|-----------|-----|--------------|----------|
| Только паттерны | Toggle | Выкл | Без MR-примеров из GitLab |
| Количество примеров | Slider 1–10 | 3 | RAG top-k |
| IID задач из GitLab | Text input | "" | Comma-separated: «123, 456, 789» |
| Миграции EF Core | Toggle | Выкл | Добавить миграции |

#### 5. Утверждение

| Настройка | По умолчанию | Описание |
|-----------|--------------|----------|
| Утверждать план перед кодогенерацией | Вкл | Показывать ApprovalGate |
| Автоматическое утверждение | Выкл | Пропускать ручное утверждение |

### Визуализация агентов (`AgentPipeline`)

Горизонтальная шкала из 4 верхнеуровневых ролей, отображающая основные фазы цикла:

```
[Explorer] ─── [Orchestrator] ─── [Coder] ─── [Tester]
  2.3k tok        3.5k tok          5.1k tok      1.5k tok
```

> **Примечание.** Под этими 4 «иконками-ролями» в текущей реализации работают **семь агентов** + детерминированные компоненты:
> - **RoslynExplorer** (0 LLM, заменил legacy LLM-Explorer);
> - **Orchestrator** (LLM, добавляет поле `why` к каждой подзадаче);
> - **Slim Coder** + **legacy Coder** (LLM с prompt caching) и **ProgrammaticTransformers** (10 функций AST→AST, без LLM);
> - **ProgrammaticFixer** (5 кодов CS, без LLM) + **FixAgent** (LLM-fallback);
> - **Tester** + **dotnet build**;
> - **ExplainerAgent** (5-й LLM-агент, post-hoc summary).
>
> На иконке `Coder` суммарно отображаются токены Slim Coder + legacy Coder + FixAgent. Пост-объяснение от ExplainerAgent отображается отдельно — компонентом `TaskExplanation` под главной рабочей областью.

**Статусы агентов** (определяются из `TaskStatus`):

| Агент | idle | waiting | active | done | error |
|-------|------|---------|--------|------|-------|
| Explorer | pending | — | analyzing/exploring | planning+ | — |
| Orchestrator | pending | analyzing/exploring | planning | coding+ | — |
| Coder | pending | analyzing-planning | coding | building+ | failed |
| Tester | pending | analyzing-coding | building/fixing | success | failed |

**Визуальные индикаторы**:
- Активный агент: анимированная иконка.
- Завершённый: зелёная галочка (overlay).
- Ошибка: красный восклицательный знак (overlay).
- Линии-коннекторы: подсвечиваются когда оба соседних агента active/done.
- Под иконкой: количество токенов в формате «2.3k tok».

### Метрики стадий (`PipelineMetrics`)

Прогресс-бары для каждого активного этапа с процентом и временем. Реагирует на WS-события `stage_progress`.

### Детали стадии (`StageDetails`)

Описание текущей выполняемой стадии. Показывает «Что происходит сейчас» — например, «ProgrammaticFixer применяет CS0246: добавление using к файлу X».

### Шлюз утверждения (`ApprovalGate`)

Жёлтый баннер, появляется при условиях:
- `status === 'planning'`
- `approvalRequired === true`
- `autoApprove === false`
- План загружен и содержит подзадачи.

**Содержимое баннера**:
```
[!] План требует утверждения          12 подзадач

Проверьте план на вкладке «План задач» перед началом кодогенерации.

[✓ Утвердить и продолжить]  [✎ Редактировать]  [✗ Отклонить]
```

| Кнопка | Действие |
|--------|----------|
| Утвердить и продолжить | `POST /api/tasks/{id}/approve` → переход к coding |
| Редактировать | Переключение на вкладку «План» |
| Отклонить | `POST /api/tasks/{id}/cancel` → статус cancelled |

### Трёхколоночная рабочая область

Появляется когда задача активна (`status !== null && status !== 'pending'`):

```
┌────────────┬─────────────────────────────┬──────────┐
│ SubtaskList│       CenterTabs            │  Metrics │
│  (левая)   │    (6 вкладок, центр)       │ (правая) │
│            │                             │          │
│ Задача 3/12│  [План] [Код] [RAG]         │ Токены   │
│ ○ Subtask 1│  [Сборка] [Лог] [Roslyn]    │ Файлы    │
│ ✓ Subtask 2│                             │ Качество │
│ ▶ Subtask 3│  (содержимое вкладки)       │ Инфра    │
│ ○ Subtask 4│                             │          │
│            │                             │          │
└────────────┴─────────────────────────────┴──────────┘
```

Под этим блоком после `success` появляется компонент `TaskExplanation` (см. отдельный раздел ниже).

### Левая панель — список подзадач (`SubtaskList`)

- Счётчик: «Задача 3 / 12».
- Список подзадач с иконками статуса:
  - `○` pending (серый)
  - `▶` in progress (синий/пульсирующий)
  - `✓` done (зелёный)
  - `✗` failed (красный)
- Текущая подзадача подсвечена.
- Каждая subtask показывает поле `why` в tooltip — для прозрачности перед reviewer'ом.
- Обновляется через WS-события `subtask_progress` и `programmatic_transformer`.

---

## Шесть вкладок центральной панели

Вкладки `CenterTabs` — 6 табов с иконками и бейджами-счётчиками.

### Бейджи на вкладках

| Вкладка | Бейдж |
|---------|-------|
| План | Число подзадач (e.g., `12`) |
| Код | Число изменённых файлов |
| Сборка | Зелёная/красная точка (статус последней сборки `dotnet build`) |
| Лог | Число сообщений прогресса |
| RAG, Roslyn | Без бейджа |

### Авто-переключение вкладок

При смене статуса задачи UI автоматически переключает активную вкладку:

| Новый статус | Вкладка |
|--------------|---------|
| `planning` | План |
| `coding` | Код |
| `building` / `fixing` | Сборка |
| `success` / `failed` | Лог |

Пользователь может переключить вкладку вручную — это переопределяет авто-переключение до следующей смены статуса.

### 1. Вкладка «План» (`PlanTab`)

**Два режима отображения** (переключатель `list` / `graph`):

**Список**:
- Строка на подзадачу: иконка статуса + заголовок + бейдж действия.
- Бейджи действий: `NEW` (create_new, зелёный), `MOD` (modify_existing, жёлтый), `SKIP` (verify_only, серый).
- Список `target_files` и `depends_on`.
- `exact_identifiers` — классы, методы, свойства.
- Поле `why` — пояснение, зачем выполняется подзадача (используется ExplainerAgent'ом и попадает в audit-лог).

**Граф** (DAG):
- Визуализация зависимостей через XYFlow + Dagre layout.
- Узлы раскрашены по статусу.
- Рёбра показывают зависимости `depends_on`.
- Длинные заголовки обрезаются (40 символов).

### 2. Вкладка «Код» (`CodeTab`)

**Левая часть — браузер файлов**:
- Фильтры: `[Все]` `[Созданные]` `[Изменённые]` `[Удалённые]`.
- Иконки с цветовой маркировкой: зелёный (created), жёлтый (modified), красный (deleted).
- Количество изменённых строк.
- Клик → просмотр diff.

**Правая часть — diff viewer**:
- Hunk-based отображение с заголовками (`@@ -10,5 +10,8 @@`).
- Номера строк (old/new) в колонках.
- Цветовая маркировка: зелёный (+added), красный (−removed), серый (context).
- Кнопка «Откатить» для каждого файла: `POST /api/tasks/{id}/files/{path}/revert`.

**Источник изменения файла** (визуальный индикатор — событие в логе):
- `programmatic_transformer` (детерминированно, без LLM) — иконка шестерёнки.
- `slim_coder` / `coder_legacy` — иконка LLM.
- `programmatic_fix` (CS0246/0117/1061/0535/0738) — иконка молотка.
- `fix_agent` (LLM-фикс) — иконка LLM + молотка.

**Нормализация действий**: бэкенд может отправлять варианты («create», «modify», «edit», «update», «delete»), UI нормализует к строгим значениям: `created` / `modified` / `deleted`.

### 3. Вкладка «RAG» (`RAGTab`)

Отображает RAG-контекст, полученный от RAG Service (Zero-Retrain Router):

- **Тип задачи**: бейдж (e.g., «add_entity»).
- **Уверенность**: 0–100 % (rule-engine match или LLM zero-shot fallback).
- **Чеклист** (`ChecklistItem[]`):
  - Слой (Entity Layer, Data Configuration, и др.).
  - Действие (что нужно сделать).
  - Уверенность и флаг required.
- **Шаблон** (`CodeTemplate`):
  - Имя шаблона.
  - Параметры (name, description, example).
  - Шаги (step, file_template, action, code_template).
- **Примеры из GitLab** (`RAGExample[]`):
  - Issue ID, заголовок, тип задачи.
  - Quality score, rerank score.
  - Количество изменённых файлов.
  - Кнопки feedback: thumbs up / thumbs down → `POST /api/tasks/{id}/rag/feedback`.
- **Hotspots**: критические точки кода.
- **Полный контекст**: текст для LLM (code-formatted блок).
- **Время**: search_time_ms, rerank_time_ms, total_time_ms.

### 4. Вкладка «Сборка» (`BuildTab`)

- **График тренда ошибок** (Recharts line chart):
  - X: номер попытки сборки.
  - Y: количество ошибок.
  - Визуализирует уменьшение/рост ошибок.
- **Список итераций сборки**:
  - Иконка: зелёная галочка (success) / красный крестик (failure).
  - Количество ошибок + дельта от предыдущей (`-3 ошибки`).
  - Раскрываемый блок с деталями ошибок.
- **Таблица ошибок** (последняя попытка):
  - Колонки: Code, File, Line:Column, Message.
  - Пример: `CS0246 | MyEntity.cs | 15:8 | The type 'StatusType' could not be found`.
  - Цветовая маркировка: коды CS, исправляемые `ProgrammaticFixer` (0246/0117/1061/0535/0738), помечены отдельным бейджем «programmatic».

### 5. Вкладка «Лог» (`LogTab`)

Потоковый вывод сообщений прогресса:
- Цветовая маркировка по типу:
  - `rag_enrichment` → синий.
  - `error` → красный.
  - `done` → зелёный.
  - `checklist` → зелёный/жёлтый.
  - `programmatic_transformer` / `programmatic_fix` → бирюзовый (детерминированные операции без LLM).
  - `audit_call` → фиолетовый (запись в `pipeline_audit`).
- Каждое сообщение: агент, этап, текст, процент, timestamp.
- Пагинация/виртуализация для 100+ сообщений.

### 6. Вкладка «Roslyn» (`RoslynTab`)

Результаты пост-валидации Roslyn (Roslyn Graph, ~50 endpoints):
- Проверки FK-пар (Foreign Key associations).
- Проверки регистрации в `DataConfiguration`.
- Проверки синтаксиса `Initializer.cs`.
- Классификация типов (entity/enum/service/DTO).
- Подсветка ошибок с путями и номерами строк.
- Cochange-визуализация: для каждого `target_file` — список файлов, исторически изменявшихся вместе (через `/api/tasks/{id}/cochange`).

---

## TaskExplanation: пост-объяснение от ExplainerAgent

Файл: `src/components/TaskExplanation.tsx`.

После завершения задачи в **success** статусе под рабочей областью появляется **collapsible** блок с разъяснением, сформированным `ExplainerAgent` (5-й LLM-агент, ~1500 prompt + ≤400 completion tokens).

### Источник данных

`TaskResponse.explanation` (тип `Explanation` в `types/api.ts`):
```typescript
{
  what_done: string;          // что сделано
  why: string;                // зачем
  what_to_check: string[];    // что проверить (чеклист)
  source: 'llm' | 'fallback'; // источник
}
```

При `source !== 'llm'` рядом с заголовком отображается бейдж — это сигнал, что использовался mechanically-generated fallback (например, при ошибке LLM или невалидном JSON).

### Содержимое

```
[▼] Объяснение изменений                       [Tests: 25/25 (100%)]
─────────────────────────────────────────────────────────────────
✓ Что сделано
   В сущность ConstructionSiteAnalog добавлены 10 новых полей,
   зарегистрированы навигационные свойства в DataConfiguration.cs
   и Initializer.cs.

◎ Зачем
   Бизнес-требование: расширить аналог для учёта параметров…

☑ Что проверить
   • Запустить тестовое создание сущности
   • Проверить FK constraints на полях RegionID, AnalogTypeID
   • Убедиться, что инициализация проходит без ошибок
```

### Бейдж исследовательских тестов (`UnitTestsBadge`)

В правом верхнем углу collapsible-заголовка может отображаться бейдж со сводкой `UnitTestSummary`:

```
Tests: 25/25 (100%)   — зелёный
Tests: 22/25 (88%)    — жёлтый при failed > 0
Tests: error          — красный при ошибке прогона
Tests: no matching    — серый при total = 0
```

> **Важно.** Бейдж с результатами `unit_tests` отображается **только в режиме исследовательского эксперимента** (факторный прогон 9 стендов × 5 повторов × 15 задач). В обычном production-сценарии (доработка кода по бизнес-требованию) набор T01..T25 не запускается, и бейдж не появляется. См. также раздел [16 этапов пайплайна](#16-этапов-пайплайна), п. 14.

### Compliance-обоснование

Компонент реализует требования объяснимости в российском регулировании:

- **Указ Президента РФ № 490 от 10.10.2019** «О развитии искусственного интеллекта в Российской Федерации» — раздел III «Принципы развития и использования ИИ»: *«Объяснимость работы ИИ и процесса достижения им результатов»*.
- **Принципы доверенного ИИ Альянса в сфере искусственного интеллекта** (РФ, 2021) — требование возможности независимого аудита решений системы.
- **Приказ ФСТЭК № 235 от 21.12.2017** § II.2 «Аудит безопасности» — журналирование действий и обоснований операций для значимых объектов КИИ.

Снижение reviewer-overhead на эталонной задаче: **~10 мин чтения diff → ~30 сек чтения summary**.

---

## Правая панель метрик

`MetricsPanel` (240px) содержит 4 суб-вкладки:

### Токены

- Прогресс-бары по агентам (цвет соответствует агенту):
  - Explorer (RoslynExplorer = 0 токенов; legacy LLM-Explorer показывает реальные).
  - Orchestrator.
  - Coder (Slim + legacy + FixAgent суммарно).
  - Tester (legacy LLM-Tester в обычном prod не активен; см. `USE_LLM_TESTER`).
  - ExplainerAgent (отдельно).
- Каждая полоса показывает долю от максимума + значение (e.g., `5.1k`).
- Итого: общее количество токенов.
- Стоимость: `$0.0374` (рассчитывается как `totalTokens * model_rate`).
- Модель: текущая модель (e.g., `claude-haiku-4.5`, `qwen2.5-coder:14b`).
- Бейдж «cache_control: ephemeral» для Anthropic, если static block был cached.

### Файлы

- Дедуплицированный список изменённых файлов.
- Цветные точки: зелёная (created), жёлтая (modified), красная (deleted).
- Имя файла (basename) + количество добавленных строк.
- Метка источника изменения: `programmatic` / `llm` / `fix`.

### Качество

- **Оценка X/10** — составная метрика:
  - Первая успешная сборка `dotnet build` = +10, вторая = +7, третья+ = +4.
  - RAG confidence > 0.8 = +2.
  - Все подзадачи done = +2.
  - Максимум: 10.
- **Roslyn вызовы** / **Text-search** — счётчики + соотношение (прогресс-бар).
- **RAG релевантность**: процент уверенности, наличие шаблона, количество примеров.
- **Чеклист регистрации**: DbContext, DI Container, EF Config, Initializer — зелёные/серые точки.
- **Консистентность кода**: high/medium/low — эвристика на основе соотношения файлов к подзадачам.
- **Programmatic ratio**: процент subtasks, выполненных через ProgrammaticTransformers (целевая цифра — 92 % на типовой modify-задаче).

### Инфра

- **Статус сервисов** (цветные пульсирующие точки):
  - Multiagent API — OK / ожидание.
  - dotnet-app — N сборок / ожидание.
  - RAG Service — running / unknown.
  - Qdrant — running / unknown.
  - Roslyn Graph (~50 endpoints, .NET 9) — running / unknown.
- **WebSocket**: подключён (зелёный) / отключен (красный).
- **OllamaScheduler stats** (только в Ollama-режиме, `GET /api/llm/scheduler/stats`):
  - `model_load_events` per-task (идеал = 1).
  - `call_count`, `queue_depth`, `current_model`.
  - Cache-hit rate (если KV-cache подключён к Slim Coder).
- **Audit-coverage**: количество записей в `pipeline_audit` для текущего run_id.
- **Инфраструктурные события**: container restart, 409, retry, OOM, exit_code — с timestamps.

---

## Compliance: аудит и replay

Файлы:
- `src/features/compliance/CompliancePage.tsx`
- `src/features/compliance/AuditFilterBar.tsx`
- `src/features/compliance/ReplayPanel.tsx`

### Назначение

Страница `/compliance` — UI для compliance-офицера / аудитора. Реализует требования:

- **152-ФЗ «О персональных данных»** ст. 19 — учёт обращений к ПДн.
- **187-ФЗ «О безопасности КИИ»** ст. 9 п. 3 — документирование инцидентов.
- **Приказ ФСТЭК № 235 от 21.12.2017** § II.2 — журналирование событий с retention ≥ 5 лет.
- **Приказ ФСТЭК № 239 от 25.12.2017** (актуализация Приказом № 159 от 28.08.2024) § VI.1 — целостность регистрационных записей.

### Список run-ов

Загружается через `GET /api/audit/runs?limit=50`. Если backend возвращает `configured: false` — показывается баннер «Audit-репозиторий не сконфигурирован», с подсказкой про переменные `AUDIT_DATABASE_URL` и `audit_enabled=true`.

Каждый run = `task_id` (UUID), сортированный по убыванию `created_at`. Клик по run → роутинг на `/compliance/{runId}` (deep-link).

### Просмотр записей run-а

Загружается через `GET /api/audit/runs/{run_id}?include_full=false`. Возвращает массив `AuditEntry`:

| Поле | Описание |
|------|----------|
| `id` | BIGSERIAL PRIMARY KEY |
| `sequence` | Порядковый номер LLM-вызова в run-е |
| `agent` | `orchestrator` / `coder` / `fix` / `explainer` / ... |
| `model` | `anthropic/claude-haiku-4.5` / `qwen2.5-coder:14b` / ... |
| `prompt_hash` | SHA-256 от `json.dumps(messages, sort_keys=True, ensure_ascii=False)` |
| `completion_hash` | SHA-256 от текста completion |
| `prompt_tokens` / `completion_tokens` | Счётчики |
| `git_commit_before` / `git_commit_after` | SHA до и после вызова |
| `subtask_id` / `subtask_why` | Контекст подзадачи (поле `why` от Orchestrator) |
| `timestamp_utc` / `duration_ms` | Время вызова |
| `metadata` | JSONB с дополнительными метаданными |
| `full_prompt` / `full_completion` | Полные тексты (только при `include_full=true`) |

### Фильтры (`AuditFilterBar`)

- **Agent** (dropdown) — фильтр по имени агента.
- **Model** (dropdown) — фильтр по модели.
- **Drift only** (toggle) — показать только записи с расхождением hash после replay.
- **Query** (text) — full-text по `prompt_hash`, `completion_hash`, `subtask_id`, `subtask_why`.

### Скачивание JSON

Кнопка `[Download]` на каждом run-е скачивает все записи как `audit-{run_id}.json` для предъявления регулятору.

### Replay (`ReplayPanel`)

Запуск повторного прогона того же run-а на тех же моделях / промптах:

```
POST /api/audit/runs/{run_id}/replay
Body: { do_call: true, json: false }
→ { replay_id, run_id, status: 'started' }
```

Прогресс отслеживается через:
- WebSocket `/ws/progress/{replay_id}` — события `replay_progress`.
- Polling `GET /api/audit/replays/{replay_id}` — fallback.

Каждая `ReplayResult` показывает:
- Sequence + agent.
- `match: bool` — совпадение `replay_hash === orig_hash`.
- Бейдж «OK» (зелёный) или «DRIFT» (красный).
- Original / replay hash.

### Метрики byte-identical replay

| LLM-провайдер | Замеренный показатель |
|---------------|----------------------|
| Claude Haiku 4.5 (Anthropic API) | ~50 % byte-identical (стохастичность модели ±1 token, документировано Anthropic) |
| Ollama + fixed seed (Stand G/H/I) | **100 % byte-identical** |

Для compliance-критичных сред рекомендуется Ollama-режим. Решение оформлено как ADR-007 (Append-only audit на restricted Postgres-роли).

### Предупреждение перед replay с реальным LLM-вызовом

`do_call=true` повторно тратит токены / ресурсы Ollama. UI показывает confirm-dialog: «Replay вызовет реальные LLM-запросы к моделям. Продолжить?»

Альтернатива: `do_call=false` — только повторный hash-расчёт без LLM-вызовов (для проверки целостности записи).

---

## Onboarding: подключение нового .NET-проекта

Файл: `src/features/onboarding/OnboardingPage.tsx`.

### Назначение

Страница `/onboarding` — мастер на 4 шага для подключения нового .NET-проекта к системе. Заменяет ранее обязательный ручной труд по составлению `PROJECT_ARCHITECTURE.md` (~3 дня для среднего проекта). Целевое время: **~4 часа**.

### Шаги мастера

```
[input] → [review] → [validate] → [apply]
```

#### Шаг 1. `input`

Поле «Путь к коду проекта»: например, `/app/code` (path внутри Roslyn Graph контейнера).

Кнопка **«Запустить auto-discovery»** → `POST /api/conventions/auto-discover`:
- Ответ — `DiscoveredConventions { ok, durationSec, filesScanned, parseErrors, conventions, error }`.
- 5 детекторов на стороне Roslyn Graph (.NET 9):
  - `AstPatternMiner` — типовые синтаксические паттерны.
  - `InitializerDetector` — object initializers.
  - `ExternalPackageDetector` — `.csproj` + Directory.Packages.props.
  - `EntityBaseTypeDetector` — иерархия domain entities.
  - `RegistrationPatternMiner` — паттерны DI-регистрации.
- Время выполнения: ~5 секунд на проект 1000–3000 файлов.

#### Шаг 2. `review`

Таблица `FieldRow` × N — каждое поле `project_conventions.json` показывается с:

- **Field**: путь к полю (`file_patterns.entity_dir_glob`, `registration_patterns[0].regex`, …).
- **Value**: значение (string / object / array).
- **Confidence**: процент уверенности (зелёный ≥ 80 %, жёлтый 50–80 %, красный < 50 %).
- **Warnings**: список замечаний (если auto-discovery нашёл что-то подозрительное).
- **Edit**: иконка карандаша → редактирование значения inline в textarea.

Recall на pilot-проектах:
- **dotnet-app** (1 386 файлов): **87.6 %** ✅.
- **eShopOnContainers** (499 файлов, microservices): 49 %.
- **ABP Framework** (3 317 файлов): 71 %.

Под таблицей: общая статистика — `files_scanned`, `duration_sec`, `parse_errors`.

#### Шаг 3. `validate`

Кнопка **«Валидировать конвенции»** → `POST /api/conventions/validate`:
- JSON-Schema проверка (`schema/project_conventions.schema.json`) + Pydantic-валидация на бэкенде.
- Ответ: `ConventionsValidation { ok, valid, errors[], warnings[], projectId, language, detail }`.
- Если `valid: false` → отображаются `errors[]` с указанием поля и причины. Можно вернуться на шаг `review` для правки.

#### Шаг 4. `apply`

Кнопка **«Сохранить конвенции»** → `POST /api/conventions/save`:
- Записывает финальный JSON в `project_conventions.json` (на стороне Roslyn Graph контейнера).
- Hot-reload без перезапуска сервиса (через `/api/conventions/load`).
- Возвращает `{ ok, saved, path, projectId }`.
- Показывает success-баннер с указанием пути.

### Архитектурное обоснование

Мастер реализует принцип «**human-in-the-loop**» из российских регуляторных документов:
- **Указ Президента РФ № 490 от 10.10.2019** (Концепция развития ИИ в РФ): сохранение контроля человека над критическими решениями.
- **Принципы доверенного ИИ Альянса в сфере ИИ** (РФ, 2021): обязательная возможность ручного review автоматических предложений системы.

Auto-discovery предлагает draft, но **не применяется автоматически** — оператор обязан проверить и при необходимости отредактировать значения с низкой уверенностью.

---

## WebSocket (реальное время)

### Подключение (`useWebSocket.ts`)

```
URL: ws://{host}/ws/progress/{taskId}?last_ts={timestamp}
```

| Параметр | Значение |
|----------|---------|
| Максимум переподключений | 10 |
| Базовая задержка | 1000 мс |
| Максимальная задержка | 10000 мс |
| Backoff | `min(1000 * 2^attempt, 10000)` |

### Ring Buffer Replay (восстановление после разрыва)

1. Каждое WS-сообщение содержит поле `ts` (timestamp).
2. Клиент сохраняет последний `ts` в `localStorage` (`ws_last_ts_{taskId}`).
3. При реконнекте передаётся `?last_ts={timestamp}`.
4. Бэкенд проигрывает все пропущенные сообщения из ring buffer (200 сообщений).

### F5-восстановление (перезагрузка страницы)

1. Zustand persist middleware восстанавливает состояние из `localStorage`.
2. `last_ts` загружается из `localStorage` → WebSocket replay.
3. План и RAG-контекст подгружаются через REST fallback (`GET /api/tasks/{taskId}`).
4. Токены подгружаются через REST (`GET /api/tasks/{taskId}/tokens`).

### Типы WS-событий

Объединённый тип `WSEvent` в `types/api.ts`. Type guards для каждого варианта (`isXxxEvent(e)`):

| Тип | Поле-маркер | Обработка на UI |
|-----|-------------|-----------------|
| `TaskProgress` | `task_id` + `step` (нет `event`) | Обновление статуса, плана, RAG, токенов |
| `file_modified` | `event: "file_modified"` | Добавление в `fileEvents`, отображение в CodeTab |
| `build_result` | `event: "build_result"` | Добавление в `buildEvents`, авто-переход на BuildTab |
| `stage_progress` | `event: "stage_progress"` | Обновление `stageStates` (percent, elapsed_ms) |
| `subtask_progress` | `event: "subtask_progress"` | Обновление счётчика подзадач и статуса в плане |
| `audit_call` | `event: "audit_call"` | Инкремент audit-счётчика; запись в `pipeline_audit` |
| `programmatic_transformer` | `event: "programmatic_transformer"` | Подсветка в логе; источник изменения файла = «programmatic» |
| `programmatic_fix` | `event: "programmatic_fix"` | Бейдж в BuildTab; код CS + файл |
| `roslyn_explorer` | `event: "roslyn_explorer"` | Сводка фаз + файлов (без LLM) |
| `model_load` | `event: "model_load"` | Обновление scheduler-метрики `model_load_events` |
| `cache_hit` | `event: "cache_hit"` | Обновление KV-cache hit rate |
| `replay_progress` | `event: "replay_progress"` | Live-обновление в `ReplayPanel` |

---

## State Management (Zustand)

### Хранилище `taskStore.ts`

Центральное хранилище на Zustand с persist-middleware.

**Ключ localStorage**: `dotnet-agent-studio-storage`.

**Персистируемые поля** (для F5-recovery):
- `taskId`, `requirement`, `settings`.
- `status`, `startedAt`, `finishedAt`.
- `stageStates` (время выполнения стадий).
- `progressMessages` (последние 100 — ограничение размера localStorage).
- `fileEvents`, `buildEvents`.
- `subtaskProgress` (current/total).
- `tokensByAgent`, `totalTokens`, `currentModel`.
- `plan`, `ragContext`.
- `explanation` (от ExplainerAgent), `unitTests` (исследовательские, см. оговорку).

**Настройки по умолчанию**:
```typescript
{
  useRag: true,
  addEfMigrations: false,
  ragTopK: 3,
  ragIssueIids: '',
  usePatternsOnly: false,
  stages: {},
  approvalRequired: true,
  autoApprove: false,
  project: 'dotnet-app',
  llmMode: 'api',          // ← режим LLM по умолчанию
  agentMode: 'multi',      // ← multi или single (Stand A baseline)
  useGraph: true,          // ← RoslynExplorer + Roslyn-валидация
}
```

### Хранилище `pipelineStore.ts`

Кэширует определения стадий пайплайна.
- Загрузка: `GET /api/pipeline/stages`.
- Fallback: 16 предопределённых стадий на клиенте (если бэкенд недоступен).

---

## API-клиент

Файл `api/client.ts` — fetch-based клиент. Все пути относительные (Vite proxy в dev / Nginx в prod).

### Эндпоинты

#### Базовые

| Метод | Путь | Описание |
|-------|------|----------|
| `GET` | `/health` | Проверка здоровья |
| `POST` | `/api/tasks` | Создание задачи |
| `GET` | `/api/tasks/{id}` | Получение задачи |
| `GET` | `/api/tasks` | Список задач |
| `POST` | `/api/tasks/{id}/cancel` | Отмена задачи |
| `POST` | `/api/tasks/{id}/approve` | Утверждение плана |
| `GET` | `/api/pipeline/stages` | Определения стадий |

#### Работа с файлами

| Метод | Путь | Описание |
|-------|------|----------|
| `GET` | `/api/tasks/{id}/files/{path}` | Содержимое файла |
| `GET` | `/api/tasks/{id}/files/{path}/diff` | Hunk-based diff файла |
| `POST` | `/api/tasks/{id}/files/{path}/revert` | Откат файла к git HEAD |

#### RAG

| Метод | Путь | Описание |
|-------|------|----------|
| `GET` | `/api/patterns/{type}` | Содержимое паттерна |
| `PUT` | `/api/patterns/{type}` | Сохранение паттерна |
| `POST` | `/api/patterns/{type}/test` | Тест паттерна |
| `GET` | `/api/patterns/stats` | Статистика покрытия |
| `POST` | `/api/tasks/{id}/rag/feedback` | Feedback на RAG-пример |
| `POST` | `/api/tasks/{id}/rag/rerun` | Перезапуск RAG-поиска |

#### LLM

| Метод | Путь | Описание |
|-------|------|----------|
| `GET` | `/api/llm/config` | Текущая LLM-конфигурация (per-agent routing) |
| `PUT` | `/api/llm/config` | Переключение режима LLM (api/ollama) |
| `GET` | `/api/llm/ollama/status` | Статус Ollama + список моделей |
| `GET` | `/api/llm/scheduler/stats` | OllamaScheduler stats (model_load_events, call_count, queue_depth) |
| `POST` | `/api/llm/scheduler/reset` | Сброс per-task scheduler-счётчиков |
| `GET` | `/api/tasks/{id}/tokens` | Расход токенов |

#### Compliance / Audit / Replay

| Метод | Путь | Описание |
|-------|------|----------|
| `GET` | `/api/audit/runs?limit=N` | Список последних run-ов |
| `GET` | `/api/audit/runs/{run_id}?include_full=bool` | Записи run-а (опционально с full_prompt/completion) |
| `POST` | `/api/audit/runs/{run_id}/replay` | Запуск replay job (background) |
| `GET` | `/api/audit/replays/{replay_id}` | Polling replay job |
| `GET` | `/api/audit/runs/{run_id}/replay/status` | Latest replay для run-а |

#### Cochange

| Метод | Путь | Описание |
|-------|------|----------|
| `GET` | `/api/tasks/{id}/cochange` | Cochange anchors для каждого target_file плана |

#### Feature flags

| Метод | Путь | Описание |
|-------|------|----------|
| `GET` | `/api/settings/flags` | Все feature flags + flag записи |
| `PUT` | `/api/settings/flags` | Обновление flags на лету (требует `ENABLE_RUNTIME_FLAG_OVERRIDE=true`) |

#### Onboarding (auto-discovery конвенций)

| Метод | Путь | Описание |
|-------|------|----------|
| `POST` | `/api/conventions/auto-discover` | Сканировать AST → draft conventions |
| `POST` | `/api/conventions/validate` | Валидация candidate conventions |
| `POST` | `/api/conventions/save` | Сохранение в `project_conventions.json` + hot-reload |

#### Проекты

| Метод | Путь | Описание |
|-------|------|----------|
| `GET` | `/api/projects` | Список проектов (silent fail → `['dotnet-app']`) |

### Обработка ошибок

- `ApiError` с HTTP-кодом.
- Silent fail для некритичных эндпоинтов:
  - `getPatternStats()` → `{}` при ошибке.
  - `listProjects()` → `['dotnet-app']` при ошибке.
  - `getOllamaStatus()` → `{ status: 'offline', models: [] }` при ошибке.
  - `sendRagFeedback()` → `undefined` при ошибке.
  - `getSchedulerStats()` → `{ scheduler_active: false, reason: 'connection failed' }`.
  - `listAuditRuns()` → `{ configured: false, runs: [] }`.
  - `getReplayStatusForRun()` → `null`.
  - `getTaskCochange()` → `{ task_id, anchors: [], configured: false }`.

---

## Сборка и деплой

### Docker (Multi-stage build)

```dockerfile
# Stage 1: Сборка SPA
FROM node:20-alpine AS builder
WORKDIR /app
COPY package.json package-lock.json* ./
RUN npm ci || npm install
COPY . .
RUN npm run build       # → dist/

# Stage 2: Nginx
FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 8501
CMD ["nginx", "-g", "daemon off;"]
```

### Nginx (reverse proxy)

| Location | Назначение | Таймаут |
|----------|-----------|---------|
| `/` | SPA assets (`try_files $uri /index.html`) | — |
| `/api/` | → `http://multiagent:8000/api/` | 300s read |
| `/health` | → `http://multiagent:8000/health` | 10s read |
| `/ws/` | → `http://multiagent:8000/ws/` (WebSocket upgrade) | 3600s read/send |
| `*.js,*.css,...` | Статические ассеты с кэшем | `expires 1y` |

Gzip включён для: `text/plain text/css application/json application/javascript text/xml image/svg+xml`.

### Технологический стек

| Технология | Версия | Назначение |
|------------|--------|-----------|
| React | 18.3 | UI-фреймворк |
| TypeScript | 5.6 | Типизация |
| Vite | 5.4 | Сборка + dev server |
| React Router | 6.20 | Клиентская маршрутизация |
| Zustand | 4.5 | State management + persist |
| Tailwind CSS | 3.4 | Стилизация |
| Radix UI | — | Headless-компоненты |
| Lucide React | — | Иконки |
| Framer Motion | 11 | Анимации |
| Recharts | 2.10 | Графики (тренд ошибок сборки) |
| Monaco Editor | — | Редактор кода |
| XYFlow | 12 | DAG-визуализация плана |
| Dagre | 0.8 | Алгоритм layout для DAG |

---

## Структура проекта

```
ui/
├── Dockerfile                      # Multi-stage: node:20 → nginx
├── nginx.conf                      # Reverse proxy + WebSocket
├── package.json                    # Node.js dependencies
├── vite.config.ts                  # Vite config + dev proxy
├── tsconfig.json                   # TypeScript config
│
├── src/
│   ├── main.tsx                    # React entry point
│   ├── App.tsx                     # Router: /, /history, /patterns, /settings, /compliance, /onboarding
│   ├── index.css                   # Tailwind directives + dark theme
│   │
│   ├── api/
│   │   └── client.ts              # Fetch-based API client (~40 endpoints)
│   │
│   ├── types/
│   │   └── api.ts                 # TypeScript типы (зеркало Pydantic-моделей)
│   │
│   ├── stores/
│   │   ├── taskStore.ts           # Zustand: состояние задачи, WS, токены, UI
│   │   └── pipelineStore.ts       # Zustand: определения 16 стадий (кэш)
│   │
│   ├── hooks/
│   │   ├── useWebSocket.ts        # WS-подключение, backoff, ring buffer replay
│   │   ├── useNotifications.ts    # Browser notifications
│   │   ├── useSessionRecovery.ts  # F5-восстановление
│   │   └── useKeyboardShortcuts.ts# Ctrl+Enter, Esc, 1-6 для вкладок
│   │
│   ├── components/
│   │   ├── layout/
│   │   │   ├── AppShell.tsx       # Обёртка: Sidebar + Header + content
│   │   │   ├── Header.tsx         # Верхняя навигация
│   │   │   └── Sidebar.tsx        # Левое меню: 5 пунктов + Settings, collapsible
│   │   ├── StatusBadge.tsx        # Цветной бейдж статуса задачи
│   │   ├── PulsingDot.tsx         # Анимированная цветная точка
│   │   ├── Timer.tsx              # Таймер длительности задачи
│   │   ├── AgentIcon.tsx          # Иконки 4 агентов с цветами и статусами
│   │   ├── TaskExplanation.tsx    # 🆕 Collapsible "Что/Зачем/Что проверить"
│   │   └── ui/                    # Headless UI кирпичи (Radix wrappers)
│   │
│   ├── features/
│   │   ├── agents/                # === Главная страница ===
│   │   │   ├── AgentsPage.tsx     # Компоновка: Input + Pipeline + 3-column
│   │   │   ├── RequirementInput.tsx# Textarea, шаблоны, кнопки Start/Stop/Reset
│   │   │   ├── AgentPipeline.tsx  # 4 агента с коннекторами и токенами
│   │   │   ├── CenterTabs.tsx     # 6 вкладок с бейджами
│   │   │   ├── SubtaskList.tsx    # Список подзадач (левая панель)
│   │   │   ├── MetricsPanel.tsx   # Метрики: токены/файлы/качество/инфра
│   │   │   ├── PipelineMetrics.tsx# Прогресс-бары стадий
│   │   │   ├── StageDetails.tsx   # Описание текущей стадии
│   │   │   ├── ApprovalGate.tsx   # Шлюз утверждения плана
│   │   │   ├── SettingsPanel.tsx  # Slide-over: LLM mode, пресеты, RAG, stages
│   │   │   ├── LlmModeSwitcher.tsx# Переключатель API ↔ Ollama
│   │   │   ├── templates.ts       # 8 шаблонов бизнес-требований
│   │   │   └── tabs/
│   │   │       ├── PlanTab.tsx    # Список/граф подзадач (XYFlow DAG)
│   │   │       ├── CodeTab.tsx    # Браузер файлов + hunk-based diff
│   │   │       ├── RAGTab.tsx     # Чеклист, шаблон, примеры, hotspots
│   │   │       ├── BuildTab.tsx   # Тренд ошибок (Recharts) + итерации
│   │   │       ├── LogTab.tsx     # Поток сообщений прогресса
│   │   │       ├── RoslynTab.tsx  # Roslyn-валидация
│   │   │       └── PlanGraph.tsx  # DAG через XYFlow + Dagre
│   │   │
│   │   ├── history/
│   │   │   └── HistoryPage.tsx    # История задач с фильтрами
│   │   ├── patterns/
│   │   │   └── PatternsPage.tsx   # Браузер RAG-паттернов
│   │   ├── settings/
│   │   │   └── SettingsPage.tsx   # Глобальные настройки
│   │   ├── compliance/            # 🆕 Compliance-аудит и replay
│   │   │   ├── CompliancePage.tsx # Список run-ов + фильтр + детали
│   │   │   ├── AuditFilterBar.tsx # Фильтры: agent / model / drift / query
│   │   │   └── ReplayPanel.tsx    # Запуск replay-job + WS-прогресс
│   │   └── onboarding/            # 🆕 Auto-discovery конвенций
│   │       └── OnboardingPage.tsx # 4 шага: input → review → validate → apply
│   │
│   ├── demo/
│   │   ├── demoMode.ts           # Демо-оркестрация (моковые данные)
│   │   └── mockData.ts           # Моковые прогресс/build события
│   │
│   └── lib/
│       └── utils.ts              # cn() — утилита Tailwind classnames
│
├── dist/                          # Сборка SPA (обслуживается Nginx)
└── public/                        # Статические ассеты
```

---

## Compliance scope

Обоснования архитектурно-инженерных решений ссылаются исключительно на **российское законодательство**:

- **152-ФЗ** «О персональных данных» от 27.07.2006 (актуальная редакция).
- **187-ФЗ** «О безопасности критической информационной инфраструктуры РФ» от 26.07.2017.
- **Приказ ФСТЭК № 235** от 21.12.2017.
- **Приказ ФСТЭК № 239** от 25.12.2017 (с актуализацией Приказом № 159 от 28.08.2024).
- **Указ Президента РФ № 490** от 10.10.2019 «О развитии искусственного интеллекта в Российской Федерации».
- **Указ Президента РФ № 166** от 30.03.2022 — запрет иностранного ПО на критической информационной инфраструктуре.
- **Принципы доверенного ИИ Альянса в сфере искусственного интеллекта** (РФ, 2021).
- **ГОСТ Р 34.11-2012** «Стрибог» (отечественный стандарт хеш-функции — опциональная альтернатива/дополнение к SHA-256).

Иностранные регуляторные акты в качестве обоснования архитектурных решений UI не используются.
