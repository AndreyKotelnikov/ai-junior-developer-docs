# Прогон: Конфигурация I, повторение 3

**Дата**: 2026-03-25 17:02
**Конфигурация**: I: Multi-agent + RAG(3) + граф
**Настройки**: agent_mode=multi, use_rag=True, rag_top_k=3, use_graph=True
**Модель**: Claude Haiku 4.5

---

## Тест 1. Portfolio +2 поля (Простая)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 64722d5e-19ea-4e88-a8fd-ef8e7c59a212 |
| Статус | success |
| Pass@1 | 1 |
| Время | 264 сек |
| Build итераций | 0 |
| Completeness | 1/1 (100%) |
| Токены (total) | 31437 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/Portfolio.cs |
| F_required | Data/Entities/Portfolio.cs |
| F_missing | — |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type | modify_entity (confidence: 0.9983) |
| Примеров загружено | 3 |
| Template | modify_entity_with_navigation_properties |

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
| task_id | 2d4a6c43-2003-4d33-8ca2-b9841d0b471d |
| Статус | failed |
| Pass@1 | 0 |
| Время | 712 сек |
| Build итераций | 0 |
| Completeness | 1/1 (100%) |
| Токены (total) | 50622 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Configurations/DataConfiguration.cs, Data/Entities/OrganizationPerson.cs |
| F_required | Data/Entities/OrganizationPerson.cs |
| F_missing | — |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type | modify_entity (confidence: 0.9983) |
| Примеров загружено | 3 |
| Template | modify_entity_with_navigation_properties |

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
| task_id | a58aa660-c32e-40b7-9985-2ff9acc19b81 |
| Статус | success |
| Pass@1 | 1 |
| Время | 323 сек |
| Build итераций | 0 |
| Completeness | 1/1 (100%) |
| Токены (total) | 57856 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/PhotoReport/PhotoReportItem.cs |
| F_required | Data/Entities/PhotoReport/PhotoReportItem.cs |
| F_missing | — |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type | modify_entity (confidence: 0.9983) |
| Примеров загружено | 3 |
| Template | modify_entity_with_navigation_properties |

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
| task_id | d5075281-7e65-4087-b5c9-1f264c341deb |
| Статус | success |
| Pass@1 | 1 |
| Время | 246 сек |
| Build итераций | 0 |
| Completeness | 1/1 (100%) |
| Токены (total) | 37260 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/SubmittedDocumentsTemplate.cs |
| F_required | Data/Entities/SubmittedDocumentsTemplate.cs |
| F_missing | — |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type | modify_entity (confidence: 0.9983) |
| Примеров загружено | 3 |
| Template | modify_entity_with_navigation_properties |

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
| task_id | b7eb5603-e865-4cd9-8f4f-0b98733d1b7e |
| Статус | success |
| Pass@1 | 1 |
| Время | 367 сек |
| Build итераций | 0 |
| Completeness | 1/1 (100%) |
| Токены (total) | 49148 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/ContractCurrency.cs |
| F_required | Data/Entities/ContractCurrency.cs |
| F_missing | — |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type | modify_entity (confidence: 0.9983) |
| Примеров загружено | 3 |
| Template | modify_entity_with_navigation_properties |

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
| task_id | 32c523db-1da1-4fdf-a2af-ac50d5328d68 |
| Статус | success |
| Pass@1 | 1 |
| Время | 628 сек |
| Build итераций | 0 |
| Completeness | 1/2 (50%) |
| Токены (total) | 77949 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/ConstructionSection.cs |
| F_required | Data/Entities/ConstructionSection.cs, Data/DataConfiguration.cs |
| F_missing | Data/DataConfiguration.cs |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type | modify_entity (confidence: 0.9983) |
| Примеров загружено | 3 |
| Template | modify_entity_with_navigation_properties |

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
| task_id | 3683f169-1c0d-4654-92e3-c70959818031 |
| Статус | success |
| Pass@1 | 1 |
| Время | 477 сек |
| Build итераций | 0 |
| Completeness | 2/3 (67%) |
| Токены (total) | 69842 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Configurations/DataConfiguration.cs, Data/Entities/Experience.cs, Data/Enums/DeveloperCategory.cs, Data/Initializer.cs |
| F_required | Data/Entities/Experience.cs, Data/DataConfiguration.cs, Data/Initializer.cs |
| F_missing | — |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type | modify_entity (confidence: 0.9983) |
| Примеров загружено | 3 |
| Template | modify_entity_with_navigation_properties |

### Валидация
| Проверка | Результат |
|----------|----------|
| API status | success |
| F_actual.length > 0 | ✅ (4 файлов) |
| F_actual ∩ F_required > 0 | ✅ |
| Итоговый статус | **success** |

