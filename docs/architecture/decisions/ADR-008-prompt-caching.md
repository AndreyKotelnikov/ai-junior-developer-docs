# ADR-008. Prompt caching через static / dynamic split

**Status**: Accepted

---

## Контекст

В baseline-системе Coder-агент получал **~7 K токенов** на каждый
subtask. При 13 subtasks одна задача = ~91 K токенов только на
Coder. Это:
- Блокировало Ollama (контекст 16 K у некоторых моделей).
- Ломало OpEx (на Anthropic API одна задача = ~$0.20).
- Не использовало prompt-caching API.

При этом структура prompt'а Coder'а имеет **большую общую часть**
между subtasks одного task'а:

```
ROLE: ... (фиксированный, ~200 tokens)
FORMAT: ... (фиксированный, ~150 tokens)
TARGET FILE CONTENT: <содержимое Entity.cs> (~3 K tokens, тот же файл)
─────────── (общий префикс, ~3.4 K tokens) ───────────
SUBTASK: ... (per-subtask, ~200 tokens)
REFERENCE SIGNATURES: ... (per-subtask, ~500 tokens)
RAG EXAMPLE: ... (per-subtask, ~1 K tokens)
INSERTION ANCHOR: ... (per-subtask, ~50 tokens)
```

3.4 K токенов **повторно вычислялись** для каждого subtask'а —
расточительно.

**Источник**: внутренний анализ архитектуры.

---

## Решение

Разделить prompt Coder'а на:
- **Static block (cached)**: ROLE + FORMAT + TARGET FILE CONTENT.
- **Dynamic block** (per-subtask): SUBTASK + signatures + RAG +
  anchor.

**Реализация**:

### WP-B5 (Slim Coder)

- `CoderAgent._execute_slim_subtask()` — новый путь.
- `LLMClient.chat()` поддерживает структурированные content-blocks
  с `cache_control: ephemeral` (Anthropic) и Ollama KV-cache.
- Активен при `use_slim_coder=True` и не-Ollama; fallback на legacy
  при custom_system_prompt (fix-loop).

### WP-D2 (KVCacheManager)

- `KVCacheManager.remember(key, prefix)` — запоминает общий
  префикс для ключа (key = `agent:role:file`).
- `KVCacheManager.build_prompt_with_cached_prefix(key, dynamic)` —
  собирает messages array с cached prefix.
- `record_call(...)` — bucketed stats: `(prompt_tokens -
  eval_count) / prompt_tokens` = cache-hit rate.

### Per-provider маппинг

| Provider | Механизм | Активация |
|---|---|---|
| Anthropic Claude | `cache_control: {"type": "ephemeral"}` | автоматически в LLMClient |
| Ollama | KV-cache reuse (через `/api/chat` + `keep_alive`) | автоматически в OllamaScheduler |
| OpenAI / OpenRouter | (no native prompt cache в момент написания) | no-op |

---

## Альтернативы

1. **Обычный promp** (без splitting) — отвергнуто (root cause).
2. **Manual cache на уровне приложения** (Redis с
   prompt-hash → completion) — отвергнуто (инвалидация при
   изменении model temperature; fragile).
3. **Compression prompt'а** (LLMLingua) — рассмотрено, в backlog'е
   (orthogonal к caching, можно объединить позже).

---

## Последствия

### Плюсы
- Slim Coder prompt size: **~7 K → 2.5 K tokens**.
- Cache hit potential: 78 %+ (после подключения).
- Per-subtask RAG: пример релевантнее, чем глобально-выбранный.
- Полный test suite multiagent: **107 → 133** (+ 26 новых тестов
  для slim path).

### Минусы
- При custom_system_prompt (fix-loop) — fallback на legacy
  Coder (без caching). Это намеренно, т. к. fix-loop требует
  кастомного prompt'а.

### Технический долг
- **Cache-hit rate 0 %** на Stand Ollama после WP-D2 — `KVCacheManager`
  готов, но `Coder._build_slim_messages` **не использует**
  `build_prompt_with_cached_prefix` (TODO ~2 часа).
  После — ожидается cache-hit ≥ 60 %, время на 13-task ≤ 120 сек.

---

## Связанные документы

- [`../detailed-architecture.md`](../detailed-architecture.md) — колонка 7 (LLM-движок) и блок 9 (инфраструктура LLM-вызовов).
- [`ADR-006-serial-ollama-scheduler.md`](ADR-006-serial-ollama-scheduler.md) — связан с KVCacheManager.
