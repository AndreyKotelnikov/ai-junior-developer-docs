# Programmatic Transformers — каталог 10 трансформеров

**Назначение**: технический справочник по 10 детерминированным
трансформерам из `multiagent/app/tools/programmatic_transformers.py`.

**Связанные документы**:
- [`../architecture/decisions/ADR-003-hybrid-deterministic-llm.md`](../architecture/decisions/ADR-003-hybrid-deterministic-llm.md) — архитектурное решение о гибридном (детерминированном + LLM) слое.
- [`ast_transformers_registry_full.md`](ast_transformers_registry_full.md) — расширенный реестр трансформеров и их доля в корпусе задач.

---

## Принцип работы

Каждый трансформер — **функция AST → AST**, использующая шаблоны
строк из `bundle.registration_patterns`. Не использует LLM,
детерминированна, имеет unit-тесты.

Активация: Orchestrator помечает subtask `programmatic=true` на
основе `bundle.operations[*].transformer`. Если трансформер
возвращает `None` (edge-case) — fallback на LLM-Coder через
`transformer.fallback_llm` event.

---

## Каталог трансформеров

### 1. `add_entity_registration(entity_name)`

**Назначение**: добавить регистрацию сущности в основной
configuration файл.

**Шаблон** (из `bundle.registration_patterns.entity_registration`):
```csharp
context.AddEntity<{entity}>().AddDefaultMnemonic();
```

**Пример до/после**:
```csharp
// До:
context.AddEntity<Foo>().AddDefaultMnemonic();
// После add_entity_registration("Bar"):
context.AddEntity<Foo>().AddDefaultMnemonic();
context.AddEntity<Bar>().AddDefaultMnemonic();
```

**Insertion strategy**: после последнего `AddEntity<>` или, если
нет — перед закрывающей скобкой метода.

---

### 2. `add_associated_entity(owner_entity, nav_property)`

**Шаблон** (`bundle.registration_patterns.associated_entity`):
```csharp
.AssociatedEntity(f => f.{nav_property})
```

**Insertion**: chain-aware, после соответствующего `AddEntity<owner_entity>()`.

---

### 3. `add_one_to_many(parent_entity, child_entity, nav_property)`

**Шаблон** (`bundle.registration_patterns.one_to_many`):
```csharp
.AddOneToManyAssociation<{child_entity}>(p => p.{nav_property})
```

**Insertion**: chain-aware, после `AddEntity<parent_entity>()` или
после предыдущих `AddOneToManyAssociation`.

---

### 4. `add_owned_collection(owner_entity, collection_property)`

**Шаблон** (`bundle.registration_patterns.owned_collection`):
```csharp
.OwnedCollection(e => e.{collection_property})
```

---

### 5. `add_using(file_path, namespace)`

**Шаблон**:
```csharp
using {namespace};
```

**Insertion**:
- После последнего `using` statement.
- Если нет `using`-ов — в начало файла после optional BOM.
- Дедупликация — если `using` уже есть, no-op.

---

### 6. `add_scalar_property(class_path, property_name, type, attributes=[])`

**Шаблон**:
```csharp
public {type} {property_name} { get; set; }
```

С опциональными атрибутами:
```csharp
[Required]
[MaxLength(50)]
public string Code { get; set; }
```

**Insertion**: внутри class body, после последнего property.

---

### 7. `add_enum_value(enum_path, value_name, numeric_value=null)`

**Шаблон**:
```csharp
{value_name},                        // если numeric_value=null
{value_name} = {numeric_value},      // если задано
```

**Insertion**: внутри enum body, перед закрывающей скобкой.

---

### 8. `register_di_service(interface_type, implementation_type, lifetime)`

**Шаблон** (lifetime ∈ Transient / Scoped / Singleton):
```csharp
services.Add{lifetime}<{interface_type}, {implementation_type}>();
```

**Insertion**: в DI-registration метод (`ConfigureServices` или
эквивалент по conventions).

---

