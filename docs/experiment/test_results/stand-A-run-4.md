# Прогон: Конфигурация A, повторение 4

**Дата**: 2026-03-24 03:52
**Конфигурация**: A: Single-agent + RAG(3)
**Настройки**: agent_mode=single, use_rag=True, rag_top_k=3, use_graph=False
**Модель**: Claude Haiku 4.5

---

## Тест 1. Portfolio +2 поля (Простая)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 030fea36-1c97-4a4d-b286-9360e5a471c2 |
| Статус | failed |
| Pass@1 | 0 |
| Время | 189 сек |
| Build итераций | 0 |
| Completeness | 1/1 (100%) |
| Токены (total) | 18453 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/Portfolio.cs |
| F_required | Data/Entities/Portfolio.cs |
| F_missing | — |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type | unknown (confidence: 0.9983) |
| Примеров загружено | 3 |
| Template | — |

### Валидация
| Проверка | Результат |
|----------|----------|
| API status | failed |
| F_actual.length > 0 | ✅ (1 файлов) |
| F_actual ∩ F_required > 0 | ✅ |
| Итоговый статус | **failed** |

### Анализ
Тест завершился с ошибкой: Single-agent: build failed after 5 attempts

---

## Тест 2. OrganizationPerson +3 поля (Простая)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | a84d3a52-7a19-47de-bf11-f00d702db07a |
| Статус | failed |
| Pass@1 | 0 |
| Время | 232 сек |
| Build итераций | 0 |
| Completeness | 1/1 (100%) |
| Токены (total) | 20231 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/OrganizationPerson.cs |
| F_required | Data/Entities/OrganizationPerson.cs |
| F_missing | — |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type | unknown (confidence: 0.9983) |
| Примеров загружено | 3 |
| Template | — |

### Валидация
| Проверка | Результат |
|----------|----------|
| API status | failed |
| F_actual.length > 0 | ✅ (1 файлов) |
| F_actual ∩ F_required > 0 | ✅ |
| Итоговый статус | **failed** |

### Анализ
Тест завершился с ошибкой: Single-agent: build failed after 5 attempts

---

## Тест 3. PhotoReportItem +2 поля (Простая)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | a10398cd-cb26-4d36-a3ac-d0ad9a7385d9 |
| Статус | failed |
| Pass@1 | 0 |
| Время | 234 сек |
| Build итераций | 0 |
| Completeness | 0/1 (0%) |
| Токены (total) | 18034 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/PhotoReportItem.cs |
| F_required | Data/Entities/PhotoReport/PhotoReportItem.cs |
| F_missing | — |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type | unknown (confidence: 0.9983) |
| Примеров загружено | 3 |
| Template | — |

### Валидация
| Проверка | Результат |
|----------|----------|
| API status | failed |
| F_actual.length > 0 | ✅ (1 файлов) |
| F_actual ∩ F_required > 0 | ✅ |
| Итоговый статус | **failed** |

### Анализ
Тест завершился с ошибкой: Single-agent: build failed after 5 attempts

---

## Тест 4. SubmittedDocumentsTemplate +2 поля (Простая)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | de9fa026-06a5-4602-b14f-5f3ccaa05173 |
| Статус | failed |
| Pass@1 | 0 |
| Время | 233 сек |
| Build итераций | 0 |
| Completeness | 1/1 (100%) |
| Токены (total) | 21013 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/SubmittedDocumentsTemplate.cs |
| F_required | Data/Entities/SubmittedDocumentsTemplate.cs |
| F_missing | — |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type | unknown (confidence: 0.9983) |
| Примеров загружено | 3 |
| Template | — |

### Валидация
| Проверка | Результат |
|----------|----------|
| API status | failed |
| F_actual.length > 0 | ✅ (1 файлов) |
| F_actual ∩ F_required > 0 | ✅ |
| Итоговый статус | **failed** |

### Анализ
Тест завершился с ошибкой: Single-agent: build failed after 5 attempts

---

## Тест 5. ContractCurrency +1 enum (Простая)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | d1b1367e-2d57-40f1-b41c-246f460741a4 |
| Статус | false_success |
| Pass@1 | 0 |
| Время | 123 сек |
| Build итераций | 0 |
| Completeness | 0/1 (0%) |
| Токены (total) | 3438 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | — |
| F_required | Data/Entities/ContractCurrency.cs |
| F_missing | Data/Entities/ContractCurrency.cs |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type | unknown (confidence: 0.9983) |
| Примеров загружено | 3 |
| Template | — |

