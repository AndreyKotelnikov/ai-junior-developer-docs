# Прогон: Конфигурация B, повторение 4

**Дата**: 2026-03-24 08:16
**Конфигурация**: B: Multi-agent, без RAG, без графа
**Настройки**: agent_mode=multi, use_rag=False, rag_top_k=0, use_graph=False
**Модель**: Claude Haiku 4.5

---

## Тест 1. Portfolio +2 поля (Простая)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | f96c5fd0-9936-4b12-85f9-71c9f5f1200c |
| Статус | success |
| Pass@1 | 1 |
| Время | 531 сек |
| Build итераций | 0 |
| Completeness | 1/1 (100%) |
| Токены (total) | 24510 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/Portfolio.cs |
| F_required | Data/Entities/Portfolio.cs |
| F_missing | — |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type |  (confidence: 0.0) |
| Примеров загружено | 0 |
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
| task_id | 52a481c0-e1d6-474f-9fb9-f252bfcfd09d |
| Статус | success |
| Pass@1 | 1 |
| Время | 618 сек |
| Build итераций | 0 |
| Completeness | 1/1 (100%) |
| Токены (total) | 28962 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/OrganizationPerson.cs |
| F_required | Data/Entities/OrganizationPerson.cs |
| F_missing | — |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type |  (confidence: 0.0) |
| Примеров загружено | 0 |
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
| task_id | 503e60fa-cedd-4455-b234-ae2d9030a385 |
| Статус | failed |
| Pass@1 | 0 |
| Время | 368 сек |
| Build итераций | 0 |
| Completeness | 1/1 (100%) |
| Токены (total) | 36334 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/PhotoReport/PhotoReportItem.cs |
| F_required | Data/Entities/PhotoReport/PhotoReportItem.cs |
| F_missing | — |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type |  (confidence: 0.0) |
| Примеров загружено | 0 |
| Template | — |

### Валидация
| Проверка | Результат |
|----------|----------|
| API status | failed |
| F_actual.length > 0 | ✅ (1 файлов) |
| F_actual ∩ F_required > 0 | ✅ |
| Итоговый статус | **failed** |

### Анализ
Тест завершился с ошибкой: Pipeline halted: 3 subtasks failed with zero changes. Last: Проверить Initializer.cs на необходимость изменений

---

## Тест 4. SubmittedDocumentsTemplate +2 поля (Простая)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | dc84c032-2258-450f-8d1d-bcbe5a984e4d |
| Статус | success |
| Pass@1 | 1 |
| Время | 399 сек |
| Build итераций | 0 |
| Completeness | 1/1 (100%) |
| Токены (total) | 25265 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/SubmittedDocumentsTemplate.cs |
| F_required | Data/Entities/SubmittedDocumentsTemplate.cs |
| F_missing | — |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type |  (confidence: 0.0) |
| Примеров загружено | 0 |
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
| task_id | 1222ff4d-eafb-4a14-b3d8-7061889f7a84 |
| Статус | success |
| Pass@1 | 1 |
| Время | 468 сек |
| Build итераций | 0 |
| Completeness | 1/1 (100%) |
| Токены (total) | 31071 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/ContractCurrency.cs |
| F_required | Data/Entities/ContractCurrency.cs |
| F_missing | — |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type |  (confidence: 0.0) |
| Примеров загружено | 0 |
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
| task_id | ca14cfd1-8b30-452b-9211-d254d278d578 |
| Статус | success |
| Pass@1 | 1 |
| Время | 948 сек |
| Build итераций | 0 |
| Completeness | 1/2 (50%) |
| Токены (total) | 33706 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/ConstructionSection.cs |
| F_required | Data/Entities/ConstructionSection.cs, Data/DataConfiguration.cs |
| F_missing | Data/DataConfiguration.cs |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type |  (confidence: 0.0) |
| Примеров загружено | 0 |
| Template | — |

### Валидация
| Проверка | Результат |
|----------|----------|
| API status | success |
| F_actual.length > 0 | ✅ (1 файлов) |
| F_actual ∩ F_required > 0 | ✅ |
| Итоговый статус | **success** |

### Анализ
Изменено 1/2 ожидаемых файлов (50%). Изменено всего файлов: 1

---

## Тест 7. Experience +4 поля (Средняя)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 1dd0ac93-864f-49ff-95b6-61027bb8622e |
| Статус | failed |
| Pass@1 | 0 |
| Время | 1241 сек |
| Build итераций | 0 |
| Completeness | 2/3 (67%) |
| Токены (total) | 36018 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/Experience.cs, Data/Initializer.cs |
| F_required | Data/Entities/Experience.cs, Data/DataConfiguration.cs, Data/Initializer.cs |
| F_missing | Data/DataConfiguration.cs |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type |  (confidence: 0.0) |
| Примеров загружено | 0 |
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

