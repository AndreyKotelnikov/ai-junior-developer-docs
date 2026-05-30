# Прогон: Конфигурация A, повторение 5

**Дата**: 2026-03-24 04:41
**Конфигурация**: A: Single-agent + RAG(3)
**Настройки**: agent_mode=single, use_rag=True, rag_top_k=3, use_graph=False
**Модель**: Claude Haiku 4.5

---

## Тест 1. Portfolio +2 поля (Простая)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 9fb08042-ce39-4f2f-b5c0-80393a4c5217 |
| Статус | failed |
| Pass@1 | 0 |
| Время | 207 сек |
| Build итераций | 0 |
| Completeness | 1/1 (100%) |
| Токены (total) | 16896 |

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
| task_id | 1ea7a4f2-8531-4339-8c54-b74b7e86412d |
| Статус | false_success |
| Pass@1 | 0 |
| Время | 135 сек |
| Build итераций | 0 |
| Completeness | 0/1 (0%) |
| Токены (total) | 3851 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | — |
| F_required | Data/Entities/OrganizationPerson.cs |
| F_missing | Data/Entities/OrganizationPerson.cs |

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

## Тест 3. PhotoReportItem +2 поля (Простая)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 1c93b5a4-c3bc-467f-93cc-12ada0936aa1 |
| Статус | failed |
| Pass@1 | 0 |
| Время | 210 сек |
| Build итераций | 0 |
| Completeness | 0/1 (0%) |
| Токены (total) | 18137 |

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
| task_id | b81d9fec-4d34-413f-a78c-4595357d1973 |
| Статус | failed |
| Pass@1 | 0 |
| Время | 203 сек |
| Build итераций | 0 |
| Completeness | 1/1 (100%) |
| Токены (total) | 22187 |

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
| task_id | 605696ff-1ddd-41bb-a45b-28d5756d6b5f |
| Статус | false_success |
| Pass@1 | 0 |
| Время | 100 сек |
| Build итераций | 0 |
| Completeness | 0/1 (0%) |
| Токены (total) | 3454 |

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
| task_id | 75d26a81-679f-4328-b7d1-b5194ecb67ab |
| Статус | false_success |
| Pass@1 | 0 |
| Время | 105 сек |
| Build итераций | 0 |
| Completeness | 0/2 (0%) |
| Токены (total) | 3774 |

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
| task_id | 77054830-21d2-481a-a10e-9967d54141d9 |
| Статус | failed |
| Pass@1 | 0 |
| Время | 271 сек |
| Build итераций | 0 |
| Completeness | 1/3 (33%) |
| Токены (total) | 22382 |

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
| task_id | 4f669085-d57d-4f06-9bcf-3cf3c1e89a5f |
| Статус | failed |
| Pass@1 | 0 |
| Время | 216 сек |
| Build итераций | 0 |
| Completeness | 1/3 (33%) |
| Токены (total) | 18641 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/MediaLink.cs |
| F_required | Data/Entities/MediaLink.cs, Data/DataConfiguration.cs, Data/Initializer.cs |
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

## Тест 9. SpecialZone +5 полей (Средняя)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 3ea64f38-4619-463a-8bca-1bbbb9997405 |
| Статус | failed |
| Pass@1 | 0 |
| Время | 181 сек |
| Build итераций | 0 |
| Completeness | 1/3 (33%) |
| Токены (total) | 20752 |

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
| task_id | 25212008-8323-4498-9115-dbd1a7bccb7f |
| Статус | failed |
| Pass@1 | 0 |
| Время | 265 сек |
| Build итераций | 0 |
| Completeness | 1/3 (33%) |
| Токены (total) | 21168 |

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
| task_id | 941617f5-fc94-476e-9907-145dd3f2a7b8 |
| Статус | false_success |
| Pass@1 | 0 |
| Время | 133 сек |
| Build итераций | 0 |
| Completeness | 0/3 (0%) |
| Токены (total) | 4025 |

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
| task_id | 7c734285-aa9e-43c3-8045-f48496be6707 |
| Статус | false_success |
| Pass@1 | 0 |
| Время | 135 сек |
| Build итераций | 0 |
| Completeness | 0/3 (0%) |
| Токены (total) | 3993 |

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
| task_id | 2050e797-7e6b-4705-86b8-951f44238f08 |
| Статус | false_success |
| Pass@1 | 0 |
| Время | 135 сек |
| Build итераций | 0 |
| Completeness | 0/10 (0%) |
| Токены (total) | 4022 |

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
| task_id | 6881d91a-1abf-42f5-80a0-053965999969 |
| Статус | false_success |
| Pass@1 | 0 |
| Время | 133 сек |
| Build итераций | 0 |
| Completeness | 0/3 (0%) |
| Токены (total) | 4629 |

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
| task_id | dd0cafec-d758-4257-a823-14fa22479582 |
| Статус | failed |
| Pass@1 | 0 |
| Время | 232 сек |
| Build итераций | 0 |
| Completeness | 1/3 (33%) |
| Токены (total) | 19140 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/SalesData.cs |
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
| F_actual.length > 0 | ✅ (1 файлов) |
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
| False success | 7 |
| Failed | 8 |
| Timeout | 0 |
| Avg completeness | 24.4% |
| Avg time | 177 сек |
| Total time | 2661 сек (44.4 мин) |

### Сводная таблица

| # | Тест | Сложность | Статус | Pass@1 | Completeness | Время |
|---|------|-----------|--------|--------|--------------|-------|
| 1 | Portfolio +2 поля | Простая | failed | 0 | 1/1 (100%) | 207 сек |
| 2 | OrganizationPerson +3 поля | Простая | false_success | 0 | 0/1 (0%) | 135 сек |
| 3 | PhotoReportItem +2 поля | Простая | failed | 0 | 0/1 (0%) | 210 сек |
| 4 | SubmittedDocumentsTemplate +2 поля | Простая | failed | 0 | 1/1 (100%) | 203 сек |
| 5 | ContractCurrency +1 enum | Простая | false_success | 0 | 0/1 (0%) | 100 сек |
| 6 | ConstructionSection +5 полей | Средняя | false_success | 0 | 0/2 (0%) | 105 сек |
| 7 | Experience +4 поля | Средняя | failed | 0 | 1/3 (33%) | 271 сек |
| 8 | MediaLink +4 поля | Средняя | failed | 0 | 1/3 (33%) | 216 сек |
| 9 | SpecialZone +5 полей | Средняя | failed | 0 | 1/3 (33%) | 181 сек |
| 10 | CheckPoint +4 поля | Средняя | failed | 0 | 1/3 (33%) | 265 сек |
| 11 | Notice +5 полей | Сложная | false_success | 0 | 0/3 (0%) | 133 сек |
| 12 | EscrowAccount +5 полей | Сложная | false_success | 0 | 0/3 (0%) | 135 сек |
| 13 | 10 сущностей +2 поля | Сложная | false_success | 0 | 0/10 (0%) | 135 сек |
| 14 | BankPolicy + BankPolicyItem | Сложная | false_success | 0 | 0/3 (0%) | 133 сек |
| 15 | SalesData +5 полей | Сложная | failed | 0 | 1/3 (33%) | 232 сек |

