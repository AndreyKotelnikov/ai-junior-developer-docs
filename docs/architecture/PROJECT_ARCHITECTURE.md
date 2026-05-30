# Project Architecture Guide (dotnet-app)

Этот документ описывает архитектуру .NET решения, структуру папок и ключевые точки, которые необходимо учитывать при доработке функционала. Он предназначен для агентов multiagent и разработчиков, чтобы изменения были согласованы во всей системе. Документ содержит реальные примеры из кода проекта.

---

## 1. Общее устройство решения

**Solution:** `Apps.sln`

**Основные проекты:**
- `WebApi` — HTTP API (REST/JSON), DI и интеграция MassTransit.
- `Data` — доменная модель, бизнес-логика, EF Core конфигурации, обработчики, импорты/экспорт.
- `Filtering` — фильтрация/сортировка и профили фильтров для UI.
- `XsltProcessor` — XSLT-процессинг, конвертация, шаблоны.

**Высокоуровневый поток:**
1. HTTP запрос → `WebApi` (контроллеры/DTO/Consumers).
2. Бизнес-логика → `Data/Services` (CRUD, расчеты, импорты, стратегии).
3. Доступ к данным → `Data/Entities` + `Data/Configurations/DataConfiguration.cs` + регистрация в `Data/Initializer.cs`.
4. Фильтрация/сортировка → `Filtering` + `Data/Filters`.

## Конвенции для агентов-разработчиков

### Добавление навигационного свойства (ПРАВИЛЬНО)

```csharp
// В сущности Data/Entities/ConstructionSiteAnalog.cs:
[DetailView, ListView]
public AnalogType AnalogType { get; set; }
public int? AnalogTypeID { get; set; }  // ← ВСЕГДА заглавные ID, не Id

// В Data/Configurations/DataConfiguration.cs:
.Entity<ConstructionSiteAnalog>(s => s
    .AssociatedEntity(f => f.AnalogType)   // ← только AssociatedEntity
    .AssociatedEntity(f => f.FloorCategory))
```

### Что НЕ делать

- Не создавать `AnalogTypeConfiguration.cs` — конфигурация только в `DataConfiguration.cs`.
- Не добавлять `DbSet<AnalogType>` в `DataContext.cs`, если сущность уже управляется через `BaseDataContext`.
- Не заменять базовый класс `BaseTitleObject` на `BaseObject` в существующих сущностях.
- Не изменять сигнатуры `OnSave` в существующих `CrudService` файлах.
- Не создавать новую сущность, если справочник уже есть в `Data/Entities/`.

## 2. Структура каталогов

```
dotnet-app/src/
├── Data/
│   ├── Entities/             # доменные сущности (POCO + атрибуты [DetailView]/[ListView])
│   ├── Configurations/       # DataConfiguration.cs — fluent-конфигурация EF
│   ├── Services/             # CRUD-сервисы, импорт/экспорт, расчёты
│   │   ├── CrudServices/
│   │   ├── EventBusHandlers/
│   │   └── Jobs/
│   ├── Filters/              # фильтры объектного уровня
│   ├── Models/               # DTO (внутренние)
│   └── Initializer.cs        # регистрация ассоциаций
├── WebApi/
│   ├── Controllers/          # HTTP endpoint'ы
│   └── DTO/                  # API-DTO для запросов/ответов
├── Filtering/                # библиотека фильтрации/сортировки
└── XsltProcessor/            # XSLT-конвертация
```

## 3. Жизненный цикл сущности

1. POCO в `Data/Entities/<EntityName>.cs` (наследует `BaseObject` или
   `BaseTitleObject`).
2. Fluent-конфигурация добавляется в `Data/Configurations/DataConfiguration.cs`
   через `.Entity<T>(...)`.
3. Регистрация ассоциаций в `Data/Initializer.cs`
   (`AddOneToManyAssociation` / `AddOneToOneAssociation` — см.
   `docs/technical/visary_framework_conventions_full.md`).
4. CRUD-сервис в `Data/Services/CrudServices/<EntityName>CrudService.cs`.
5. Контроллер в `WebApi/Controllers/<EntityName>Controller.cs` (если требуется
   публичный API).

## 4. Где смотреть в первую очередь при доработке

- Добавление поля в сущность — `Data/Entities/`, `Data/Configurations/`.
- Бизнес-правило при сохранении — соответствующий `CrudService`.
- Импорт/экспорт — `Data/Services/Jobs/`.
- Фильтрация в UI — `Data/Filters/` + `Filtering/`.

