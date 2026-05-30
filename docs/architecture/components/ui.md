# UI — пользовательский интерфейс

**Назначение**: фронтенд для конечного пользователя: ввод бизнес-требования, мониторинг прогресса в реальном времени, просмотр AI-сгенерированных изменений (diff), чтение объяснения и метрик, работа с историей, паттернами, аудитом (Compliance) и онбордингом нового проекта.

---

## 1. Технологический стек

- **React 18** + TypeScript.
- **Vite** для сборки.
- **TailwindCSS** + Radix UI компоненты.
- **TanStack Query** для асинхронного состояния.
- **Nginx 1.25** как обратный прокси и раздача статики, порт **8501**.

Обратный прокси перенаправляет `/api/* → multiagent:8000`, а также обеспечивает WebSocket-апгрейд для канала прогресса.

---

## 2. Пять страниц приложения

Интерфейс состоит из **пяти страниц** и выдвижной панели настроек. Страницы History, Patterns, Compliance и Onboarding загружаются лениво (`React.lazy`).

| Иконка | Страница | Маршрут | Назначение |
|---|---|---|---|
| `Bot` | Agents | `/` | Главная — создание и мониторинг задач |
| `History` | History | `/history` | История выполненных задач с фильтрами |
| `Shapes` | Patterns | `/patterns` | Браузер RAG-паттернов и шаблонов |
| `ShieldCheck` | Compliance | `/compliance`, `/compliance/:runId` | Compliance-аудит, журнал `pipeline_audit`, replay |
| `Compass` | Onboard | `/onboarding` | Подключение нового .NET-проекта (auto-discovery конвенций) |

Кнопка настроек открывает выдвижную панель (slide-over) на странице Agents.

---

## 3. Шестнадцать этапов пайплайна

Главная страница (Agents) отображает прогресс задачи в виде **16 этапов**. Этапы определены в `pipelineStore.ts` (клиент, с fallback) и `stage_defaults.py` (бэкенд).

| # | Этап | Описание | LLM | Агент / компонент |
|---|------|---------|-----|-------------------|
| 1 | `repo_map_build` | Построение карты классов и методов | Нет | — |
| 2 | `rag_enrichment` | Поиск паттернов в RAG | Нет | — |
| 3 | `read_structure` | Чтение `project_conventions.json` | Нет | — |
| 4 | `explorer_phase1` | Локализация файлов | Нет (через RoslynExplorer) | RoslynExplorer |
| 5 | `explorer_phase2` | Извлечение сигнатур | Нет | RoslynExplorer |
| 6 | `explorer_phase3` | Anchors для вставки кода | Нет | RoslynExplorer |
| 7 | `orchestrator_rag_context` | RAG-контекст для плана | Нет | — |
| 8 | `orchestrator_create_plan` | Генерация плана подзадач (с полем `why`) | Да | Orchestrator |
| 9 | `coding` | Slim Coder для творческих subtasks | Да | Coder |
| 10 | `roslyn_post_validation` | Roslyn-валидация (FK, DataConfig, Initializer) | Нет | Roslyn Graph |
| 11 | `programmatic_patches` | 10 трансформеров AST→AST (~92 % subtasks) | Нет | ProgrammaticTransformers |
| 12 | `build_and_fix` | `dotnet build` + автоисправление (до 5 попыток) | Часть | Tester + LLM FixAgent |
| 13 | `programmatic_fix` | Фиксер 5 кодов CS-ошибок | Нет | ProgrammaticFixer |
| 14 | `unit_tests` | Запуск xUnit-набора — только в режиме исследовательского эксперимента | Нет | — |
| 15 | `explainer` | Пост-объяснение «что / зачем / что проверить» | Да | ExplainerAgent |
| 16 | `run` | Запуск приложения для проверки | Нет | — |

> Этап `unit_tests` доступен в метаданных пайплайна, но в обычном пользовательском сценарии (доработка кода по бизнес-требованию) xUnit-набор не запускается — он существует только для повышения достоверности измерений в факторном эксперименте. При обычном прогоне пайплайн завершается шагом `dotnet build` + `explainer`.

---

## 4. Ключевые компоненты страницы Agents

### 4.1. `RequirementInput`

Форма ввода бизнес-требования, выбор LLM-режима (облачный / локальный air-gapped), кнопки «Запустить» и «Отменить».

### 4.2. `TaskExplanation`

Collapsible-секция с пост-объяснением от ExplainerAgent в трёх разделах:

```
┌─ Объяснение AI ─────────────────────────────┐
│ ▶ Что сделано                                │
│   - Добавлена сущность InspectionType с 4    │
│     полями: Code, Status, CurrentUser, Version│
│   - Зарегистрирована в DataConfiguration     │
│   - Зарегистрирована в Initializer           │
│ ▶ Зачем                                      │
│   - Code (string) — уникальный идентификатор │
│   - Status (enum) — управление жизненным циклом│
│ ▶ Что проверить                              │
│   - Запросить тестовое создание InspectionType│
│   - Убедиться, что unique constraint работает│
└──────────────────────────────────────────────┘
```

Источник: поле `task.explanation` в API.

### 4.3. `DiffViewer`

Side-by-side diff с подсветкой синтаксиса C#.

### 4.4. `XUnitBadge`

Краткий badge с результатами xUnit-тестов (только в исследовательском режиме): зелёный — все passed, жёлтый — частично, красный — 0 из N.

---

## 5. Канал прогресса в реальном времени (WebSocket)

Прогресс задачи приходит на UI по WebSocket-каналу:

```
ws://{host}/ws/progress/{task_id}?last_ts={timestamp}
```

- Подключение инкапсулировано в хуке `useWebSocket.ts` (reconnect с backoff, ring-buffer replay пропущенных событий).
- При переподключении `last_ts` берётся из `localStorage`, и сервер воспроизводит пропущенные события.
- Индикатор соединения: зелёный (подключён) / красный (отключён).
- Для страницы Compliance аналогично используется канал `/ws/progress/{replay_id}` с событиями `replay_progress`.

---

## 6. Точки интеграции с бэкендом

| Метод | Эндпоинт | Назначение |
|---|---|---|
| `POST` | `/api/tasks` | запуск задачи |
| `GET` | `/api/tasks/{id}` | статус задачи |
| `GET` | `/api/audit/runs/{run_id}` | audit trail |
| `WS` | `/ws/progress/{task_id}` | прогресс в реальном времени |

---

## 7. Связанные документы

- [`../detailed-architecture.md`](../detailed-architecture.md) — колонка 1 (Веб-интерфейс).
- [`../PROJECT_ARCHITECTURE.md`](../PROJECT_ARCHITECTURE.md) — общая архитектура.