## Тест 8. MediaLink +4 поля (Средняя)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 5e6e0c61-f659-4522-9d69-69494a48882f |
| Статус | failed |
| Pass@1 | 0 |
| Время | 1256 сек |
| Build итераций | 0 |
| Completeness | 0/3 (0%) |
| Токены (total) | 43012 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Configurations/DataConfiguration.cs, Data/Entities/ConstructionSite.cs, Data/Entities/MediaLinkEntities/MediaLink.cs |
| F_required | Data/Entities/MediaLink.cs, Data/DataConfiguration.cs, Data/Initializer.cs |
| F_missing | Data/Initializer.cs |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type |  (confidence: 0.0) |
| Примеров загружено | 0 |
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

## Тест 9. SpecialZone +5 полей (Средняя)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 9b5d39cd-1e8c-4f1f-8157-9c8ce0b12ad2 |
| Статус | success |
| Pass@1 | 1 |
| Время | 996 сек |
| Build итераций | 0 |
| Completeness | 1/3 (33%) |
| Токены (total) | 32239 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Configurations/DataConfiguration.cs, Data/EF/DataContext.cs, Data/Entities/SpecialZone.cs |
| F_required | Data/Entities/SpecialZone.cs, Data/DataConfiguration.cs, Data/Initializer.cs |
| F_missing | Data/Initializer.cs |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type |  (confidence: 0.0) |
| Примеров загружено | 0 |
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

## Тест 10. CheckPoint +4 поля (Средняя)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 747d9424-2cb9-4939-9ded-d02269cf2873 |
| Статус | success |
| Pass@1 | 1 |
| Время | 1238 сек |
| Build итераций | 0 |
| Completeness | 1/3 (33%) |
| Токены (total) | 37264 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Bindings/JournalEventsConfiguration.cs, Data/Configurations/DataConfiguration.cs, Data/Entities/BuildProject/ConstructionSite.cs, Data/Entities/CheckLists/CheckPoint.cs, Data/Initializer.cs |
| F_required | Data/Entities/CheckPoint.cs, Data/DataConfiguration.cs, Data/Initializer.cs |
| F_missing | — |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type |  (confidence: 0.0) |
| Примеров загружено | 0 |
| Template | — |

### Валидация
| Проверка | Результат |
|----------|----------|
| API status | success |
| F_actual.length > 0 | ✅ (5 файлов) |
| F_actual ∩ F_required > 0 | ✅ |
| Итоговый статус | **success** |

### Анализ
Изменено 1/3 ожидаемых файлов (33%). Изменено всего файлов: 5

---

## Тест 11. Notice +5 полей (Сложная)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | e2b4eed2-807f-4706-bbc5-a0038428ae71 |
| Статус | success |
| Pass@1 | 1 |
| Время | 945 сек |
| Build итераций | 0 |
| Completeness | 1/3 (33%) |
| Токены (total) | 43690 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Configurations/DataConfiguration.cs, Data/Entities/ConstructionSection.cs, Data/Entities/Notice.cs, Data/Entities/Tranche.cs |
| F_required | Data/Entities/Notice.cs, Data/DataConfiguration.cs, Data/Initializer.cs |
| F_missing | Data/Initializer.cs |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type |  (confidence: 0.0) |
| Примеров загружено | 0 |
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
| task_id | ee5ac5ff-8d64-46d6-b3d3-d68c108d5359 |
| Статус | success |
| Pass@1 | 1 |
| Время | 652 сек |
| Build итераций | 0 |
| Completeness | 0/3 (0%) |
| Токены (total) | 32556 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/Organization.cs |
| F_required | Data/Entities/EscrowAccount.cs, Data/DataConfiguration.cs, Data/Initializer.cs |
| F_missing | Data/Entities/EscrowAccount.cs, Data/DataConfiguration.cs, Data/Initializer.cs |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type |  (confidence: 0.0) |
| Примеров загружено | 0 |
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
| task_id | d6679c5e-fae0-4d2c-b144-0d068c8feefe |
| Статус | success |
| Pass@1 | 1 |
| Время | 1523 сек |
| Build итераций | 0 |
| Completeness | 6/10 (60%) |
| Токены (total) | 58512 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/BankPolicy/BankPolicy.cs, Data/Entities/BankPolicy/BankPolicyItem.cs, Data/Entities/CheckLists/CheckListItem.cs, Data/Entities/CheckPoint.cs, Data/Entities/Discussion.cs, Data/Entities/DiscussionProtocol.cs, Data/Entities/MediaLinkEntities/MediaLink.cs, Data/Entities/Notice.cs, Data/Entities/ProjectAnalog.cs, Data/Entities/TargetProgram.cs |
| F_required | Data/Entities/Discussion.cs, Data/Entities/BankPolicy.cs, Data/Entities/Notice.cs, Data/Entities/CheckPoint.cs, Data/Entities/MediaLink.cs, Data/Entities/ProjectAnalog.cs, Data/Entities/TargetProgram.cs, Data/Entities/CheckListItem.cs, Data/Entities/DiscussionProtocol.cs, Data/Entities/BankPolicyItem.cs |
| F_missing | — |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type |  (confidence: 0.0) |
| Примеров загружено | 0 |
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
| task_id | dd38171d-736b-4a81-a179-6d2ab6998dce |
| Статус | success |
| Pass@1 | 1 |
| Время | 1644 сек |
| Build итераций | 0 |
| Completeness | 0/3 (0%) |
| Токены (total) | 53541 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/EF/Initializer.cs, Data/Entities/BankPolicy/BankPolicy.cs, Data/Entities/BankPolicy/BankPolicyItem.cs |
| F_required | Data/Entities/BankPolicy.cs, Data/Entities/BankPolicyItem.cs, Data/DataConfiguration.cs |
| F_missing | Data/DataConfiguration.cs |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type |  (confidence: 0.0) |
| Примеров загружено | 0 |
| Template | — |

