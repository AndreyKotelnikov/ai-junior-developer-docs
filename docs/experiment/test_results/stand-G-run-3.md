# Прогон: Конфигурация G, повторение 3

**Дата**: 2026-03-25 16:41
**Конфигурация**: G: Multi-agent + граф (без RAG)
**Настройки**: agent_mode=multi, use_rag=False, rag_top_k=0, use_graph=True
**Модель**: Claude Haiku 4.5

---

## Тест 1. Portfolio +2 поля (Простая)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | d60f0da0-1e24-414d-8265-d9fb3002bbbf |
| Статус | success |
| Pass@1 | 1 |
| Время | 361 сек |
| Build итераций | 0 |
| Completeness | 1/1 (100%) |
| Токены (total) | 29592 |

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

## Тест 2. OrganizationPerson +3 поля (Простая)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 7eef1ee6-0fb7-45a9-9ab8-625548a21fb2 |
| Статус | success |
| Pass@1 | 1 |
| Время | 438 сек |
| Build итераций | 0 |
| Completeness | 1/1 (100%) |
| Токены (total) | 30846 |

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
| task_id | c636f323-dc83-40c5-a1ce-ec2f83f90c75 |
| Статус | success |
| Pass@1 | 1 |
| Время | 232 сек |
| Build итераций | 0 |
| Completeness | 1/1 (100%) |
| Токены (total) | 24878 |

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
| task_id | ef7cb455-cebc-4417-84b8-689277ecdac1 |
| Статус | success |
| Pass@1 | 1 |
| Время | 328 сек |
| Build итераций | 0 |
| Completeness | 1/1 (100%) |
| Токены (total) | 29133 |

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
| task_id | 4f657837-0e23-4ae2-b356-88d879d7b28c |
| Статус | success |
| Pass@1 | 1 |
| Время | 368 сек |
| Build итераций | 0 |
| Completeness | 1/1 (100%) |
| Токены (total) | 40323 |

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
| task_id | 253fe533-3aef-4792-a7bb-5b86e15cae26 |
| Статус | failed |
| Pass@1 | 0 |
| Время | 256 сек |
| Build итераций | 0 |
| Completeness | 1/2 (50%) |
| Токены (total) | 45861 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Configurations/DataConfiguration.cs, Data/Entities/ConstructionSection.cs |
| F_required | Data/Entities/ConstructionSection.cs, Data/DataConfiguration.cs |
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
| API status | failed |
| F_actual.length > 0 | ✅ (2 файлов) |
| F_actual ∩ F_required > 0 | ✅ |
| Итоговый статус | **failed** |

### Анализ
Тест завершился с ошибкой: Build fix loop aborted: errors grew for 3 consecutive attempts (1 -> 2). Fix loop is making things worse.

---

## Тест 7. Experience +4 поля (Средняя)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 1c1a9627-71f5-4a7e-982c-1160d882abc2 |
| Статус | success |
| Pass@1 | 1 |
| Время | 444 сек |
| Build итераций | 0 |
| Completeness | 2/3 (67%) |
| Токены (total) | 42158 |

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
| task_id | 5e70911f-aa6b-43a5-8b17-5b5d08029062 |
| Статус | success |
| Pass@1 | 1 |
| Время | 675 сек |
| Build итераций | 0 |
| Completeness | 1/3 (33%) |
| Токены (total) | 51004 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Configurations/DataConfiguration.cs, Data/Entities/MediaLinkEntities/MediaLink.cs, Data/Initializer.cs |
| F_required | Data/Entities/MediaLink.cs, Data/DataConfiguration.cs, Data/Initializer.cs |
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

## Тест 9. SpecialZone +5 полей (Средняя)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 4bbc22b2-2e72-4627-8800-3fb10260020c |
| Статус | success |
| Pass@1 | 1 |
| Время | 464 сек |
| Build итераций | 0 |
| Completeness | 2/3 (67%) |
| Токены (total) | 48812 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/SpecialZone.cs, Data/Initializer.cs |
| F_required | Data/Entities/SpecialZone.cs, Data/DataConfiguration.cs, Data/Initializer.cs |
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
Изменено 2/3 ожидаемых файлов (67%). Изменено всего файлов: 2

---