### Валидация
| Проверка | Результат |
|----------|----------|
| API status | success |
| F_actual.length > 0 | ❌ (0 файлов) |
| F_actual ∩ F_required > 0 | ❌ |
| Итоговый статус | **false_success** |

### Анализ
API вернул success, но ни один файл не изменён — ложный успех

---

## Тест 6. ConstructionSection +5 полей (Средняя)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | e3e7b1c1-ff7b-4df9-b23a-72993632e542 |
| Статус | false_success |
| Pass@1 | 0 |
| Время | 126 сек |
| Build итераций | 0 |
| Completeness | 0/2 (0%) |
| Токены (total) | 3681 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | — |
| F_required | Data/Entities/ConstructionSection.cs, Data/DataConfiguration.cs |
| F_missing | Data/Entities/ConstructionSection.cs, Data/DataConfiguration.cs |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type | unknown (confidence: 0.9983) |
| Примеров загружено | 3 |
| Template | — |

### Валидация
| Проверка | Результат |
|----------|----------|
| API status | success |
| F_actual.length > 0 | ❌ (0 файлов) |
| F_actual ∩ F_required > 0 | ❌ |
| Итоговый статус | **false_success** |

### Анализ
API вернул success, но ни один файл не изменён — ложный успех

---

## Тест 7. Experience +4 поля (Средняя)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 72d40612-7e67-4cd8-8e24-005a168daddd |
| Статус | failed |
| Pass@1 | 0 |
| Время | 221 сек |
| Build итераций | 0 |
| Completeness | 1/3 (33%) |
| Токены (total) | 21141 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/Experience.cs |
| F_required | Data/Entities/Experience.cs, Data/DataConfiguration.cs, Data/Initializer.cs |
| F_missing | Data/DataConfiguration.cs, Data/Initializer.cs |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type | unknown (confidence: 0.9983) |
| Примеров загружено | 3 |
| Template | — |

### Валидация
| Проверка | Результат |
|----------|----------|
| API status | failed |
| F_actual.length > 0 | ✅ (1 файлов) |
| F_actual ∩ F_required > 0 | ✅ |
| Итоговый статус | **failed** |

### Анализ
Тест завершился с ошибкой: Single-agent: build failed after 5 attempts

---

## Тест 8. MediaLink +4 поля (Средняя)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 28ced834-f6d5-4430-9678-aa7bd052332f |
| Статус | false_success |
| Pass@1 | 0 |
| Время | 144 сек |
| Build итераций | 0 |
| Completeness | 0/3 (0%) |
| Токены (total) | 3617 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | — |
| F_required | Data/Entities/MediaLink.cs, Data/DataConfiguration.cs, Data/Initializer.cs |
| F_missing | Data/Entities/MediaLink.cs, Data/DataConfiguration.cs, Data/Initializer.cs |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type | unknown (confidence: 0.9983) |
| Примеров загружено | 3 |
| Template | — |

### Валидация
| Проверка | Результат |
|----------|----------|
| API status | success |
| F_actual.length > 0 | ❌ (0 файлов) |
| F_actual ∩ F_required > 0 | ❌ |
| Итоговый статус | **false_success** |

### Анализ
API вернул success, но ни один файл не изменён — ложный успех

---

## Тест 9. SpecialZone +5 полей (Средняя)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | bdba9d23-0d9a-447a-bfc0-a25121561ea2 |
| Статус | failed |
| Pass@1 | 0 |
| Время | 234 сек |
| Build итераций | 0 |
| Completeness | 1/3 (33%) |
| Токены (total) | 25914 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/SpecialZone.cs |
| F_required | Data/Entities/SpecialZone.cs, Data/DataConfiguration.cs, Data/Initializer.cs |
| F_missing | Data/DataConfiguration.cs, Data/Initializer.cs |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type | unknown (confidence: 0.9983) |
| Примеров загружено | 3 |
| Template | — |

### Валидация
| Проверка | Результат |
|----------|----------|
| API status | failed |
| F_actual.length > 0 | ✅ (1 файлов) |
| F_actual ∩ F_required > 0 | ✅ |
| Итоговый статус | **failed** |

### Анализ
Тест завершился с ошибкой: Single-agent: build failed after 5 attempts

---

