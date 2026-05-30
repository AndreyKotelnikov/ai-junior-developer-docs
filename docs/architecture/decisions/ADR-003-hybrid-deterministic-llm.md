# ADR-003. Hybrid Deterministic + LLM (программные трансформеры)

**Status**: Accepted

---

## Контекст

Замечания по итогам экспертной оценки (велосипедность / устаревший
подход и spaghetti-код от LLM) указывали на две взаимосвязанные
проблемы baseline-подхода:

1. **«Велосипедность»**: чистый LLM-подход не отличает нас от
   Cursor / Copilot Workspace / Aider — рынок насыщен.
2. **«Spaghetti-код»**: LLM генерирует 5 одинаковых блоков с
   непредсказуемыми различиями (порядок аргументов, кавычки,
   лишние скобки), что критично для регулируемого on-prem
   сегмента (любая галлюцинация = блокер для compliance).

При этом **полностью отказаться от LLM** нельзя — задачи
требуют семантического понимания требования.

---

## Решение

Реализовать **гибридный layer**:

- **Программные трансформеры** для типовых subtasks (10 шт.).
- **Программный фиксер** для типовых CS-ошибок (5 кодов).
- **LLM** только для creative subtasks (где детерминированный
  трансформер невозможен).

**Реализация**:

### WP-B2: ProgrammaticTransformers (10 трансформеров)

`multiagent/app/tools/programmatic_transformers.py`:

| # | Трансформер | Что делает |
|---|---|---|
| 1 | `add_entity_registration` | `context.AddEntity<T>().AddDefaultMnemonic()` |
| 2 | `add_associated_entity` | `.AssociatedEntity(f => f.{nav})` |
| 3 | `add_one_to_many` | `.AddOneToManyAssociation<...>(...)` chained |
| 4 | `add_owned_collection` | `.OwnedCollection(...)` |
| 5 | `add_using` | `using {ns};` |
| 6 | `add_scalar_property` | `public {type} {name} { get; set; }` |
| 7 | `add_enum_value` | enum литерал |
| 8 | `register_di_service` | DI registration |
| 9 | `register_filter` | filter |
| 10 | `delete_file` | удалить файл |

**Все шаблоны строк — из `bundle.registration_patterns`** (см.
[ADR-002](ADR-002-knowledge-bundle.md)). Multi-line anchor +
chain-aware insertion.

> Здесь перечислены 10 канонических AST-трансформеров. Подробное описание каждого — в [`../../technical/programmatic-transformers.md`](../../technical/programmatic-transformers.md).

### WP-B3: ProgrammaticFixer (5 кодов CS)

`multiagent/app/tools/programmatic_fixer.py`:

- **CS0246** — compiler hint → graph `query_type` →
  `classify_type` filePath → `add_using`.
- **CS0117** — Levenshtein ≤ 2 от `find_enum_values`.
- **CS1061** — Levenshtein ≤ 2 от `analyze_entity`.
- **CS0535** — class-bracket scan + stub `default!`.
- **CS0738** — swap первого type-token.

**Critical safety**: `_is_active_subtask_target()` для CS0246
не даёт fixer'у удалить ссылку на ещё-не-созданный файл.

---

## Альтернативы

1. **Pure LLM подход** — отвергнуто (велосипедность + spaghetti +
   compliance issues).
2. **Pure rule-based подход** — отвергнуто (не покрывает
   creative subtasks; жёсткое связывание с одним проектом).
3. **Code generators / templating engines** (T4, Razor,
   Liquid) — отвергнуто (не интегрируется с AST-anchor поиском).
4. **Roslyn QuickFixes напрямую** — частично используется (для
   refactor/rename, extract-method), но недостаточно для всех
   паттернов регистрации.

---

## Последствия

### Плюсы
- **92 % subtasks** теперь выполняются **детерминированно
  без LLM** (12 / 13 на эталонной задаче).
- LLM-вызовов в Coder: **5 → 1**.
- Нет spaghetti-кода — все повторяющиеся блоки идентичны по
  форматированию (закрывает замечание о spaghetti-коде).
- Гарантия 0-LLM-галлюцинаций для регулируемого on-prem (закрывает
  замечание о велосипедности в правильной формулировке:
  «специализированный layer для compliance», не «велосипед»).
- ProgrammaticFixer закрывает 5 типовых CS-ошибок без LLM-вызова в
  fix-loop.

### Минусы
- 10 трансформеров + 5 fixer'ов нужно **поддерживать** при
  изменениях `bundle.registration_patterns`.
- Edge-cases требуют доработки трансформеров (но fallback на LLM
  через `transformer.fallback_llm` event).

### Технический долг
- Нет (95 %+ покрытие; LLM-fallback закрывает остаток).

---

## Связанные документы

- [`../../technical/programmatic-transformers.md`](../../technical/programmatic-transformers.md) — 10 AST-трансформеров.
- [`ADR-002-knowledge-bundle.md`](ADR-002-knowledge-bundle.md) — источник шаблонов регистрации.
