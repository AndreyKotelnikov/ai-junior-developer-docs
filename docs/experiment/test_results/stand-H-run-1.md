# Прогон: Конфигурация H, повторение 1

**Дата**: 2026-03-25 23:32
**Конфигурация**: H: Multi-agent + граф + Ollama (без RAG)
**Настройки**: agent_mode=multi, use_rag=False, rag_top_k=0, use_graph=True
**Модель**: qwen2.5-coder:14b

---

## Тест 1. Portfolio +2 поля (Простая)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | da801138-e2e9-4005-8923-e857a5ad6737 |
| Статус | success |
| Pass@1 | 1 |
| Время | 326 сек |
| Build итераций | 0 |
| Completeness | 1/1 (100%) |
| Токены (total) | 11794 |

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
| task_id | 4f491d65-5b1b-4ccf-ba62-53251a1e3d1b |
| Статус | success |
| Pass@1 | 1 |
| Время | 492 сек |
| Build итераций | 0 |
| Completeness | 1/1 (100%) |
| Токены (total) | 18531 |

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
| task_id | 3c7e994f-c501-4378-ae61-2af3351eda56 |
| Статус | success |
| Pass@1 | 1 |
| Время | 394 сек |
| Build итераций | 0 |
| Completeness | 0/1 (0%) |
| Токены (total) | 12449 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/PhotoReportItem.cs |
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
Изменено 0/1 ожидаемых файлов (0%). Изменено всего файлов: 1

---

## Тест 4. SubmittedDocumentsTemplate +2 поля (Простая)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 89493be5-a770-4c2b-b87e-a61c96dff294 |
| Статус | success |
| Pass@1 | 1 |
| Время | 339 сек |
| Build итераций | 0 |
| Completeness | 1/1 (100%) |
| Токены (total) | 12574 |

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
| task_id | cd5e5dd4-6c10-4e78-af72-abb3ce09ef92 |
| Статус | success |
| Pass@1 | 1 |
| Время | 353 сек |
| Build итераций | 0 |
| Completeness | 1/1 (100%) |
| Токены (total) | 10970 |

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
| task_id | 4097c5cd-3c70-49fe-a76c-27692e5ba653 |
| Статус | failed |
| Pass@1 | 0 |
| Время | 675 сек |
| Build итераций | 0 |
| Completeness | 1/2 (50%) |
| Токены (total) | 20097 |

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
| API status | failed |
| F_actual.length > 0 | ✅ (1 файлов) |
| F_actual ∩ F_required > 0 | ✅ |
| Итоговый статус | **failed** |

### Анализ
Тест завершился с ошибкой: Build failed after 7 attempts

---

## Тест 7. Experience +4 поля (Средняя)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 033a50ff-81f6-490d-ac79-dd4e9d96d93e |
| Статус | success |
| Pass@1 | 1 |
| Время | 587 сек |
| Build итераций | 0 |
| Completeness | 1/3 (33%) |
| Токены (total) | 20448 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/Experience.cs |
| F_required | Data/Entities/Experience.cs, Data/DataConfiguration.cs, Data/Initializer.cs |
| F_missing | Data/DataConfiguration.cs, Data/Initializer.cs |

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
Изменено 1/3 ожидаемых файлов (33%). Изменено всего файлов: 1

---

## Тест 8. MediaLink +4 поля (Средняя)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 8428dfc8-ecfc-43b3-b3f7-344ae46295a7 |
| Статус | success |
| Pass@1 | 1 |
| Время | 604 сек |
| Build итераций | 0 |
| Completeness | 1/3 (33%) |
| Токены (total) | 22615 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/MediaLink.cs |
| F_required | Data/Entities/MediaLink.cs, Data/DataConfiguration.cs, Data/Initializer.cs |
| F_missing | Data/DataConfiguration.cs, Data/Initializer.cs |

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
Изменено 1/3 ожидаемых файлов (33%). Изменено всего файлов: 1

---

## Тест 9. SpecialZone +5 полей (Средняя)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 85a556c4-f658-45f3-b8df-3d0fc39ec8b7 |
| Статус | failed |
| Pass@1 | 0 |
| Время | 594 сек |
| Build итераций | 0 |
| Completeness | 1/3 (33%) |
| Токены (total) | 21692 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/SpecialZone.cs |
| F_required | Data/Entities/SpecialZone.cs, Data/DataConfiguration.cs, Data/Initializer.cs |
| F_missing | Data/DataConfiguration.cs, Data/Initializer.cs |

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
| F_actual.length > 0 | ✅ (1 файлов) |
| F_actual ∩ F_required > 0 | ✅ |
| Итоговый статус | **failed** |

### Анализ
Тест завершился с ошибкой: Build failed after 7 attempts

---

## Тест 10. CheckPoint +4 поля (Средняя)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | f2118925-67a3-40b8-9deb-399abb697bb9 |
| Статус | success |
| Pass@1 | 1 |
| Время | 575 сек |
| Build итераций | 0 |
| Completeness | 1/3 (33%) |
| Токены (total) | 21002 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/CheckPoint.cs |
| F_required | Data/Entities/CheckPoint.cs, Data/DataConfiguration.cs, Data/Initializer.cs |
| F_missing | Data/DataConfiguration.cs, Data/Initializer.cs |

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
Изменено 1/3 ожидаемых файлов (33%). Изменено всего файлов: 1

---

## Тест 11. Notice +5 полей (Сложная)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 170d9d80-5a67-4c7d-8961-e030937568f1 |
| Статус | success |
| Pass@1 | 1 |
| Время | 1003 сек |
| Build итераций | 0 |
| Completeness | 1/3 (33%) |
| Токены (total) | 31570 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/Notice.cs |
| F_required | Data/Entities/Notice.cs, Data/DataConfiguration.cs, Data/Initializer.cs |
| F_missing | Data/DataConfiguration.cs, Data/Initializer.cs |

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
Изменено 1/3 ожидаемых файлов (33%). Изменено всего файлов: 1

