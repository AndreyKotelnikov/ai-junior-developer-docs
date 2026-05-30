# Roslyn Graph Endpoints — справочник эндпоинтов

Справочник по HTTP-API сервиса `roslyn-graph` (.NET 9, Minimal API): около
**50 эндпоинтов**, сгруппированных в **14 функциональных категорий**, с
параметрами, структурами ответов и примерами. Семантический граф C# строится
поверх платформы Microsoft.CodeAnalysis (Roslyn) и обслуживает фазу локализации
изменений без обращения к языковой модели.

Машиночитаемое описание контракта доступно по `GET /openapi/v1.json`.

## Сводка категорий и эндпоинтов

Полный перечень категорий с фактическим числом эндпоинтов (по маршрутам сервиса):

| # | Категория | Эндпоинтов | Назначение |
|:-:|---|:-:|---|
| 1 | `/api/graph/*` | 7 | построение и обход графа: `build`, `query`, `neighbors`, `stats`, `invalidate`, `update-file`, `usage-of-pattern` |
| 2 | `/api/analyze/*` | 5 | семантический анализ: `entity`, `file`, `service`, `nav-properties`, `invalidate` |
| 3 | `/api/find/*` | 9 | локализация точек правки: `insertion-point`, `dataconfig`, `initializer`, `registration`, `usages`, `anchor`, `di-registrations`, `enum-values`, `similar-service` |
| 4 | `/api/registry/*` | 5 | реестр шаблонов: `get`, `validate`, `template`, `template-for-property`, `all` |
| 5 | `/api/impact/*` | 4 | анализ влияния: `analyze`, `callers`, `references`, `method-dataflow` |
| 6 | `/api/analog/*` | 2 | подбор аналогов: `predict`, `find-similar` |
| 7 | `/api/classify/*` | 2 | классификация типа задачи: `type`, `batch` |
| 8 | `/api/suggest/*` | 2 | подсказки: `anchor`, `fix` |
| 9 | `/api/conventions/*` | 5 | конвенции проекта: `current`, `load`, `auto-discover`, `validate`, `save` |
| 10 | `/api/validate/*` | 1 | проверка регистраций: `registrations` |
| 11 | `/api/refactor/*` | 3 | рефакторинг: `rename`, `extract-method`, `move-type` |
| 12 | `/api/ui/*` | 1 | детектор UI-представлений: `detect-view-patterns` |
| 13 | `/api/cochange/*` | 1 | co-change-зависимости из истории git: `files` |
| 14 | `/api/diagnostics/*` | 1 | семантическая диагностика: `semantic` |
| — | служебные | 3 | `/api/status`, `/health`, `/swagger` |

Итого функциональных эндпоинтов — около 50 (плюс служебные). Ниже приведены
представительные эндпоинты каждой категории с примерами запросов и ответов;
полный контракт — в OpenAPI-описании сервиса.

---

## 1. Группа `/api/find/*` (5 endpoints)

### 1.1. `POST /api/find/insertion-point`

Найти, куда вставить новый код в файле.

**Request**:
```json
{
  "file": "Data/Configurations/DataConfiguration.cs",
  "type": "Foo",
  "operation": "add_entity_registration"
}
```

**Response**:
```json
{
  "line": 42,
  "column": 0,
  "context": "// existing entity registrations",
  "anchor_text": "context.AddEntity<Bar>().AddDefaultMnemonic();"
}
```

### 1.2. `POST /api/find/dataconfig`

Найти основной DataConfiguration файл проекта.

### 1.3. `POST /api/find/initializer`

Найти Initializer файл проекта.

### 1.4. `POST /api/find/enum-values`

Извлечь все значения enum.

**Request**: `{"enum_name": "Status"}`
**Response**: `{"values": ["Active", "Inactive", "Pending"]}`

### 1.5. `POST /api/find/similar-service`

Найти аналог сервиса для нового типа.

**Request**: `{"target_type": "FooService", "operation": "create"}`
**Response**: `{"similar": ["BarService", "BazService"], "scores": [0.87, 0.65]}`

---

## 2. Группа `/api/analyze/*` (3 endpoints)

### 2.1. `POST /api/analyze/file`

AST-анализ файла.

**Request**: `{"file": "Data/Entities/Foo.cs"}`
**Response**: `{"namespace": "...", "classes": [...], "usings": [...], "members": [...]}`

### 2.2. `POST /api/analyze/entity`

Детали entity-класса (свойства, навигации, атрибуты).

### 2.3. `POST /api/analyze/type`

Универсальный анализ любого типа.

---

## 3. Группа `/api/suggest/*` (2 endpoints)

### 3.1. `POST /api/suggest/anchor`

Текстовый якорь для вставки.

### 3.2. `POST /api/suggest/fix` (WP-C3)

Программное предложение исправления для CS-ошибки.

**Request**: `{"file": "...", "diagnostic": {"code": "CS0246", "line": 12}}`
**Response**: `{"patch": "+using X;", "confidence": 0.95}`

---

## 4. Группа `/api/refactor/*` (3 endpoints, WP-C3)

### 4.1. `POST /api/refactor/rename`

Переименование символа через Roslyn `Renamer.RenameSymbolAsync`.

