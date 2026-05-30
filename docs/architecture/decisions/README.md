# Architecture Decision Records (ADR)

**Назначение**: формальная документация ключевых архитектурных
решений с контекстом, альтернативами и последствиями.

---

## О формате ADR

Каждое ADR — отдельная страница со следующей структурой:

```markdown
# ADR-NNN. Краткое название решения

**Status**: Accepted | Superseded by ADR-XXX | Deprecated
**Date**: YYYY-MM-DD
**Авторы**: tech-lead

## Контекст
(Какая проблема стояла, какие были варианты)

## Решение
(Что мы решили сделать)

## Альтернативы
(Какие варианты рассматривали и почему отвергли)

## Последствия
(Что получили: плюсы, минусы, технический долг)

## Связанные документы
- ...
```

---

## Список ADR

| # | Название | Статус | Дата |
|---|---|---|---|
| [ADR-001](ADR-001-roslyn-incremental-validation.md) | Roslyn-инкрементальная валидация в fix-loop | Accepted | 2026-04-23 |
| [ADR-002](ADR-002-knowledge-bundle.md) | KnowledgeBundle как единый источник истины | Accepted | 2026-04-23 |
| [ADR-003](ADR-003-hybrid-deterministic-llm.md) | Hybrid Deterministic + LLM (программные трансформеры) | Accepted | 2026-04-23 |
| [ADR-004](ADR-004-zero-retrain-router.md) | Zero-Retrain Task Router (замена SetFit) | Accepted | 2026-04-23 |
| [ADR-005](ADR-005-roslyn-only-explorer.md) | Roslyn-only Explorer (0 LLM в фазе исследования) | Accepted | 2026-04-23 |
| [ADR-006](ADR-006-serial-ollama-scheduler.md) | Serial-Ollama Scheduler с per-agent priority | Accepted | 2026-04-23 |
| [ADR-007](ADR-007-append-only-audit.md) | Append-only audit на restricted Postgres-роли | Accepted | 2026-04-23 |
| [ADR-008](ADR-008-prompt-caching.md) | Prompt caching через static / dynamic split | Accepted | 2026-04-23 |

---

## Статусы

- **Accepted** — решение принято и реализовано.
- **Superseded by ADR-XXX** — заменено более новым ADR (старое
  оставляется для истории).
- **Deprecated** — не используется, оставлено для контекста.

---

## Связанные категории

- [`../PROJECT_ARCHITECTURE.md`](../PROJECT_ARCHITECTURE.md) — высокоуровневая архитектура.
- [`../detailed-architecture.md`](../detailed-architecture.md) — детальная архитектура по семи функциональным колонкам.
