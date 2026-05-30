# Реестр 10 AST-трансформеров и тестовое покрытие

## 1. Назначение документа

Документ фиксирует **полный реестр всех десяти детерминированных AST-трансформеров** проекта AI Junior Developer — нейросимвольная альтернатива LLM-вызову для типовых EF Core-операций.

10 AST-трансформеров реализуют **главную техническую ось дифференциации проекта** (гибридный детерминированный + LLM-конвейер) и закрывают около 92 % подзадач **на эталонной инструментальной задаче «доработка существующей сущности EF Core»** (12 / 13 подзадач решены без LLM-вызова); по другим типам задач замеры покрытия не проводились — повышение этого показателя является направлением дальнейшей работы.

## 2. Архитектурный контекст

Каждый AST-трансформер — это **функция Python вида** `transform(source_ast: SyntaxTree, params: TransformerParams) -> SyntaxTree`, реализованная в модуле `multiagent/app/tools/programmatic_transformers.py`. Параметры трансформера типизированно валидируются через Pydantic v2 (`extra="forbid"`); шаблон строки берётся из `bundle.registration_patterns` (конвенции выносятся в `project_conventions.json`); инстанциация — через f-string подстановку с защитной проверкой `_is_active_subtask_target()` (трансформер не модифицирует файлы, не относящиеся к текущей подзадаче).

Coder-агент **сначала пытается применить детерминированный AST-трансформер** для каждой подзадачи; если ни один трансформер не покрывает текущую подзадачу — она направляется на Slim Coder с per-subtask RAG-контекстом (~ 2,5 K токенов промпта).

## 3. Полный реестр 10 трансформеров

**Таблица — Реестр всех 10 AST-трансформеров с параметрами и тестовым покрытием**

| № | Имя трансформера | Что делает | Источник параметров | Целевой файл | Unit-тестов |
|:-:|---|---|---|---|:-:|
| 1 | `add_entity_registration` | Вставляет `context.AddEntity<T>().AddDefaultMnemonic()` в `Initializer.cs` | `bundle.registration_patterns.entity_registration` | `Initializer.cs` | 4 |
| 2 | `add_associated_entity` | Регистрирует ассоциацию 1:1 lookup-FK через `.AssociatedEntity(f => f.{nav})` | `bundle.registration_patterns.associated_entity` | `Initializer.cs` | 4 |
| 3 | `add_one_to_many` | Добавляет связь 1:N через `.AddOneToManyAssociation<{child}>(p => p.{nav})` (chained) | `bundle.registration_patterns.one_to_many` | `Initializer.cs` | 4 |
| 4 | `add_owned_collection` | Регистрирует владеющую коллекцию через `.OwnedCollection(e => e.{nav})` | `bundle.registration_patterns.owned_collection` | `Initializer.cs` | 3 |
| 5 | `add_using` | Вставляет `using {namespace};` после последнего using-блока (с дедупликацией) | — (parsing-only, без bundle) | любой `*.cs` | 3 |
| 6 | `add_scalar_property` | Добавляет `public {type} {name} { get; set; }` в класс сущности | — (template-based) | `*Entity*.cs` | 4 |
| 7 | `add_enum_value` | Вставляет `{value} = {numeric},` в enum-объявление с автоинкрементом значения | — (template-based) | `*Enum*.cs` | 3 |
| 8 | `register_di_service` | Регистрирует сервис в DI-контейнере: `services.Add{Lifetime}<{iface}, {impl}>()` | `bundle.registration_patterns.di_service` | `Startup.cs` / `*ServiceRegistration.cs` | 3 |
| 9 | `register_filter` | Регистрирует фильтр в выборках через `filter_register` | `bundle.registration_patterns.filter` | `*FilterRegistration*.cs` | 2 |
| 10 | `delete_file` | Удаляет файл с safety-проверкой и записью в audit-log | — (через `FileTools.delete_file`) | любой целевой | 1 |

**Итого:** **31 unit-тест на 10 трансформеров** (среднее 3,1 теста на трансформер); полный набор тестов — в `multiagent/tests/tools/test_programmatic_transformers.py`.

> Помимо десяти канонических трансформеров реализация содержит и несколько вспомогательных трансформеров (`add_entity_block_in_dataconfig`, `register_mnemonic_filter`, `add_scalar_properties_bulk`), однако в качестве канонического набора в работе рассматриваются именно 10 перечисленных выше трансформеров.

## 4. Покрытие подзадач эталонной задачи без LLM-вызова

Эталонная инструментальная задача «доработка существующей сущности» декомпозируется Orchestrator на **13 атомарных подзадач**. Из них **12 закрываются 10-ю AST-трансформерами без LLM-вызова** (≈ 92 % покрытия); 13-я подзадача (нестандартная бизнес-логика валидации) направляется на Slim Coder.

**Таблица — Соответствие 13 подзадач эталонной задачи 10 трансформерам**