### Анализ
Изменено 2/3 ожидаемых файлов (67%). Изменено всего файлов: 4

---

## Тест 8. MediaLink +4 поля (Средняя)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 59e9db21-a6eb-44d7-8dc3-318429dc85e0 |
| Статус | success |
| Pass@1 | 1 |
| Время | 475 сек |
| Build итераций | 0 |
| Completeness | 1/3 (33%) |
| Токены (total) | 80879 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/MediaLinkEntities/MediaLink.cs, Data/Initializer.cs |
| F_required | Data/Entities/MediaLink.cs, Data/DataConfiguration.cs, Data/Initializer.cs |
| F_missing | Data/DataConfiguration.cs |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type | modify_entity (confidence: 0.9983) |
| Примеров загружено | 3 |
| Template | modify_entity_with_navigation_properties |

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

## Тест 9. SpecialZone +5 полей (Средняя)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | abb8fb4e-16dc-4fe1-ad95-ee78aa17b40c |
| Статус | success |
| Pass@1 | 1 |
| Время | 641 сек |
| Build итераций | 0 |
| Completeness | 1/3 (33%) |
| Токены (total) | 79446 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Configurations/DataConfiguration.cs, Data/Entities/SpecialZone.cs |
| F_required | Data/Entities/SpecialZone.cs, Data/DataConfiguration.cs, Data/Initializer.cs |
| F_missing | Data/Initializer.cs |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type | modify_entity (confidence: 0.9983) |
| Примеров загружено | 3 |
| Template | modify_entity_with_navigation_properties |

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
| task_id | a763b9d2-ab35-4881-bb71-b9c2fdc851b3 |
| Статус | success |
| Pass@1 | 1 |
| Время | 583 сек |
| Build итераций | 0 |
| Completeness | 1/3 (33%) |
| Токены (total) | 72260 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/CheckLists/CheckPoint.cs, Data/Initializer.cs |
| F_required | Data/Entities/CheckPoint.cs, Data/DataConfiguration.cs, Data/Initializer.cs |
| F_missing | Data/DataConfiguration.cs |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type | modify_entity (confidence: 0.9983) |
| Примеров загружено | 3 |
| Template | modify_entity_with_navigation_properties |

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

## Тест 11. Notice +5 полей (Сложная)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | d947d2ee-1676-4180-93a1-45b6f8c3b6cc |
| Статус | success |
| Pass@1 | 1 |
| Время | 458 сек |
| Build итераций | 0 |
| Completeness | 2/3 (67%) |
| Токены (total) | 80458 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/Notice.cs, Data/Initializer.cs |
| F_required | Data/Entities/Notice.cs, Data/DataConfiguration.cs, Data/Initializer.cs |
| F_missing | Data/DataConfiguration.cs |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type | modify_entity (confidence: 0.9983) |
| Примеров загружено | 3 |
| Template | modify_entity_with_navigation_properties |

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

## Тест 12. EscrowAccount +5 полей (Сложная)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | c944ac2f-df20-4498-9a4f-898dcb26602e |
| Статус | success |
| Pass@1 | 1 |
| Время | 539 сек |
| Build итераций | 0 |
| Completeness | 1/3 (33%) |
| Токены (total) | 68130 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/RoomEntites/EscrowAccount.cs, Data/Initializer.cs |
| F_required | Data/Entities/EscrowAccount.cs, Data/DataConfiguration.cs, Data/Initializer.cs |
| F_missing | Data/DataConfiguration.cs |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type | modify_entity (confidence: 0.9983) |
| Примеров загружено | 3 |
| Template | modify_entity_with_navigation_properties |

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

## Тест 13. 10 сущностей +2 поля (Сложная)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 20db6e89-5e65-47ea-ad16-7ef6d3651798 |
| Статус | success |
| Pass@1 | 1 |
| Время | 1110 сек |
| Build итераций | 0 |
| Completeness | 6/10 (60%) |
| Токены (total) | 192334 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/BankPolicy/BankPolicy.cs, Data/Entities/BankPolicy/BankPolicyItem.cs, Data/Entities/CheckLists/CheckListItem.cs, Data/Entities/CheckPoint.cs, Data/Entities/Discussion.cs, Data/Entities/DiscussionProtocol.cs, Data/Entities/MediaLinkEntities/MediaLink.cs, Data/Entities/Notice.cs, Data/Entities/ProjectAnalog.cs, Data/Entities/TargetProgram.cs |
| F_required | Data/Entities/Discussion.cs, Data/Entities/BankPolicy.cs, Data/Entities/Notice.cs, Data/Entities/CheckPoint.cs, Data/Entities/MediaLink.cs, Data/Entities/ProjectAnalog.cs, Data/Entities/TargetProgram.cs, Data/Entities/CheckListItem.cs, Data/Entities/DiscussionProtocol.cs, Data/Entities/BankPolicyItem.cs |
| F_missing | — |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type | modify_entity (confidence: 0.9983) |
| Примеров загружено | 3 |
| Template | modify_entity_with_navigation_properties |

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
| task_id | 8e6753ac-c954-4c1b-bfbd-8a94b819bae6 |
| Статус | failed |
| Pass@1 | 0 |
| Время | 617 сек |
| Build итераций | 0 |
| Completeness | 0/3 (0%) |
| Токены (total) | 131363 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/BankPolicy/BankPolicy.cs, Data/Entities/BankPolicy/BankPolicyItem.cs |
| F_required | Data/Entities/BankPolicy.cs, Data/Entities/BankPolicyItem.cs, Data/DataConfiguration.cs |
| F_missing | Data/DataConfiguration.cs |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type | modify_entity (confidence: 0.9983) |
| Примеров загружено | 3 |
| Template | modify_entity_with_navigation_properties |

