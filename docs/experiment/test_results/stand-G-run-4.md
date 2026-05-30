# Прогон: Конфигурация G, повторение 4

**Дата**: 2026-03-25 18:33
**Конфигурация**: G: Multi-agent + граф (без RAG)
**Настройки**: agent_mode=multi, use_rag=False, rag_top_k=0, use_graph=True
**Модель**: Claude Haiku 4.5

---

## Тест 1. Portfolio +2 поля (Простая)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | d1dcf927-55e9-454a-9fdc-3444d58fd068 |
| Статус | success |
| Pass@1 | 1 |
| Время | 445 сек |
| Build итераций | 0 |
| Completeness | 1/1 (100%) |
| Токены (total) | 32921 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Configurations/DataConfiguration.cs, Data/Entities/Portfolio.cs |
| F_required | Data/Entities/Portfolio.cs |
| F_missing | — |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type | modify_entity (confidence: 0.9983) |
| Примеров загружено | 0 |
| Template | modify_entity_with_navigation_properties |

### Валидация
| Проверка | Результат |
|----------|----------|
| API status | success |
| F_actual.length > 0 | ✅ (2 файлов) |
| F_actual ∩ F_required > 0 | ✅ |
| Итоговый статус | **success** |

### Анализ
Все 1 ожидаемых файлов изменены

---

## Тест 2. OrganizationPerson +3 поля (Простая)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 700aafd4-8940-453f-85d8-b958b82819c3 |
| Статус | success |
| Pass@1 | 1 |
| Время | 396 сек |
| Build итераций | 0 |
| Completeness | 1/1 (100%) |
| Токены (total) | 34602 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/OrganizationPerson.cs |
| F_required | Data/Entities/OrganizationPerson.cs |
| F_missing | — |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type | modify_entity (confidence: 0.9983) |
| Примеров загружено | 0 |
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

## Тест 3. PhotoReportItem +2 поля (Простая)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 793f32aa-2b0c-430b-b5a4-e3334ac5e682 |
| Статус | success |
| Pass@1 | 1 |
| Время | 407 сек |
| Build итераций | 0 |
| Completeness | 1/1 (100%) |
| Токены (total) | 37151 |

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
| Примеров загружено | 0 |
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
| task_id | 9eb4249f-a306-4383-afd1-dcdc5891a5f3 |
| Статус | success |
| Pass@1 | 1 |
| Время | 335 сек |
| Build итераций | 0 |
| Completeness | 1/1 (100%) |
| Токены (total) | 32763 |

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
| Примеров загружено | 0 |
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
| task_id | d7148c5b-77d8-4550-a6f6-e379e7e54b29 |
| Статус | success |
| Pass@1 | 1 |
| Время | 244 сек |
| Build итераций | 0 |
| Completeness | 1/1 (100%) |
| Токены (total) | 24272 |

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
| Примеров загружено | 0 |
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
| task_id | 79a107d3-0bf5-478a-9617-1c44710f35aa |
| Статус | success |
| Pass@1 | 1 |
| Время | 729 сек |
| Build итераций | 0 |
| Completeness | 1/2 (50%) |
| Токены (total) | 45698 |

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
| Примеров загружено | 0 |
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
| task_id | 550edea6-aa4b-4ca7-92fe-6378048b0d92 |
| Статус | success |
| Pass@1 | 1 |
| Время | 463 сек |
| Build итераций | 0 |
| Completeness | 2/3 (67%) |
| Токены (total) | 39800 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Configurations/DataConfiguration.cs, Data/Entities/Experience.cs, Data/Initializer.cs |
| F_required | Data/Entities/Experience.cs, Data/DataConfiguration.cs, Data/Initializer.cs |
| F_missing | — |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type | modify_entity (confidence: 0.9983) |
| Примеров загружено | 0 |
| Template | modify_entity_with_navigation_properties |

### Валидация
| Проверка | Результат |
|----------|----------|
| API status | success |
| F_actual.length > 0 | ✅ (3 файлов) |
| F_actual ∩ F_required > 0 | ✅ |
| Итоговый статус | **success** |