## Тест 10. CheckPoint +4 поля (Средняя)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 5d7c7469-d29c-4328-b320-4a1a0c04e354 |
| Статус | failed |
| Pass@1 | 0 |
| Время | 222 сек |
| Build итераций | 0 |
| Completeness | 1/3 (33%) |
| Токены (total) | 20388 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/CheckPoint.cs |
| F_required | Data/Entities/CheckPoint.cs, Data/DataConfiguration.cs, Data/Initializer.cs |
| F_missing | Data/DataConfiguration.cs, Data/Initializer.cs |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type | unknown (confidence: 0.9983) |
| Примеров загружено | 3 |
| Template | — |

### Валидация
| Проверка | Результат |
|----------|----------|
| API status | failed |
| F_actual.length > 0 | ✅ (1 файлов) |
| F_actual ∩ F_required > 0 | ✅ |
| Итоговый статус | **failed** |

### Анализ
Тест завершился с ошибкой: Single-agent: build failed after 5 attempts

---

## Тест 11. Notice +5 полей (Сложная)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 9376c383-3c6b-48a1-add9-20425b0d2fdc |
| Статус | false_success |
| Pass@1 | 0 |
| Время | 144 сек |
| Build итераций | 0 |
| Completeness | 0/3 (0%) |
| Токены (total) | 4047 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | — |
| F_required | Data/Entities/Notice.cs, Data/DataConfiguration.cs, Data/Initializer.cs |
| F_missing | Data/Entities/Notice.cs, Data/DataConfiguration.cs, Data/Initializer.cs |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type | unknown (confidence: 0.9983) |
| Примеров загружено | 3 |
| Template | — |

### Валидация
| Проверка | Результат |
|----------|----------|
| API status | success |
| F_actual.length > 0 | ❌ (0 файлов) |
| F_actual ∩ F_required > 0 | ❌ |
| Итоговый статус | **false_success** |

### Анализ
API вернул success, но ни один файл не изменён — ложный успех

---

## Тест 12. EscrowAccount +5 полей (Сложная)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 033e519a-ac3b-4ed2-9b00-113a2f486fd3 |
| Статус | failed |
| Pass@1 | 0 |
| Время | 242 сек |
| Build итераций | 0 |
| Completeness | 1/3 (33%) |
| Токены (total) | 19333 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/EscrowAccount.cs |
| F_required | Data/Entities/EscrowAccount.cs, Data/DataConfiguration.cs, Data/Initializer.cs |
| F_missing | Data/DataConfiguration.cs, Data/Initializer.cs |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type | unknown (confidence: 0.9983) |
| Примеров загружено | 3 |
| Template | — |

### Валидация
| Проверка | Результат |
|----------|----------|
| API status | failed |
| F_actual.length > 0 | ✅ (1 файлов) |
| F_actual ∩ F_required > 0 | ✅ |
| Итоговый статус | **failed** |

### Анализ
Тест завершился с ошибкой: Single-agent: build failed after 5 attempts

---

## Тест 13. 10 сущностей +2 поля (Сложная)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | ef03351b-7081-4857-9393-e28392ca2a0a |
| Статус | false_success |
| Pass@1 | 0 |
| Время | 121 сек |
| Build итераций | 0 |
| Completeness | 0/10 (0%) |
| Токены (total) | 4174 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | — |
| F_required | Data/Entities/Discussion.cs, Data/Entities/BankPolicy.cs, Data/Entities/Notice.cs, Data/Entities/CheckPoint.cs, Data/Entities/MediaLink.cs, Data/Entities/ProjectAnalog.cs, Data/Entities/TargetProgram.cs, Data/Entities/CheckListItem.cs, Data/Entities/DiscussionProtocol.cs, Data/Entities/BankPolicyItem.cs |
| F_missing | Data/Entities/Discussion.cs, Data/Entities/BankPolicy.cs, Data/Entities/Notice.cs, Data/Entities/CheckPoint.cs, Data/Entities/MediaLink.cs, Data/Entities/ProjectAnalog.cs, Data/Entities/TargetProgram.cs, Data/Entities/CheckListItem.cs, Data/Entities/DiscussionProtocol.cs, Data/Entities/BankPolicyItem.cs |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type | unknown (confidence: 0.9983) |
| Примеров загружено | 3 |
| Template | — |

### Валидация
| Проверка | Результат |
|----------|----------|
| API status | success |
| F_actual.length > 0 | ❌ (0 файлов) |
| F_actual ∩ F_required > 0 | ❌ |
| Итоговый статус | **false_success** |

### Анализ
API вернул success, но ни один файл не изменён — ложный успех

---

