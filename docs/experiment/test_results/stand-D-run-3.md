# Прогон: Конфигурация D, повторение 3

**Дата**: 2026-03-24 05:58
**Конфигурация**: D: Multi-agent + RAG(5)
**Настройки**: agent_mode=multi, use_rag=True, rag_top_k=5, use_graph=False
**Модель**: Claude Haiku 4.5

---

## Тест 1. Portfolio +2 поля (Простая)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 3f614d6d-1a7f-4391-8004-308c0df482a1 |
| Статус | failed |
| Pass@1 | 0 |
| Время | 198 сек |
| Build итераций | 0 |
| Completeness | 1/1 (100%) |
| Токены (total) | 28344 |

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
| Примеров загружено | 5 |
| Template | — |

### Валидация
| Проверка | Результат |
|----------|----------|
| API status | failed |
| F_actual.length > 0 | ✅ (1 файлов) |
| F_actual ∩ F_required > 0 | ✅ |
| Итоговый статус | **failed** |

### Анализ
Тест завершился с ошибкой: Pipeline halted: 3 subtasks failed with zero changes. Last: Verify DataContext OnModelCreating method

---

## Тест 2. OrganizationPerson +3 поля (Простая)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 63889bae-68d5-4ecf-8f28-de04f2656096 |
| Статус | success |
| Pass@1 | 1 |
| Время | 268 сек |
| Build итераций | 0 |
| Completeness | 1/1 (100%) |
| Токены (total) | 29320 |

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
| Примеров загружено | 5 |
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
| task_id | 507fa5fa-67a6-4567-881d-4cf245baec10 |
| Статус | success |
| Pass@1 | 1 |
| Время | 274 сек |
| Build итераций | 0 |
| Completeness | 1/1 (100%) |
| Токены (total) | 48726 |

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
| Примеров загружено | 5 |
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
| task_id | 9e7b7971-2b36-4bd0-b835-a1a41d892124 |
| Статус | success |
| Pass@1 | 1 |
| Время | 299 сек |
| Build итераций | 0 |
| Completeness | 1/1 (100%) |
| Токены (total) | 27611 |

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
| Примеров загружено | 5 |
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
| task_id | fec6294b-ce51-483c-b95c-503debb94820 |
| Статус | success |
| Pass@1 | 1 |
| Время | 348 сек |
| Build итераций | 0 |
| Completeness | 1/1 (100%) |
| Токены (total) | 30526 |

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
| Примеров загружено | 5 |
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
| task_id | 2367a38e-760d-47ed-9d05-de020ad421ca |
| Статус | success |
| Pass@1 | 1 |
| Время | 420 сек |
| Build итераций | 0 |
| Completeness | 1/2 (50%) |
| Токены (total) | 34020 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Configurations/DataConfiguration.cs, Data/Entities/ConstructionSection.cs |
| F_required | Data/Entities/ConstructionSection.cs, Data/DataConfiguration.cs |
| F_missing | — |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type | unknown (confidence: 0.9983) |
| Примеров загружено | 5 |
| Template | — |

### Валидация
| Проверка | Результат |
|----------|----------|
| API status | success |
| F_actual.length > 0 | ✅ (2 файлов) |
| F_actual ∩ F_required > 0 | ✅ |
| Итоговый статус | **success** |

### Анализ
Изменено 1/2 ожидаемых файлов (50%). Изменено всего файлов: 2

---

## Тест 7. Experience +4 поля (Средняя)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 7772a127-f874-4585-8608-3c343a12561b |
| Статус | failed |
| Pass@1 | 0 |
| Время | 783 сек |
| Build итераций | 0 |
| Completeness | 2/3 (67%) |
| Токены (total) | 46935 |

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
| Примеров загружено | 5 |
| Template | — |

### Валидация
| Проверка | Результат |
|----------|----------|
| API status | failed |
| F_actual.length > 0 | ✅ (3 файлов) |
| F_actual ∩ F_required > 0 | ✅ |
| Итоговый статус | **failed** |

### Анализ
Тест завершился с ошибкой: Build fix loop aborted: errors grew for 3 consecutive attempts (4 -> 4). Fix loop is making things worse.

---

## Тест 8. MediaLink +4 поля (Средняя)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 64cf5716-b4b5-44ad-b233-39ecc0740b68 |
| Статус | failed |
| Pass@1 | 0 |
| Время | 1075 сек |
| Build итераций | 0 |
| Completeness | 1/3 (33%) |
| Токены (total) | 62955 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Configurations/DataConfiguration.cs, Data/Entities/ConstructionSite.cs, Data/Entities/MediaLinkEntities/MediaLink.cs, Data/Initializer.cs |
| F_required | Data/Entities/MediaLink.cs, Data/DataConfiguration.cs, Data/Initializer.cs |
| F_missing | — |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type | unknown (confidence: 0.9983) |
| Примеров загружено | 5 |
| Template | — |

### Валидация
| Проверка | Результат |
|----------|----------|
| API status | failed |
| F_actual.length > 0 | ✅ (4 файлов) |
| F_actual ∩ F_required > 0 | ✅ |
| Итоговый статус | **failed** |

### Анализ
Тест завершился с ошибкой: Build failed after 5 attempts

---

## Тест 9. SpecialZone +5 полей (Средняя)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 33b8b94b-d99c-474a-b65a-b724480bf308 |
| Статус | success |
| Pass@1 | 1 |
| Время | 633 сек |
| Build итераций | 0 |
| Completeness | 1/3 (33%) |
| Токены (total) | 41423 |

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
| Примеров загружено | 5 |
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
| task_id | 6bde3ef7-7e0c-4ab0-a568-ca0dcc05072c |
| Статус | success |
| Pass@1 | 1 |
| Время | 519 сек |
| Build итераций | 0 |
| Completeness | 0/3 (0%) |
| Токены (total) | 38666 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/CheckLists/CheckPoint.cs |
| F_required | Data/Entities/CheckPoint.cs, Data/DataConfiguration.cs, Data/Initializer.cs |
| F_missing | Data/DataConfiguration.cs, Data/Initializer.cs |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type | unknown (confidence: 0.9983) |
| Примеров загружено | 5 |
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

