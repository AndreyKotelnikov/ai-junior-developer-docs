# ADR-005. Roslyn-only Explorer (0 LLM в фазе исследования)

**Status**: Accepted

---

## Контекст

В baseline-системе Explorer-агент тратил **3 LLM-вызова** на
задачу:

| Phase | Назначение | Tokens |
|---|---|---|
| 1 | «найти файлы по ключевым словам» | ~3 K |
| 2 | «вытянуть сигнатуры reference types» | ~5 K |
| 3 | «найти insertion points и якоря» | ~4 K |

Итого ~12 K tokens на задачу, **только** на исследование.

**Проблемы**:
- Это увеличивало токены в 3× без качественного выигрыша —
  ВСЯ информация уже доступна в `roslyn-graph` (cochange, vector
  search, signature extraction, insertion-point detection).
- LLM-Explorer вводил **стохастичность** (мог пропустить файл).
- **Блокировал Ollama-режим** — 3 параллельных LLM-вызова на 24 ГБ
  GPU невозможны.

**Источник**: внутренний анализ архитектуры (раздел «Hybrid
Deterministic + LLM»).

---

## Решение

Создать **`RoslynExplorer`** — компонент, использующий ТОЛЬКО
Roslyn graph и rag-service, **без LLM-вызовов**:

```
Phase 1 — File localization
  ├─ /api/cochange/files (anchor=key_type)
  ├─ /api/v1/search/vector (top_k=5)
  └─ /api/find/insertion-point (CamelCase tokens)
  → weighted scoring: cochange × 3.0 + RAG × 1.5 + graph × 2.0

Phase 2 — Signature extraction
  ├─ /api/analyze/file (top-3 candidates)
  └─ /api/analyze/entity (target_type)

Phase 3 — Anchors
  ├─ /api/find/insertion-point (per file)
  └─ /api/suggest/anchor
```

**Реализация**:
- `multiagent/app/agents/roslyn_explorer.py` (~250 строк).
- Feature flag `use_roslyn_explorer=True` (default).
- Fallback на LLM-Explorer при пустом результате (graceful
  degradation).
- 12 unit-тестов.

---

## Альтернативы

1. **Сократить prompt LLM-Explorer'а** — отвергнуто (не решает
   фундаментальную проблему: вся информация уже в graph).
2. **Кеширование результатов LLM-Explorer'а** — отвергнуто (cache
   hit невелик из-за вариативности requirement'ов).
3. **Single-call merged Explorer** (1 LLM-вызов вместо 3) —
   отвергнуто (сокращение в 3× недостаточно для Ollama; всё ещё
   стохастичность).

---

## Последствия

### Плюсы
- LLM-вызовов в Explorer: **3 → 0**.
- Tokens: **~12 K → 0** в Explorer-фазе.
- Готовность к Ollama (нет параллельных LLM-вызовов).
- Воспроизводимость (детерминированный поиск = одинаковый
  результат на одинаковом коде).
- 12 новых unit-тестов.

### Минусы
- Качество поиска зависит от качества `cochange_rules.json` и
  RAG-индекса (если они слабые, RoslynExplorer может пропустить
  релевантный файл).

### Технический долг
- Нет (graceful degradation на LLM-Explorer закрывает edge cases).

---

## Связанные документы

- [`../detailed-architecture.md`](../detailed-architecture.md) — колонка 5 (Roslyn-граф) и фаза Roslyn-навигации.
- [`ADR-001-roslyn-incremental-validation.md`](ADR-001-roslyn-incremental-validation.md) — Roslyn-валидация в fix-loop.
