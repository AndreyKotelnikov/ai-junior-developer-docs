# Pattern Extraction Service

> **Статус: DEPRECATED с 13.04.2026.** Этот компонент (SetFit + 6-стадийный пайплайн) выведен из эксплуатации и заменён в production Zero-Retrain Router. Документ сохранён для воспроизводимости гипотезы H2a.

Сервис извлечения паттернов доработок из истории GitLab для интеллектуальной помощи AI-агентам при разработке .NET-приложения.

## Оглавление

- [Общая информация](#общая-информация)
- [Архитектура](#архитектура)
- [Системные требования](#системные-требования)
- [Установка и запуск](#установка-и-запуск)
- [Переменные окружения](#переменные-окружения)
- [Полный пайплайн: от сырых данных до результатов](#полный-пайплайн-от-сырых-данных-до-результатов)
- [API Reference](#api-reference)
  - [Health](#health)
  - [Extraction (Этап 1)](#extraction-этап-1--извлечение-данных)
  - [Classification (Этап 2)](#classification-этап-2--классификация-задач)
  - [Pattern Mining (Этап 3)](#pattern-mining-этап-3--извлечение-паттернов)
  - [AST Analysis & Templates (Этап 4)](#ast-analysis--templates-этап-4--ast-анализ-и-шаблоны)
  - [Navigation Rules (Этап 4.5)](#navigation-rules-этап-45--извлечение-навигационных-правил)
  - [Quality & Artifacts (Этап 5)](#quality--artifacts-этап-5--оценка-качества-и-артефакты)
  - [Qdrant Indexing (Этап 6)](#qdrant-indexing-этап-6--индексация-в-qdrant)
  - [Pipeline (Запуск всех этапов)](#pipeline-запуск-всех-этапов)
- [Взаимодействие с другими сервисами](#взаимодействие-с-другими-сервисами)
- [Структура проекта](#структура-проекта)
- [Выходные артефакты](#выходные-артефакты)
- [Типы задач (таксономия)](#типы-задач-таксономия)
- [Алгоритмы и пороговые значения](#алгоритмы-и-пороговые-значения)
- [Устранение неполадок](#устранение-неполадок)
- [Вклад в проект](#вклад-в-проект)

---

## Общая информация

### Проблема

Текущий RAG-сервис выполняет поиск по тексту бизнес-требования через семантические эмбеддинги, но результаты часто нерелевантны:

- Поиск ведётся по всей базе из 1 154 пар MR-diff без учёта типа задачи
- Текстовые эмбеддинги плохо различают структурные паттерны кода
- Отсутствует анализ: какие файлы должны меняться вместе, какие паттерны повторяются
- Нет оценки качества — агенты могут получить плохой пример как образец

### Решение

`pattern-extraction` — офлайн-пайплайн, который:

1. **Извлекает данные** из БД GitLab (issues, merge requests, code changes)
2. **Классифицирует задачи** по типам (add_entity, modify_service и т.д.) через BERTopic + LLM + SetFit
3. **Майнит co-change паттерны** (какие файлы всегда меняются вместе) через FP-Growth
4. **Анализирует AST** C#-кода через tree-sitter и синтезирует параметризованные шаблоны
5. **Извлекает навигационные правила** — связки «навигационное свойство → регистрация в DataConfiguration.cs / Initializer.cs»
6. **Оценивает качество** каждого MR (включая navigation_completeness) и генерирует MD-файлы с паттернами
7. **Индексирует** результаты в Qdrant для гибридного семантического поиска

Результат — структурированные чеклисты, шаблоны кода и лучшие примеры для каждого типа задачи, которые AI-агенты используют при генерации кода.

### Целевая архитектура

```
Бизнес-требование (от пользователя)
        │
        ▼
┌──────────────────────────┐
│  SetFit Classifier       │ ← Определяет тип задачи (< 50ms, GPU)
│  (paraphrase-multilingual│
│   -mpnet-base-v2)        │
└──────────┬───────────────┘
           │ task_type = "add_entity"
           ▼
┌──────────────────────────┐
│  Qdrant Hybrid Search    │
│  - Dense: multilingual   │
│    e5-base (768-dim)     │
│  - Sparse: BM25          │
│  - Filter: task_type,    │
│    quality_score ≥ 0.5   │
└──────────┬───────────────┘
           │ top-5 candidates
           ▼
┌──────────────────────────────────────────────────────────┐
│  Few-shot Prompt Assembly (rag-service)                  │
│  - 2-3 лучших исторических примера                       │
│  - Чеклист файлов для данного типа задачи                │
│  - Шаблон кода (параметризованный)                       │
│  - Hotspots (файлы, которые часто забывают)              │
└──────────────────────────────────────────────────────────┘
           │
           ▼
     Агенты-разработчики (multiagent)
```

---

## Архитектура

### Сервисы в docker-compose.yml

| Сервис | Назначение | GPU | Порт |
|--------|-----------|-----|------|
| `pattern-extraction` | Офлайн-пайплайн: классификация, co-change mining, AST-анализ, генерация MD | Да | 8200 |
| `rag-service` | Онлайн-пайплайн: маршрутизация, поиск, few-shot assembly | Да | 8100 |
| `qdrant` | Векторная БД для гибридного поиска | Нет | 6333 |
| `postgres` | PostgreSQL 16 + pgvector 0.8.0 (данные GitLab) | Нет | 5432 |
| `multiagent` | Агенты-разработчики | Нет | 8000 |
| `ui` | Streamlit UI для управления | Нет | 8501 |

### Используемые модели

| Задача | Модель | Размер | Где работает |
|--------|--------|--------|--------------|
| Классификация задач (runtime) | SetFit + `paraphrase-multilingual-mpnet-base-v2` | ~420 MB | Локально GPU |
| Кластеризация (BERTopic) | `paraphrase-multilingual-mpnet-base-v2` + UMAP + HDBSCAN | ~620 MB | Локально GPU |
| Эмбеддинги для RAG | `intfloat/multilingual-e5-base` | ~278 MB | Локально GPU |
| Эмбеддинги кода | `voyageai/voyage-code-3` (fallback: `multilingual-e5-base`) | API | OpenRouter |
| LLM-разметка задач | Claude Sonnet 4 | API | OpenRouter |
| LLM-синтез шаблонов | Claude Sonnet 4 | API | OpenRouter |

---

## Системные требования

### Обязательные

- **Docker Desktop** с поддержкой GPU (NVIDIA Container Toolkit)
- **NVIDIA GPU** с CUDA compute capability ≥ 7.0 и ≥ 8 GB VRAM (рекомендуется 16 GB)
- **Docker Compose** v2+
- **PostgreSQL** с данными GitLab (issues, merge_requests, changes, comments, issue_merge_requests)
- Минимум **8 GB RAM** для контейнера (рекомендуется 16 GB)

### Опциональные (для полного пайплайна)

- **OpenRouter API Key** — для LLM-классификации и синтеза шаблонов
- **Доступ к Voyage Code-3** — для code-эмбеддингов (есть fallback на `multilingual-e5-base`)

### Протестировано на

```
NVIDIA GeForce RTX 3080 Ti Laptop GPU (16 GB VRAM)
Windows 10 Pro + WSL2
Docker Desktop 4.x
```

---

## Установка и запуск

### Шаг 1. Клонирование репозитория

```bash
git clone <repository-url>
cd dotnet-multiagent-system
```

### Шаг 2. Настройка переменных окружения

Создайте файл `.env` в корне `dotnet-multiagent-system/`:

```env
# PostgreSQL
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres

# OpenRouter API (для LLM-классификации и синтеза шаблонов)
OPENROUTER_API_KEY=sk-or-v1-your-key-here
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1

# Qdrant
QDRANT_HOST=qdrant
QDRANT_PORT=6333

# Опционально (модели по умолчанию)
VOYAGE_CODE_MODEL=voyageai/voyage-code-3
LOG_LEVEL=INFO
```

> **Важно:** `OPENROUTER_API_KEY` необходим для этапов классификации (LLM) и синтеза шаблонов (AST). Без него эти этапы будут пропущены, но извлечение данных, mining паттернов и SetFit-обучение будут работать.

### Шаг 3. Подготовка данных в PostgreSQL

Сервис ожидает, что в БД PostgreSQL `gitlab` (порт 5432) существуют следующие таблицы:

| Таблица | Ключевые колонки |
|---------|-----------------|
| `issues` | id, iid, project_iid, title, description, state, created_at, type, assignee |
| `merge_requests` | id, project_id, project_iid, iid, title, description, merged_at, source_branch, sha, changes_count, author |
| `changes` | id, mr_id, new_path, old_path, diff, new_file, deleted_file, renamed_file |
| `comments` | id, iid, issue_id, body, author, created_at, system |
| `issue_merge_requests` | id, issue_id, mr_id |
| `projects` | id, name, iid, target_branch |

Эти таблицы обычно заполняются из выгрузки GitLab. Скрипты инициализации можно разместить в `postgres/init-scripts/`.

### Шаг 4. Сборка и запуск контейнеров

```bash
# Собрать и запустить все сервисы
docker compose up -d --build

# Или собрать только pattern-extraction и зависимости
docker compose up -d --build postgres qdrant pattern-extraction
```

### Шаг 5. Проверка работоспособности

```bash
# Проверить health всех контейнеров
docker compose ps

# Проверить health pattern-extraction
curl http://localhost:8200/health
```

Ожидаемый ответ:

```json
{
  "status": "ok",
  "service": "pattern-extraction"
}
```

### Шаг 6. Пересборка отдельных сервисов

```bash
# Пересобрать только pattern-extraction
docker compose build pattern-extraction && docker compose up -d pattern-extraction

# Пересобрать rag-service
docker compose build rag-service && docker compose up -d rag-service

# Просмотр логов
docker compose logs -f pattern-extraction
```

---

## Переменные окружения

### pattern-extraction

| Переменная | Значение по умолчанию | Описание |
|-----------|----------------------|----------|
| `DB_HOST` | `postgres` | Хост PostgreSQL |
| `DB_PORT` | `5432` | Порт PostgreSQL |
| `DB_USER` | `postgres` | Пользователь БД |
| `DB_PASSWORD` | `postgres` | Пароль БД |
| `DB_NAME` | `gitlab` | Имя базы данных |
| `OPENROUTER_API_KEY` | _(пусто)_ | Ключ OpenRouter для LLM |
| `OPENROUTER_BASE_URL` | `https://openrouter.ai/api/v1` | URL OpenRouter API |
| `LLM_TEMPLATE_MODEL` | `anthropic/claude-sonnet-4` | Модель LLM для классификации и синтеза шаблонов |
| `QDRANT_HOST` | `qdrant` | Хост Qdrant |
| `QDRANT_PORT` | `6333` | Порт Qdrant REST API |
| `VOYAGE_CODE_MODEL` | `voyageai/voyage-code-3` | Модель для code-эмбеддингов |
| `LOG_LEVEL` | `INFO` | Уровень логирования |
| `DATA_DIR` | `/app/data` | Каталог промежуточных данных |
| `OUTPUTS_DIR` | `/app/outputs` | Каталог отчётов (EDA, BERTopic) |
| `MODELS_DIR` | `/app/models` | Каталог обученных моделей |
| `TEMPLATES_DIR` | `/app/data/templates` | Каталог шаблонов по типам задач |

### rag-service (связанные переменные)

| Переменная | Значение по умолчанию | Описание |
|-----------|----------------------|----------|
| `PATTERN_EXTRACTION_URL` | `http://pattern-extraction:8200` | URL pattern-extraction сервиса |
| `SETFIT_MODEL_PATH` | `/app/models/external/task_classifier` | Путь к модели SetFit (read-only монтирование из pattern-extraction) |
| `EMBEDDING_MODEL_NAME` | `intfloat/multilingual-e5-base` | Модель для семантических эмбеддингов |

---

## Полный пайплайн: от сырых данных до результатов

Ниже описан полный процесс — от первого запуска контейнеров на чистой машине до готовых паттернов. На входе — только сырые данные из БД GitLab.

### Предварительные условия

1. Docker Desktop запущен с поддержкой GPU
2. Файл `.env` создан с необходимыми переменными (см. [Установка](#шаг-2-настройка-переменных-окружения))
3. PostgreSQL содержит данные GitLab
4. Контейнеры запущены: `docker compose up -d --build postgres qdrant pattern-extraction`

### Способ 1: Запуск полного пайплайна одной командой

Самый простой способ — запустить все этапы через Pipeline API:

```bash
curl --location --request POST 'http://localhost:8200/api/v1/pipeline/run-all'
```

Ответ:

```json
{
  "status": "started",
  "stages": ["extract", "classify", "mine_patterns", "ast_analyze", "nav_rules", "quality_score", "generate_artifacts", "index_qdrant"]
}
```

Отслеживание прогресса:

```bash
curl http://localhost:8200/api/v1/pipeline/status
```

```json
{
  "status": "running",
  "current_stage": "classify",
  "progress": 0.125,
  "stages_completed": ["extract"],
  "stages_remaining": ["classify", "mine_patterns", "ast_analyze", "nav_rules", "quality_score", "generate_artifacts", "index_qdrant"],
  "error": null
}
```

> **Время выполнения:** Полный пайплайн занимает ~30-60 минут (зависит от GPU и количества задач). Этап LLM-классификации — самый долгий (~15-20 минут для 1300 задач, таймаут 12 часов).

### Способ 2: Пошаговый запуск каждого этапа

Для лучшего контроля можно запускать этапы по отдельности.

---

#### Этап 1. Извлечение данных из GitLab БД

Извлекает все issues, merge requests, code changes и comments, нормализует файловые пути к архитектурным слоям.

**Запуск:**

```bash
curl --location --request POST 'http://localhost:8200/api/v1/extract/run'
```

**Проверка статуса:**

```bash
curl http://localhost:8200/api/v1/extract/status
```

```json
{
  "status": "running",
  "progress": 0.45,
  "total_issues": 1300,
  "processed_issues": 585,
  "message": "Extraction in progress"
}
```

**Просмотр статистики после завершения:**

```bash
curl http://localhost:8200/api/v1/extract/stats
```

```json
{
  "total_issues": 1300,
  "total_merge_requests": 850,
  "total_changes": 5200,
  "issues_with_mr": 780,
  "issues_without_mr": 520,
  "arch_layer_distribution": {
    "entity": 420,
    "service": 380,
    "configuration": 350,
    "controller": 280,
    "migration": 210,
    "initializer": 190,
    "dto": 150,
    "other": 120
  },
  "avg_files_per_mr": 6.12,
  "top_changed_files": [
    {"path": "Data/Configurations/DataConfiguration.cs", "count": 185},
    {"path": "Data/Initializer.cs", "count": 142}
  ]
}
```

**Результат:**
- `volumes/pattern-extraction/data/issues_dataset.json` — полный датасет
- `volumes/pattern-extraction/data/issues_dataset.parquet` — Parquet-формат
- `volumes/pattern-extraction/outputs/eda_report.html` — HTML-отчёт с визуализациями

**Формат данных (одна запись issues_dataset.json):**

```json
{
  "issue_id": 33555,
  "issue_iid": 388,
  "title": "Добавить поля в сущность ConstructionSiteAnalog",
  "description": "Необходимо добавить поля...",
  "comments": ["Нужно ещё добавить...", "..."],
  "merge_requests": [
    {
      "mr_id": 693,
      "mr_iid": 267,
      "title": "feat: добавление полей ConstructionSiteAnalog",
      "files_changed": [
        {
          "path": "Data/Entities/ConstructionSiteAnalog.cs",
          "normalized_path": "Data/Entities/ConstructionSiteAnalog.cs",
          "arch_layer": "entity",
          "arch_module": "ConstructionSiteAnalog",
          "change_type": "modified",
          "diff": "@@ -10,4 +10,12 @@...",
          "added_lines": 70,
          "deleted_lines": 4
        }
      ]
    }
  ],
  "total_files_changed": 1,
  "arch_layers_affected": ["entity"],
  "has_migration": false,
  "has_configuration_change": false,
  "has_initializer_change": false,
  "has_service_change": false,
  "has_controller_change": false
}
```

---

#### Этап 2. Классификация задач по типам

Трёхступенчатый процесс: BERTopic кластеризация → LLM-разметка → обучение SetFit.

**Запуск (полный пайплайн классификации):**

```bash
curl --location 'http://localhost:8200/api/v1/classification/run' \
  --header 'Content-Type: application/json' \
  --data '{
    "skip_bertopic": false,
    "skip_llm": false,
    "force_retrain": false
  }'
```

**Запуск (только SetFit, если LLM-разметка уже выполнена):**

```bash
curl --location 'http://localhost:8200/api/v1/classification/run' \
  --header 'Content-Type: application/json' \
  --data '{
    "skip_bertopic": true,
    "skip_llm": true,
    "force_retrain": true
  }'
```

**Проверка статуса:**

```bash
curl http://localhost:8200/api/v1/classification/status
```

```json
{
  "stage": "llm_classification",
  "progress": 0.45,
  "current_step": "LLM classifying 350/780",
  "errors": []
}
```

**Статистика классификации:**

```bash
curl http://localhost:8200/api/v1/classification/stats
```

```json
{
  "total_classified": 780,
  "distribution": {
    "add_entity": 145,
    "modify_entity": 180,
    "add_service": 95,
    "modify_service": 120,
    "import_export": 45,
    "filtering_sorting": 55,
    "config_infra": 40,
    "bug_fix": 50,
    "refactoring": 30,
    "ui_view": 20
  },
  "accuracy": 0.89,
  "taxonomy": {
    "add_entity": "Добавление новой сущности EF Core",
    "modify_entity": "Доработка существующей сущности (поля, связи)",
    "add_service": "Добавление нового сервиса/обработчика/API endpoint",
    "modify_service": "Доработка логики существующего сервиса",
    "import_export": "Алгоритмы импорта/экспорта (Excel, XML, XSLT)",
    "filtering_sorting": "Фильтрация, сортировка, поиск",
    "config_infra": "Конфигурация, DI, миграции, настройки",
    "bug_fix": "Исправление ошибок",
    "refactoring": "Рефакторинг без изменения функциональности",
    "ui_view": "Изменения представления (ViewComponents, атрибуты)"
  }
}
```

**Классификация произвольного текста (runtime):**

```bash
curl --location 'http://localhost:8200/api/v1/classification/classify' \
  --header 'Content-Type: application/json' \
  --data '{
    "text": "Добавить новую сущность ConstructionSiteAnalog с полями для площади и адреса"
  }'
```

```json
{
  "task_type": "add_entity",
  "confidence": 0.94,
  "top_3": [
    {"type": "add_entity", "score": 0.94},
    {"type": "modify_entity", "score": 0.04},
    {"type": "add_service", "score": 0.01}
  ]
}
```

**Просмотр элементов для ручной валидации:**

```bash
# Все типы (по 12 случайных на каждый тип)
curl http://localhost:8200/api/v1/classification/review

# Конкретный тип (до 15 элементов)
curl 'http://localhost:8200/api/v1/classification/review?task_type=add_entity'
```

```json
{
  "items": [
    {
      "issue_id": 33555,
      "title": "Добавить поля в сущность ConstructionSiteAnalog",
      "description_preview": "Необходимо добавить поля для хранения...",
      "predicted_type": "modify_entity",
      "confidence": 0.87
    }
  ],
  "total": 12
}
```

**Результат:**
- `volumes/pattern-extraction/data/classified_issues.json` — размеченный датасет
- `volumes/pattern-extraction/data/taxonomy.json` — таксономия типов
- `volumes/pattern-extraction/data/bertopic_results.json` — результаты кластеризации
- `volumes/pattern-extraction/outputs/bertopic_report.html` — визуализация кластеров
- `volumes/pattern-extraction/models/task_classifier/` — обученная модель SetFit
- `volumes/pattern-extraction/models/task_classifier/training_metrics.json` — метрики обучения

---

#### Этап 3. Извлечение паттернов (Co-change Mining)

Майнинг ассоциативных правил: какие файлы/слои всегда меняются вместе.

**Запуск:**

```bash
curl --location 'http://localhost:8200/api/v1/patterns/mine' \
  --header 'Content-Type: application/json' \
  --data '{
    "min_support": 0.05,
    "min_confidence": 0.5,
    "min_lift": 1.2,
    "max_len": 8
  }'
```

Или с параметрами по умолчанию:

```bash
curl --location --request POST 'http://localhost:8200/api/v1/patterns/mine'
```

**Проверка статуса:**

```bash
curl http://localhost:8200/api/v1/patterns/status
```

```json
{
  "stage": "building_checklists",
  "progress": 0.75,
  "current_task_type": "add_service",
  "details": "Processing task type 5/10"
}
```

**Статистика паттернов:**

```bash
curl http://localhost:8200/api/v1/patterns/stats
```

```json
{
  "total_task_types": 10,
  "total_rules": 87,
  "total_hotspots": 45,
  "task_types": [
    {
      "task_type": "add_entity",
      "issue_count": 145,
      "checklist_items": 6,
      "hotspot_count": 8,
      "rule_count": 12
    }
  ]
}
```

**Получение чеклиста для типа задачи:**

```bash
curl http://localhost:8200/api/v1/patterns/add_entity/checklist
```

```json
{
  "task_type": "add_entity",
  "total_issues_analyzed": 145,
  "checklist_items": 6,
  "hotspot_count": 8,
  "rule_count": 12,
  "data": {
    "task_type": "add_entity",
    "total_issues_analyzed": 145,
    "checklist": [
      {
        "layer": "entity",
        "action": "create",
        "confidence": 1.0,
        "required": true,
        "typical_file": null
      },
      {
        "layer": "configuration",
        "action": "modify",
        "confidence": 0.94,
        "required": true,
        "typical_file": "Data/Configurations/DataConfiguration.cs"
      },
      {
        "layer": "initializer",
        "action": "modify",
        "confidence": 0.88,
        "required": true,
        "typical_file": "Data/Initializer.cs"
      },
      {
        "layer": "migration",
        "action": "create",
        "confidence": 0.82,
        "required": true,
        "typical_file": null
      }
    ],
    "hotspot_files": [
      {
        "path": "Data/Configurations/DataConfiguration.cs",
        "change_freq": 0.94,
        "description": ""
      }
    ],
    "co_change_rules": [
      {
        "antecedent": ["entity"],
        "consequent": ["configuration"],
        "support": 0.85,
        "confidence": 0.94,
        "lift": 1.1
      }
    ]
  }
}
```

**Получение хотспотов (файлы, которые чаще всего забывают изменить):**

```bash
curl http://localhost:8200/api/v1/patterns/hotspots
```

```json
{
  "total": 25,
  "hotspots": [
    {
      "path": "Data/Configurations/DataConfiguration.cs",
      "change_freq": 0.94,
      "description": ""
    },
    {
      "path": "Data/Initializer.cs",
      "change_freq": 0.88,
      "description": ""
    }
  ]
}
```

**Temporal coupling (файлы, которые исторически менялись вместе):**

```bash
curl 'http://localhost:8200/api/v1/patterns/temporal-coupling?top_n=50&min_coupling=0.5'
```

```json
{
  "total": 50,
  "pairs": [
    {
      "file1": "Data/Entities/ConstructionSite.cs",
      "file2": "Data/Configurations/DataConfiguration.cs",
      "co_change_count": 42,
      "coupling_degree": 0.87,
      "support": 0.05
    }
  ]
}
```

**Результат:**
- `volumes/pattern-extraction/data/checklists.json` — чеклисты по типам задач
- `volumes/pattern-extraction/data/temporal_coupling.parquet` — пары связанных файлов

---

#### Этап 4. AST-анализ и синтез шаблонов

Парсинг C#-кода через tree-sitter, извлечение структурных элементов и генерация параметризованных шаблонов через LLM.

**Запуск:**

```bash
curl --location --request POST 'http://localhost:8200/api/v1/artifacts/analyze'
```

**Проверка статуса:**

```bash
curl http://localhost:8200/api/v1/artifacts/analyze/status
```

```json
{
  "status": "running",
  "total_mrs": 850,
  "processed_mrs": 340,
  "failed_mrs": 5,
  "progress": 0.4,
  "current_file": "Data/Entities/User.cs",
  "error": null
}
```

**Список сгенерированных шаблонов:**

```bash
curl http://localhost:8200/api/v1/artifacts/templates
```

```json
[
  {
    "task_type": "add_entity",
    "template_name": "add_ef_core_entity",
    "description": "Шаблон добавления новой сущности EF Core",
    "steps_count": 4,
    "parameters_count": 6,
    "source_examples_count": 12,
    "generated_at": "2026-02-18T10:30:00"
  }
]
```

**Получение шаблона для типа задачи:**

```bash
curl http://localhost:8200/api/v1/patterns/add_entity/template
```

```json
{
  "task_type": "add_entity",
  "template_name": "add_ef_core_entity",
  "description": "Шаблон добавления новой сущности EF Core",
  "parameters": [
    {
      "name": "entity_name",
      "description": "Имя новой сущности",
      "example": "ConstructionSiteAnalog"
    }
  ],
  "steps": [
    {
      "step": 1,
      "file_template": "Data/Entities/{entity_name}.cs",
      "action": "create",
      "code_template": "using Visary.Abstractions;\n...",
      "notes": "Создать файл сущности с навигационными свойствами"
    }
  ],
  "source_examples_count": 12,
  "generated_at": "2026-02-18T10:30:00"
}
```

**Результат:**
- `volumes/pattern-extraction/data/ast_deltas.json` — структурные дельты
- `volumes/pattern-extraction/data/navigation_rules.json` — навигационные правила (генерируется автоматически)
- `volumes/pattern-extraction/data/templates/{task_type}.json` — шаблоны по типам

---

#### Этап 4.5. Извлечение навигационных правил

Анализ AST-дельт для извлечения связок «навигационное свойство → регистрация в DataConfiguration.cs / Initializer.cs». Эта стадия запускается автоматически после AST-анализа, а также может быть вызвана отдельно.

**Запуск (отдельно):**

```bash
curl --location --request POST 'http://localhost:8200/api/v1/artifacts/nav-rules'
```

**Проверка статуса:**

```bash
curl http://localhost:8200/api/v1/artifacts/nav-rules/status
```

```json
{
  "status": "completed",
  "error": null
}
```

**Логика:**
- Для каждого MR собирает навигационные свойства из entity-дельт (где `is_navigation == true`)
- Проверяет наличие соответствующих паттернов в configuration- и initializer-дельтах
- Формирует `NavigationRegistration` с полями `config_registered`, `config_pattern`, `initializer_registered`, `initializer_pattern`
- Результат используется в quality scoring (вес `navigation_completeness = 15%`) и в промпте синтеза шаблонов

**Результат:**
- `volumes/pattern-extraction/data/navigation_rules.json` — навигационные правила по MR

---

#### Этап 5. Оценка качества и генерация артефактов

Расчёт quality score для каждого MR, генерация MD-файлов с паттернами и AGENT.md.

> **Примечание:** Этапы `quality_score` и `generate_artifacts` используют один и тот же эндпоинт (`POST /api/v1/artifacts/generate`). При запуске через пайплайн они выполняются один раз, даже если оба этапа указаны в списке.

**Запуск:**

```bash
curl --location --request POST 'http://localhost:8200/api/v1/artifacts/generate'
```

**Проверка статуса:**

```bash
curl http://localhost:8200/api/v1/artifacts/status
```

```json
{
  "stage": "generating_patterns",
  "progress": 0.6,
  "current_task_type": "add_service",
  "error": null
}
```

**Стадии генерации:**

| Диапазон progress | Стадия |
|---|---|
| 0.0 — 0.3 | Quality scoring |
| 0.4 — 0.8 | Генерация pattern MD-файлов |
| 0.85 — 1.0 | Генерация AGENT.md |

**Отчёт по качеству:**

```bash
curl http://localhost:8200/api/v1/artifacts/quality-report
```

```json
{
  "total_mrs": 850,
  "scored_mrs": 820,
  "avg_score": 0.68,
  "by_task_type": {
    "add_entity": {
      "count": 145,
      "avg_score": 0.72,
      "min_score": 0.15,
      "max_score": 0.95
    }
  },
  "score_distribution": [
    {"range": "0.0-0.2", "count": 30},
    {"range": "0.2-0.4", "count": 85},
    {"range": "0.4-0.6", "count": 210},
    {"range": "0.6-0.8", "count": 350},
    {"range": "0.8-1.0", "count": 145}
  ]
}
```

**Получение AGENT.md:**

```bash
curl http://localhost:8200/api/v1/artifacts/agent-md
```

Возвращает текст Markdown.

**Список паттерн-файлов:**

```bash
curl http://localhost:8200/api/v1/artifacts/patterns
```

```json
[
  {
    "task_type": "add_entity",
    "file_path": "/app/history_cases/patterns/add_entity.md",
    "examples_count": 12,
    "avg_quality": 0.78
  }
]
```

**Получение конкретного паттерна:**

```bash
curl http://localhost:8200/api/v1/artifacts/patterns/add_entity
```

Возвращает текст Markdown с чеклистом, шаблонами, примерами и co-change правилами.

**Результат:**
- `volumes/pattern-extraction/data/quality_scores.json` — оценки качества
- `history_cases/AGENT.md` — руководство для AI-агентов
- `history_cases/patterns/{task_type}.md` — паттерн-файлы по типам

---

#### Этап 6. Индексация в Qdrant

Загрузка эмбеддингов и метаданных в векторную БД Qdrant для гибридного поиска.

**Запуск:**

```bash
curl --location --request POST 'http://localhost:8200/api/v1/index/qdrant'
```

**Проверка статуса:**

```bash
curl http://localhost:8200/api/v1/index/qdrant/status
```

```json
{
  "stage": "embedding",
  "total": 820,
  "processed": 450,
  "errors": 0,
  "started_at": "2026-02-18T10:00:00",
  "completed_at": null
}
```

**Статистика коллекции Qdrant:**

```bash
curl http://localhost:8200/api/v1/index/qdrant/stats
```

```json
{
  "total_points": 820,
  "collection_exists": true,
  "task_type_distribution": {
    "add_entity": 145,
    "modify_entity": 180,
    "add_service": 95,
    "modify_service": 120,
    "import_export": 45,
    "filtering_sorting": 55,
    "config_infra": 40,
    "bug_fix": 50,
    "refactoring": 30,
    "ui_view": 20
  }
}
```

**Результат:** Коллекция `code_patterns` в Qdrant с двумя dense-векторами (`nl_dense`, `code_dense`) и sparse BM25.

---

### После завершения пайплайна

После успешного выполнения всех этапов система готова к использованию. Теперь необходимо запустить индексацию rag-service (для обратной совместимости со старым поиском):

```bash
curl --location 'http://localhost:8100/api/v1/index' \
  --header 'Content-Type: application/json' \
  --data '{
    "mode": "full"
  }'
```

```json
{
  "status": "completed",
  "mode": "full",
  "issues_processed": 780,
  "issues_updated": 780,
  "duration_ms": 45230.5
}
```

Теперь rag-service может использовать оба пути поиска:
- Новый: гибридный поиск через Qdrant + классификация + чеклисты из pattern-extraction
- Старый (fallback): pgvector-поиск по эмбеддингам issues

---

## API Reference

Базовый URL: `http://localhost:8200`

### Health

#### `GET /health`

Проверка работоспособности сервиса.

**Ответ:**

```json
{"status": "ok", "service": "pattern-extraction"}
```

---

### Extraction (Этап 1 — Извлечение данных)

#### `POST /api/v1/extract/run`

Запуск извлечения данных из PostgreSQL.

**Параметры:** нет

**Ответ:**

```json
{
  "task_id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "started",
  "message": "Extraction started"
}
```

> Если извлечение уже запущено, вернёт `status: "running"`.

---

#### `GET /api/v1/extract/status`

Текущий прогресс извлечения.

**Ответ:**

| Поле | Тип | Описание |
|------|-----|----------|
| `status` | string | `idle` / `running` / `completed` / `failed` |
| `progress` | float | 0.0 — 1.0 |
| `total_issues` | int | Всего задач в БД |
| `processed_issues` | int | Обработано задач |
| `message` | string | Текстовое описание |

---

#### `GET /api/v1/extract/stats`

Статистика извлечённых данных.

**Ответ:**

| Поле | Тип | Описание |
|------|-----|----------|
| `total_issues` | int | Всего задач |
| `total_merge_requests` | int | Всего MR |
| `total_changes` | int | Всего изменённых файлов |
| `issues_with_mr` | int | Задачи со связанными MR |
| `issues_without_mr` | int | Задачи без MR |
| `arch_layer_distribution` | object | Распределение по архитектурным слоям |
| `avg_files_per_mr` | float | Среднее кол-во файлов на MR |
| `top_changed_files` | array | Топ-30 самых изменяемых файлов |

---

### Classification (Этап 2 — Классификация задач)

#### `POST /api/v1/classification/run`

Запуск пайплайна классификации.

**Тело запроса:**

| Поле | Тип | По умолчанию | Описание |
|------|-----|-------------|----------|
| `skip_bertopic` | bool | `false` | Пропустить BERTopic кластеризацию |
| `skip_llm` | bool | `false` | Пропустить LLM-классификацию |
| `force_retrain` | bool | `false` | Принудительно переобучить SetFit |

**Пример:**

```bash
curl --location 'http://localhost:8200/api/v1/classification/run' \
  --header 'Content-Type: application/json' \
  --data '{"skip_bertopic": false, "skip_llm": false, "force_retrain": false}'
```

---

#### `GET /api/v1/classification/status`

**Ответ:**

| Поле | Тип | Описание |
|------|-----|----------|
| `stage` | string | `idle` / `bertopic` / `llm_classification` / `setfit_training` / `completed` / `failed` |
| `progress` | float | 0.0 — 1.0 |
| `current_step` | string | Текущий шаг |
| `errors` | array | Список ошибок |

**Диапазоны progress по стадиям:**

| Стадия | Диапазон progress |
|--------|-------------------|
| BERTopic | 0.05 — 0.2 |
| LLM Classification | 0.2 — 0.7 |
| SetFit Training | 0.7 — 1.0 |

---

#### `GET /api/v1/classification/stats`

Статистика классификации.

**Ответ:**

| Поле | Тип | Описание |
|------|-----|----------|
| `total_classified` | int | Количество классифицированных задач |
| `distribution` | object | Распределение по типам `{task_type: count}` |
| `accuracy` | float / null | Точность SetFit на тестовой выборке |
| `taxonomy` | object | Описания типов задач |

---

#### `POST /api/v1/classification/classify`

Классификация произвольного текста (runtime, SetFit).

**Тело запроса:**

| Поле | Тип | Описание |
|------|-----|----------|
| `text` | string | Текст бизнес-требования |

**Ответ:**

| Поле | Тип | Описание |
|------|-----|----------|
| `task_type` | string | Предсказанный тип задачи |
| `confidence` | float | Уверенность (0.0 — 1.0) |
| `top_3` | array | Топ-3 типа с вероятностями |

> **Код 503** — модель SetFit не загружена. Нужно сначала запустить классификацию.

---

#### `GET /api/v1/classification/review`

Элементы для ручной валидации классификации.

**Query-параметры:**

| Параметр | Тип | Описание |
|----------|-----|----------|
| `task_type` | string / null | Фильтр по типу задачи |

**Ответ:** Список `ReviewItem` с `issue_id`, `title`, `description_preview`, `predicted_type`, `confidence`.

---

### Pattern Mining (Этап 3 — Извлечение паттернов)

#### `POST /api/v1/patterns/mine`

Запуск майнинга ассоциативных правил.

**Тело запроса:**

| Поле | Тип | По умолчанию | Описание |
|------|-----|-------------|----------|
| `min_support` | float | `0.05` | Минимальная поддержка правила |
| `min_confidence` | float | `0.5` | Минимальная уверенность |
| `min_lift` | float | `1.2` | Минимальный lift |
| `max_len` | int | `8` | Макс. размер itemset |

---

#### `GET /api/v1/patterns/status`

**Ответ:** `stage`, `progress`, `current_task_type`, `details`

---

#### `GET /api/v1/patterns/stats`

**Ответ:** `total_task_types`, `total_rules`, `total_hotspots`, `task_types[]`

---

#### `GET /api/v1/patterns/{task_type}/checklist`

Чеклист файлов для типа задачи.

**Path-параметры:**

| Параметр | Тип | Описание |
|----------|-----|----------|
| `task_type` | string | Тип задачи (например, `add_entity`) |

> **Код 404** — чеклист не найден. Нужно сначала запустить mining.

---

#### `GET /api/v1/patterns/{task_type}/template`

Параметризованный шаблон кода для типа задачи.

> **Код 404** — шаблон не найден. Нужно сначала запустить AST-анализ.

---

#### `GET /api/v1/patterns/hotspots`

Все хотспоты (часто изменяемые файлы) по всем типам задач.

**Ответ:** `total`, `hotspots[]` (path, change_freq, description)

---

#### `GET /api/v1/patterns/temporal-coupling`

Пары файлов, которые исторически менялись вместе.

**Query-параметры:**

| Параметр | Тип | По умолчанию | Описание |
|----------|-----|-------------|----------|
| `top_n` | int | `100` | Количество пар (1 — 1000) |
| `min_coupling` | float | `0.3` | Минимальный coupling_degree (0.0 — 1.0) |

---

### AST Analysis & Templates (Этап 4 — AST-анализ и шаблоны)

#### `POST /api/v1/artifacts/analyze`

Запуск AST-анализа и синтеза шаблонов. Парсит все C#-файлы из MR через tree-sitter, затем вызывает LLM для генерации параметризованных шаблонов.

> **Код 409** — анализ уже запущен.

---

#### `GET /api/v1/artifacts/analyze/status`

**Ответ:**

| Поле | Тип | Описание |
|------|-----|----------|
| `status` | string | `idle` / `running` / `completed` / `failed` |
| `total_mrs` | int | Всего MR для анализа |
| `processed_mrs` | int | Обработано MR |
| `failed_mrs` | int | Неудачных парсингов |
| `progress` | float | 0.0 — 1.0 |
| `current_file` | string / null | Текущий анализируемый файл |
| `error` | string / null | Ошибка |

---

#### `GET /api/v1/artifacts/templates`

Список сгенерированных шаблонов. Возвращает сводку по каждому шаблону.

---

### Quality & Artifacts (Этап 5 — Оценка качества и артефакты)

#### `POST /api/v1/artifacts/generate`

Запуск расчёта quality scores + генерация MD-файлов (паттерны + AGENT.md).

> **Код 409** — генерация уже запущена.

---

#### `GET /api/v1/artifacts/status`

**Ответ:**

| Поле | Тип | Описание |
|------|-----|----------|
| `stage` | string | `idle` / `scoring` / `generating_patterns` / `generating_agent_md` / `completed` / `failed` |
| `progress` | float | 0.0 — 1.0 |
| `current_task_type` | string / null | Текущий тип задачи |
| `error` | string / null | Ошибка |

---

#### `GET /api/v1/artifacts/quality-report`

Отчёт по quality scoring.

> **Код 404** — scores не рассчитаны. Нужно сначала запустить `POST /generate`.

---

#### `GET /api/v1/artifacts/agent-md`

Скачивание `AGENT.md` (text/markdown).

> **Код 404** — AGENT.md не сгенерирован.

---

#### `GET /api/v1/artifacts/patterns`

Список всех паттерн-файлов с метаданными.

---

#### `GET /api/v1/artifacts/patterns/{task_type}`

Скачивание паттерн-файла для конкретного типа задачи (text/markdown).

> **Код 404** — паттерн не найден.

---

### Navigation Rules (Этап 4.5 — Извлечение навигационных правил)

#### `POST /api/v1/artifacts/nav-rules`

Запуск извлечения навигационных правил из AST-дельт. Требует `ast_deltas.json`.

> **Код 404** — `ast_deltas.json` не найден. Нужно сначала запустить AST-анализ.

**Ответ:**

```json
{"status": "started"}
```

---

#### `GET /api/v1/artifacts/nav-rules/status`

**Ответ:**

| Поле | Тип | Описание |
|------|-----|----------|
| `status` | string | `idle` / `running` / `completed` / `failed` |
| `error` | string / null | Ошибка |

---

### Qdrant Indexing (Этап 6 — Индексация в Qdrant)

#### `POST /api/v1/index/qdrant`

Запуск индексации паттернов в Qdrant.

---

#### `GET /api/v1/index/qdrant/status`

**Ответ:**

| Поле | Тип | Описание |
|------|-----|----------|
| `stage` | string | `idle` / `loading_model` / `creating_collection` / `loading_data` / `embedding` / `completed` / `error` |
| `total` | int | Всего записей для индексации |
| `processed` | int | Проиндексировано |
| `errors` | int | Количество ошибок |
| `started_at` | string / null | Время начала |
| `completed_at` | string / null | Время завершения |

---

#### `GET /api/v1/index/qdrant/stats`

**Ответ:**

| Поле | Тип | Описание |
|------|-----|----------|
| `total_points` | int | Точек в Qdrant |
| `collection_exists` | bool | Существует ли коллекция |
| `task_type_distribution` | object | Распределение по типам `{task_type: count}` |

---

### Pipeline (Запуск всех этапов)

#### `POST /api/v1/pipeline/run-all`

Запуск полного пайплайна всех стадий с нуля одним запросом.

**Параметры:** нет

**Ответ:**

```json
{
  "status": "started",
  "stages": ["extract", "classify", "mine_patterns", "ast_analyze", "nav_rules", "quality_score", "generate_artifacts", "index_qdrant"]
}
```

> Если пайплайн уже запущен, вернёт `status: "running"`.

---

#### `POST /api/v1/pipeline/run`

Запуск нескольких этапов пайплайна последовательно (выборочные этапы).

**Тело запроса:**

| Поле | Тип | Описание |
|------|-----|----------|
| `stages` | array[string] | Список этапов для выполнения (минимум 1) |

**Допустимые этапы:**

| Этап | Описание | Необходимые входные файлы | Таймаут |
|------|----------|--------------------------|---------|
| `extract` | Извлечение данных из PostgreSQL | — | 1 час |
| `classify` | BERTopic + LLM + SetFit классификация | `issues_dataset.json` | 12 часов |
| `mine_patterns` | FP-Growth + temporal coupling + checklists | `classified_issues.json` | 1 час |
| `ast_analyze` | AST-анализ + шаблоны через LLM | `classified_issues.json` | 1 час |
| `nav_rules` | Извлечение навигационных правил из AST-дельт | `ast_deltas.json` | 1 час |
| `quality_score` | Quality scoring (completeness + navigation + size + coherence) | `classified_issues.json`, `checklists.json` | 1 час |
| `generate_artifacts` | Генерация MD-файлов + AGENT.md | `classified_issues.json`, `checklists.json` | 1 час |
| `index_qdrant` | Индексация в Qdrant | `classified_issues.json` | 1 час |

> **Примечание:** Этапы `quality_score` и `generate_artifacts` выполняются одним вызовом к `POST /api/v1/artifacts/generate`. Если оба указаны, дублирование обрабатывается автоматически.

**Пример (выборочные этапы):**

```bash
curl --location 'http://localhost:8200/api/v1/pipeline/run' \
  --header 'Content-Type: application/json' \
  --data '{
    "stages": ["extract", "classify", "mine_patterns", "ast_analyze", "nav_rules", "quality_score", "generate_artifacts", "index_qdrant"]
  }'
```

**Пример (полный пайплайн одной командой):**

```bash
curl --location --request POST 'http://localhost:8200/api/v1/pipeline/run-all'
```

**Ответ:**

```json
{"status": "started"}
```

> Если пайплайн уже запущен, вернёт `status: "running"`.

---

#### `GET /api/v1/pipeline/status`

**Ответ:**

| Поле | Тип | Описание |
|------|-----|----------|
| `status` | string | `idle` / `running` / `completed` / `failed` |
| `current_stage` | string / null | Текущий выполняемый этап |
| `progress` | float | 0.0 — 1.0 |
| `stages_completed` | array | Завершённые этапы |
| `stages_remaining` | array | Оставшиеся этапы |
| `error` | string / null | Ошибка |

---

### API rag-service (связанные эндпоинты)

Эти эндпоинты находятся в `rag-service` (порт 8100), но используют данные из `pattern-extraction`.

#### `POST /api/v1/index`

Индексация issues в pgvector (старый пайплайн).

**Тело запроса:**

| Поле | Тип | По умолчанию | Описание |
|------|-----|-------------|----------|
| `mode` | string | `"incremental"` | `"full"` — полная переиндексация, `"incremental"` — только новые |

**Пример:**

```bash
curl --location 'http://localhost:8100/api/v1/index' \
  --header 'Content-Type: application/json' \
  --data '{
    "mode": "full"
  }'
```

**Ответ:**

```json
{
  "status": "completed",
  "mode": "full",
  "issues_processed": 780,
  "issues_updated": 780,
  "duration_ms": 45230.5
}
```

---

#### `POST /api/v1/search/hybrid`

Гибридный поиск: классификация запроса → поиск в Qdrant → обогащение чеклистом.

**Тело запроса:**

| Поле | Тип | По умолчанию | Описание |
|------|-----|-------------|----------|
| `query` | string | _(обязательно)_ | Текст запроса |
| `top_k` | int | `5` | Количество результатов |
| `quality_min` | float | `0.3` | Минимальный quality score |
| `include_checklist` | bool | `true` | Включить чеклист из pattern-extraction |
| `include_hotspots` | bool | `true` | Включить хотспоты |

**Пример:**

```bash
curl --location 'http://localhost:8100/api/v1/search/hybrid' \
  --header 'Content-Type: application/json' \
  --data '{
    "query": "Добавить новую сущность для хранения аналогов строительных объектов",
    "top_k": 5,
    "include_checklist": true,
    "include_hotspots": true
  }'
```

**Ответ:**

```json
{
  "task_type": "add_entity",
  "confidence": 0.94,
  "examples": [
    {
      "issue_id": 33555,
      "issue_iid": 388,
      "mr_id": 693,
      "title": "Добавить сущность ConstructionSiteAnalog",
      "description": "...",
      "task_type": "add_entity",
      "quality_score": 0.85,
      "arch_layers": ["entity", "configuration", "initializer"],
      "files_changed": ["Data/Entities/ConstructionSiteAnalog.cs", "..."],
      "score": 0.92
    }
  ],
  "checklist": [
    {"layer": "entity", "action": "create", "confidence": 1.0, "required": true}
  ],
  "hotspots": [
    {"path": "Data/Configurations/DataConfiguration.cs", "change_freq": 0.94}
  ],
  "search_time_ms": 120.5
}
```

---

#### `GET /api/v1/search/hybrid/status`

Проверка статуса всех сервисов для гибридного поиска.

```bash
curl http://localhost:8100/api/v1/search/hybrid/status
```

```json
{
  "classifier_loaded": true,
  "qdrant_ready": true,
  "qdrant_info": {"points_count": 820},
  "pattern_extraction_reachable": true
}
```

---

#### `POST /api/v1/search/context`

Полный RAG-пайплайн: classify → search → rerank → assemble.

**Тело запроса:**

| Поле | Тип | По умолчанию | Описание |
|------|-----|-------------|----------|
| `query` | string | _(обязательно)_ | Текст бизнес-требования |
| `top_k` | int | `3` | Количество примеров |
| `include_checklist` | bool | `true` | Включить чеклист |
| `include_template` | bool | `true` | Включить шаблон кода |
| `include_hotspots` | bool | `true` | Включить хотспоты |
| `max_context_tokens` | int | `8000` | Максимум токенов контекста |

**Пример:**

```bash
curl --location 'http://localhost:8100/api/v1/search/context' \
  --header 'Content-Type: application/json' \
  --data '{
    "query": "Добавить поля в сущность ConstructionSiteAnalog: площадь, адрес, координаты",
    "top_k": 3,
    "include_checklist": true,
    "include_template": true,
    "include_hotspots": true,
    "max_context_tokens": 8000
  }'
```

**Ответ:**

```json
{
  "task_type": "modify_entity",
  "confidence": 0.91,
  "context": "## Тип задачи: modify_entity\n\n## Чеклист файлов...",
  "checklist": [],
  "template": {},
  "examples": [
    {
      "issue_id": 33555,
      "title": "...",
      "description": "...",
      "task_type": "modify_entity",
      "quality_score": 0.85,
      "rerank_score": 0.92,
      "files_changed": [{"path": "Data/Entities/ConstructionSiteAnalog.cs"}],
      "diffs": null
    }
  ],
  "hotspots": [],
  "fallback": false,
  "search_time_ms": 120,
  "rerank_time_ms": 850,
  "total_time_ms": 1250
}
```

> Поле `context` содержит готовый few-shot контекст для агентов, включая чеклист, шаблон и примеры.
> Если `confidence < 0.5`, включается fallback на pgvector и `fallback: true`.

---

## Взаимодействие с другими сервисами

### Схема взаимодействия

```
┌──────────┐    HTTP     ┌───────────────────┐    HTTP     ┌──────────────┐
│    UI    │───────────▶ │   rag-service     │───────────▶ │  pattern-    │
│ (8501)   │◀─────────── │   (8100)          │◀─────────── │  extraction  │
└──────────┘             │                   │             │  (8200)      │
                         │  - Классификация  │             │              │
                         │  - Qdrant поиск   │             │  - Чеклисты  │
                         │  - Re-ranking     │             │  - Шаблоны   │
                         │  - Context        │             │  - Хотспоты  │
                         │    assembly       │             │  - Mining    │
                         └──────┬────────────┘             └──────┬───────┘
                                │                                  │
                     ┌──────────┼──────────────────────────────────┤
                     │          │                                  │
                     ▼          ▼                                  ▼
              ┌───────────┐  ┌───────┐                    ┌───────────┐
              │ PostgreSQL │  │Qdrant │                    │ PostgreSQL │
              │  (5432)    │  │(6333) │                    │  (5432)    │
              │ pgvector   │  │       │                    │ GitLab DB  │
              └───────────┘  └───────┘                    └───────────┘
```

### Направления взаимодействия

| Источник | Назначение | Протокол | Описание |
|----------|-----------|----------|----------|
| `rag-service` → `pattern-extraction` | HTTP REST | Получение чеклистов, шаблонов, хотспотов |
| `rag-service` → `Qdrant` | gRPC/REST | Гибридный поиск паттернов |
| `rag-service` → `PostgreSQL` | SQL (asyncpg) | Fallback-поиск через pgvector |
| `pattern-extraction` → `PostgreSQL` | SQL (asyncpg) | Извлечение данных GitLab |
| `pattern-extraction` → `Qdrant` | REST | Индексация паттернов |
| `pattern-extraction` → `OpenRouter` | HTTPS | LLM-классификация, синтез шаблонов |
| `multiagent` → `rag-service` | HTTP REST | Получение контекста для задач |
| `ui` → `rag-service` | HTTP REST | Поиск и статистика |
| `ui` → `pattern-extraction` | HTTP REST | Управление паттернами |

### Обмен моделями

`rag-service` монтирует каталог моделей `pattern-extraction` как read-only:

```yaml
# docker-compose.yml (rag-service)
volumes:
  - ./volumes/pattern-extraction/models:/app/models/external:ro
```

Благодаря этому `rag-service` использует обученную модель SetFit (`/app/models/external/task_classifier`) для классификации запросов в runtime без необходимости обучения модели заново.

### Обмен артефактами

`pattern-extraction` записывает результаты в:
- `volumes/pattern-extraction/data/` — промежуточные данные (JSON, Parquet)
- `volumes/pattern-extraction/models/` — обученные модели
- `history_cases/` — MD-файлы с паттернами и AGENT.md

`rag-service` и `multiagent` читают из этих каталогов.

### Qdrant (общая коллекция)

Оба сервиса работают с коллекцией `code_patterns` в Qdrant:
- `pattern-extraction` создаёт и наполняет коллекцию (write)
- `rag-service` выполняет гибридный поиск (read)

Структура коллекции:
- **nl_dense** (768-dim) — эмбеддинги текста задачи (`intfloat/multilingual-e5-base`)
- **code_dense** (768-dim) — эмбеддинги кода (`voyageai/voyage-code-3`, fallback: `multilingual-e5-base`)
- **sparse_bm25** — разреженные BM25-эмбеддинги для keyword-поиска
- Payload: `issue_id`, `issue_iid`, `mr_id`, `mr_iid`, `title`, `description`, `task_type`, `quality_score`, `arch_layers`, `files_changed`, `total_files`, `has_template`
- Payload-индексы: `task_type`, `quality_score`, `issue_id`

Подготовка текстов для эмбеддингов:
- NL-вектор: заголовок задачи + описание (первые 1000 символов)
- Code-вектор: диффы, объединённые вместе (первые 2000 символов)
- BM25: NL-текст + code-текст (первые 500 символов кода)

---

## Структура проекта

```
pattern-extraction/
├── Dockerfile                          # NVIDIA CUDA 12.1.1 + Python 3.11
├── requirements.txt                    # Основные зависимости (FastAPI, SQLAlchemy, ...)
├── requirements-gpu.txt                # GPU-зависимости (PyTorch, SetFit, BERTopic, ...)
├── README.md                           # Этот файл
└── app/
    ├── __init__.py
    ├── main.py                         # FastAPI app, lifespan, инициализация
    ├── config.py                       # Pydantic Settings (env-переменные)
    │
    ├── db/
    │   ├── models.py                   # SQLAlchemy ORM (Issue, MR, Change, Comment)
    │   └── session.py                  # Async SQLAlchemy engine и session factory
    │
    ├── api/
    │   ├── router.py                   # Корневой роутер (агрегация 6 sub-routers)
    │   ├── extraction/
    │   │   ├── router.py               # POST /extract/run, GET /status, /stats
    │   │   └── schemas.py              # ExtractionRunResponse, StatusResponse, StatsResponse
    │   ├── classification/
    │   │   ├── router.py               # POST /run, /classify, GET /status, /stats, /review
    │   │   └── schemas.py              # ClassifyRequest/Response, RunClassificationRequest
    │   ├── patterns/
    │   │   ├── router.py               # POST /mine, GET /status, /stats, /hotspots, /{task_type}/checklist
    │   │   └── schemas.py              # MineRequest, ChecklistResponse, HotspotsResponse
    │   ├── artifacts/
    │   │   └── router.py               # POST /analyze, /generate, /nav-rules, GET /quality-report, /agent-md
    │   ├── indexing/
    │   │   └── router.py               # POST /qdrant, GET /qdrant/status, /qdrant/stats
    │   └── pipeline/
    │       └── router.py               # POST /pipeline/run, /run-all, GET /status
    │
    ├── models/                         # Pydantic-модели (domain)
    │   ├── classification.py           # TaskType enum, TASK_TYPE_DESCRIPTIONS, LEGACY_TYPE_MERGE
    │   ├── patterns.py                 # ChecklistItem, HotspotFile, CochangeRule, MiningProgress
    │   ├── quality.py                  # QualityScore (+ navigation_completeness), ArtifactProgress, QualityReport
    │   ├── templates.py                # ASTDelta, NavigationRegistration, PropertyInfo, EntityInfo, CodeTemplate, AnalysisProgress
    │   ├── indexing.py                 # IndexingProgress, QdrantPointPayload, IndexingStats
    │   └── pipeline.py                 # PipelineRunRequest, PipelineProgress, ALL_STAGES
    │
    ├── extractors/                     # Этап 1: извлечение данных
    │   ├── issue_extractor.py          # Извлечение issues + MRs + changes из PostgreSQL
    │   ├── mr_extractor.py             # Извлечение MR-данных
    │   └── data_normalizer.py          # Нормализация путей → архитектурные слои
    │
    ├── classifiers/                    # Этап 2: классификация
    │   ├── bertopic_explorer.py        # BERTopic кластеризация (unsupervised)
    │   ├── llm_classifier.py           # LLM-классификация через OpenRouter
    │   └── setfit_classifier.py        # SetFit fine-tuning и inference
    │
    ├── miners/                         # Этап 3: майнинг паттернов
    │   ├── cochange_miner.py           # Построение транзакций из MRs
    │   ├── fpgrowth_rules.py           # FP-Growth ассоциативные правила
    │   ├── temporal_coupling.py        # Temporal coupling между файлами
    │   └── checklist_builder.py        # Агрегация правил → чеклисты
    │
    ├── analyzers/                      # Этап 4: AST-анализ
    │   ├── ast_analyzer.py             # Batch AST-анализ всех MRs
    │   ├── csharp_parser.py            # tree-sitter C# парсер (Visary-паттерны)
    │   ├── navigation_rule_extractor.py # Извлечение навигационных правил (nav → config/initializer)
    │   └── template_synthesizer.py     # Синтез шаблонов через LLM
    │
    ├── scorers/                        # Этап 5: оценка качества
    │   └── quality_scorer.py           # Расчёт quality score для MRs
    │
    ├── generators/                     # Этап 5: генерация артефактов
    │   ├── pattern_md_generator.py     # Генерация patterns/{task_type}.md
    │   └── agent_md_generator.py       # Генерация AGENT.md
    │
    ├── indexers/                        # Этап 6: индексация
    │   └── qdrant_indexer.py           # Загрузка в Qdrant (batch_size=100)
    │
    ├── pipeline/                       # Оркестрация
    │   └── orchestrator.py             # Последовательный запуск этапов (polling)
    │
    └── utils/
        ├── eda_generator.py            # Генерация EDA HTML-отчёта
        └── text_cleaner.py             # Очистка markdown, подсчёт строк
```

---

## Выходные артефакты

### Промежуточные данные (`volumes/pattern-extraction/data/`)

| Файл | Этап | Описание |
|------|------|----------|
| `issues_dataset.json` | 1 | Полный датасет issues + MRs + changes |
| `issues_dataset.parquet` | 1 | Parquet-версия датасета |
| `classified_issues.json` | 2 | Задачи с типами и confidence |
| `taxonomy.json` | 2 | Таксономия типов задач |
| `bertopic_results.json` | 2 | Результаты BERTopic кластеризации |
| `checklists.json` | 3 | Чеклисты по типам задач |
| `temporal_coupling.parquet` | 3 | Пары связанных файлов |
| `ast_deltas.json` | 4 | AST-дельты по всем MRs |
| `navigation_rules.json` | 4.5 | Навигационные правила (property → config/initializer) |
| `templates/{task_type}.json` | 4 | Параметризованные шаблоны |
| `quality_scores.json` | 5 | Quality scores для всех MRs (включая navigation_completeness) |

### Модели (`volumes/pattern-extraction/models/`)

| Каталог | Описание |
|---------|----------|
| `task_classifier/` | Обученная модель SetFit |
| `task_classifier/classifier_meta.json` | Метаданные модели (используется при загрузке) |
| `task_classifier/training_metrics.json` | Метрики обучения (accuracy, per-class F1) |

### Отчёты (`volumes/pattern-extraction/outputs/`)

| Файл | Описание |
|------|----------|
| `eda_report.html` | Визуализация распределений данных |
| `bertopic_report.html` | Визуализация кластеров BERTopic |

### Паттерн-файлы (`history_cases/`)

| Файл | Описание |
|------|----------|
| `AGENT.md` | Руководство для AI-агентов |
| `patterns/add_entity.md` | Паттерн: добавление сущности EF Core |
| `patterns/modify_entity.md` | Паттерн: доработка сущности |
| `patterns/add_service.md` | Паттерн: добавление сервиса |
| `patterns/modify_service.md` | Паттерн: доработка сервиса |
| `patterns/import_export.md` | Паттерн: импорт/экспорт |
| `patterns/filtering_sorting.md` | Паттерн: фильтрация и сортировка |
| `patterns/config_infra.md` | Паттерн: конфигурация и инфраструктура |
| `patterns/bug_fix.md` | Паттерн: исправление ошибок |
| `patterns/refactoring.md` | Паттерн: рефакторинг |
| `patterns/ui_view.md` | Паттерн: UI/представления |

---

## Типы задач (таксономия)

| Тип | Описание | Пример |
|-----|----------|--------|
| `add_entity` | Добавление новой сущности EF Core | «Создать сущность ConstructionSiteAnalog» |
| `modify_entity` | Доработка существующей сущности (поля, связи) | «Добавить поле площади в ConstructionSite» |
| `add_service` | Добавление нового сервиса/обработчика/API endpoint | «Создать сервис расчёта аналогов» |
| `modify_service` | Доработка логики существующего сервиса | «Добавить фильтрацию по дате в сервис» |
| `import_export` | Алгоритмы импорта/экспорта (Excel, XML, XSLT) | «Импорт данных из Excel в сущность» |
| `filtering_sorting` | Фильтрация, сортировка, поиск | «Добавить сортировку по площади» |
| `config_infra` | Конфигурация, DI, миграции, настройки | «Настроить DI для нового сервиса» |
| `bug_fix` | Исправление ошибок | «Исправить расчёт площади» |
| `refactoring` | Рефакторинг без изменения функциональности | «Переименовать метод Calculate» |
| `ui_view` | Изменения представления (ViewComponents, атрибуты) | «Добавить колонку в ListView» |

### Совместимость с устаревшими типами

Для обратной совместимости поддерживается автоматическое преобразование:

| Устаревший тип | Преобразуется в |
|----------------|----------------|
| `add_api_endpoint` | `add_service` |
| `migration_schema` | `config_infra` |

### Нормализация файловых путей к архитектурным слоям

| Паттерн пути | Архитектурный слой |
|--------------|--------------------|
| `Data/Entities/*.cs` | `entity` |
| `Data/Configurations/*.cs` | `configuration` |
| `Data/Services/EventBusHandlers/*.cs` | `event_handler` |
| `Data/Services/*.cs` | `service` |
| `Data/Initializer.cs` | `initializer` |
| `Data/Migrations/*.cs` | `migration` |
| `Data/Enums/*.cs` | `enum` |
| `Data/Models/*.cs` | `model` |
| `Data/Filters/*.cs` | `filter` |
| `Data/Extensions/*.cs` | `extension` |
| `Data/EF/*.cs` | `ef_context` |
| `WebApi/Controllers/*.cs` | `controller` |
| `WebApi/DTOs/*.cs` | `dto` |
| `WebApi/Mappings/*.cs` | `mapping` |
| `WebApi/Extensions/*.cs` | `api_extension` |
| `Filtering/*.cs` | `filtering` |
| `XsltProcessor/*.cs` | `xslt` |

---

## Алгоритмы и пороговые значения

### Классификация

| Параметр | Значение | Описание |
|----------|----------|----------|
| Модель SetFit | `paraphrase-multilingual-mpnet-base-v2` | Базовая модель для fine-tuning |
| Device | `cuda` | GPU-ускорение |
| Min labeled samples | 20 | Минимум для запуска обучения |
| Oversampling target | 120 samples/class | Oversampling для классов с < 120 примерами |
| Train/test split | 80/20 | Стратифицированное разделение данных |
| Batch size | 32 | Размер батча при обучении |
| Num epochs | 4 | Количество эпох обучения |
| Num iterations | 60 | Количество итераций SetFit contrastive learning |

### Pattern Mining (FP-Growth)

| Параметр | Значение по умолчанию | Описание |
|----------|----------------------|----------|
| `min_support` | 0.05 | Минимальная доля MRs, содержащих itemset |
| `min_confidence` | 0.5 | Минимальная вероятность следствия при наличии предпосылки |
| `min_lift` | 1.2 | Минимальный lift (> 1 = положительная корреляция) |
| `max_len` | 8 | Максимальная длина itemset |
| Min transactions per type | 5 | Типы с < 5 MRs пропускаются |
| Hotspot threshold | 0.3 | Минимальная change_freq для хотспота |
| Required layer threshold | 0.6 | Минимальная confidence для обязательного слоя |

### Quality Scoring

| Компонент | Вес | Описание |
|-----------|-----|----------|
| Completeness | 30% | Затронуты ли все необходимые архитектурные слои |
| Navigation completeness | 15% | Все навигационные свойства зарегистрированы в config/initializer |
| Size score | 20% | Размер MR в пределах 50-500 строк (оптимально) |
| Coherence | 20% | Доля файлов с определённым архитектурным слоем (не «other») |
| Description quality | 15% | Качество описания задачи (0.5 за описание > 50 символов + 0.5 за наличие комментариев) |

**Оценка размера (size score):**

| Размер MR (строк) | Score |
|--------------------|-------|
| 0 | 0.0 |
| 50 — 500 | 1.0 (оптимум) |
| 500 — 5000 | Линейное убывание до 0.0 |
| > 5000 | 0.0 |

### Temporal Coupling

| Параметр | Значение | Описание |
|----------|----------|----------|
| Min co-change count | 2 | Минимум 2 совместных изменения |
| coupling_degree | co_count / max(count_f1, count_f2) | Степень связанности файлов |

### Qdrant индексация

| Параметр | Значение | Описание |
|----------|----------|----------|
| nl_dense dimension | 768 | Размер вектора текстовых эмбеддингов (`multilingual-e5-base`) |
| code_dense dimension | 768 | Размер вектора code-эмбеддингов (Voyage Code-3 или e5-base fallback) |
| sparse_bm25 | IDF modifier | BM25 с IDF-модификатором |
| quality_score filter | ≥ 0.5 | Минимальный score для попадания в индекс |
| batch_size | 100 | Размер батча при загрузке в Qdrant |

### Pipeline Orchestrator (polling)

| Параметр | Значение | Описание |
|----------|----------|----------|
| `POLL_INTERVAL` | 5 секунд | Интервал опроса статуса этапа |
| `DEFAULT_STAGE_TIMEOUT` | 3600 секунд (1 час) | Таймаут по умолчанию для этапа |
| `classify` timeout | 43200 секунд (12 часов) | Таймаут для этапа классификации |
| `MAX_POLL_ERRORS` | 5 | Максимум ошибок опроса до сбоя |
| `STARTUP_GRACE_POLLS` | 3 | Допуск «idle»-статусов при старте (grace period) |

---

## Устранение неполадок

### Контейнер не стартует

```bash
# Проверить логи
docker compose logs pattern-extraction

# Проверить GPU
docker run --rm --gpus all nvidia/cuda:12.1.1-runtime-ubuntu22.04 nvidia-smi
```

### «SetFit model not loaded» (код 503 на /classification/classify)

Модель SetFit не обучена. Нужно запустить этап классификации:

```bash
curl --location 'http://localhost:8200/api/v1/classification/run' \
  --header 'Content-Type: application/json' \
  --data '{"skip_bertopic": true, "skip_llm": true, "force_retrain": true}'
```

> Для обучения нужен файл `classified_issues.json`. Если его нет — запустите полную классификацию (`skip_llm: false`).

### «issues_dataset.json not found»

Этап извлечения не выполнен:

```bash
curl --location --request POST 'http://localhost:8200/api/v1/extract/run'
```

### «No checklist for task_type» (код 404)

Этап mining не выполнен:

```bash
curl --location --request POST 'http://localhost:8200/api/v1/patterns/mine'
```

### Qdrant не доступен

```bash
# Проверить health Qdrant
curl http://localhost:6333/healthz

# Перезапустить
docker compose restart qdrant
```

### LLM-классификация зависла

Проверьте `OPENROUTER_API_KEY` в `.env`. Без ключа LLM-этап будет пропущен с предупреждением.

### Нехватка GPU памяти

BERTopic и SetFit используют ~1.5 GB VRAM каждый (пиковое значение). Если GPU памяти недостаточно:

1. Запускайте этапы по отдельности (не через pipeline)
2. Между этапами перезапустите контейнер для освобождения VRAM:
   ```bash
   docker compose restart pattern-extraction
   ```

### Медленная LLM-классификация

LLM-классификация 1300 задач через OpenRouter занимает ~15-20 минут (таймаут: 12 часов). Прогресс можно отслеживать:

```bash
watch -n 5 'curl -s http://localhost:8200/api/v1/classification/status | python -m json.tool'
```

### Этап пайплайна завис в статусе «idle»

Оркестратор допускает до 3 опросов со статусом `idle` после запуска этапа (`STARTUP_GRACE_POLLS`). Если этап не перешёл в `running` после grace period — он считается проваленным. Проверьте логи конкретного этапа.

### Этап пайплайна не отвечает

Если эндпоинт статуса не отвечает 5 раз подряд (`MAX_POLL_ERRORS`), пайплайн завершается с ошибкой. Проверьте, что контейнер работает: `docker compose ps`.

---

## Вклад в проект

### Требования к разработке

1. Python 3.11+
2. NVIDIA GPU с CUDA 12.1+
3. Docker Desktop с поддержкой GPU

### Локальная разработка (без Docker)

```bash
cd pattern-extraction

# Создать виртуальное окружение
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

# Установить зависимости
pip install -r requirements-gpu.txt
pip install -r requirements.txt

# Задать переменные окружения
export DB_HOST=localhost
export DB_PORT=5432
export DB_USER=postgres
export DB_PASSWORD=postgres
export DB_NAME=gitlab
export QDRANT_HOST=localhost
export QDRANT_PORT=6333

# Запустить сервис
uvicorn app.main:app --host 0.0.0.0 --port 8200 --reload
```

### Добавление нового типа задачи

1. Добавьте тип в `app/models/classification.py` (enum `TaskType` и `TASK_TYPE_DESCRIPTIONS`)
2. Перезапустите LLM-классификацию с `force_retrain: true`
3. Пайплайн автоматически создаст чеклист, шаблон и MD-файл для нового типа

### Добавление нового архитектурного слоя

1. Добавьте правило в `app/extractors/data_normalizer.py` (`ARCH_LAYER_RULES`)
2. Перезапустите этап извлечения и все последующие этапы

### Обновление моделей

- **SetFit:** Переобучите через API с `force_retrain: true`
- **BERTopic:** Перезапустите классификацию с `skip_bertopic: false`
- **Эмбеддинги:** Измените `EMBEDDING_MODEL_NAME` в docker-compose и перезапустите индексацию

### Структура коммитов

- `feat:` — новая функциональность
- `fix:` — исправление ошибки
- `refactor:` — рефакторинг без изменения поведения
- `docs:` — документация
- `perf:` — оптимизация производительности