## Тест 10. CheckPoint +4 поля (Средняя)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 652ce609-b64d-4596-b482-fc535b22ae7e |
| Статус | success |
| Pass@1 | 1 |
| Время | 517 сек |
| Build итераций | 0 |
| Completeness | 1/3 (33%) |
| Токены (total) | 42872 |

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

## Тест 11. Notice +5 полей (Сложная)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | a5a9313d-c9c3-43ca-b0e6-9daece0585bd |
| Статус | success |
| Pass@1 | 1 |
| Время | 484 сек |
| Build итераций | 0 |
| Completeness | 2/3 (67%) |
| Токены (total) | 45483 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Configurations/DataConfiguration.cs, Data/Entities/Notice.cs, Data/Initializer.cs |
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
| F_actual.length > 0 | ✅ (3 файлов) |
| F_actual ∩ F_required > 0 | ✅ |
| Итоговый статус | **success** |

### Анализ
Изменено 2/3 ожидаемых файлов (67%). Изменено всего файлов: 3

---

## Тест 12. EscrowAccount +5 полей (Сложная)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 7db22518-d075-41e0-9465-37247cdd4e32 |
| Статус | success |
| Pass@1 | 1 |
| Время | 431 сек |
| Build итераций | 0 |
| Completeness | 1/3 (33%) |
| Токены (total) | 39369 |

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
| task_id | 8e65ba60-3216-4230-8f2f-98796256ed70 |
| Статус | success |
| Pass@1 | 1 |
| Время | 753 сек |
| Build итераций | 0 |
| Completeness | 6/10 (60%) |
| Токены (total) | 79353 |

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
| task_id | 2d8e82fa-0191-4dd5-a1c3-a0e29a10899a |
| Статус | failed |
| Pass@1 | 0 |
| Время | 485 сек |
| Build итераций | 0 |
| Completeness | 0/3 (0%) |
| Токены (total) | 60351 |

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
Тест завершился с ошибкой: Pipeline halted: 3 subtasks failed with zero changes. Last: Register User->BankPolicy association in Initializer

---

## Тест 15. SalesData +5 полей (Сложная)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 951712d0-2b6b-42e8-b0e1-e1bceeb79b93 |
| Статус | success |
| Pass@1 | 1 |
| Время | 382 сек |
| Build итераций | 0 |
| Completeness | 1/3 (33%) |
| Токены (total) | 39056 |

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
| Pass@1 | 13/15 (87%) |
| False success | 0 |
| Failed | 2 |
| Timeout | 0 |
| Avg completeness | 62.9% |
| Avg time | 441 сек |
| Total time | 6618 сек (110.3 мин) |

### Сводная таблица

| # | Тест | Сложность | Статус | Pass@1 | Completeness | Время |
|---|------|-----------|--------|--------|--------------|-------|
| 1 | Portfolio +2 поля | Простая | success | 1 | 1/1 (100%) | 361 сек |
| 2 | OrganizationPerson +3 поля | Простая | success | 1 | 1/1 (100%) | 438 сек |
| 3 | PhotoReportItem +2 поля | Простая | success | 1 | 1/1 (100%) | 232 сек |
| 4 | SubmittedDocumentsTemplate +2 поля | Простая | success | 1 | 1/1 (100%) | 328 сек |
| 5 | ContractCurrency +1 enum | Простая | success | 1 | 1/1 (100%) | 368 сек |
| 6 | ConstructionSection +5 полей | Средняя | failed | 0 | 1/2 (50%) | 256 сек |
| 7 | Experience +4 поля | Средняя | success | 1 | 2/3 (67%) | 444 сек |
| 8 | MediaLink +4 поля | Средняя | success | 1 | 1/3 (33%) | 675 сек |
| 9 | SpecialZone +5 полей | Средняя | success | 1 | 2/3 (67%) | 464 сек |
| 10 | CheckPoint +4 поля | Средняя | success | 1 | 1/3 (33%) | 517 сек |
| 11 | Notice +5 полей | Сложная | success | 1 | 2/3 (67%) | 484 сек |
| 12 | EscrowAccount +5 полей | Сложная | success | 1 | 1/3 (33%) | 431 сек |
| 13 | 10 сущностей +2 поля | Сложная | success | 1 | 6/10 (60%) | 753 сек |
| 14 | BankPolicy + BankPolicyItem | Сложная | failed | 0 | 0/3 (0%) | 485 сек |
| 15 | SalesData +5 полей | Сложная | success | 1 | 1/3 (33%) | 382 сек |

