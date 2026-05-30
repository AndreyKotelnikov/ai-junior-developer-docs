# Прогон: Конфигурация A, повторение 1

**Дата**: 2026-03-24 01:28
**Конфигурация**: A: Single-agent + RAG(3)
**Настройки**: agent_mode=single, use_rag=True, rag_top_k=3, use_graph=False
**Модель**: Claude Haiku 4.5

---

## Тест 1. Portfolio +2 поля (Простая)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | f03c1400-5b14-492d-973a-fb2139096a1c |
| Статус | failed |
| Pass@1 | 0 |
| Время | 330 сек |
| Build итераций | 0 |
| Completeness | 1/1 (100%) |
| Токены (total) | 18135 |

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
| task_id | d62ed654-af6c-4f0c-be94-cedd687490da |
| Статус | failed |
| Pass@1 | 0 |
| Время | 244 сек |
| Build итераций | 0 |
| Completeness | 1/1 (100%) |
| Токены (total) | 20424 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/OrganizationPerson.cs, Data/Filters/SubmittedDocumentsOrganizationPersonFilter.cs |
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
Тест завершился с ошибкой: Single-agent: build failed after 5 attempts

---

## Тест 3. PhotoReportItem +2 поля (Простая)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | f5d45fcc-a4ac-4436-9ea7-25a2797fde8e |
| Статус | failed |
| Pass@1 | 0 |
| Время | 231 сек |
| Build итераций | 0 |
| Completeness | 0/1 (0%) |
| Токены (total) | 17445 |

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
| task_id | e2d6b91b-0439-4b0b-a9f9-67dd99c48813 |
| Статус | failed |
| Pass@1 | 0 |
| Время | 244 сек |
| Build итераций | 0 |
| Completeness | 1/1 (100%) |
| Токены (total) | 20963 |

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
| task_id | 8dc990e3-c017-4d6c-a37e-9509608f4860 |
| Статус | false_success |
| Pass@1 | 0 |
| Время | 137 сек |
| Build итераций | 0 |
| Completeness | 0/1 (0%) |
| Токены (total) | 3470 |

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
| task_id | 0d89ccce-e63f-4b3a-9d40-c8a84d241e2d |
| Статус | failed |
| Pass@1 | 0 |
| Время | 245 сек |
| Build итераций | 0 |
| Completeness | 1/2 (50%) |
| Токены (total) | 22052 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/ConstructionSection.cs |
| F_required | Data/Entities/ConstructionSection.cs, Data/DataConfiguration.cs |
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
| F_actual.length > 0 | ✅ (1 файлов) |
| F_actual ∩ F_required > 0 | ✅ |
| Итоговый статус | **failed** |

### Анализ
Тест завершился с ошибкой: Single-agent: build failed after 5 attempts

---

## Тест 7. Experience +4 поля (Средняя)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | bc8980e5-794e-45be-bace-0881e25afd10 |
| Статус | success |
| Pass@1 | 1 |
| Время | 134 сек |
| Build итераций | 0 |
| Completeness | 0/3 (0%) |
| Токены (total) | 3690 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/Enums/DeveloperCategory.cs |
| F_required | Data/Entities/Experience.cs, Data/DataConfiguration.cs, Data/Initializer.cs |
| F_missing | Data/Entities/Experience.cs, Data/DataConfiguration.cs, Data/Initializer.cs |

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

## Тест 8. MediaLink +4 поля (Средняя)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | 3568325f-8a01-41e9-947c-1a16f3830a32 |
| Статус | false_success |
| Pass@1 | 0 |
| Время | 128 сек |
| Build итераций | 0 |
| Completeness | 0/3 (0%) |
| Токены (total) | 3456 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | — |
| F_required | Data/Entities/MediaLink.cs, Data/DataConfiguration.cs, Data/Initializer.cs |
| F_missing | Data/Entities/MediaLink.cs, Data/DataConfiguration.cs, Data/Initializer.cs |

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

