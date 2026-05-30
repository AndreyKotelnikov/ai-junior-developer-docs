# ADR-006. Serial-Ollama Scheduler с per-agent priority

**Status**: Accepted

---

## Контекст

Целевые сегменты для коммерциализации (банки, госсектор, КИИ)
требуют **air-gapped on-prem** развёртывания через Ollama.
В baseline-системе наивный Ollama-режим работал, но в
production-режиме создавал шесть фундаментальных проблем:

1. **Конкуренция за GPU**: на RTX 4090 24 ГБ помещается одна 14B
   модель. При 4 параллельных вызовах агентов Ollama
   последовательно выгружал/загружал модели → ~10 минут «холостого»
   времени на задачу.
2. **Отсутствие приоритизации**: Orchestrator (критический путь) ждал
   наравне с Explainer (post-hoc).
3. **Нет per-agent routing**: все агенты использовали одну
   глобальную модель из `OLLAMA_DEFAULT_MODEL`.
4. **KV-cache не использовался** — `/api/generate` со склеенной
   строкой prompt разрушал переиспользование префикса.
5. **Холодный старт каждого вызова** при истечении `keep_alive`.
6. **Нет агрегации метрик** для разговора с заказчиком о TCO.

**Источник**: результаты пилотного применения, внутренний анализ
и замечания по итогам экспертной оценки.

---

## Решение

Реализовать **Serial-Ollama Scheduler** — async heap-queue с одним
worker'ом, сериализующий все Ollama-вызовы с приоритизацией по
агенту:

### `OllamaScheduler` (~290 строк)

- **Single-worker queue**: все вызовы идут через одну точку.
- **Priority по агенту** (нижний priority = выше):
  ```
  orchestrator   = 1   ← план задачи, критический путь
  explorer       = 2   ← локализация файлов
  coder          = 3   ← основная генерация кода
  fix / tester   = 5   ← fix-loop
  explainer      = 7   ← post-hoc, фоновый
  ```
- **Native `/api/chat`** (вместо `/api/generate`): даёт
  `prompt_eval_count` (для KV-cache stats), `keep_alive` per-call.
- **`model_load_events`** счётчик per-task.
- **`_normalise_keep_alive`** — коэрсит `"-1"`, `"3600"`, `"5m"` к
  int (regression-test).

### `ModelRouter` (~55 строк)

Per-agent routing через 3-уровневый fallback:
- Env override (`OLLAMA_CODER_MODEL=...`)
- DEFAULTS dict
- Generic fallback (`OLLAMA_DEFAULT_MODEL`)

Канонизация sub-агентов: `explorer-phase1/2/3` → `explorer`.

### `KVCacheManager` (~120 строк)

- `record_call(...)` — bucketed stats per-key.
- `remember(key, prefix)` — запоминает общий префикс.
- `build_prompt_with_cached_prefix(...)` — собирает messages
  array, где первый блок попадает в KV-cache.

---

## Альтернативы

1. **Multi-worker queue** — отвергнуто (требует multi-GPU; не
   соответствует hardware-target'у).
2. **Cloud-only deployment (Anthropic)** — отвергнуто (закрывает
   air-gapped сегмент).
3. **Off-the-shelf message broker** (RabbitMQ, Redis Queue) —
   отвергнуто (overkill для in-process серилизации).
4. **`Ollama keep_alive` без scheduler'а** — отвергнуто (не решает
   приоритизацию и per-agent routing).

---

## Последствия

### Плюсы
- Время LLM-части простой 1-task: **n/a → 50.5 сек** ✅ (цель ≤ 150).
- `model_load_events` per-task: **1** ✅ (идеал).
- Per-agent routing работает ✅.
- Закрыт **air-gapped on-prem сегмент** (банки, госсектор, КИИ).
- Закрыто замечание по итогам экспертной оценки об адаптивности
  под смену моделей (через env-переменную).

### Минусы
- Single-worker = последовательное выполнение (не параллелизуется).
  Это намеренно: на single-GPU параллелизм ухудшает производительность
  из-за выгрузок модели.
- На complex 13-task задаче `qwen2.5-coder:14b` галлюцинировал
  (не регрессия scheduler'а — ограничение модели).

### Технический долг
- `KVCacheManager` готов, но `Coder._build_slim_messages` не
  использует `build_prompt_with_cached_prefix` (TODO ~2 часа).
  После — ожидается cache-hit ≥ 60 %, время на 13-task ≤ 120 сек.

---

## Связанные документы

- [`../detailed-architecture.md`](../detailed-architecture.md) — колонка 7 (LLM-движок) и блок 9 (инфраструктура LLM-вызовов).
- [`ADR-008-prompt-caching.md`](ADR-008-prompt-caching.md) — связан с KVCacheManager.