### Анализ
Изменено 2/3 ожидаемых файлов (67%). Изменено всего файлов: 3

---

## Тест 8. MediaLink +4 поля (Средняя)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | cc40657f-adf1-4d0e-bca2-92b339dbb043 |
| Статус | success |
| Pass@1 | 1 |
| Время | 516 сек |
| Build итераций | 0 |
| Completeness | 1/3 (33%) |
| Токены (total) | 48336 |

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
| Примеров загружено | 0 |
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
| task_id | e3ab2111-2ff7-4df2-8593-7fe8cf0c8508 |
| Статус | success |
| Pass@1 | 1 |
| Время | 697 сек |
| Build итераций | 0 |
| Completeness | 2/3 (67%) |
| Токены (total) | 44877 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Configurations/DataConfiguration.cs, Data/Entities/SpecialZone.cs, Data/Initializer.cs |
| F_required | Data/Entities/SpecialZone.cs, Data/DataConfiguration.cs, Data/Initializer.cs |
| F_missing | — |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type | modify_entity (confidence: 0.9983) |
| Примеров загружено | 0 |
| Template | modify_entity_with_navigation_properties |

### Валидация
| Проверка | Результат |
|----------|----------|
| API status | success |
| F_actual.length > 0 | ✅ (3 файлов) |
| F_actual ∩ F_required > 0 | ✅ |
| Итоговый статус | **success** |

### Анализ
Изменено 2/3 ожидаемых файлов (67%). Изменено всего файлов: 3

---

## Тест 10. CheckPoint +4 поля (Средняя)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 434b558c-c439-46b2-9a26-5822300c6a6d |
| Статус | success |
| Pass@1 | 1 |
| Время | 601 сек |
| Build итераций | 0 |
| Completeness | 1/3 (33%) |
| Токены (total) | 48951 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Configurations/DataConfiguration.cs, Data/Entities/CheckLists/CheckPoint.cs, Data/Initializer.cs |
| F_required | Data/Entities/CheckPoint.cs, Data/DataConfiguration.cs, Data/Initializer.cs |
| F_missing | — |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type | modify_entity (confidence: 0.9983) |
| Примеров загружено | 0 |
| Template | modify_entity_with_navigation_properties |

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
| task_id | 925d71f1-224c-4246-956b-13902d2568c8 |
| Статус | success |
| Pass@1 | 1 |
| Время | 592 сек |
| Build итераций | 0 |
| Completeness | 2/3 (67%) |
| Токены (total) | 60058 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Configurations/DataConfiguration.cs, Data/Entities/ConstructionSection.cs, Data/Entities/Notice.cs, Data/Entities/Tranche.cs, Data/Initializer.cs |
| F_required | Data/Entities/Notice.cs, Data/DataConfiguration.cs, Data/Initializer.cs |
| F_missing | — |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type | modify_entity (confidence: 0.9983) |
| Примеров загружено | 0 |
| Template | modify_entity_with_navigation_properties |

### Валидация
| Проверка | Результат |
|----------|----------|
| API status | success |
| F_actual.length > 0 | ✅ (5 файлов) |
| F_actual ∩ F_required > 0 | ✅ |
| Итоговый статус | **success** |

### Анализ
Изменено 2/3 ожидаемых файлов (67%). Изменено всего файлов: 5

---

## Тест 12. EscrowAccount +5 полей (Сложная)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 44e25fa5-b9f4-48cc-b4b5-c8c79789d74a |
| Статус | success |
| Pass@1 | 1 |
| Время | 515 сек |
| Build итераций | 0 |
| Completeness | 1/3 (33%) |
| Токены (total) | 38786 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Configurations/DataConfiguration.cs, Data/Entities/RoomEntites/EscrowAccount.cs, Data/Initializer.cs |
| F_required | Data/Entities/EscrowAccount.cs, Data/DataConfiguration.cs, Data/Initializer.cs |
| F_missing | — |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type | modify_entity (confidence: 0.9983) |
| Примеров загружено | 0 |
| Template | modify_entity_with_navigation_properties |

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

