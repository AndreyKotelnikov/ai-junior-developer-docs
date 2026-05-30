# Roadmap проекта: Q3 2026 и далее

**Период**: Q3 2026 → 2027 (планируемое).

**Назначение**: показать перспективное развитие проекта AI Junior Developer
после защиты. План улучшений объединяет задачи **R1–R17**; настоящий документ
описывает направления роста на следующие периоды.

---

## 1. Что было на конец Q2 2026

К моменту защиты основной план улучшений (задачи R1–R17) выполнен:
- закрыты все код-релевантные замечания эксперта и пилотов;
- обеспечено соответствие ключевым регуляторам (152-ФЗ, 187-ФЗ, Приказы ФСТЭК № 235 и № 239, Указ № 490);
- документация реструктурирована по тематическим разделам.

---

## 2. Ближайшие технические задачи (≤ 2 недели)

1. **Подключить `KVCacheManager` к slim Coder**.
   - Цель: cache-hit ≥ 60 %, время на 13-задачную сюиту ≤ 120 сек на стенде Ollama.
2. **Slim-путь для fix-LLM**.
   - Цель: ≤ 30 K токенов на полный путь.
3. **End-to-end runner для xUnit-сюиты**.
   - Цель: Pass@1 на 25 задачах ≥ 70 %.
4. **Очистка стека от исторического конвейера извлечения паттернов**.
   - Освобождает ≈ 1.1 ГБ legacy-зависимостей.

---

## 3. Q3 2026 (среднесрочно, ~3 месяца)

### 3.1. WP-D1 — MR-Archaeology

**Объём**: 4 коннектора (GitLab + GitHub + Bitbucket + Azure
DevOps).

**Стратегическая ценность**: vendor lock-in moat для GTM.

**Блокеры**: доступ к API нескольких форжей; тестовое pilot-репо
на 500+ MR.

### 3.2. WP-D5 — Roslyn Graph SDK packaging (B2B2B)

**Объём**: Docker `roslyn-graph:commercial` + SDK-клиенты Python /
TS / C# + OpenAPI + landing page + pricing.

**Блокеры**: 1+ LOI от потенциального B2B2B-клиента.

### 3.3. Замена `qwen2.5-coder:14b` на `qwen2.5-coder:32b`

**Цель**: полная 13-task задача на Stand Ollama без галлюцинаций.

**Блокеры**: 48+ ГБ GPU (или 2× RTX 4090, или 1× A100 40 ГБ).

---

## 4. Q4 2026 (долгосрочно)

### 4.1. WP-D4 — Stand A/B Self-Optimizer

**Объём**: gradient boosting model `(task_signature, stand) →
predicted_metrics` + continuous learning + auto-routing.

**Блокеры**: ≥ 100 завершённых задач в `pipeline_audit` от живого
пилота.

### 4.2. WP-D6 — Legacy .NET Migration pilot (3.1 → 6)

**Объём**: библиотека breaking-change трансформеров (EF6 → EF Core,
ASP.NET Framework → ASP.NET Core) + UI-мастер + pilot на real-world
проекте.

**Блокеры**: product-fit research — есть ли платежеспособный спрос
на legacy-миграции.

### 4.3. PII-redaction для public SaaS

**Объём**: модуль `prompt_redactor` с regex-паттернами для имён,
email, телефонов, идентификаторов.

**Блокеры**: ясные требования от первого public SaaS заказчика.

---

## 5. Q1 2027+ (стратегическое развитие)

### 5.1. Расширение на не-.NET стеки

- **Java** через tree-sitter + детекторы аналогичные C2.
- **Python** для AI/ML-проектов.
- **TypeScript / Node.js**.

### 5.2. Multi-tenant поддержка

- Несколько `conventions.json` параллельно для SaaS-сценария.
- Tenant isolation в `pipeline_audit` (через `tenant_id`).
- Per-tenant rate limiting и quotas.

### 5.3. Active learning loop

Использовать `pipeline_audit` для автоматического дообучения
модели-роутера (D4 + новые варианты).

### 5.4. Encrypted at-rest storage

- Application-level AES-GCM для `full_prompt` / `full_completion`.
- Vault-managed keys.
- Postgres TDE (для Enterprise клиентов).

### 5.5. mTLS между сервисами

Для расширенной защиты внутри docker network.

---

## 6. Стратегические направления GTM

### 6.1. Банковский сегмент РФ

- **Банки 2-го эшелона** — Stand Ollama on-prem.
- **Банки 1-го эшелона** через интегратора — full air-gapped + 152-ФЗ.

### 6.2. Госсектор и субъекты КИИ

- **Госкомпании** через интегратора — full air-gapped + 187-ФЗ.
- **Субъекты КИИ** категории 2–3 — air-gapped + audit + Приказы
  ФСТЭК № 235, № 239.
- (При необходимости) Сертификация ФСТЭК для категории 1 объектов
  КИИ.

### 6.3. Legacy migration

- Уникальная вертикаль (`.NET 3.1 / 4.x → 6+`).
- Большой TAM (миллионы legacy-проектов в РФ).

### 6.4. B2B2B SDK

- Roslyn Graph как самостоятельный коммерческий продукт.
- Free tier для OSS, commercial для SaaS / Enterprise РФ.

---

## 7. Риски и mitigation

| # | Риск | Mitigation |
|---|---|---|
| 1 | Ollama / Qwen ухудшает качество относительно Anthropic | Stand H (32B) или Hybrid (Anthropic для Orchestrator + Ollama для Coder) |
| 2 | Anthropic / OpenAI выходят в on-prem версии | Фокус на data-moat (MR-Archaeology) + compliance — где on-prem LLM их не заменит |
| 3 | Big tech (MS) поглощает legacy .NET сегмент | Legacy 3.1/4.x — ниша, которую MS сворачивает; мы комплементарны |
| 4 | Команда теряет мотивацию на долгих волнах | Visible metrics, demos после каждого WP, recognition |

---

## 8. Метрики успеха (target к концу 2027)

| Метрика | Текущая | Target |
|---|---|---|
| Активных pilot-клиентов | 0 (production) | 5+ |
| LOI / контрактов B2B2B | 0 | 3+ |
| Покрытие стеков | .NET (1) | .NET + Java (2) |
| Pass@1 на широкой сюите | success на эталонной | ≥ 80 % на 50+ задачах |
| Время задачи (Stand Ollama) | 50 сек 1-task | ≤ 90 сек на сложной |
| Compliance certifications | 0 | Сертификация ФСТЭК для объектов КИИ |

---

## 9. Связанные документы

- [`../../technical/improvement_tasks_full.md`](../../technical/improvement_tasks_full.md) — карточки задач плана улучшений (R1–R17).
- [`../../compliance/compliance-matrix.md`](../../compliance/compliance-matrix.md) — матрица нормативного соответствия.