| Подзадача | Что делает | AST-трансформер | LLM? |
|:-:|---|:-:|:-:|
| 1 | Создание класса сущности с базовым типом | `add_entity_registration` (часть 1) | нет |
| 2 | Регистрация в `Initializer.cs` через `AddEntity<T>()` | `add_entity_registration` (часть 2) | нет |
| 3 | Добавление 1-го FK-поля (`CategoryID`) | `add_scalar_property` | нет |
| 4 | Регистрация ассоциации `1:1 lookup` для FK | `add_associated_entity` | нет |
| 5 | Добавление 2-го FK-поля (`ParentID`) | `add_scalar_property` | нет |
| 6 | Регистрация навигационной коллекции `Children` | `add_one_to_many` | нет |
| 7 | Добавление скалярного свойства `Name: string` | `add_scalar_property` | нет |
| 8 | Добавление скалярного свойства `Code: string` | `add_scalar_property` | нет |
| 9 | Добавление скалярного свойства `Priority: int` | `add_scalar_property` | нет |
| 10 | Добавление `using` для пространства имён ассоциации | `add_using` | нет |
| 11 | Регистрация CRUD-сервиса в DI | `register_di_service` | нет |
| 12 | Регистрация фильтра по `CategoryID` в выборках | `register_filter` | нет |
| 13 | Кастомная валидация в методе `Validate()` (бизнес-логика) | — | **да** (Slim Coder) |

**Эффект:** для эталонной задачи число LLM-вызовов снижено с 10 до 1 (12 из 13 подзадач без LLM; LLM-вызовов 5 → 1; токенов 7 K → 2,5 K); фактический разброс зависит от типа задачи.

## 5. Структура шаблона трансформера (пример реализации)

Пример типизированной реализации трансформера `add_one_to_many` на Python:

```python
def transform_add_one_to_many(
    source: SyntaxTree,
    parent_entity: str,
    child_entity: str,
    nav_property: str,
    bundle: ProjectBundle,
) -> SyntaxTree:
    """
    Добавляет регистрацию ассоциации 1:N в Initializer.cs:
        .AddOneToManyAssociation<ChildEntity>(p => p.NavProperty)
    
    Шаблон строки берётся из bundle.registration_patterns.one_to_many,
    что обеспечивает project-agnostic-применение трансформера.
    """
    template = bundle.registration_patterns.one_to_many
    # template = ".AddOneToManyAssociation<{child}>(p => p.{nav})"
    
    insertion = template.format(child=child_entity, nav=nav_property)
    
    # Защитная проверка: anchor должен соответствовать активной подзадаче
    if not _is_active_subtask_target(source, parent_entity):
        raise TransformerSafetyError(
            f"Anchor for {parent_entity} not in active subtask scope"
        )
    
    return source.insert_after_anchor(
        anchor=f"AddEntity<{parent_entity}>()",
        text=insertion,
    )
```

Ключевые свойства реализации:

- **Pure-функция:** трансформер не имеет побочных эффектов вне возвращаемого `SyntaxTree`.
- **Параметризация через `bundle`:** шаблон строки внешний, трансформер не содержит hardcoded-имён фреймворка — это обеспечивает применимость к любому .NET-проекту через смену `project_conventions.json` (см. ADR-002).
- **Safety-проверка:** трансформер проверяет, что anchor (точка вставки) принадлежит активной подзадаче, иначе бросает `TransformerSafetyError`.
- **Roslyn-based парсинг:** все операции с `SyntaxTree` — через `Microsoft.CodeAnalysis.CSharp.SyntaxFactory` (микросервис `roslyn-graph` обеспечивает HTTP-API для этих операций).

## 6. Архитектурные принципы выбора 10 трансформеров

10 трансформеров покрывают типовые EF Core-операции по принципу **80 / 20** — двадцать процентов архитектурных операций, покрывающие восемьдесят процентов реальных задач корпоративных CRM/ERP-проектов на стеке ASP.NET Core 3.1 + EF Core. Принципы выбора:

1. **Только детерминированные паттерны** — трансформер реализуется только тогда, когда операция имеет точный синтаксический шаблон, не зависящий от семантики бизнес-домена (например, регистрация ассоциации `1:N` имеет инвариантную форму вне зависимости от того, какие именно сущности связаны).
2. **Покрытие через статистику корпуса** — анализ 1 154 пар MR-diff корпоративного GitLab показал, что ≈ 70 % (809 из 1 154) задач затрагивают набор {Entity, DbContext, Initializer.cs, DataConfiguration.cs}, а 92 % из этих задач — типовые операции из 10 шаблонов.
3. **Один трансформер — одна операция** — каждый трансформер выполняет ровно одно изменение AST, что обеспечивает ортогональность и упрощает тестирование (модульное покрытие).
4. **Safety-инварианты на уровне Roslyn** — трансформер не может оставить файл в состоянии, которое не пройдёт Roslyn-валидацию (инкрементальная валидация после каждого трансформера).

## 7. Источник данных

- **Реализация:** `multiagent/app/tools/programmatic_transformers.py` (10 функций трансформеров).
- **Тестовое покрытие:** `multiagent/tests/tools/test_programmatic_transformers.py` (31 unit-тест).
- **Параметры:** `project_conventions.json` секция `registration_patterns` (~ 11 шаблонов).
- **Эмпирическая валидация:** эталонная задача «доработка существующей сущности», 13 подзадач из факторного эксперимента.