## Тест 11. Notice +5 полей (Сложная)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 26291f07-2512-4a9a-b7e9-78278647c9ff |
| Статус | success |
| Pass@1 | 1 |
| Время | 542 сек |
| Build итераций | 0 |
| Completeness | 1/3 (33%) |
| Токены (total) | 45360 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Configurations/DataConfiguration.cs, Data/Entities/Notice.cs, Data/Entities/Tranche.cs |
| F_required | Data/Entities/Notice.cs, Data/DataConfiguration.cs, Data/Initializer.cs |
| F_missing | Data/Initializer.cs |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type | unknown (confidence: 0.9983) |
| Примеров загружено | 5 |
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

## Тест 12. EscrowAccount +5 полей (Сложная)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 6bed08a1-678f-40e1-8109-f912873fdd48 |
| Статус | false_success |
| Pass@1 | 0 |
| Время | 533 сек |
| Build итераций | 0 |
| Completeness | 0/3 (0%) |
| Токены (total) | 41130 |

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
| Примеров загружено | 5 |
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
| task_id | f5221c9e-5398-46d5-95eb-5a3ad8f12262 |
| Статус | success |
| Pass@1 | 1 |
| Время | 461 сек |
| Build итераций | 0 |
| Completeness | 6/10 (60%) |
| Токены (total) | 58944 |

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
| Примеров загружено | 5 |
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
| task_id | 182ec5af-37d3-4ab8-a1e0-79841f84232b |
| Статус | failed |
| Pass@1 | 0 |
| Время | 547 сек |
| Build итераций | 0 |
| Completeness | 0/3 (0%) |
| Токены (total) | 54781 |

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
| Примеров загружено | 5 |
| Template | — |

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
| task_id | 9814295b-6f99-4842-9779-2a92a9b8e731 |
| Статус | success |
| Pass@1 | 1 |
| Время | 702 сек |
| Build итераций | 0 |
| Completeness | 0/3 (0%) |
| Токены (total) | 58044 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Configurations/DataConfiguration.cs, Data/Entities/CheckLists/CheckListItem.cs, Data/Entities/CheckPoint.cs, Data/Entities/MediaLinkEntities/MediaLink.cs, Data/Entities/Notice.cs, Data/Entities/ProjectAnalog.cs, Data/Entities/SalesEntities/SalesData.cs, Data/Entities/TargetProgram.cs |
| F_required | Data/Entities/SalesData.cs, Data/DataConfiguration.cs, Data/Initializer.cs |
| F_missing | Data/Initializer.cs |

### RAG контекст
| Метрика | Значение |
|---------|----------|
| task_type | unknown (confidence: 0.9983) |
| Примеров загружено | 5 |
| Template | — |

### Валидация
| Проверка | Результат |
|----------|----------|
| API status | success |
| F_actual.length > 0 | ✅ (8 файлов) |
| F_actual ∩ F_required > 0 | ✅ |
| Итоговый статус | **success** |

### Анализ
Изменено 0/3 ожидаемых файлов (0%). Изменено всего файлов: 8

---


## Итоги прогона

| Метрика | Значение |
|---------|----------|
| Всего тестов | 15 |
| Pass@1 | 10/15 (67%) |
| False success | 1 |
| Failed | 4 |
| Timeout | 0 |
| Avg completeness | 51.7% |
| Avg time | 507 сек |
| Total time | 7602 сек (126.7 мин) |

### Сводная таблица

| # | Тест | Сложность | Статус | Pass@1 | Completeness | Время |
|---|------|-----------|--------|--------|--------------|-------|
| 1 | Portfolio +2 поля | Простая | failed | 0 | 1/1 (100%) | 198 сек |
| 2 | OrganizationPerson +3 поля | Простая | success | 1 | 1/1 (100%) | 268 сек |
| 3 | PhotoReportItem +2 поля | Простая | success | 1 | 1/1 (100%) | 274 сек |
| 4 | SubmittedDocumentsTemplate +2 поля | Простая | success | 1 | 1/1 (100%) | 299 сек |
| 5 | ContractCurrency +1 enum | Простая | success | 1 | 1/1 (100%) | 348 сек |
| 6 | ConstructionSection +5 полей | Средняя | success | 1 | 1/2 (50%) | 420 сек |
| 7 | Experience +4 поля | Средняя | failed | 0 | 2/3 (67%) | 783 сек |
| 8 | MediaLink +4 поля | Средняя | failed | 0 | 1/3 (33%) | 1075 сек |
| 9 | SpecialZone +5 полей | Средняя | success | 1 | 1/3 (33%) | 633 сек |
| 10 | CheckPoint +4 поля | Средняя | success | 1 | 0/3 (0%) | 519 сек |
| 11 | Notice +5 полей | Сложная | success | 1 | 1/3 (33%) | 542 сек |
| 12 | EscrowAccount +5 полей | Сложная | false_success | 0 | 0/3 (0%) | 533 сек |
| 13 | 10 сущностей +2 поля | Сложная | success | 1 | 6/10 (60%) | 461 сек |
| 14 | BankPolicy + BankPolicyItem | Сложная | failed | 0 | 0/3 (0%) | 547 сек |
| 15 | SalesData +5 полей | Сложная | success | 1 | 0/3 (0%) | 702 сек |

