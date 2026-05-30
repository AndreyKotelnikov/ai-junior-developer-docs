# Прогон: Конфигурация I, повторение 4

**Дата**: 2026-03-25 19:17
**Конфигурация**: I: Multi-agent + RAG(3) + граф
**Настройки**: agent_mode=multi, use_rag=True, rag_top_k=3, use_graph=True
**Модель**: Claude Haiku 4.5

---

## Тест 1. Portfolio +2 поля (Простая)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 0976e567-aa05-4ca9-b075-4206d654e848 |
| Статус | success |
| Pass@1 | 1 |
| Время | 339 сек |
| Build итераций | 0 |
| Completeness | 1/1 (100%) |
| Токены (total) | 43637 |

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
| task_id | 80eca963-f3d0-4185-ba1b-69e92d796e6b |
| Статус | failed |
| Pass@1 | 0 |
| Время | 554 сек |
| Build итераций | 0 |
| Completeness | 1/1 (100%) |
| Токены (total) | 59058 |

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
| task_id | 4f6c435a-b6e1-4744-bb16-0b0ae2d75119 |
| Статус | success |
| Pass@1 | 1 |
| Время | 221 сек |
| Build итераций | 0 |
| Completeness | 1/1 (100%) |
| Токены (total) | 49023 |

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
| task_id | 2ccfd538-95a9-461b-b80d-676483a29688 |
| Статус | success |
| Pass@1 | 1 |
| Время | 350 сек |
| Build итераций | 0 |
| Completeness | 1/1 (100%) |
| Токены (total) | 47391 |

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
| task_id | a4b735b9-9ef5-4747-883e-d3c8315ecc7a |
| Статус | success |
| Pass@1 | 1 |
| Время | 330 сек |
| Build итераций | 0 |
| Completeness | 1/1 (100%) |
| Токены (total) | 46137 |

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
| task_id | 9a132b05-3d65-4b53-b3c3-44a96e7df765 |
| Статус | success |
| Pass@1 | 1 |
| Время | 610 сек |
| Build итераций | 0 |
| Completeness | 1/2 (50%) |
| Токены (total) | 64419 |

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
| task_id | 1b982c67-c472-469f-8f29-a5cb9b3e8c1b |
| Статус | success |
| Pass@1 | 1 |
| Время | 460 сек |
| Build итераций | 0 |
| Completeness | 2/3 (67%) |
| Токены (total) | 64121 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/Experience.cs, Data/Initializer.cs |
| F_required | Data/Entities/Experience.cs, Data/DataConfiguration.cs, Data/Initializer.cs |
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

## Тест 8. MediaLink +4 поля (Средняя)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 8b4a615d-70ac-4b88-88eb-ae25f52d2fd6 |
| Статус | success |
| Pass@1 | 1 |
| Время | 531 сек |
| Build итераций | 0 |
| Completeness | 1/3 (33%) |
| Токены (total) | 69548 |

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
| task_id | 0cb631f0-5301-4665-9640-91bc969ee1bd |
| Статус | success |
| Pass@1 | 1 |
| Время | 577 сек |
| Build итераций | 0 |
| Completeness | 2/3 (67%) |
| Токены (total) | 59522 |

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
| Примеров загружено | 3 |
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
| task_id | 6633b69f-b033-4a3a-8707-6f7c57efe55c |
| Статус | success |
| Pass@1 | 1 |
| Время | 617 сек |
| Build итераций | 0 |
| Completeness | 1/3 (33%) |
| Токены (total) | 66948 |

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
| Примеров загружено | 3 |
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
| task_id | fc49e2d4-3d2a-4c42-b5f2-69c9eb527db4 |
| Статус | success |
| Pass@1 | 1 |
| Время | 560 сек |
| Build итераций | 0 |
| Completeness | 2/3 (67%) |
| Токены (total) | 89887 |

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
| task_id | 56e9e2ce-4359-469d-85f4-c50c432e55f2 |
| Статус | success |
| Pass@1 | 1 |
| Время | 607 сек |
| Build итераций | 0 |
| Completeness | 1/3 (33%) |
| Токены (total) | 65467 |

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
| Примеров загружено | 3 |
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
| task_id | c40d9e01-1c5c-45db-afd4-fbb158d88ad8 |
| Статус | success |
| Pass@1 | 1 |
| Время | 798 сек |
| Build итераций | 0 |
| Completeness | 6/10 (60%) |
| Токены (total) | 169010 |

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
| task_id | d434ffde-db59-4dab-8212-281923b4e121 |
| Статус | success |
| Pass@1 | 1 |
| Время | 821 сек |
| Build итераций | 0 |
| Completeness | 0/3 (0%) |
| Токены (total) | 98175 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Configurations/DataConfiguration.cs, Data/Entities/BankPolicy/BankPolicy.cs, Data/Entities/BankPolicy/BankPolicyItem.cs |
| F_required | Data/Entities/BankPolicy.cs, Data/Entities/BankPolicyItem.cs, Data/DataConfiguration.cs |
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
| task_id | e215b808-1e33-4600-bff8-eb136fae5f33 |
| Статус | success |
| Pass@1 | 1 |
| Время | 787 сек |
| Build итераций | 0 |
| Completeness | 1/3 (33%) |
| Токены (total) | 152968 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/SalesEntities/SalesData.cs, Data/Initializer.cs |
| F_required | Data/Entities/SalesData.cs, Data/DataConfiguration.cs, Data/Initializer.cs |
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


## Итоги прогона

| Метрика | Значение |
|---------|----------|
| Всего тестов | 15 |
| Pass@1 | 14/15 (93%) |
| False success | 0 |
| Failed | 1 |
| Timeout | 0 |
| Avg completeness | 62.9% |
| Avg time | 544 сек |
| Total time | 8162 сек (136.0 мин) |

### Сводная таблица

| # | Тест | Сложность | Статус | Pass@1 | Completeness | Время |
|---|------|-----------|--------|--------|--------------|-------|
| 1 | Portfolio +2 поля | Простая | success | 1 | 1/1 (100%) | 339 сек |
| 2 | OrganizationPerson +3 поля | Простая | failed | 0 | 1/1 (100%) | 554 сек |
| 3 | PhotoReportItem +2 поля | Простая | success | 1 | 1/1 (100%) | 221 сек |
| 4 | SubmittedDocumentsTemplate +2 поля | Простая | success | 1 | 1/1 (100%) | 350 сек |
| 5 | ContractCurrency +1 enum | Простая | success | 1 | 1/1 (100%) | 330 сек |
| 6 | ConstructionSection +5 полей | Средняя | success | 1 | 1/2 (50%) | 610 сек |
| 7 | Experience +4 поля | Средняя | success | 1 | 2/3 (67%) | 460 сек |
| 8 | MediaLink +4 поля | Средняя | success | 1 | 1/3 (33%) | 531 сек |
| 9 | SpecialZone +5 полей | Средняя | success | 1 | 2/3 (67%) | 577 сек |
| 10 | CheckPoint +4 поля | Средняя | success | 1 | 1/3 (33%) | 617 сек |
| 11 | Notice +5 полей | Сложная | success | 1 | 2/3 (67%) | 560 сек |
| 12 | EscrowAccount +5 полей | Сложная | success | 1 | 1/3 (33%) | 607 сек |
| 13 | 10 сущностей +2 поля | Сложная | success | 1 | 6/10 (60%) | 798 сек |
| 14 | BankPolicy + BankPolicyItem | Сложная | success | 1 | 0/3 (0%) | 821 сек |
| 15 | SalesData +5 полей | Сложная | success | 1 | 1/3 (33%) | 787 сек |