## Тест 14. BankPolicy + BankPolicyItem (Сложная)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 0ab35cab-6394-40ce-84e2-42cf41a8657c |
| Статус | false_success |
| Pass@1 | 0 |
| Время | 121 сек |
| Build итераций | 0 |
| Completeness | 0/3 (0%) |
| Токены (total) | 3777 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | — |
| F_required | Data/Entities/BankPolicy.cs, Data/Entities/BankPolicyItem.cs, Data/DataConfiguration.cs |
| F_missing | Data/Entities/BankPolicy.cs, Data/Entities/BankPolicyItem.cs, Data/DataConfiguration.cs |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type | unknown (confidence: 0.9983) |
| Примеров загружено | 3 |
| Template | — |

### Валидация
| Проверка | Результат |
|----------|----------|
| API status | success |
| F_actual.length > 0 | ❌ (0 файлов) |
| F_actual ∩ F_required > 0 | ❌ |
| Итоговый статус | **false_success** |

### Анализ
API вернул success, но ни один файл не изменён — ложный успех

---

## Тест 15. SalesData +5 полей (Сложная)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 1b9d3c44-cbe4-40bd-9cd9-2d83bbde00ba |
| Статус | failed |
| Pass@1 | 0 |
| Время | 295 сек |
| Build итераций | 0 |
| Completeness | 1/3 (33%) |
| Токены (total) | 34847 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/SalesData.cs, Services/CrudServices/SalesDataCrudService.cs, Services/EventBusHandlers/SalesDataCalculationUpdaterFromSalesData.cs |
| F_required | Data/Entities/SalesData.cs, Data/DataConfiguration.cs, Data/Initializer.cs |
| F_missing | Data/DataConfiguration.cs, Data/Initializer.cs |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type | unknown (confidence: 0.9983) |
| Примеров загружено | 3 |
| Template | — |

### Валидация
| Проверка | Результат |
|----------|----------|
| API status | failed |
| F_actual.length > 0 | ✅ (3 файлов) |
| F_actual ∩ F_required > 0 | ✅ |
| Итоговый статус | **failed** |

### Анализ
Тест завершился с ошибкой: Single-agent: build failed after 5 attempts

---


## Итоги прогона

| Метрика | Значение |
|---------|----------|
| Всего тестов | 15 |
| Pass@1 | 0/15 (0%) |
| False success | 6 |
| Failed | 9 |
| Timeout | 0 |
| Avg completeness | 31.1% |
| Avg time | 192 сек |
| Total time | 2881 сек (48.0 мин) |

### Сводная таблица

| # | Тест | Сложность | Статус | Pass@1 | Completeness | Время |
|---|------|-----------|--------|--------|--------------|-------|
| 1 | Portfolio +2 поля | Простая | failed | 0 | 1/1 (100%) | 189 сек |
| 2 | OrganizationPerson +3 поля | Простая | failed | 0 | 1/1 (100%) | 232 сек |
| 3 | PhotoReportItem +2 поля | Простая | failed | 0 | 0/1 (0%) | 234 сек |
| 4 | SubmittedDocumentsTemplate +2 поля | Простая | failed | 0 | 1/1 (100%) | 233 сек |
| 5 | ContractCurrency +1 enum | Простая | false_success | 0 | 0/1 (0%) | 123 сек |
| 6 | ConstructionSection +5 полей | Средняя | false_success | 0 | 0/2 (0%) | 126 сек |
| 7 | Experience +4 поля | Средняя | failed | 0 | 1/3 (33%) | 221 сек |
| 8 | MediaLink +4 поля | Средняя | false_success | 0 | 0/3 (0%) | 144 сек |
| 9 | SpecialZone +5 полей | Средняя | failed | 0 | 1/3 (33%) | 234 сек |
| 10 | CheckPoint +4 поля | Средняя | failed | 0 | 1/3 (33%) | 222 сек |
| 11 | Notice +5 полей | Сложная | false_success | 0 | 0/3 (0%) | 144 сек |
| 12 | EscrowAccount +5 полей | Сложная | failed | 0 | 1/3 (33%) | 242 сек |
| 13 | 10 сущностей +2 поля | Сложная | false_success | 0 | 0/10 (0%) | 121 сек |
| 14 | BankPolicy + BankPolicyItem | Сложная | false_success | 0 | 0/3 (0%) | 121 сек |
| 15 | SalesData +5 полей | Сложная | failed | 0 | 1/3 (33%) | 295 сек |