### 9. `register_filter(entity, filter_name, body_stub)`

**Назначение**: регистрация LINQ-фильтра по conventions проекта.

**Insertion**: в filter-registration метод.

---

### 10. `delete_file(path)`

**Назначение**: удаление файла (через `FileTools.delete_file`).

**Use case**: subtask explicitly marked for deletion (например,
после миграции содержимого в другой файл).

**Safety**: проверка `_is_active_subtask_target()` — нельзя удалить
файл, который сам является target'ом активного subtask'а.

---

## Multi-line anchor + chain-aware insertion

Главная сложность — **edge-case с 50+ одинаковыми suffix-блоками**
в `DataConfiguration.cs`. Если просто использовать regex
`/\.AddEntity<>/` для anchor — получим первый match, что неверно
(нужно вставить **в правильное место**, не в первое попавшееся).

Решение:
1. Найти **все** matches.
2. Пройти по AST в обратном порядке, чтобы insertion'ы не
   повлияли друг на друга.
3. Использовать **multi-line anchor** (включая комментарии и
   контекст вокруг).
4. **Chain-aware**: если есть chain `.AddEntity<X>().AddDefaultMnemonic()
   .AddOneToManyAssociation<Y>(...)`, новый `.AddOneToManyAssociation`
   добавляется в **правильную позицию** chain'а (с учётом
   `bundle.registration_patterns[*].kind`).

---

## Шаблоны из bundle.registration_patterns

Ни один трансформер **не имеет hardcoded строк**. Все шаблоны —
из конвенций:

```jsonc
// project_conventions.json
"registration_patterns": [
  {
    "name": "entity_registration",
    "pattern": "\\.AddEntity<(\\w+)>\\(\\)",
    "template": "context.AddEntity<{entity}>().AddDefaultMnemonic()",
    "kind": "method_call"
  },
  {
    "name": "one_to_many",
    "pattern": "\\.AddOneToManyAssociation<(\\w+)>\\(...\\)",
    "template": ".AddOneToManyAssociation<{child}>(p => p.{nav})",
    "kind": "method_call_chained"
  }
  // ... ещё 4
]
```

При смене проекта (с другим ORM-фреймворком) — **только** правка
conventions, без изменений в коде трансформеров.

---

## Тесты

`multiagent/tests/test_programmatic_transformers.py` — **31 unit-
тест**:
- Happy paths для всех 10 трансформеров.
- Edge cases: пустой файл, дубликат регистрации, conflict в chain.
- Multi-line anchor сценарии.

---

## Интеграция с pipeline

```python
# multiagent/app/pipeline/executor.py
async def _execute_subtask(self, sub: SubTask):
    if sub.programmatic and sub.transformer in TRANSFORMERS:
        transformer = TRANSFORMERS[sub.transformer]
        result = transformer(**sub.transformer_args)
        if result is None:
            # Edge case — fallback на LLM
            await self._llm_coder.execute(sub)
            self._emit_metric("transformer.fallback_llm")
        else:
            await file_tools.write(result)
    else:
        await self._llm_coder.execute(sub)
```

---

## Метрики

На эталонной задаче (10-полевая модификация сущности):
- Subtasks через программные трансформеры: **12 / 13 = 92 %**.
- LLM-вызовов в Coder: **5 → 1**.
- `transformer.fallback_llm` events: **0** (все успешно).

---

## Известные ограничения

- Только C#-синтаксис (для других языков — нужны новые трансформеры
  или AST-абстракция через tree-sitter).
- Edge-cases в кастомных DSL могут требовать ручной правки
  conventions.

---

## Связанные документы

- [`../architecture/decisions/ADR-003-hybrid-deterministic-llm.md`](../architecture/decisions/ADR-003-hybrid-deterministic-llm.md) — гибридный (детерминированный + LLM) слой.
- [`ast_transformers_registry_full.md`](ast_transformers_registry_full.md) — расширенный реестр трансформеров и доля задач в корпусе.
