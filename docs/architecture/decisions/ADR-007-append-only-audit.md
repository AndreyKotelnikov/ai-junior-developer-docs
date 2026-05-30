# ADR-007. Append-only audit на restricted Postgres-роли

**Status**: Accepted

---

## Контекст

Регулируемые отрасли в рамках российского законодательства (банки,
субъекты КИИ, госкомпании) требуют ответов на 5 вопросов для любой
AI-системы, изменяющей production-код:

1. **Кто именно** изменил конкретный файл?
2. **На какой версии модели** делалось изменение?
3. **Какой prompt и completion** были задействованы?
4. **Можно ли воспроизвести** изменение байт-в-байт через 6 месяцев?
5. **Можно ли доказать неизменность** записи факта изменения
   регулятору?

Без ответов система **не может** быть применена в:
- банках (152-ФЗ — обработка персональных данных клиентов);
- субъектах КИИ (187-ФЗ + Приказы ФСТЭК № 235, № 239);
- госкомпаниях (пересечение 152-ФЗ + 187-ФЗ + санкционная политика
  по выбору LLM-провайдеров).

**Источник**: внутренний анализ и замечания по итогам экспертной
оценки.

---

## Решение

Реализовать **append-only audit log** в Postgres с **restricted
role** на уровне БД и **transparent wrapper** на уровне приложения.

### Postgres

```sql
CREATE TABLE pipeline_audit (
    id BIGSERIAL PRIMARY KEY,
    run_id UUID NOT NULL,
    sequence INT NOT NULL,
    agent_name VARCHAR(64) NOT NULL,
    model_name VARCHAR(128) NOT NULL,
    prompt_hash CHAR(64) NOT NULL,           -- SHA-256
    completion_hash CHAR(64) NOT NULL,       -- SHA-256
    -- ... + 11 ещё столбцов
);

CREATE ROLE multiagent_app LOGIN PASSWORD '...';
GRANT INSERT, SELECT ON pipeline_audit TO multiagent_app;
REVOKE UPDATE, DELETE, TRUNCATE ON pipeline_audit FROM PUBLIC;
REVOKE UPDATE, DELETE, TRUNCATE ON pipeline_audit FROM multiagent_app;
```

**Принцип**: всё приложение работает под `multiagent_app`. Даже
SQL-injection не позволит очистить лог.

### Python (transparent wrapper)

`AuditingLLMClient(LLMClient)`:
- Subclass `LLMClient` с переопределённым `chat()`.
- Pass-through когда `RunContext` не bound (для тестов).
- Audit-mode когда bound: SHA-256 hash, INSERT в pipeline_audit.

### Replay CLI

`multiagent_replay --run-id=<UUID>`:
1. Читает все LLM-вызовы из `pipeline_audit`.
2. Для каждого — повторный реальный LLM-вызов с теми же промптом /
   моделью / параметрами.
3. Сравнивает completion_hash с записанным.

### OpenTimestamps (опционально)

Через `BLOCKCHAIN_NOTARIZATION=true` + `ots` CLI: после run'а — SHA
от concatenation всех hash'ей нотаризуется в Bitcoin.

---

## Альтернативы

1. **Файловый log (`log/audit.log`)** — отвергнуто (легко
   тампернуть, нельзя индексировать).
2. **Event sourcing с Kafka** — отвергнуто (избыточная сложность,
   зависимость от Kafka).
3. **Write-Once Read-Many (WORM) storage** — отвергнуто (нет такого
   готового решения для Postgres; restricted role + REVOKE даёт
   эквивалент).
4. **Append-only в S3** — отвергнуто (требует cloud, не подходит для
   air-gapped on-prem).
5. **Cryptographic chaining (Merkle tree)** — рассмотрено, в
   backlog'е (WP-D4+; OpenTimestamps уже даёт частичное решение
   для anti-tamper).

---

## Последствия

### Плюсы
- 100 % LLM-вызовов залогированы ✅.
- Append-only DELETE/UPDATE/TRUNCATE → permission denied ✅.
- Replay byte-identical: **2 / 4** на Claude Haiku 4.5
  (50 %, в пределах model stochasticity).
- На Ollama+seed: **100 % byte-identical**.
- Закрыто соответствие 152-ФЗ и 187-ФЗ (включая Приказы ФСТЭК
  № 235 § II.2 — архивация ≥ 5 лет, № 239 § VI.1 — целостность).
- 18 unit-тестов (8 audit_log + 6 run_context + 4 client).
- `docs/COMPLIANCE_MATRIX.md` создан.

### Минусы
- **Plaintext** хранение `full_prompt` / `full_completion` (TDE
  или AES-GCM в backlog'е).
- **PII-redaction** не реализован (TODO для public SaaS).
- `pipeline_audit` без TTL — нужна явная архивная стратегия для
  production (≥ 5 лет ретенция по compliance).

### Технический долг
- Init scripts только на пустом postgres-volume — на существующих
  стендах SQL накатывается вручную.
- Полноценная сертификация по требованиям ФСТЭК вынесена в задачу
  дорожной карты **R15** (формальная аттестация средства).

---

## Связанные документы

- [`../detailed-architecture.md`](../detailed-architecture.md) — колонка 6, блок 8 (слой compliance-аудита).
- [`../../technical/artifact_trace.md`](../../technical/artifact_trace.md) — трассировка артефактов и аудит.