## Тест 13. 10 сущностей +2 поля (Сложная)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 101c645c-e787-48f3-ac46-f25c1fe315d9 |
| Статус | success |
| Pass@1 | 1 |
| Время | 602 сек |
| Build итераций | 0 |
| Completeness | 6/10 (60%) |
| Токены (total) | 74965 |

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
| Примеров загружено | 0 |
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
| task_id | 675075dc-8121-4fb5-b249-773f59f3e3d9 |
| Статус | failed |
| Pass@1 | 0 |
| Время | 435 сек |
| Build итераций | 0 |
| Completeness | 0/3 (0%) |
| Токены (total) | 60649 |

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
| Примеров загружено | 0 |
| Template | modify_entity_with_navigation_properties |

### Валидация
| Проверка | Результат |
|----------|----------|
| API status | failed |
| F_actual.length > 0 | ✅ (2 файлов) |
| F_actual ∩ F_required > 0 | ✅ |
| Итоговый статус | **failed** |

### Анализ
Тест завершился с ошибкой: Pipeline halted: 3 subtasks failed with zero changes. Last: Register BankPolicy.Responsible association in Initializer

---

## Тест 15. SalesData +5 полей (Сложная)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | d9fc139e-bed6-45a1-b2d6-bca76d15eee7 |
| Статус | success |
| Pass@1 | 1 |
| Время | 603 сек |
| Build итераций | 0 |
| Completeness | 1/3 (33%) |
| Токены (total) | 52566 |

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
| Примеров загружено | 0 |
| Template | modify_entity_with_navigation_properties |

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


## Итоги прогона

| Метрика | Значение |
|---------|----------|
| Всего тестов | 15 |
| Pass@1 | 14/15 (93%) |
| False success | 0 |
| Failed | 1 |
| Timeout | 0 |
| Avg completeness | 62.9% |
| Avg time | 505 сек |
| Total time | 7580 сек (126.3 мин) |

### Сводная таблица

| # | Тест | Сложность | Статус | Pass@1 | Completeness | Время |
|---|------|-----------|--------|--------|--------------|-------|
| 1 | Portfolio +2 поля | Простая | success | 1 | 1/1 (100%) | 445 сек |
| 2 | OrganizationPerson +3 поля | Простая | success | 1 | 1/1 (100%) | 396 сек |
| 3 | PhotoReportItem +2 поля | Простая | success | 1 | 1/1 (100%) | 407 сек |
| 4 | SubmittedDocumentsTemplate +2 поля | Простая | success | 1 | 1/1 (100%) | 335 сек |
| 5 | ContractCurrency +1 enum | Простая | success | 1 | 1/1 (100%) | 244 сек |
| 6 | ConstructionSection +5 полей | Средняя | success | 1 | 1/2 (50%) | 729 сек |
| 7 | Experience +4 поля | Средняя | success | 1 | 2/3 (67%) | 463 сек |
| 8 | MediaLink +4 поля | Средняя | success | 1 | 1/3 (33%) | 516 сек |
| 9 | SpecialZone +5 полей | Средняя | success | 1 | 2/3 (67%) | 697 сек |
| 10 | CheckPoint +4 поля | Средняя | success | 1 | 1/3 (33%) | 601 сек |
| 11 | Notice +5 полей | Сложная | success | 1 | 2/3 (67%) | 592 сек |
| 12 | EscrowAccount +5 полей | Сложная | success | 1 | 1/3 (33%) | 515 сек |
| 13 | 10 сущностей +2 поля | Сложная | success | 1 | 6/10 (60%) | 602 сек |
| 14 | BankPolicy + BankPolicyItem | Сложная | failed | 0 | 0/3 (0%) | 435 сек |
| 15 | SalesData +5 полей | Сложная | success | 1 | 1/3 (33%) | 603 сек |