### 4.2. `POST /api/refactor/extract-method`

Извлечение метода из кода.

### 4.3. `POST /api/refactor/move-type`

Перенос типа в другой файл с генерацией `using`.

---

## 5. Группа `/api/validate/*` (1 endpoint, WP-C3)

### 5.1. `POST /api/validate/registrations`

TaskPack-driven completeness проверка регистраций.

**Request**: `{"task_pack": {...}, "changed_files": ["..."]}`
**Response**: `{"missing_registrations": [...], "complete": false}`

---

## 6. Группа `/api/impact/*` (2 endpoints)

### 6.1. `POST /api/impact/references`

Все ссылки на символ.

### 6.2. `POST /api/impact/method-dataflow` (WP-C3)

Поля → return; side-effects; callers.

---

## 7. Группа `/api/diagnostics/*` (1 endpoint, WP-A2)

### 7.1. `POST /api/diagnostics/semantic`

Roslyn semantic-валидация без full build.

**Request**:
```json
{
  "files": ["Data/Entities/Foo.cs"],
  "severity_filter": ["error", "warning"],
  "category_filter": ["compilation"]
}
```

**Response**:
```json
{
  "diagnostics": [
    {
      "file": "Data/Entities/Foo.cs",
      "line": 12,
      "code": "CS0246",
      "severity": "error",
      "message": "..."
    }
  ],
  "duration_ms": 6234
}
```

**Метрики**: ~6 сек на файл (vs ~60 сек full build).

---

## 8. Группа `/api/graph/*` (2 endpoints)

### 8.1. `POST /api/graph/build`

Построение полного dependency graph.

> **Замечание**: при первом вызове после рестарта возможен HTTP 400
> из-за MSBuildLocator race-condition (см.
> подробнее — [`../architecture/detailed-architecture.md`](../architecture/detailed-architecture.md)).

### 8.2. `POST /api/graph/usage-of-pattern` (WP-C3)

Поиск usage именованного паттерна (`bundle.registration_patterns`).

---

## 9. Группа `/api/conventions/*` (3 endpoints, WP-C1+C2)

### 9.1. `POST /api/conventions/load`

**Hot-reload** conventions без перезапуска.

**Request**: полный `project_conventions.json`.
**Response**:
- 200: `{"status": "ok", "patterns_loaded": N}`.
- 400: `{"error": "Validation failed: <field>: <reason>"}`.

### 9.2. `GET /api/conventions/current`

Текущие загруженные conventions.

### 9.3. `POST /api/conventions/auto-discover` (WP-C2)

Auto-discovery — генерация `project_conventions.draft.json` из
AST + git-log.

**Request**:
```json
{
  "code_path": "/app/code",
  "git_path": "/app/code/.git",
  "language_hint": "csharp"
}
```

**Response**: `project_conventions.draft.json` + `_metadata`
с `confidence_score` и `warnings`.

**Метрики**: ~5 сек на типовой проект (1 000–3 000 файлов).

---

## 10. Группа `/api/cochange/*` (1 endpoint, WP-C4)

### 10.1. `POST /api/cochange/files`

Apriori-анализ git-log: какие файлы обычно меняются вместе с
anchor'ом.

**Request**:
```json
{
  "anchor": "Data/Entities/Foo.cs",
  "window": 200,
  "min_support": 3
}
```

**Response**:
```json
{
  "items": [
    {"file": "Data/Configurations/DataConfiguration.cs", "support": 47, "confidence": 0.94}
  ],
  "cached": false,
  "duration_ms": 1234
}
```

**Метрики**:
- Cold latency: ~900–1400 мс.
- Warm latency (cache hit, TTL 1 час): 0 мс compute.
- Precision@5 на горячих anchor'ах: **89 %**.

---

## 11. Группа `/api/ui/*` (1 endpoint, WP-C3)

### 11.1. `POST /api/ui/detect-view-patterns`

Detect UI-паттерны в .cshtml / Razor файлах.

---

## 12. Прочие endpoints (4)

### 12.1. `POST /api/classify/type`

Классификация типа: entity / service / controller / external / ...

### 12.2. `POST /api/query/type`

Поиск типа по имени.

### 12.3. `POST /api/analog/predict`

Предсказание аналога для нового типа (на основе bundle.entity_base_types).

### 12.4. `GET /api/status`

Health + текущее состояние сервиса.

---

## 13. OpenAPI / Swagger UI

```bash
GET /openapi/v1.json                  # машиночитаемая спецификация
GET /swagger                          # Swagger UI (для browser)
```

Около 50 функциональных эндпоинтов в 14 категориях (плюс служебные
`/api/status`, `/health`, `/swagger`); часть путей имеет варианты GET и POST.

---

## 14. Аутентификация

Версия 1.0.0 — **без аутентификации** (on-prem контур, network
isolation). Public SaaS — TODO.

---

## 15. Связанные документы

- [`../architecture/detailed-architecture.md`](../architecture/detailed-architecture.md) — место сервиса `roslyn-graph` в общей архитектуре.
- [`programmatic-transformers.md`](programmatic-transformers.md) — детерминированные AST-трансформеры, использующие эти эндпоинты.
