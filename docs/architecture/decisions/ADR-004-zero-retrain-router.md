# ADR-004. Zero-Retrain Task Router (замена SetFit)

**Status**: Accepted

---

## Контекст

В baseline для классификации задач (определения типа операции:
`add_entity`, `modify_entity`, ...) использовался **SetFit** —
few-shot text classifier на базе sentence-transformers.

**Проблемы**:
- При подключении нового клиента требовался полный ML-цикл:
  ручная разметка примеров, fit модели, валидация, упаковка в
  Docker volume.
- Это занимало **1–2 дня работы ML-инженера** на каждого нового
  клиента — не масштабируется.
- Модель занимала ~1.1 ГБ в RAM.
- **Один-label классификация** — нельзя было выразить «добавить
  сущность + сервис для неё» как `add_entity` + `add_service`.
- Зависимость от сервиса `pattern-extraction` (~20 минут блокировки
  запуска контейнеров).

**Источник**: результаты пилотного применения системы.

---

## Решение

Заменить SetFit на **трёхуровневый Zero-Retrain Router**:

```
requirement
    ↓
[1] TaskSignature.extract()
    → {mentioned_types, type_roles, verbs, paths}
    ↓
[2] RuleEngine.match(signature, bundle.operations)
    → matched_operations[] (multi-label)
    ↓
[3] LLM zero-shot fallback (≤ 200 tokens)
    → filter hallucinations against valid_op_names
```

**Ключевые свойства**:
- **Zero retraining** — правила в `project_conventions.json`,
  не ML-модель.
- **Multi-label** — одно требование = несколько operations.
- **Cheap fallback** — LLM-вызов только когда правила не
  сматчились (≤ 200 tokens, ~$0.0002).
- **No model in RAM** — экономия 1.1 ГБ.

**Реализация**:
- 6 новых модулей в `rag-service/app/services/`:
  `bundle_loader`, `roslyn_client`, `llm_client`, `task_signature`,
  `rule_engine`, `operation_router`.
- Удалён `setfit` из `requirements-gpu.txt`.
- Удалена 1.1 ГБ модель из `volumes/pattern-extraction/.../`.

---

## Альтернативы

1. **Fine-tune SetFit per-client** — отвергнуто (root cause
   проблемы).
2. **BERT fine-tuning** — отвергнуто (ещё дороже SetFit'а).
3. **Pure LLM classifier (no rules)** — отвергнуто
   (стохастичность + cost).
4. **Embedding-based routing** (через сравнение с эталонами) —
   отвергнуто (требует размеченной выборки эталонов; rule-based
   точнее на 90 % входов).

---

## Последствия

### Плюсы
- Способ классификации: **multi-label**, любые operations.
- Размер модели в RAM: **1.1 ГБ → 0**.
- Скорость (rule-based): **100–300 мс → 3–130 мс**.
- Дообучение под нового клиента: **1–2 дня → не требуется**
  (правила в JSON).
- Rule-based hit на 20 синтетических требованиях: **18 / 20 = 90 %**.
- LLM-fallback на 20 синтетических: **1 / 20 = 5 %** (1 случай —
  откровенно неоднозначное требование).

### Минусы
- Правила нужно **вручную** прописывать в `conventions.json` для
  кастомных типов задач (но это **разово**, без ML-цикла).

### Технический долг
- Сервис `pattern-extraction` функционально не нужен, но
  физически в `docker-compose.yml` (TODO WP-C5).
- rag-service Docker image не пересобран после удаления SetFit
  (TODO ~1 час на стабильной сети).

---

## Связанные документы

- [`../detailed-architecture.md`](../detailed-architecture.md) — колонка 2 (RAG-сервис, Zero-Retrain Router).
- [`ADR-002-knowledge-bundle.md`](ADR-002-knowledge-bundle.md) — правила operations хранятся в `project_conventions.json`.
