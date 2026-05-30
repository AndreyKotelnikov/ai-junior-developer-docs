# Прогон: Конфигурация C, повторение 3

**Дата**: 2026-03-24 06:04
**Конфигурация**: C: Multi-agent + RAG(3)
**Настройки**: agent_mode=multi, use_rag=True, rag_top_k=3, use_graph=False
**Модель**: Claude Haiku 4.5

---

## Тест 1. Portfolio +2 поля (Простая)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | e8ee127f-44f4-4f8a-bea1-25c0eda89dc0 |
| Статус | success |
| Pass@1 | 1 |
| Время | 228 сек |
| Build итераций | 0 |
| Completeness | 1/1 (100%) |
| Токены (total) | 20835 |

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
| task_id | 9b132016-482d-4feb-ac7c-3e584448ff30 |
| Статус | failed |
| Pass@1 | 0 |
| Время | 683 сек |
| Build итераций | 0 |
| Completeness | 1/1 (100%) |
| Токены (total) | 28507 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/EF/DataContext.cs, Data/Entities/OrganizationPerson.cs |
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
Тест завершился с ошибкой: Build fix loop aborted: errors grew for 3 consecutive attempts (1 -> 1). Fix loop is making things worse.

---

## Тест 3. PhotoReportItem +2 поля (Простая)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 02c4fdc2-d02e-4994-9688-446a6c227f41 |
| Статус | success |
| Pass@1 | 1 |
| Время | 248 сек |
| Build итераций | 0 |
| Completeness | 1/1 (100%) |
| Токены (total) | 36394 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/PhotoReport/PhotoReportItem.cs |
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
Все 1 ожидаемых файлов изменены

---

## Тест 4. SubmittedDocumentsTemplate +2 поля (Простая)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 76f0bc10-fe7b-4724-a0e8-676ae0c49b20 |
| Статус | success |
| Pass@1 | 1 |
| Время | 240 сек |
| Build итераций | 0 |
| Completeness | 1/1 (100%) |
| Токены (total) | 21030 |

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
| task_id | 9719408f-48f9-4df1-999d-93942874c912 |
| Статус | success |
| Pass@1 | 1 |
| Время | 274 сек |
| Build итераций | 0 |
| Completeness | 1/1 (100%) |
| Токены (total) | 32760 |

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
| task_id | 36cc0f3a-5769-47b4-af77-c7c057fceee2 |
| Статус | failed |
| Pass@1 | 0 |
| Время | 715 сек |
| Build итераций | 0 |
| Completeness | 0/2 (0%) |
| Токены (total) | 35250 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Configurations/DataConfiguration.cs, Data/Initializer.cs |
| F_required | Data/Entities/ConstructionSection.cs, Data/DataConfiguration.cs |
| F_missing | Data/Entities/ConstructionSection.cs |

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

## Тест 7. Experience +4 поля (Средняя)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 6be27566-a4a3-4e8b-a1bf-facf4206a730 |
| Статус | success |
| Pass@1 | 1 |
| Время | 492 сек |
| Build итераций | 0 |
| Completeness | 1/3 (33%) |
| Токены (total) | 39094 |

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
| API status | success |
| F_actual.length > 0 | ✅ (1 файлов) |
| F_actual ∩ F_required > 0 | ✅ |
| Итоговый статус | **success** |

### Анализ
Изменено 1/3 ожидаемых файлов (33%). Изменено всего файлов: 1

---

## Тест 8. MediaLink +4 поля (Средняя)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 5662b6c5-d546-46c3-bb60-279051c50665 |
| Статус | success |
| Pass@1 | 1 |
| Время | 482 сек |
| Build итераций | 0 |
| Completeness | 0/3 (0%) |
| Токены (total) | 41181 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/ConstructionSite.cs, Data/Entities/MediaLinkEntities/MediaLink.cs |
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
| API status | success |
| F_actual.length > 0 | ✅ (2 файлов) |
| F_actual ∩ F_required > 0 | ✅ |
| Итоговый статус | **success** |

