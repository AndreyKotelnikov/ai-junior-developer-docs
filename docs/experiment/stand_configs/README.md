# Конфигурации стендов факторного эксперимента

**Назначение папки** — 9 Docker Compose-конфигураций стендов A–I факторного эксперимента системы **AI Junior Developer**. Каждый файл `docker-compose.stand-<id>.yml` задаёт воспроизводимое развёртывание одного стенда с явной фиксацией значений факторов (архитектура, RAG top_k, семантический граф, LLM-модель). Документ содержит сводную таблицу стендов, принципы отбора конфигураций, технический каркас и параметры инференса.

---

## 1. Технический каркас стендов

Каждый стенд запускается отдельным compose-файлом `docker-compose.stand-<id>.yml`. Сервисы общего каркаса:

| Сервис | Роль |
|---|---|
| `multiagent` | FastAPI с мультиагентным конвейером |
| `rag-service` | FastAPI + Qdrant — гибридный поиск примеров |
| `roslyn-graph` | .NET-микросервис статического семантического анализа C# |
| `qdrant` | векторное хранилище корпуса примеров |
| `postgres` | журнал `pipeline_audit` (audit-log с `REVOKE` на DML) |
| `ollama` | локальный LLM-движок; запускается **только на стендах F и H** |

## 2. Параметры инференса

- `temperature = 0` — на всех 9 стендах;
- параметр `seed` в текущей реализации **явно не фиксируется** — ограничение воспроизводимости (зафиксировано как задача R10 реестра перспективных задач).

## 3. Воспроизводимость

Воспроизводимость факторного прогона обеспечена двумя артефактами:

1. Git-репозиторий проекта с зафиксированным коммитом;
2. 9 Docker Compose-конфигураций этой папки с явной фиксацией значений факторов.

Эти артефакты позволяют любому эксперту развернуть систему в той же конфигурации и повторить факторный прогон 9 стендов × 5 повторов × 15 задач = **675 наблюдений**.

## 4. Соответствие файлов стендам

| Файл | Стенд | Architecture | RAG top_k | Graph | Модель |
|---|:-:|:-:|:-:|:-:|:-:|
| `docker-compose.stand-a.yml` | A | single | 3 | off | Claude Haiku 4.5 |
| `docker-compose.stand-b.yml` | B | multi | 0 | off | Claude Haiku 4.5 |
| `docker-compose.stand-c.yml` | C | multi | 3 | off | Claude Haiku 4.5 |
| `docker-compose.stand-d.yml` | D | multi | 5 | off | Claude Haiku 4.5 |
| `docker-compose.stand-e.yml` | E | multi | 5 | on | Claude Haiku 4.5 |
| `docker-compose.stand-f.yml` | F | multi | 3 | off | Ollama `qwen2.5-coder:14b` |
| `docker-compose.stand-g.yml` | G | multi | 0 | on | Claude Haiku 4.5 |
| `docker-compose.stand-h.yml` | H | multi | 0 | on | Ollama `qwen2.5-coder:14b` |
| `docker-compose.stand-i.yml` | I | multi | 3 | on | Claude Haiku 4.5 |
