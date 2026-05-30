# Прогон: Конфигурация F, повторение 1

**Дата**: 2026-03-24 06:33
**Конфигурация**: F: Multi-agent + RAG(3) + Ollama
**Настройки**: agent_mode=multi, use_rag=True, rag_top_k=3, use_graph=False
**Модель**: qwen2.5-coder:14b

---

## Тест 1. Portfolio +2 поля (Простая)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 8a5534b4-7ce4-4cb1-8055-f46037c154b3 |
| Статус | false_success |
| Pass@1 | 0 |
| Время | 492 сек |
| Build итераций | 0 |
| Completeness | 0/1 (0%) |
| Токены (total) | 11048 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | — |
| F_required | Data/Entities/Portfolio.cs |
| F_missing | Data/Entities/Portfolio.cs |

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

## Тест 2. OrganizationPerson +3 поля (Простая)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | f503e040-77f4-427e-b764-1f013ef7d716 |
| Статус | success |
| Pass@1 | 1 |
| Время | 492 сек |
| Build итераций | 0 |
| Completeness | 1/1 (100%) |
| Токены (total) | 15340 |

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
| API status | success |
| F_actual.length > 0 | ✅ (1 файлов) |
| F_actual ∩ F_required > 0 | ✅ |
| Итоговый статус | **success** |

### Анализ
Все 1 ожидаемых файлов изменены

---

## Тест 3. PhotoReportItem +2 поля (Простая)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | ec03abae-52e7-4e3b-bdb6-438a46f54800 |
| Статус | success |
| Pass@1 | 1 |
| Время | 475 сек |
| Build итераций | 0 |
| Completeness | 0/1 (0%) |
| Токены (total) | 11262 |

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
| task_id | 4420db65-4031-477c-ae98-f447b4222a7e |
| Статус | success |
| Pass@1 | 1 |
| Время | 369 сек |
| Build итераций | 0 |
| Completeness | 1/1 (100%) |
| Токены (total) | 11263 |

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
| task_id | f205f866-22d8-4a52-8ffc-43deb41db231 |
| Статус | success |
| Pass@1 | 1 |
| Время | 523 сек |
| Build итераций | 0 |
| Completeness | 1/1 (100%) |
| Токены (total) | 10928 |

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
| task_id | 75c15e4b-d0a2-4f58-ad84-0f37851ee685 |
| Статус | failed |
| Pass@1 | 0 |
| Время | 760 сек |
| Build итераций | 0 |
| Completeness | 1/2 (50%) |
| Токены (total) | 17279 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Configurations/DataConfiguration.cs, Data/Entities/ConstructionSection.cs, Data/Initializer.cs |
| F_required | Data/Entities/ConstructionSection.cs, Data/DataConfiguration.cs |
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
Тест завершился с ошибкой: Build fix loop aborted: errors grew for 3 consecutive attempts (3 -> 12). Fix loop is making things worse.

---

## Тест 7. Experience +4 поля (Средняя)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 050c143e-4797-4504-bf1f-6e4ddf58b53f |
| Статус | failed |
| Pass@1 | 0 |
| Время | 837 сек |
| Build итераций | 0 |
| Completeness | 2/3 (67%) |
| Токены (total) | 23189 |

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
| task_id | fed49075-a158-46ee-99cc-284e69dc34fd |
| Статус | failed |
| Pass@1 | 0 |
| Время | 907 сек |
| Build итераций | 0 |
| Completeness | 1/3 (33%) |
| Токены (total) | 20892 |

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
| task_id | 0d6e353c-c111-47ff-9424-9bcc1c0d19a8 |
| Статус | failed |
| Pass@1 | 0 |
| Время | 915 сек |
| Build итераций | 0 |
| Completeness | 2/3 (67%) |
| Токены (total) | 20581 |

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
Тест завершился с ошибкой: Build fix loop aborted: errors grew for 3 consecutive attempts (19 -> 19). Fix loop is making things worse.

---

## Тест 10. CheckPoint +4 поля (Средняя)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | a589c875-69f7-4405-9f9f-0c4d6fe989e1 |
| Статус | success |
| Pass@1 | 1 |
| Время | 931 сек |
| Build итераций | 0 |
| Completeness | 1/3 (33%) |
| Токены (total) | 20935 |

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
| API status | success |
| F_actual.length > 0 | ✅ (1 файлов) |
| F_actual ∩ F_required > 0 | ✅ |
| Итоговый статус | **success** |

### Анализ
Изменено 1/3 ожидаемых файлов (33%). Изменено всего файлов: 1

---