### Валидация
| Проверка | Результат |
|----------|----------|
| API status | success |
| F_actual.length > 0 | ✅ (3 файлов) |
| F_actual ∩ F_required > 0 | ✅ |
| Итоговый статус | **success** |

### Анализ
Изменено 0/3 ожидаемых файлов (0%). Изменено всего файлов: 3

---

## Тест 15. SalesData +5 полей (Сложная)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | ef8a0c0c-f19f-4b0e-bcca-0c5d897d9b77 |
| Статус | success |
| Pass@1 | 1 |
| Время | 501 сек |
| Build итераций | 0 |
| Completeness | 0/3 (0%) |
| Токены (total) | 32909 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/SalesEntities/SalesData.cs |
| F_required | Data/Entities/SalesData.cs, Data/DataConfiguration.cs, Data/Initializer.cs |
| F_missing | Data/DataConfiguration.cs, Data/Initializer.cs |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type |  (confidence: 0.0) |
| Примеров загружено | 0 |
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
| Avg completeness | 51.8% |
| Avg time | 889 сек |
| Total time | 13328 сек (222.1 мин) |

### Сводная таблица

| # | Тест | Сложность | Статус | Pass@1 | Completeness | Время |
|---|------|-----------|--------|--------|--------------|-------|
| 1 | Portfolio +2 поля | Простая | success | 1 | 1/1 (100%) | 531 сек |
| 2 | OrganizationPerson +3 поля | Простая | success | 1 | 1/1 (100%) | 618 сек |
| 3 | PhotoReportItem +2 поля | Простая | failed | 0 | 1/1 (100%) | 368 сек |
| 4 | SubmittedDocumentsTemplate +2 поля | Простая | success | 1 | 1/1 (100%) | 399 сек |
| 5 | ContractCurrency +1 enum | Простая | success | 1 | 1/1 (100%) | 468 сек |
| 6 | ConstructionSection +5 полей | Средняя | success | 1 | 1/2 (50%) | 948 сек |
| 7 | Experience +4 поля | Средняя | failed | 0 | 2/3 (67%) | 1241 сек |
| 8 | MediaLink +4 поля | Средняя | failed | 0 | 0/3 (0%) | 1256 сек |
| 9 | SpecialZone +5 полей | Средняя | success | 1 | 1/3 (33%) | 996 сек |
| 10 | CheckPoint +4 поля | Средняя | success | 1 | 1/3 (33%) | 1238 сек |
| 11 | Notice +5 полей | Сложная | success | 1 | 1/3 (33%) | 945 сек |
| 12 | EscrowAccount +5 полей | Сложная | success | 1 | 0/3 (0%) | 652 сек |
| 13 | 10 сущностей +2 поля | Сложная | success | 1 | 6/10 (60%) | 1523 сек |
| 14 | BankPolicy + BankPolicyItem | Сложная | success | 1 | 0/3 (0%) | 1644 сек |
| 15 | SalesData +5 полей | Сложная | success | 1 | 0/3 (0%) | 501 сек |

