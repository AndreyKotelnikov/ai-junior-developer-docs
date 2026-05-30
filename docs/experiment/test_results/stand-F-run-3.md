# Прогон: Конфигурация F, повторение 3

**Дата**: 2026-03-24 14:55
**Конфигурация**: F: Multi-agent + RAG(3) + Ollama
**Настройки**: agent_mode=multi, use_rag=True, rag_top_k=3, use_graph=False
**Модель**: qwen2.5-coder:14b

---

## Тест 1. Portfolio +2 поля (Простая)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | e9a7c9e1-4f1d-4129-84ae-14737e957ccb |
| Статус | success |
| Pass@1 | 1 |
| Время | 653 сек |
| Build итераций | 0 |
| Completeness | 1/1 (100%) |
| Токены (total) | 11051 |

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
| API status | success |
| F_actual.length > 0 | ✅ (1 файлов) |
| F_actual ∩ F_required > 0 | ✅ |
| Итоговый статус | **success** |

### Анализ
Все 1 ожидаемых файлов изменены

---

## Тест 2. OrganizationPerson +3 поля (Простая)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 2a3fc18c-275e-42ae-87b7-64fd47733428 |
| Статус | failed |
| Pass@1 | 0 |
| Время | 1074 сек |
| Build итераций | 0 |
| Completeness | 1/1 (100%) |
| Токены (total) | 15637 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Configurations/DataConfiguration.cs, Data/Entities/OrganizationPerson.cs |
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
| F_actual.length > 0 | ✅ (2 файлов) |
| F_actual ∩ F_required > 0 | ✅ |
| Итоговый статус | **failed** |

### Анализ
Тест завершился с ошибкой: Build fix loop aborted: errors grew for 3 consecutive attempts (2 -> 2). Fix loop is making things worse.

---

## Тест 3. PhotoReportItem +2 поля (Простая)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | cd31fd0a-e6dd-4315-b2ea-1537b4ccc5c5 |
| Статус | success |
| Pass@1 | 1 |
| Время | 805 сек |
| Build итераций | 0 |
| Completeness | 0/1 (0%) |
| Токены (total) | 10506 |

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
| API status | success |
| F_actual.length > 0 | ✅ (1 файлов) |
| F_actual ∩ F_required > 0 | ✅ |
| Итоговый статус | **success** |

### Анализ
Изменено 0/1 ожидаемых файлов (0%). Изменено всего файлов: 1

---

## Тест 4. SubmittedDocumentsTemplate +2 поля (Простая)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | aa855913-a72d-49e5-aa8e-611d2aec4a9a |
| Статус | success |
| Pass@1 | 1 |
| Время | 525 сек |
| Build итераций | 0 |
| Completeness | 1/1 (100%) |
| Токены (total) | 11741 |

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
| API status | success |
| F_actual.length > 0 | ✅ (1 файлов) |
| F_actual ∩ F_required > 0 | ✅ |
| Итоговый статус | **success** |

### Анализ
Все 1 ожидаемых файлов изменены

---

## Тест 5. ContractCurrency +1 enum (Простая)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 5f675052-1b19-48d5-9a9f-6ef0077ffd8a |
| Статус | success |
| Pass@1 | 1 |
| Время | 528 сек |
| Build итераций | 0 |
| Completeness | 1/1 (100%) |
| Токены (total) | 10596 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/ContractCurrency.cs |
| F_required | Data/Entities/ContractCurrency.cs |
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
| API status | success |
| F_actual.length > 0 | ✅ (1 файлов) |
| F_actual ∩ F_required > 0 | ✅ |
| Итоговый статус | **success** |

### Анализ
Все 1 ожидаемых файлов изменены

---

## Тест 6. ConstructionSection +5 полей (Средняя)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 3b6a73cd-0da8-445e-87e4-6e6c8f19f318 |
| Статус | failed |
| Pass@1 | 0 |
| Время | 744 сек |
| Build итераций | 0 |
| Completeness | 1/2 (50%) |
| Токены (total) | 17357 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/ConstructionSection.cs, Data/Initializer.cs |
| F_required | Data/Entities/ConstructionSection.cs, Data/DataConfiguration.cs |
| F_missing | Data/DataConfiguration.cs |

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
| F_actual.length > 0 | ✅ (2 файлов) |
| F_actual ∩ F_required > 0 | ✅ |
| Итоговый статус | **failed** |

### Анализ
Тест завершился с ошибкой: Build failed after 5 attempts

---

## Тест 7. Experience +4 поля (Средняя)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 02096930-25fa-462e-87b5-8c30be5056df |
| Статус | failed |
| Pass@1 | 0 |
| Время | 956 сек |
| Build итераций | 0 |
| Completeness | 2/3 (67%) |
| Токены (total) | 25135 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Configurations/DataConfiguration.cs, Data/Entities/Experience.cs, Data/Initializer.cs |
| F_required | Data/Entities/Experience.cs, Data/DataConfiguration.cs, Data/Initializer.cs |
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
| F_actual.length > 0 | ✅ (3 файлов) |
| F_actual ∩ F_required > 0 | ✅ |
| Итоговый статус | **failed** |