### Анализ
Изменено 0/3 ожидаемых файлов (0%). Изменено всего файлов: 2

---

## Тест 9. SpecialZone +5 полей (Средняя)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 2b6ab2bc-84c2-4284-8b38-088076d102e5 |
| Статус | success |
| Pass@1 | 1 |
| Время | 593 сек |
| Build итераций | 0 |
| Completeness | 1/3 (33%) |
| Токены (total) | 36486 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Configurations/DataConfiguration.cs, Data/Entities/SpecialZone.cs |
| F_required | Data/Entities/SpecialZone.cs, Data/DataConfiguration.cs, Data/Initializer.cs |
| F_missing | Data/Initializer.cs |

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
Изменено 1/3 ожидаемых файлов (33%). Изменено всего файлов: 2

---

## Тест 10. CheckPoint +4 поля (Средняя)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | d10f0b0a-1cec-49dd-8989-a8409feb294f |
| Статус | success |
| Pass@1 | 1 |
| Время | 642 сек |
| Build итераций | 0 |
| Completeness | 1/3 (33%) |
| Токены (total) | 49557 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/CheckLists/CheckPoint.cs, Data/Entities/ConstructionSite.cs, Data/Initializer.cs |
| F_required | Data/Entities/CheckPoint.cs, Data/DataConfiguration.cs, Data/Initializer.cs |
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
| F_actual.length > 0 | ✅ (3 файлов) |
| F_actual ∩ F_required > 0 | ✅ |
| Итоговый статус | **success** |

### Анализ
Изменено 1/3 ожидаемых файлов (33%). Изменено всего файлов: 3

---

## Тест 11. Notice +5 полей (Сложная)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | a07f4516-b8b3-4f74-83d9-e18ba5865c08 |
| Статус | success |
| Pass@1 | 1 |
| Время | 894 сек |
| Build итераций | 0 |
| Completeness | 1/3 (33%) |
| Токены (total) | 56487 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Configurations/DataConfiguration.cs, Data/Entities/ConstructionSection.cs, Data/Entities/Notice.cs, Data/Entities/Tranche.cs |
| F_required | Data/Entities/Notice.cs, Data/DataConfiguration.cs, Data/Initializer.cs |
| F_missing | Data/Initializer.cs |

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
| F_actual.length > 0 | ✅ (4 файлов) |
| F_actual ∩ F_required > 0 | ✅ |
| Итоговый статус | **success** |

### Анализ
Изменено 1/3 ожидаемых файлов (33%). Изменено всего файлов: 4

---

## Тест 12. EscrowAccount +5 полей (Сложная)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 8cb8acb2-71d8-436d-9717-a19a91369e04 |
| Статус | success |
| Pass@1 | 1 |
| Время | 464 сек |
| Build итераций | 0 |
| Completeness | 0/3 (0%) |
| Токены (total) | 47278 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/Organization.cs |
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
| F_actual.length > 0 | ✅ (1 файлов) |
| F_actual ∩ F_required > 0 | ❌ |
| Итоговый статус | **success** |

### Анализ
Изменено 0/3 ожидаемых файлов (0%). Изменено всего файлов: 1

---

## Тест 13. 10 сущностей +2 поля (Сложная)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | a049ba8b-07a0-40cf-8f4b-4e710e3ebf6e |
| Статус | success |
| Pass@1 | 1 |
| Время | 985 сек |
| Build итераций | 0 |
| Completeness | 6/10 (60%) |
| Токены (total) | 67762 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/BankPolicy/BankPolicy.cs, Data/Entities/BankPolicy/BankPolicyItem.cs, Data/Entities/CheckLists/CheckListItem.cs, Data/Entities/CheckPoint.cs, Data/Entities/Discussion.cs, Data/Entities/DiscussionProtocol.cs, Data/Entities/MediaLinkEntities/MediaLink.cs, Data/Entities/Notice.cs, Data/Entities/ProjectAnalog.cs, Data/Entities/TargetProgram.cs |
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
| API status | success |
| F_actual.length > 0 | ✅ (10 файлов) |
| F_actual ∩ F_required > 0 | ✅ |
| Итоговый статус | **success** |

