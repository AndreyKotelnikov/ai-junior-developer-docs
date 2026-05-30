# Проверка теоретического потолка Completeness по 15 эталонам F_required

**Источник.** `docs/experiment/0.1_tests.md` — канонический документ с описанием 15 тестовых заданий и эталонных множеств файлов.

**Дата проверки.** 2026-05-23.

**Цель.** Установить, входят ли в эталонные множества F_required любых из 15 задач файлы, расположенные в NuGet-пакетах фреймворка Visary (физически недоступные системе на запись), и оценить теоретический потолок метрики Completeness на текущей тестовой базе.

---

## Сводная разбивка F_required по 15 задачам

| # | Сущность | |F_required| | Файлы | NuGet-side? |
|:-:|---|:-:|---|:-:|
| T01 | Portfolio | 1 | Data/Entities/Portfolio.cs | нет |
| T02 | OrganizationPerson | 1 | Data/Entities/OrganizationPerson.cs | нет |
| T03 | PhotoReportItem | 1 | Data/Entities/PhotoReport/PhotoReportItem.cs | нет |
| T04 | SubmittedDocumentsTemplate | 1 | Data/Entities/SubmittedDocumentsTemplate.cs | нет |
| T05 | ContractCurrency | 1 | Data/Entities/ContractCurrency.cs | нет |
| T06 | ConstructionSection | 2 | Entity + Data/Configurations/DataConfiguration.cs | нет |
| T07 | Experience | 3 | Entity + DataConfiguration + Data/Initializer.cs | нет |
| T08 | MediaLink | 3 | Entity + DataConfiguration + Initializer | нет |
| T09 | SpecialZone | 3 | Entity + DataConfiguration + Initializer | нет |
| T10 | CheckPoint | 3 | Entity + DataConfiguration + Initializer | нет |
| T11 | Notice | 3 | Entity + DataConfiguration + Initializer | нет |
| T12 | EscrowAccount | 3 | Entity + DataConfiguration + Initializer | нет |
| T13 | 10 сущностей (bulk) | 10 | 10 файлов в Data/Entities/ (Discussion, BankPolicy, Notice, CheckPoint, MediaLink, ProjectAnalog, TargetProgram, CheckListItem, DiscussionProtocol, BankPolicyItem) | нет |
| T14 | BankPolicy + BankPolicyItem | 3 | 2 Entity + DataConfiguration (Initializer не требуется: User — Visary-сущность) | нет |
| T15 | SalesData | 3 | Entity + DataConfiguration + Initializer | нет |

**Итого:** |F_required суммарно| = 1 + 1 + 1 + 1 + 1 + 2 + 3 + 3 + 3 + 3 + 3 + 3 + 10 + 3 + 3 = **41 файл**.

---

## Результат проверки

| Параметр | Значение |
|---|---|
| Всего файлов в эталонах 15 задач (|F_required суммарно|) | **41** |
| Из них доступны для модификации системой (`dotnet-app/src/`) | **41 (100 %)** |
| Из них в NuGet-пакетах фреймворка Visary (недоступны) | **0 (0 %)** |
| Доля недостижимых файлов (Z) | **0,0 %** |
| **Теоретический потолок Completeness на текущей тестовой базе** | **100 %** (= 100 − Z) |
| Фактический максимум Completeness (стенд G) | 62,44 % |
| Разрыв до теоретического потолка | 37,56 п.п. |

---

## Содержательный комментарий

1. **Все 41 файл F_required находятся в директории `dotnet-app/src/`** — все три типа артефактов модификации сущностей (`Data/Entities/*.cs`, `Data/Configurations/DataConfiguration.cs`, `Data/Initializer.cs`) — расположены в проекте `dotnet-app` и физически доступны системе на запись.

2. **Visary-фреймворк присутствует в эталонах только через `using`-директивы** (`using Visary.Abstractions;`, `using Visary.Core.DAL.Attributes;`, `using Visary.Security.Entities;` и т. п.) — это импорты атрибутов и базовых классов из NuGet-пакетов фреймворка. Сами файлы NuGet-пакетов в эталоны не входят и не модифицируются.

3. **FK к Visary-сущностям (User, Role) регистрируются только в DataConfiguration.cs**, без правок в самих NuGet-side файлах User.cs / Role.cs. Это явно зафиксировано в текстах задач T06, T08, T09, T14: «User — Visary-сущность, регистрация в Initializer не требуется».

4. **Эталоны построены по принципу «всё, что необходимо для бизнес-задачи, лежит в зоне доступа системы».** Это согласуется с архитектурным принципом разделения «корпоративный фреймворк Visary (NuGet, неизменяемый) vs прикладной код dotnet-app (модифицируемый)».

5. **Теоретический потолок Completeness = 100 % формально подтверждён.** Все 37,56 п.п. разрыва до потолка — техническая точка роста системы (преимущественно систематический пропуск регистраций в `DataConfiguration.cs`, см. § 6.2 файла `stats_report.md`), а не зашитое в постановке задачи архитектурное ограничение.

---

**Подпись.** Проверка проведена сплошным просмотром раздела «Файлы для изменения» в `docs/experiment/0.1_tests.md` для каждой из 15 задач. Все пути валидированы относительно структуры `dotnet-app/src/` (.NET Core 3.1, 1559 файлов, Apps.sln).

---

## Структура разрыва Completeness 100 % − 62,44 % = 37,56 п.п.

Фактический разрыв до теоретического потолка распределён неравномерно. Анализ 75 прогонов стенда G:

- **82,4 % пропусков** — файл `Data/DataConfiguration.cs` (отсутствие регистрации навигационных свойств после добавления FK).
- Остаток — единичные пропуски `Data/Initializer.cs` и самих файлов сущностей.

По сложности задач: на простых Completeness достигает 100 %; весь дефицит сосредоточен на средних и сложных многофайловых задачах. Это техническая, а не структурная точка роста.

### План закрытия разрыва

| Задача | Описание | Срок |
|:-:|---|:-:|
| **R3** | xUnit-сюита T01..T25 — функциональная валидация | ближайший спринт |
| **R7** | Расширение co-change-графа на runtime-зависимости (рёбра CALLS) | ближайший спринт |
| **R-задача оптимизации AST-трансформеров** | `DataConfiguration` / `Initializer` — закрытие 82,4 % пропусков | в составе плана улучшений |

**Ожидаемый уровень после закрытия R3 + R7:** по предварительным оценкам на пилотных .NET-проектах без внутреннего NuGet-фреймворка Visary Completeness достигал значений порядка 90 %; экстраполяция на целевое приложение после доработки трансформеров — 80–85 %.

### Согласованность с гипотезой H3

Провал KPI Completeness 85 % **не отменяет** научный результат H3: прирост Completeness от включения графа формально подтверждён (+10,56 п.п., mixed-effects *p* = 0,000643). Две величины измеряют разное: H3 — прирост от включения графа; KPI — абсолютный уровень полноты.