### Анализ
Тест завершился с ошибкой: Build fix loop aborted: errors grew for 3 consecutive attempts (2 -> 2). Fix loop is making things worse.

---

## Тест 8. MediaLink +4 поля (Средняя)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | ea292c72-8b9b-40c4-86de-5b5e3ffb178f |
| Статус | failed |
| Pass@1 | 0 |
| Время | 981 сек |
| Build итераций | 0 |
| Completeness | 1/3 (33%) |
| Токены (total) | 20978 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/MediaLinkEntities/MediaLink.cs, Data/Initializer.cs |
| F_required | Data/Entities/MediaLink.cs, Data/DataConfiguration.cs, Data/Initializer.cs |
| F_missing | Data/DataConfiguration.cs |

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
| F_actual.length > 0 | ✅ (2 файлов) |
| F_actual ∩ F_required > 0 | ✅ |
| Итоговый статус | **failed** |

### Анализ
Тест завершился с ошибкой: Build fix loop aborted: errors grew for 3 consecutive attempts (20 -> 20). Fix loop is making things worse.

---

## Тест 9. SpecialZone +5 полей (Средняя)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 7334869b-a979-4668-825c-fa854f3f909b |
| Статус | failed |
| Pass@1 | 0 |
| Время | 1159 сек |
| Build итераций | 0 |
| Completeness | 2/3 (67%) |
| Токены (total) | 21656 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Configurations/DataConfiguration.cs, Data/Entities/SpecialZone.cs, Data/Initializer.cs |
| F_required | Data/Entities/SpecialZone.cs, Data/DataConfiguration.cs, Data/Initializer.cs |
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
| F_actual.length > 0 | ✅ (3 файлов) |
| F_actual ∩ F_required > 0 | ✅ |
| Итоговый статус | **failed** |

### Анализ
Тест завершился с ошибкой: Build failed after 5 attempts

---

## Тест 10. CheckPoint +4 поля (Средняя)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 843e0334-00a1-4344-9903-a684a0c093bc |
| Статус | failed |
| Pass@1 | 0 |
| Время | 640 сек |
| Build итераций | 0 |
| Completeness | 1/3 (33%) |
| Токены (total) | 17362 |

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
Тест завершился с ошибкой: Build fix loop aborted: errors grew for 3 consecutive attempts (1 -> 1). Fix loop is making things worse.

---

## Тест 11. Notice +5 полей (Сложная)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 87e102bb-959b-4ce5-bf35-b4df960a4dcd |
| Статус | failed |
| Pass@1 | 0 |
| Время | 862 сек |
| Build итераций | 0 |
| Completeness | 2/3 (67%) |
| Токены (total) | 20601 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Configurations/DataConfiguration.cs, Data/Entities/Notice.cs, Data/Initializer.cs |
| F_required | Data/Entities/Notice.cs, Data/DataConfiguration.cs, Data/Initializer.cs |
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
| F_actual.length > 0 | ✅ (3 файлов) |
| F_actual ∩ F_required > 0 | ✅ |
| Итоговый статус | **failed** |

### Анализ
Тест завершился с ошибкой: Build failed after 5 attempts

---

## Тест 12. EscrowAccount +5 полей (Сложная)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 98d08c59-4ff9-4c13-9a4c-c8a66b3161ad |
| Статус | false_success |
| Pass@1 | 0 |
| Время | 618 сек |
| Build итераций | 0 |
| Completeness | 0/3 (0%) |
| Токены (total) | 14076 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | — |
| F_required | Data/Entities/EscrowAccount.cs, Data/DataConfiguration.cs, Data/Initializer.cs |
| F_missing | Data/Entities/EscrowAccount.cs, Data/DataConfiguration.cs, Data/Initializer.cs |

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

## Тест 13. 10 сущностей +2 поля (Сложная)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 2ec4e5f8-1f12-467e-961b-ff5a2de5b2d6 |
| Статус | failed |
| Pass@1 | 0 |
| Время | 1222 сек |
| Build итераций | 0 |
| Completeness | 10/10 (100%) |
| Токены (total) | 32712 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Configurations/DataConfiguration.cs, Data/Entities/BankPolicy.cs, Data/Entities/BankPolicyItem.cs, Data/Entities/CheckListItem.cs, Data/Entities/CheckPoint.cs, Data/Entities/Discussion.cs, Data/Entities/DiscussionProtocol.cs, Data/Entities/MediaLink.cs, Data/Entities/Notice.cs, Data/Entities/ProjectAnalog.cs, Data/Entities/TargetProgram.cs |
| F_required | Data/Entities/Discussion.cs, Data/Entities/BankPolicy.cs, Data/Entities/Notice.cs, Data/Entities/CheckPoint.cs, Data/Entities/MediaLink.cs, Data/Entities/ProjectAnalog.cs, Data/Entities/TargetProgram.cs, Data/Entities/CheckListItem.cs, Data/Entities/DiscussionProtocol.cs, Data/Entities/BankPolicyItem.cs |
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
| F_actual.length > 0 | ✅ (11 файлов) |
| F_actual ∩ F_required > 0 | ✅ |
| Итоговый статус | **failed** |