### Валидация
| Проверка | Результат |
|----------|----------|
| API status | failed |
| F_actual.length > 0 | ✅ (2 файлов) |
| F_actual ∩ F_required > 0 | ✅ |
| Итоговый статус | **failed** |

### Анализ
Тест завершился с ошибкой: Pipeline halted: 3 subtasks failed with zero changes. Last: Register User.BankPolicies association in Initializer

---

## Тест 15. SalesData +5 полей (Сложная)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 3a000e3c-e9be-4b52-98dd-4e0b2f5c14e0 |
| Статус | failed |
| Pass@1 | 0 |
| Время | 592 сек |
| Build итераций | 0 |
| Completeness | 1/3 (33%) |
| Токены (total) | 195688 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Configurations/DataConfiguration.cs, Data/Entities/SalesEntities/SalesData.cs, Data/Initializer.cs |
| F_required | Data/Entities/SalesData.cs, Data/DataConfiguration.cs, Data/Initializer.cs |
| F_missing | — |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type | modify_entity (confidence: 0.9983) |
| Примеров загружено | 3 |
| Template | modify_entity_with_navigation_properties |

### Валидация
| Проверка | Результат |
|----------|----------|
| API status | failed |
| F_actual.length > 0 | ✅ (3 файлов) |
| F_actual ∩ F_required > 0 | ✅ |
| Итоговый статус | **failed** |

### Анализ
Тест завершился с ошибкой: Pipeline halted: 3 subtasks failed with zero changes. Last: Register SalesManager (User) one-to-many association in Initializer

---


## Итоги прогона

| Метрика | Значение |
|---------|----------|
| Всего тестов | 15 |
| Pass@1 | 12/15 (80%) |
| False success | 0 |
| Failed | 3 |
| Timeout | 0 |
| Avg completeness | 60.7% |
| Avg time | 535 сек |
| Total time | 8032 сек (133.9 мин) |

### Сводная таблица

| # | Тест | Сложность | Статус | Pass@1 | Completeness | Время |
|---|------|-----------|--------|--------|--------------|-------|
| 1 | Portfolio +2 поля | Простая | success | 1 | 1/1 (100%) | 264 сек |
| 2 | OrganizationPerson +3 поля | Простая | failed | 0 | 1/1 (100%) | 712 сек |
| 3 | PhotoReportItem +2 поля | Простая | success | 1 | 1/1 (100%) | 323 сек |
| 4 | SubmittedDocumentsTemplate +2 поля | Простая | success | 1 | 1/1 (100%) | 246 сек |
| 5 | ContractCurrency +1 enum | Простая | success | 1 | 1/1 (100%) | 367 сек |
| 6 | ConstructionSection +5 полей | Средняя | success | 1 | 1/2 (50%) | 628 сек |
| 7 | Experience +4 поля | Средняя | success | 1 | 2/3 (67%) | 477 сек |
| 8 | MediaLink +4 поля | Средняя | success | 1 | 1/3 (33%) | 475 сек |
| 9 | SpecialZone +5 полей | Средняя | success | 1 | 1/3 (33%) | 641 сек |
| 10 | CheckPoint +4 поля | Средняя | success | 1 | 1/3 (33%) | 583 сек |
| 11 | Notice +5 полей | Сложная | success | 1 | 2/3 (67%) | 458 сек |
| 12 | EscrowAccount +5 полей | Сложная | success | 1 | 1/3 (33%) | 539 сек |
| 13 | 10 сущностей +2 поля | Сложная | success | 1 | 6/10 (60%) | 1110 сек |
| 14 | BankPolicy + BankPolicyItem | Сложная | failed | 0 | 0/3 (0%) | 617 сек |
| 15 | SalesData +5 полей | Сложная | failed | 0 | 1/3 (33%) | 592 сек |