## Тест 11. Notice +5 полей (Сложная)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | ed31f110-ed72-461c-a80d-b5c00c97a222 |
| Статус | failed |
| Pass@1 | 0 |
| Время | 1118 сек |
| Build итераций | 0 |
| Completeness | 2/3 (67%) |
| Токены (total) | 21810 |

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
| task_id | 59007362-7b2a-4336-97b4-d4f0cd2158c1 |
| Статус | failed |
| Pass@1 | 0 |
| Время | 1059 сек |
| Build итераций | 0 |
| Completeness | 2/3 (67%) |
| Токены (total) | 20667 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Configurations/DataConfiguration.cs, Data/Entities/EscrowAccount.cs, Data/Initializer.cs |
| F_required | Data/Entities/EscrowAccount.cs, Data/DataConfiguration.cs, Data/Initializer.cs |
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
Тест завершился с ошибкой: Build fix loop aborted: errors grew for 3 consecutive attempts (1 -> 1). Fix loop is making things worse.

---

## Тест 13. 10 сущностей +2 поля (Сложная)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | e29eda3f-538b-4f5c-9fb6-48fecbae0ae8 |
| Статус | failed |
| Pass@1 | 0 |
| Время | 1629 сек |
| Build итераций | 0 |
| Completeness | 10/10 (100%) |
| Токены (total) | 32720 |

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
Тест завершился с ошибкой: Build fix loop aborted: errors grew for 3 consecutive attempts (10 -> 12). Fix loop is making things worse.

---

## Тест 14. BankPolicy + BankPolicyItem (Сложная)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 54b8a09c-b57a-4f79-9090-a5acb3a5faf7 |
| Статус | success |
| Pass@1 | 1 |
| Время | 1206 сек |
| Build итераций | 0 |
| Completeness | 2/3 (67%) |
| Токены (total) | 19993 |

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
| task_id | 6c3d3b33-ee73-4559-9efb-61dd6906f55a |
| Статус | failed |
| Pass@1 | 0 |
| Время | 1274 сек |
| Build итераций | 0 |
| Completeness | 2/3 (67%) |
| Токены (total) | 26442 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Configurations/DataConfiguration.cs, Data/Entities/SalesData.cs, Data/Initializer.cs |
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
| F_actual.length > 0 | ✅ (3 файлов) |
| F_actual ∩ F_required > 0 | ✅ |
| Итоговый статус | **failed** |

### Анализ
Тест завершился с ошибкой: Build fix loop aborted: errors grew for 3 consecutive attempts (1 -> 1). Fix loop is making things worse.

---


## Итоги прогона

| Метрика | Значение |
|---------|----------|
| Всего тестов | 15 |
| Pass@1 | 6/15 (40%) |
| False success | 1 |
| Failed | 8 |
| Timeout | 0 |
| Avg completeness | 61.1% |
| Avg time | 866 сек |
| Total time | 12987 сек (216.4 мин) |

### Сводная таблица

| # | Тест | Сложность | Статус | Pass@1 | Completeness | Время |
|---|------|-----------|--------|--------|--------------|-------|
| 1 | Portfolio +2 поля | Простая | false_success | 0 | 0/1 (0%) | 492 сек |
| 2 | OrganizationPerson +3 поля | Простая | success | 1 | 1/1 (100%) | 492 сек |
| 3 | PhotoReportItem +2 поля | Простая | success | 1 | 0/1 (0%) | 475 сек |
| 4 | SubmittedDocumentsTemplate +2 поля | Простая | success | 1 | 1/1 (100%) | 369 сек |
| 5 | ContractCurrency +1 enum | Простая | success | 1 | 1/1 (100%) | 523 сек |
| 6 | ConstructionSection +5 полей | Средняя | failed | 0 | 1/2 (50%) | 760 сек |
| 7 | Experience +4 поля | Средняя | failed | 0 | 2/3 (67%) | 837 сек |
| 8 | MediaLink +4 поля | Средняя | failed | 0 | 1/3 (33%) | 907 сек |
| 9 | SpecialZone +5 полей | Средняя | failed | 0 | 2/3 (67%) | 915 сек |
| 10 | CheckPoint +4 поля | Средняя | success | 1 | 1/3 (33%) | 931 сек |
| 11 | Notice +5 полей | Сложная | failed | 0 | 2/3 (67%) | 1118 сек |
| 12 | EscrowAccount +5 полей | Сложная | failed | 0 | 2/3 (67%) | 1059 сек |
| 13 | 10 сущностей +2 поля | Сложная | failed | 0 | 10/10 (100%) | 1629 сек |
| 14 | BankPolicy + BankPolicyItem | Сложная | success | 1 | 2/3 (67%) | 1206 сек |
| 15 | SalesData +5 полей | Сложная | failed | 0 | 2/3 (67%) | 1274 сек |