---

## Тест 12. EscrowAccount +5 полей (Сложная)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 1d05048e-32f3-4b77-bc88-3d1d4a8d5fba |
| Статус | success |
| Pass@1 | 1 |
| Время | 1033 сек |
| Build итераций | 0 |
| Completeness | 1/3 (33%) |
| Токены (total) | 29595 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/EscrowAccount.cs |
| F_required | Data/Entities/EscrowAccount.cs, Data/DataConfiguration.cs, Data/Initializer.cs |
| F_missing | Data/DataConfiguration.cs, Data/Initializer.cs |

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
Изменено 1/3 ожидаемых файлов (33%). Изменено всего файлов: 1

---

## Тест 13. 10 сущностей +2 поля (Сложная)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | fe36cd5f-9811-44a9-8663-78f474061022 |
| Статус | success |
| Pass@1 | 1 |
| Время | 571 сек |
| Build итераций | 0 |
| Completeness | 0/10 (0%) |
| Токены (total) | 17988 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | DataAccessLayer/Initializer.cs |
| F_required | Data/Entities/Discussion.cs, Data/Entities/BankPolicy.cs, Data/Entities/Notice.cs, Data/Entities/CheckPoint.cs, Data/Entities/MediaLink.cs, Data/Entities/ProjectAnalog.cs, Data/Entities/TargetProgram.cs, Data/Entities/CheckListItem.cs, Data/Entities/DiscussionProtocol.cs, Data/Entities/BankPolicyItem.cs |
| F_missing | Data/Entities/Discussion.cs, Data/Entities/BankPolicy.cs, Data/Entities/Notice.cs, Data/Entities/CheckPoint.cs, Data/Entities/MediaLink.cs, Data/Entities/ProjectAnalog.cs, Data/Entities/TargetProgram.cs, Data/Entities/CheckListItem.cs, Data/Entities/DiscussionProtocol.cs, Data/Entities/BankPolicyItem.cs |

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
| F_actual ∩ F_required > 0 | ❌ |
| Итоговый статус | **success** |

### Анализ
Изменено 0/10 ожидаемых файлов (0%). Изменено всего файлов: 1

---

## Тест 14. BankPolicy + BankPolicyItem (Сложная)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | aba3c061-7b76-4736-a3ab-108879fc1d27 |
| Статус | success |
| Pass@1 | 1 |
| Время | 574 сек |
| Build итераций | 0 |
| Completeness | 2/3 (67%) |
| Токены (total) | 29104 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/BankPolicy.cs, Data/Entities/BankPolicyItem.cs |
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
| task_id | e105c49e-8561-46cd-af1d-65f575c66963 |
| Статус | failed |
| Pass@1 | 0 |
| Время | 1849 сек |
| Build итераций | 0 |
| Completeness | 1/3 (33%) |
| Токены (total) | 31975 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Bindings/JournalEventsConfiguration.cs, Data/Entities/SalesData.cs |
| F_required | Data/Entities/SalesData.cs, Data/DataConfiguration.cs, Data/Initializer.cs |
| F_missing | Data/DataConfiguration.cs, Data/Initializer.cs |

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
Тест завершился с ошибкой: Build fix loop aborted: errors grew for 4 consecutive attempts (7 -> 9). Fix loop is making things worse.

---


## Итоги прогона

| Метрика | Значение |
|---------|----------|
| Всего тестов | 15 |
| Pass@1 | 12/15 (80%) |
| False success | 0 |
| Failed | 3 |
| Timeout | 0 |
| Avg completeness | 50.0% |
| Avg time | 665 сек |
| Total time | 9969 сек (166.2 мин) |

### Сводная таблица

| # | Тест | Сложность | Статус | Pass@1 | Completeness | Время |
|---|------|-----------|--------|--------|--------------|-------|
| 1 | Portfolio +2 поля | Простая | success | 1 | 1/1 (100%) | 326 сек |
| 2 | OrganizationPerson +3 поля | Простая | success | 1 | 1/1 (100%) | 492 сек |
| 3 | PhotoReportItem +2 поля | Простая | success | 1 | 0/1 (0%) | 394 сек |
| 4 | SubmittedDocumentsTemplate +2 поля | Простая | success | 1 | 1/1 (100%) | 339 сек |
| 5 | ContractCurrency +1 enum | Простая | success | 1 | 1/1 (100%) | 353 сек |
| 6 | ConstructionSection +5 полей | Средняя | failed | 0 | 1/2 (50%) | 675 сек |
| 7 | Experience +4 поля | Средняя | success | 1 | 1/3 (33%) | 587 сек |
| 8 | MediaLink +4 поля | Средняя | success | 1 | 1/3 (33%) | 604 сек |
| 9 | SpecialZone +5 полей | Средняя | failed | 0 | 1/3 (33%) | 594 сек |
| 10 | CheckPoint +4 поля | Средняя | success | 1 | 1/3 (33%) | 575 сек |
| 11 | Notice +5 полей | Сложная | success | 1 | 1/3 (33%) | 1003 сек |
| 12 | EscrowAccount +5 полей | Сложная | success | 1 | 1/3 (33%) | 1033 сек |
| 13 | 10 сущностей +2 поля | Сложная | success | 1 | 0/10 (0%) | 571 сек |
| 14 | BankPolicy + BankPolicyItem | Сложная | success | 1 | 2/3 (67%) | 574 сек |
| 15 | SalesData +5 полей | Сложная | failed | 0 | 1/3 (33%) | 1849 сек |