### Анализ
Изменено 6/10 ожидаемых файлов (60%). Изменено всего файлов: 10

---

## Тест 14. BankPolicy + BankPolicyItem (Сложная)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 085431f4-3625-4e98-9dea-11234f08a37c |
| Статус | failed |
| Pass@1 | 0 |
| Время | 547 сек |
| Build итераций | 0 |
| Completeness | 0/3 (0%) |
| Токены (total) | 51903 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/BankPolicy/BankPolicy.cs, Data/Entities/BankPolicy/BankPolicyItem.cs |
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
| API status | failed |
| F_actual.length > 0 | ✅ (2 файлов) |
| F_actual ∩ F_required > 0 | ✅ |
| Итоговый статус | **failed** |

### Анализ
Тест завершился с ошибкой: Pipeline halted: 3 subtasks failed with zero changes. Last: Обновить регистрацию BankPolicy в Initializer.cs

---

## Тест 15. SalesData +5 полей (Сложная)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | bf0e4587-5c99-4a5b-844e-95d84be37387 |
| Статус | success |
| Pass@1 | 1 |
| Время | 466 сек |
| Build итераций | 0 |
| Completeness | 0/3 (0%) |
| Токены (total) | 40760 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/SalesEntities/SalesData.cs |
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
| API status | success |
| F_actual.length > 0 | ✅ (1 файлов) |
| F_actual ∩ F_required > 0 | ✅ |
| Итоговый статус | **success** |

### Анализ
Изменено 0/3 ожидаемых файлов (0%). Изменено всего файлов: 1

---


## Итоги прогона

| Метрика | Значение |
|---------|----------|
| Всего тестов | 15 |
| Pass@1 | 12/15 (80%) |
| False success | 0 |
| Failed | 3 |
| Timeout | 0 |
| Avg completeness | 46.2% |
| Avg time | 530 сек |
| Total time | 7953 сек (132.6 мин) |

### Сводная таблица

| # | Тест | Сложность | Статус | Pass@1 | Completeness | Время |
|---|------|-----------|--------|--------|--------------|-------|
| 1 | Portfolio +2 поля | Простая | success | 1 | 1/1 (100%) | 228 сек |
| 2 | OrganizationPerson +3 поля | Простая | failed | 0 | 1/1 (100%) | 683 сек |
| 3 | PhotoReportItem +2 поля | Простая | success | 1 | 1/1 (100%) | 248 сек |
| 4 | SubmittedDocumentsTemplate +2 поля | Простая | success | 1 | 1/1 (100%) | 240 сек |
| 5 | ContractCurrency +1 enum | Простая | success | 1 | 1/1 (100%) | 274 сек |
| 6 | ConstructionSection +5 полей | Средняя | failed | 0 | 0/2 (0%) | 715 сек |
| 7 | Experience +4 поля | Средняя | success | 1 | 1/3 (33%) | 492 сек |
| 8 | MediaLink +4 поля | Средняя | success | 1 | 0/3 (0%) | 482 сек |
| 9 | SpecialZone +5 полей | Средняя | success | 1 | 1/3 (33%) | 593 сек |
| 10 | CheckPoint +4 поля | Средняя | success | 1 | 1/3 (33%) | 642 сек |
| 11 | Notice +5 полей | Сложная | success | 1 | 1/3 (33%) | 894 сек |
| 12 | EscrowAccount +5 полей | Сложная | success | 1 | 0/3 (0%) | 464 сек |
| 13 | 10 сущностей +2 поля | Сложная | success | 1 | 6/10 (60%) | 985 сек |
| 14 | BankPolicy + BankPolicyItem | Сложная | failed | 0 | 0/3 (0%) | 547 сек |
| 15 | SalesData +5 полей | Сложная | success | 1 | 0/3 (0%) | 466 сек |