## Тест 9. SpecialZone +5 полей (Средняя)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | d9cdd6e9-d005-4bfb-bb16-fadf55f05314 |
| Статус | failed |
| Pass@1 | 0 |
| Время | 217 сек |
| Build итераций | 0 |
| Completeness | 1/3 (33%) |
| Токены (total) | 20591 |

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
| task_id | 9e09f935-2604-4032-af1d-4603bce68210 |
| Статус | failed |
| Pass@1 | 0 |
| Время | 276 сек |
| Build итераций | 0 |
| Completeness | 1/3 (33%) |
| Токены (total) | 21835 |

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
| task_id | 23100807-161d-46bd-8add-a2c00c5e39dd |
| Статус | false_success |
| Pass@1 | 0 |
| Время | 146 сек |
| Build итераций | 0 |
| Completeness | 0/3 (0%) |
| Токены (total) | 3615 |

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
| task_id | ecffe508-f5a1-4be8-90e7-d5d7cb3b8a3d |
| Статус | failed |
| Pass@1 | 0 |
| Время | 208 сек |
| Build итераций | 0 |
| Completeness | 1/3 (33%) |
| Токены (total) | 19786 |

### Файлы
| Метрика | Значение |
|---------|----------|
| F_actual | Data/Entities/EscrowAccount.cs |
| F_required | Data/Entities/EscrowAccount.cs, Data/DataConfiguration.cs, Data/Initializer.cs |
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

## Тест 13. 10 сущностей +2 поля (Сложная)

### Основные метрики
| Метрика | Значение |
|---------|----------|
| task_id | a19462d3-4f38-4d0a-95f8-ee33fea96159 |
| Статус | false_success |
| Pass@1 | 0 |
| Время | 138 сек |
| Build итераций | 0 |
| Completeness | 0/10 (0%) |
| Токены (total) | 4236 |

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
| task_id | f7a67343-5ce3-4db3-a131-b32bc42dd907 |
| Статус | false_success |
| Pass@1 | 0 |
| Время | 124 сек |
| Build итераций | 0 |
| Completeness | 0/3 (0%) |
| Токены (total) | 4105 |

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
| task_id | b7f55cd6-3160-4920-baed-f05aee9170b6 |
| Статус | failed |
| Pass@1 | 0 |
| Время | 188 сек |
| Build итераций | 0 |
| Completeness | 1/3 (33%) |
| Токены (total) | 21066 |

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
| Pass@1 | 1/15 (7%) |
| False success | 5 |
| Failed | 9 |
| Timeout | 0 |
| Avg completeness | 32.2% |
| Avg time | 199 сек |
| Total time | 2990 сек (49.8 мин) |

### Сводная таблица

| # | Тест | Сложность | Статус | Pass@1 | Completeness | Время |
|---|------|-----------|--------|--------|--------------|-------|
| 1 | Portfolio +2 поля | Простая | failed | 0 | 1/1 (100%) | 330 сек |
| 2 | OrganizationPerson +3 поля | Простая | failed | 0 | 1/1 (100%) | 244 сек |
| 3 | PhotoReportItem +2 поля | Простая | failed | 0 | 0/1 (0%) | 231 сек |
| 4 | SubmittedDocumentsTemplate +2 поля | Простая | failed | 0 | 1/1 (100%) | 244 сек |
| 5 | ContractCurrency +1 enum | Простая | false_success | 0 | 0/1 (0%) | 137 сек |
| 6 | ConstructionSection +5 полей | Средняя | failed | 0 | 1/2 (50%) | 245 сек |
| 7 | Experience +4 поля | Средняя | success | 1 | 0/3 (0%) | 134 сек |
| 8 | MediaLink +4 поля | Средняя | false_success | 0 | 0/3 (0%) | 128 сек |
| 9 | SpecialZone +5 полей | Средняя | failed | 0 | 1/3 (33%) | 217 сек |
| 10 | CheckPoint +4 поля | Средняя | failed | 0 | 1/3 (33%) | 276 сек |
| 11 | Notice +5 полей | Сложная | false_success | 0 | 0/3 (0%) | 146 сек |
| 12 | EscrowAccount +5 полей | Сложная | failed | 0 | 1/3 (33%) | 208 сек |
| 13 | 10 сущностей +2 поля | Сложная | false_success | 0 | 0/10 (0%) | 138 сек |
| 14 | BankPolicy + BankPolicyItem | Сложная | false_success | 0 | 0/3 (0%) | 124 сек |
| 15 | SalesData +5 полей | Сложная | failed | 0 | 1/3 (33%) | 188 сек |

