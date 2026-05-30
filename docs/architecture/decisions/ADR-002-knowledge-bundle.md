# ADR-002. KnowledgeBundle как единый источник истины

**Status**: Accepted

---

## Контекст

В baseline-системе проектная специфика была **рассеяна по ~163
hardcoded местам**:
- 113 строк в `roslyn-graph` (`PatternRegistry.cs` 70,
  `ProjectAnalyzer.cs` 30, `AnalogPredictor.cs` 3,
  `DependencyGraphBuilder.cs` 5, `Program.cs` 5).
- ~50 строк в `multiagent/app/agents/` (системные промпты с
  dotnet-specific терминами).

**Последствия**:
- Подключение нового .NET-проекта = ~3 недели ручной работы,
  включая пересборку контейнеров.
- Невозможен B2B2B SDK (нельзя продавать «универсальный
  C#-анализатор», который работает только с одной кодовой базой).
- Замечание по итогам экспертной оценки: «вы помогаете разработчику
  писать код, но заставляете его руками писать архитектуру для агента».
- То же отмечалось по итогам пилотного применения.

---

## Решение

Ввести **унифицированную схему `project_conventions.json`** как
**единственный источник истины** о специфике проекта. Все
hardcoded-строки выносятся в этот JSON.

**Реализация (3 связанных WP)**:

1. **WP-B1 (KnowledgeBundle)**:
   - 5 Pydantic-схем (`ProjectBundle`, `FilePattern`,
     `RegistrationPattern`, `LayerSpec`, `OperationRule`).
   - JSON Schema `schema/project_conventions.schema.json`.
   - `ProjectBundleLoader` (jsonschema + Pydantic, fail-fast).
   - `TaskPackBuilder` для сборки task-specific Pack.

2. **WP-B7 (чистка multiagent agents)**:
   - Удалены все упоминания dotnet-specific (`Initializer`,
     `DataConfiguration`, `Visary`, `AddDefaultMnemonic`, ...) из
     системных промптов.
   - Constants хидрируются из `bundle.*`.
   - Системные промпты сокращены 2× (10 500 → 5 655 chars).

3. **WP-C1 (Project-agnostic Roslyn Graph)**:
   - Все 113 hardcoded строк вынесены в conventions.
   - Сервис стартует только с валидным conventions, иначе
     fail-fast.
   - Endpoints `/api/conventions/load` (hot-reload) и
     `/api/conventions/current`.

---

## Альтернативы

1. **Параметризация через env-переменные** — отвергнуто (не
   масштабируется на 100+ настроек, нет валидации структуры).
2. **Генератор conventions из исходников** — отвергнуто (хрупкость
   при изменениях, нет гарантии корректности). Auto-discovery
   (WP-C2) — это **complement**, не замена.
3. **Параметризация через DSL** — отвергнуто (избыточная
   сложность, JSON Schema достаточно).
4. **Branching codebase per client** — отвергнуто (catastrophic
   maintenance overhead при росте клиентов).

---

## Последствия

### Плюсы
- Hardcoded строк в `multiagent/agents/` = **0** (с ~50).
- Hardcoded строк в `roslyn-graph/` = **0** (с 113).
- Время онбординга нового .NET-проекта: **~3 недели → ~4 часа**.
- Foundation для B2B2B SDK (WP-D5).
- Hot-reload conventions без перезапуска сервисов.

### Минусы
- Дополнительный config-файл (~180 строк JSON для dotnet-app),
  который нужно поддерживать.
- При ошибках в conventions сервис **отказывается стартовать**
  (fail-fast) — это **фича**, но требует чёткой документации.

### Технический долг
- Auto-discovery (WP-C2) — partial recall (~80–88 %); 100 %
  невозможно для произвольных проектов.

---

## Связанные документы

- [`../detailed-architecture.md`](../detailed-architecture.md) — колонка 6, блок 10 (Конвенции проекта).
- [`ADR-003-hybrid-deterministic-llm.md`](ADR-003-hybrid-deterministic-llm.md) — программные трансформеры используют `bundle.registration_patterns`.