### Анализ
Тест завершился с ошибкой: Build fix loop aborted: errors grew for 3 consecutive attempts (1 -> 1). Fix loop is making things worse.

---

## Тест 14. BankPolicy + BankPolicyItem (Сложная)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | db0f6f45-6fe7-4428-8f8a-48da3b7fb0dc |
| Статус | success |
| Pass@1 | 1 |
| Время | 947 сек |
| Build итераций | 0 |
| Completeness | 2/3 (67%) |
| Токены (total) | 27204 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/BankPolicy.cs, Data/Entities/BankPolicyItem.cs |
| F_required | Data/Entities/BankPolicy.cs, Data/Entities/BankPolicyItem.cs, Data/DataConfiguration.cs |
| F_missing | Data/DataConfiguration.cs |

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
| F_actual.length > 0 | ✅ (2 файлов) |
| F_actual ∩ F_required > 0 | ✅ |
| Итоговый статус | **success** |

### Анализ
Изменено 2/3 ожидаемых файлов (67%). Изменено всего файлов: 2

---

## Тест 15. SalesData +5 полей (Сложная)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 9ade95d7-8832-4bc8-ba14-ab142d419048 |
| Статус | failed |
| Pass@1 | 0 |
| Время | 1448 сек |
| Build итераций | 0 |
| Completeness | 2/3 (67%) |
| Токены (total) | 26494 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Bindings/JournalEventsConfiguration.cs, Data/Configurations/DataConfiguration.cs, Data/Entities/SalesData.cs, Data/Initializer.cs |
| F_required | Data/Entities/SalesData.cs, Data/DataConfiguration.cs, Data/Initializer.cs |
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
| F_actual.length > 0 | ✅ (4 файлов) |
| F_actual ∩ F_required > 0 | ✅ |
| Итоговый статус | **failed** |

### Анализ
Тест завершился с ошибкой: Build fix loop aborted: errors grew for 3 consecutive attempts (8 -> 8). Fix loop is making things worse.

---


## Итоги прогона

| Метрика | Значение |
|---------|----------|
| Всего тестов | 15 |
| Pass@1 | 5/15 (33%) |
| False success | 1 |
| Failed | 9 |
| Timeout | 0 |
| Avg completeness | 63.3% |
| Avg time | 877 сек |
| Total time | 13162 сек (219.4 мин) |

### Сводная таблица

| # | Тест | Сложность | Статус | Pass@1 | Completeness | Время |
|---|------|-----------|--------|--------|--------------|-------|
| 1 | Portfolio +2 поля | Простая | success | 1 | 1/1 (100%) | 653 сек |
| 2 | OrganizationPerson +3 поля | Простая | failed | 0 | 1/1 (100%) | 1074 сек |
| 3 | PhotoReportItem +2 поля | Простая | success | 1 | 0/1 (0%) | 805 сек |
| 4 | SubmittedDocumentsTemplate +2 поля | Простая | success | 1 | 1/1 (100%) | 525 сек |
| 5 | ContractCurrency +1 enum | Простая | success | 1 | 1/1 (100%) | 528 сек |
| 6 | ConstructionSection +5 полей | Средняя | failed | 0 | 1/2 (50%) | 744 сек |
| 7 | Experience +4 поля | Средняя | failed | 0 | 2/3 (67%) | 956 сек |
| 8 | MediaLink +4 поля | Средняя | failed | 0 | 1/3 (33%) | 981 сек |
| 9 | SpecialZone +5 полей | Средняя | failed | 0 | 2/3 (67%) | 1159 сек |
| 10 | CheckPoint +4 поля | Средняя | failed | 0 | 1/3 (33%) | 640 сек |
| 11 | Notice +5 полей | Сложная | failed | 0 | 2/3 (67%) | 862 сек |
| 12 | EscrowAccount +5 полей | Сложная | false_success | 0 | 0/3 (0%) | 618 сек |
| 13 | 10 сущностей +2 поля | Сложная | failed | 0 | 10/10 (100%) | 1222 сек |
| 14 | BankPolicy + BankPolicyItem | Сложная | success | 1 | 2/3 (67%) | 947 сек |
| 15 | SalesData +5 полей | Сложная | failed | 0 | 2/3 (67%) | 1448 сек |

