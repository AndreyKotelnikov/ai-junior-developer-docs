# ADR-001. Roslyn-инкрементальная валидация в fix-loop

**Status**: Accepted

---

## Контекст

В baseline-системе (до плана 0.13) после правок Coder-агента
pipeline запускал `dotnet build` для проверки корректности —
**~60 секунд на итерацию**. Если fix-loop делал 3–5 итераций
(типичный сценарий для modify_entity-задачи), общее время
задачи легко превышало 10 минут.

Это:
- ломало UX (разработчик не мог ждать 10 минут);
- приводило к timeout'ам в Streamlit UI;
- делало невозможным запуск на CI;
- блокировало интеграцию системы в обычный рабочий день.

**Источник**: результаты пилотного применения системы.

---

## Решение

Использовать **Roslyn semantic-валидацию** через
долгоживущий `MSBuildWorkspace` для **первичной** валидации в
fix-loop. Полный `dotnet build` оставить только как:
- финальная проверка после успешной Roslyn-валидации;
- fallback при недоступности Roslyn graph;
- в случаях, когда Roslyn не покрывает (cross-project ошибки
  линковки).

**Реализация**:
- `roslyn-graph/Analysis/SemanticDiagnosticsAnalyzer.cs` (~275 строк):
  долгоживущий `MSBuildWorkspace`, фильтр noise (`CS0518/CS0012/
  CS0656/CS1705`), per-document baseline.
- HTTP endpoint `POST /api/diagnostics/semantic`.
- `multiagent/app/tools/roslyn_graph_client.py.validate_files(...)`.
- `multiagent/app/pipeline/executor.py._roslyn_validate_changed`.

---

## Альтернативы

1. **Оставить full `dotnet build`** — отвергнуто (не решает
   проблему пилота P-03).
2. **`dotnet build --incremental`** — отвергнуто (incremental
   build всё равно тратит ~30+ секунд на типовое изменение,
   плюс не даёт structured diagnostics).
3. **Custom компиляторный pipeline без MSBuild** — отвергнуто
   (хрупкость, дублирование функциональности Roslyn).
4. **Pre-build `Solution` загрузка с heated cache** — отвергнуто
   (не сильно лучше Roslyn semantic).

---

## Последствия

### Плюсы
- Среднее время одной итерации fix-loop: **≈ 60 сек → 8.88 сек**.
- Полных `dotnet build` за задачу: **1–3 → 1**.
- Открыт путь к CI-интеграции.

### Минусы
- Дополнительный сервис (`roslyn-graph`) теперь критичен —
  graceful degradation на full build при `RoslynGraphUnavailable`.
- MSBuildLocator race-condition на первом старте (известное
  ограничение компонента `roslyn-graph`).

### Технический долг
- Нет.

---

## Связанные документы

- [`../detailed-architecture.md`](../detailed-architecture.md) — колонка 5 (Roslyn-граф и .NET-приложение).
- [`ADR-005-roslyn-only-explorer.md`](ADR-005-roslyn-only-explorer.md) — Roslyn-only Explorer.
