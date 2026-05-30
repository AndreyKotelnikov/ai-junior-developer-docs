# Расширенная Research Gap Matrix: 30+ систем AI-кодогенерации по 7 структурным характеристикам

## 1. Назначение

Полная (расширенная) версия позиционной матрицы (Research Gap Matrix). Документ раскрывает матрицу из **45 сравниваемых систем** (плюс целевая система — итого 46 строк) по 7 структурным характеристикам с детальными комментариями к каждой ячейке и ссылками на первоисточник (peer-reviewed публикация, whitepaper, официальная документация или верифицированный пресс-релиз).

Назначение: дать независимым рецензентам возможность проверить корректность каждой ячейки матрицы (✅ / ⚠️ / ❌ / «—»). Документ служит формальным обоснованием уникальности ниши AI Junior Developer.

## 2. Связанные документы

- `docs/competitors/GigaCode_Enterprise_on_premise.md` — детальное сопоставление с ближайшим российским конкурентом.
- `docs/competitors/gigacode_vs_aijd_full.md` — развёрнутое позиционирование AIJD vs GigaCode по 12 осям.

## 3. Легенда условных обозначений

- **✅** — компонент **явно реализован** и подтверждён первоисточником (peer-reviewed публикация, whitepaper, официальная документация или верифицированный пресс-релиз).
- **⚠️** — компонент **частично реализован, спорен или подтверждён только косвенно** (маркетинговая копия без техдокументации, beta-фича, поддержка через сторонний LSP, OSS research code без production-grade зрелости).
- **❌** — компонент **отсутствует** или явно не поддерживается (для коммерческих продуктов отсутствие подтверждается официальной документацией, например «we don't offer on-premises deployment today» — Cursor Security).
- **«—»** — **неприменимо** (например, столбец Multi-agent для бенчмарка).
- **«по данным разработчика»** — обязательная пометка для коммерческих систем без независимого peer-review (GigaCode, Kodify, KodaCode, T-Bank AI Agent, Devin, Cursor, Windsurf, Augment, Trae и др.).

## 4. Семь структурных характеристик матрицы

| Признак | Что означает ✅ |
|---|---|
| **Multi-agent (M-A)** | Архитектура ≥ 2 LLM-агентов с разделёнными ролями (planner / coder / tester / explorer и т. п.); координация через workflow / DAG / state machine |
| **RAG** | Retrieval-augmented generation: проектный контекст подаётся через retrieval-индекс (BM25, embeddings, RRF и т. п.), не только через окно контекста модели |
| **Граф** | Compiler-level или AST-граф зависимостей кода (CALLS, INHERITS, USES_TYPE и т. п.); графовые соседи подаются как контекст агента |
| **.NET** | Специализация на стеке ASP.NET Core / EF Core (а не общеязыковая поддержка C# в списке из 35+ языков) |
| **Русский (RU)** | Понимание русскоязычных требований из NL-описаний задач; русскоязычная документация |
| **On-premise** | Production-grade on-prem развёртывание (а не OSS research code, который теоретически можно развернуть, но без enterprise-зрелости) |
| **Enterprise** | Подтверждённое промышленное использование (Fortune 500, банки, госструктуры) с публично доступными метриками adoption |

---

## 5. Расширенная матрица 45 сравниваемых систем × 7 признаков

### 5.1. Мультиагентные системы (peer-reviewed + arXiv)

| # | Система | Venue / arXiv | M-A | RAG | Граф | .NET | RU | On-prem | Enterprise |
|:-:|---|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 1 | **MetaGPT** | ICLR 2024 oral; arXiv:2308.00352 | ✅ (5 ролей: PM / Architect / PM / Engineer / QA) | ⚠️ (v0.8+) | ❌ | ❌ | ❌ | ⚠️ (OSS research code) | ❌ |
| 2 | **ChatDev** | ACL 2024; arXiv:2307.07924 | ✅ (waterfall: CEO / CTO / programmer / reviewer / tester) | ❌ | ❌ | ❌ | ❌ | ⚠️ (OSS) | ❌ |
| 3 | **MapCoder** | ACL 2024; arXiv:2405.11403 | ✅ (4 агента: Retrieval / Planning / Coding / Debugging) | ❌ | ❌ | ❌ | ❌ | ⚠️ (OSS) | ❌ |
| 4 | **AgentCoder** | arXiv:2312.13010 (v3, May 2024) | ✅ (programmer / test designer / test executor) | ❌ | ❌ | ❌ | ❌ | ⚠️ (OSS) | ❌ |
| 5 | **AgileCoder** | arXiv:2406.11912 (2024) | ✅ (PM / Developer / Tester) | ❌ | ✅ Dynamic Code Graph Generator → Code Dependency Graph | ❌ | ❌ | ⚠️ (OSS, FSoft-AI4Code) | ❌ |
| 6 | **CodeCoR** | arXiv:2501.07811 (Jan 2025) | ✅ (4 агента: prompt / coding / test / repair) | ❌ | ❌ | ❌ | ❌ | ⚠️ (research code) | ❌ |
| 7 | **AdaCoder** | arXiv:2504.04220 | ✅ (4 агента) | ❌ | ❌ | ❌ | ❌ | ⚠️ (OSS) | ❌ |
| 8 | **Self-Organized Agents (SoA)** | arXiv:2404.02183 | ✅ (mother / child; dynamic multiplication) | ❌ | ❌ | ❌ | ❌ | ⚠️ (OSS) | ❌ |
| 9 | **AutoGen v0.4** (Microsoft) | MS Research blog, Jan 2025 | ✅ (AgentChat, GroupChat) | ⚠️ (user code) | ❌ | ⚠️ (Python + .NET interop) | ❌ | ✅ (OSS, Apache 2.0) | ✅ (преемник — Microsoft Agent Framework) |
| 10 | **HyperAgent** | arXiv:2409.16299 | ✅ (Planner / Navigator / Code Editor / Executor) | ✅ (Navigator: go-to-def + search) | ❌ | ❌ | ❌ | ⚠️ (OSS) | ❌ |

### 5.2. Repository-level / SWE-bench агенты

| # | Система | Venue / arXiv | M-A | RAG | Граф | .NET | RU | On-prem | Enterprise |
|:-:|---|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 11 | **AutoCodeRover** | ISSTA 2024; arXiv:2404.05427 | ⚠️ (LLM + tool loop) | ✅ (iterative code search по AST) | ✅ (AST: класс / метод) | ❌ | ❌ | ⚠️ (OSS) | ⚠️ (Sonar Foundation Agent fork) |
| 12 | **RepairAgent** | ICSE 2025; arXiv:2403.17134 | ❌ (single LLM + FSM) | ✅ (repair tools) | ❌ | ❌ | ❌ | ⚠️ (OSS, sola-st/RepairAgent) | ❌ |
| 13 | **MarsCode Agent** (ByteDance) | arXiv:2409.00899 | ✅ (Reproducer / Localizer / Editor) | ✅ | ✅ «code knowledge graph» + graph reasoning | ❌ | ❌ | ❌ (cloud SaaS) | ✅ |
| 14 | **CodeR** | arXiv:2406.01304 | ✅ (multi-agent w/ task graphs) | ✅ (BM25 + coverage) | ⚠️ task graphs — это план / workflow, не code AST | ❌ | ❌ | ⚠️ (research code) | ❌ |
| 15 | **OpenHands** | ICLR 2025; arXiv:2407.16741 | ⚠️ (платформа multi-agent; базовый CodeAct — single) | ✅ | ❌ | ❌ | ❌ | ✅ (MIT) | ⚠️ (All-Hands.ai) |
| 16 | **Devin / Devin 2.0** (Cognition) | cognition.ai/blog/devin-2 (2024–2025) | ⚠️ (в 2025 Cognition признала «narrower multi-agent») | ✅ (Devin Search / Wiki) | ❌ | ❌ | ❌ | ❌ (cloud SaaS) | ✅ (Goldman Sachs пилот, CIO M. Argenti, CNBC 11.07.2025; Mercedes-Benz: 200 000 строк COBOL за 8 дней) |
| 17 | **SWE-Agent** | NeurIPS 2024; arXiv:2405.15793 | ❌ (single + ACI) | ⚠️ (file tools) | ❌ | ❌ | ❌ | ⚠️ (OSS) | ❌ |
| 18 | **Cursor / Cursor Composer 2.0** (Anysphere) | cursor.com/blog/composer (Oct 2025); cursor.com/security | ⚠️ (subagents parallel) | ✅ (Merkle-tree + embeddings) | ❌ | ⚠️ (через VS Code LSP) | ❌ | ❌ (cursor.com/security: «we don't offer on-premises deployment today») | ✅ (Fortune 22.04.2026: «67 % of Fortune 500 companies use the firm's technology») |
| 19 | **Live-SWE-agent** | arXiv:2511.13646 (Nov 2025) | ❌ (single, self-evolving) | ❌ (bash only) | ❌ | ❌ | ❌ | ⚠️ (research OSS) | ❌ |
| 20 | **Augment Agent** | augmentcode.com | ⚠️ (Agent + parallel tools) | ✅ (Context Engine) | ❌ | ❌ | ❌ | ⚠️ (cloud + GHES connector) | ✅ (ISO/IEC 42001, SOC 2) |
| 21 | **Trae** (ByteDance) | trae.ai; github.com/bytedance/trae-agent | ⚠️ (Builder Mode + Trae-Agent OSS) | ✅ | ❌ | ❌ | ❌ (EN + Chinese) | ❌ | ⚠️ |

### 5.3. Граф-аугментированные системы

| # | Система | Venue / arXiv | M-A | RAG | Граф | .NET | RU | On-prem | Enterprise |
|:-:|---|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 22 | **GraphCoder** | ASE 2024 | ❌ | ✅ | ✅ Code Context Graph (CCG) | ❌ | ❌ | ⚠️ (OSS) | ❌ |
| 23 | **RepoGraph** | ICLR 2025; arXiv:2410.14684 | ⚠️ (plug-in для агентов) | ✅ | ✅ repo-level structure graph | ❌ | ❌ | ⚠️ (OSS) | ❌ |
| 24 | **CodexGraph** | arXiv:2408.03910 (preprint, peer-review не подтверждён) | ⚠️ (LLM + graph DB tool) | ✅ | ✅ узлы MODULE / CLASS / FUNCTION; рёбра CONTAINS / INHERITS / USES | ❌ | ❌ | ⚠️ (OSS, modelscope-agent) | ⚠️ |
| 25 | **CGM (Code Graph Model)** | NeurIPS 2025 poster; arXiv:2505.16901 | ❌ | ✅ | ✅ | ❌ | ❌ | ⚠️ | ❌ |
| 26 | **RANGER** | arXiv:2509.25257 | ⚠️ (retrieval agent + MCTS) | ✅ (graph-enhanced) | ✅ repo KG + Cypher + MCTS | ❌ | ❌ | ⚠️ (research) | ❌ |
| 27 | **CoSIL** | arXiv:2503.22424; ASE 2025 | ❌ (single LLM loop) | ⚠️ (LLM-driven search) | ✅ call graph + module call graph (динамически) | ❌ | ❌ | ⚠️ (OSS) | ❌ |
| 28 | **CoCoMIC** | LREC-COLING 2024; arXiv:2212.10007 (Amazon Science) | ❌ | ✅ | ✅ project context graph via CCFinder (static) | ❌ | ❌ | ⚠️ (OSS, amazon-science/cocomic) | ❌ |

### 5.4. Антиагентные / процедурные

| # | Система | Venue / arXiv | M-A | RAG | Граф | .NET | RU | On-prem | Enterprise |
|:-:|---|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 29 | **Agentless** | arXiv:2407.01489 (Xia et al.; **preprint, не ICML 2024** — peer-review не подтверждён в dblp/arXiv) | ❌ (3-фазный процесс localize → repair → validate) | ✅ | ❌ | ❌ | ❌ | ⚠️ (OSS) | ❌ |
| 30 | **Aider** | OSS, Aider-AI/aider; без peer-review | ❌ (single LLM) | ✅ (repo map, tree-sitter) | ⚠️ (repo map ≠ полный код-граф) | ⚠️ | ❌ | ✅ (CLI, локальные модели через LiteLLM) | ❌ |

### 5.5. RAG-системы для кода

| # | Система | Venue / arXiv | M-A | RAG | Граф | .NET | RU | On-prem | Enterprise |
|:-:|---|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 31 | **RepoCoder** | EMNLP 2023; arXiv:2303.12570 | ❌ | ✅ | ❌ | ❌ | ❌ | ⚠️ (OSS) | ❌ |
| 32 | **HyDE** (Hypothetical Document Embeddings) | ACL/EACL 2023; arXiv:2212.10496 | ❌ | ✅ | ❌ | ❌ | ⚠️ (multilingual, не RU-первый) | ⚠️ (OSS) | ❌ |
| 33 | **Coming** (Martinez & Monperrus) | tool paper | ❌ | ❌ | ⚠️ co-change edge mining (без LLM-интеграции) | ❌ | ❌ | ⚠️ (OSS) | ❌ |

### 5.6. Промышленные IDE-co-pilot

| # | Система | Источник | M-A | RAG | Граф | .NET | RU | On-prem | Enterprise |
|:-:|---|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 34 | **GitHub Copilot** (классический) | docs.github.com | ❌ | ⚠️ (Copilot Spaces) | ❌ | ✅ (deep VS integration) | ❌ | ❌ — docs.github.com: «Copilot is not currently available for GitHub Enterprise Server» | ✅ (Copilot Business / Enterprise) |
| 35 | **GitHub Copilot Coding Agent (CCA)** | github.blog | ⚠️ (агент в issues) | ✅ | ❌ | ✅ | ❌ | ❌ | ✅ |
| 36 | **Continue.dev** | continue.dev (Apache 2.0); github.com/continuedev/continue | ⚠️ (Agent mode + checks) | ✅ | ❌ | ⚠️ | ❌ | ✅ (OSS + локальные модели) | ⚠️ (Continue Hub) |
| 37 | **Tabby (TabbyML)** | tabbyml.com | ❌ | ✅ (Context Providers; RAG completion с v0.3) | ❌ | ⚠️ (multi-language) | ❌ | ✅ (self-hosted, Apache 2.0, on-prem Copilot alternative) | ✅ (SSO, team management) |
| 38 | **Codeium / Windsurf Enterprise** | windsurf.com/enterprise | ⚠️ (Cascade + sub-agents) | ✅ | ⚠️ (knowledge graphs в маркетинге, без whitepaper) | ⚠️ (70+ языков, не специализация) | ❌ | ✅ (fully self-hosted / air-gapped; FedRAMP High, DoD IL5/IL6/ITAR) | ✅ (cognition.ai/blog/windsurf, июль 2025: «$82M ARR; 350+ enterprise customers; hundreds of thousands of DAU») |
| 39 | **Amazon Q Developer** | aws.amazon.com/q/developer | ⚠️ (transform agents .NET, Java) | ✅ | ❌ | ✅ (Q Developer Transform: .NET Framework → cross-platform .NET 8) | ❌ | ❌ (cloud AWS) | ✅ (Q Developer Pro) |

### 5.7. Российские системы

| # | Система | Источник | M-A | RAG | Граф | .NET | RU | On-prem | Enterprise |
|:-:|---|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 40 | **GigaCode** (СберТех) | platformv.sbertech.ru; kod.ru (GigaConf 2024) | ⚠️ (Agent Mode с ноября 2025) | ✅ | ❌ | ⚠️ (C# в общем списке, без специализации) | ✅ | ✅ | ✅ (А. Белевцев, GigaConf 2024: «более 45 тыс. установок плагина на GitVerse и около 25 тыс. активных пользователей в месяц»; реестр росПО) |
| 41 | **KodaCode** (ООО «КОДА», ex-СберТех команда) | kodacode.ru; habr.com/companies/koda; CNews | ⚠️ (агентский режим + CLI) | ✅ (KodaRetrieval) | ❌ | ⚠️ (C# в списке) | ✅ («отлично понимает русский язык») | ⚠️ (on-prem для B2B; основной режим — cloud) | ⚠️ (Habr 02.03.2026: «10 000+ активных пользователей; ~4 млрд токенов в день») |
| 42 | **Kodify** (MWS AI / MTS AI, 2024) | mts.ai; forbes.ru/tekhnologii/514918 | ❌ | ⚠️ | ❌ | ❌ (Python + Java официально) | ✅ | ✅ (главное преимущество) | ✅ (внутри МТС с 2024) |
| 43 | **Kodify 2** (MWS AI, 2025) | mts.ai/product/kodify; habr.com/mts_ai | ❌ | ✅ | ❌ | ⚠️ (90 языков, включая C#) | ✅ | ✅ | ✅ (внешним заказчикам, OpenAI-совместимый API) |
| 44 | **Kodify Nano** (MWS AI OSS, 2025) | cnews.ru/2025-06-11 | ❌ | ⚠️ | ❌ | ⚠️ (Qwen2.5-Coder, 90 языков, C#) | ✅ | ✅ (1 ГБ RAM квант) | ⚠️ (free OSS) |
| 45 | **T-Bank AI Agent** (Т-Технологии) | forbes.ru/tekhnologii/545720 | ⚠️ (агентский режим на одном Qwen3-Coder-480B; multi-agent не подтверждено) | ⚠️ (262K контекст ≠ retrieval-индекс) | ❌ | ⚠️ | ✅ (русскоязычные бенчмарки приоритет) | ❌ (B2B-коробка анонсирована, on-prem не подтверждён) | ✅ (Forbes: «80 % инженеров — более 10 тыс. пользователей в месяц») |

### 5.8. Целевая система настоящей работы

| # | Система | Источник | M-A | RAG | Граф | .NET | RU | On-prem | Enterprise |
|:-:|---|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 46 | **AI Junior Developer** (целевая система, 2026) | настоящая работа | ✅ (4 роли в эксперименте: Orchestrator + RoslynExplorer + Coder + Tester; 7 ролей в production) | ✅ (1 154 пары MR-diff; E5-multilingual + BM25 + RRF + Cross-Encoder; MRR = 0,765) | ✅ Compiler-level Roslyn-граф; рёбра CALLS / INHERITS / USES_TYPE / **COCHANGES** | ✅ ASP.NET Core + EF Core (специализация) | ✅ (русскоязычные требования) | ✅ Ollama + qwen2.5-coder:14b Q4_K_M; 16 ГБ VRAM минимум | ⚠️ Пилоты в подготовке |

---

## 6. Уникальные пересечения признаков

Анализ матрицы (45 сравниваемых систем × 7 признаков) показывает **четыре пересечения признаков**, ни одно из которых не закрыто полностью ни одной из 45 систем:

| # | Пересечение | Кто ближе всего | Чего не хватает | Какой гипотезой закрывается |
|:-:|---|---|---|:-:|
| 1 | **Multi-agent × .NET × Enterprise** | AutoGen v0.4 (Microsoft) — Multi-agent ✅, Enterprise ✅, .NET interop ⚠️ | .NET специализация (а не interop через 1 язык в общем списке) | **H1** |
| 2 | **Compiler-level граф × .NET** | RANGER, CoSIL, CodexGraph — Граф ✅, но Python / Java; ни одной системы с C#-семантикой компилятора | Roslyn-семантика C# с биндингом символов и выводом типов | **H3** |
| 3 | **On-prem × RU × .NET** | GigaCode / KodaCode / Kodify 2 — On-prem ✅, RU ✅; Windsurf — On-prem ✅; ни одной системы с .NET-специализацией | Специализация на ASP.NET Core + EF Core в air-gapped-контуре | **H4** |
| 4 | **Co-change-edges × LLM-pipeline** | Coming (Martinez & Monperrus) — co-change edge mining, но без LLM-интеграции | Промышленная интеграция co-change-рёбер COCHANGES в семантический граф LLM-pipeline | **H3** (направление 4) |

**USES_TYPE и COCHANGES** как типы рёбер семантического графа **не упомянуты ни в одной из 45 верифицированных систем** — это самостоятельный научно-инженерный вклад настоящей работы.

---

## 7. Бенчмарки (вынесены из матрицы)

Бенчмарки — это инструменты оценки качества, а не системы кодогенерации; они не классифицируются по 7 структурным характеристикам матрицы и в настоящую позиционную матрицу не включены. Для полноты приведены отдельно.

| # | Бенчмарк | Venue / arXiv | Что измеряет | Peer-review статус |
|:-:|---|---|---|:-:|
| Б1 | **HumanEval** | Chen et al., arXiv:2107.03374 (2021) | Pass@k на 164 ручных Python-задачах | ✅ industry standard |
| Б2 | **MBPP** | Austin et al., 2021 | Pass@k на 974 задачах с тестами | ✅ |
| Б3 | **SWE-bench Verified** | OpenAI / Princeton, 2024 | Real-world Python issues from GitHub | ⚠️ верифицированная выборка |
| Б4 | **SWE-bench Pro** | Deng X. et al., arXiv:2509.16941 (2025) | Industrial-grade SWE-tasks, устойчив к контаминации | ⚠️ arXiv preprint без peer-review |
| Б5 | **CodeRAG-Bench** | Wang Z. et al., Findings of NAACL 2025 | RAG quality для кода: BM25 / BGE / GIST / SFR text retrievers | ✅ Findings (не main track) |
| Б6 | **MERA Code** | mera.a-ai.ru | Русскоязычные задачи кодогенерации | ✅ российская инициатива |
| Б7 | **RepoBench** | Liu T. et al., ICLR 2024 | Repository-level код-completion | ✅ |
| Б8 | **EvoCodeBench** | EvoCodeBench, 2024 | Эволюционирующий бенчмарк с защитой от контаминации | ⚠️ preprint |

---

## 8. Список первоисточников с URL

### 8.1. Рецензируемые публикации

- MetaGPT — https://arxiv.org/abs/2308.00352 ; ICLR 2024 oral
- ChatDev — https://arxiv.org/abs/2307.07924 ; ACL 2024
- MapCoder — https://arxiv.org/abs/2405.11403 ; ACL 2024
- RepoCoder — https://arxiv.org/abs/2303.12570 ; EMNLP 2023
- GraphCoder — https://dl.acm.org ; ASE 2024
- RepoGraph — https://openreview.net ; ICLR 2025
- CGM — https://arxiv.org/abs/2505.16901 ; NeurIPS 2025 poster
- AutoCodeRover — https://arxiv.org/abs/2404.05427 ; ISSTA 2024
- RepairAgent — https://arxiv.org/abs/2403.17134 ; ICSE 2025
- OpenHands — https://arxiv.org/abs/2407.16741 ; ICLR 2025
- SWE-Agent — https://arxiv.org/abs/2405.15793 ; NeurIPS 2024
- CoCoMIC — https://arxiv.org/abs/2212.10007 ; LREC-COLING 2024
- CodeRAG-Bench — https://aclanthology.org ; Findings of NAACL 2025
- HyDE — https://arxiv.org/abs/2212.10496 ; ACL/EACL 2023
- CoSIL — https://arxiv.org/abs/2503.22424 ; ASE 2025

### 8.2. arXiv preprints без подтверждённой peer-review

- AgentCoder — https://arxiv.org/abs/2312.13010
- AgileCoder — https://arxiv.org/abs/2406.11912
- CodeCoR — https://arxiv.org/abs/2501.07811
- AdaCoder — https://arxiv.org/abs/2504.04220
- Self-Organized Agents — https://arxiv.org/abs/2404.02183
- CodexGraph — https://arxiv.org/abs/2408.03910
- CodeR — https://arxiv.org/abs/2406.01304
- MarsCode Agent — https://arxiv.org/abs/2409.00899
- HyperAgent — https://arxiv.org/abs/2409.16299
- Agentless — https://arxiv.org/abs/2407.01489
- RANGER — https://arxiv.org/abs/2509.25257
- Live-SWE-agent — https://arxiv.org/abs/2511.13646
- SWE-Bench Pro — https://arxiv.org/abs/2509.16941

### 8.3. Коммерческие продукты

- AutoGen v0.4 — https://www.microsoft.com/en-us/research/blog/autogen-v0-4
- Devin — https://cognition.ai/blog/devin-2 ; https://cognition.ai/blog/mercedes-benz-cognition
- Cursor — https://cursor.com/blog/composer ; https://cursor.com/security
- Augment Agent — https://www.augmentcode.com/
- Trae — https://www.trae.ai/ ; https://github.com/bytedance/trae-agent
- GitHub Copilot — https://docs.github.com/en/copilot
- Continue.dev — https://www.continue.dev/ ; https://github.com/continuedev/continue
- Tabby — https://www.tabbyml.com/ ; https://github.com/TabbyML/tabby
- Windsurf / Codeium — https://windsurf.com/enterprise ; https://cognition.ai/blog/windsurf
- Amazon Q Developer — https://aws.amazon.com/q/developer/
- Aider — https://github.com/Aider-AI/aider

### 8.4. Российские системы

- GigaCode — https://platformv.sbertech.ru/ ; kod.ru (GigaConf 2024)
- KodaCode — https://kodacode.ru/ ; https://kodacode.ru/about-company ; https://www.cnews.ru/news/line/2025-12-09 ; https://habr.com/ru/companies/koda/articles/1005608/
- Kodify (MWS AI) — https://mts.ai/product/kodify/ ; https://www.forbes.ru/tekhnologii/514918 ; https://www.cnews.ru/news/line/2025-06-11_mts_otkryla ; https://habr.com/ru/companies/mts_ai/posts/
- T-Bank AI Agent — https://www.forbes.ru/tekhnologii/545720

---

## 9. Caveats и ограничения матрицы

- **Оценки для коммерческих систем без peer-review** (GigaCode, Kodify, KodaCode, T-Bank AI Agent, Devin, Cursor, Windsurf, Augment, Trae) основаны на пресс-релизах, маркетинговых whitepaper и блогах разработчиков. Независимых peer-review бенчмарков нет; обязательна пометка «по данным разработчика».
- **Agentless, SWE-Bench Pro, CodexGraph, CodeR, RANGER, Live-SWE-agent** на момент составления матрицы — arXiv preprints без подтверждённой peer-review публикации. Это не дисквалифицирует их как источник, но требует явной пометки.
- **Devin 2.0** — характеристика multi-agent эволюционировала: в 2024 г. Cognition позиционировала как single-agent, в 2025 г. признала «narrower class of multi-agent». Используется пометка ⚠️ с примечанием.
- **AutoGen v0.4 поддержка .NET** — официальный Microsoft Research blog указывает на .NET interop, но не на специализацию. Правильная классификация — ⚠️, а не ✅ для столбца .NET.
- **CoCoMIC** имеет два arXiv-ID: v1 (arXiv:2212.10007, dec 2022) и связанный arXiv:2402.09727 (отдельная / follow-up работа). Финальная peer-review публикация — LREC-COLING 2024.
- **Эта матрица не покрывает все возможные коммерческие продукты** (например, Tongyi Lingma от Alibaba, Cody от Sourcegraph, JetBrains AI Assistant, Replit Agent) — для финальной публикации диссертации эти системы стоит верифицировать дополнительно.
- **Live-SWE-agent (arXiv:2511.13646, ноябрь 2025)** — очень свежий preprint; включён для полноты, но зрелость продукта на момент защиты не подтверждена.
- **Условные обозначения On-premise** требуют различения: ✅ означает production-grade on-prem deployment с enterprise-зрелостью; ⚠️ — OSS research code, который теоретически можно развернуть локально, но без production-grade hardening. Эта различие критично для интерпретации матрицы — большинство OSS research-систем формально «можно развернуть», но в практике B2B-сегмента это не считается on-prem-предложением.

---

## 10. Связь с гипотезами H1–H4 + H2b

| Гипотеза | Незакрытый пробел | Подтверждение пробела матрицей |
|:-:|---|---|
| **H1.** Multi-agent для enterprise .NET | M-A × .NET × Enterprise | Ближайший — AutoGen v0.4 (M-A ✅, Enterprise ✅, .NET interop ⚠️). Пересечение остаётся пустым. |
| **H2a.** RAG в изоляции | RAG без графа | RepoCoder / HyDE / Aider — RAG ✅ без графа. Достаточно литературы для постановки гипотезы. |
| **H2b.** Синергия RAG × Граф | M-A × RAG × Граф × .NET / RU | GraphCoder / RepoGraph / CodexGraph / CGM / CoSIL / RANGER закрывают M-A / RAG / Граф, но ни одна не имеет .NET ✅ и RU ✅. |
| **H3.** Compiler-level граф C# + co-change-рёбра | Граф × .NET; Co-change × LLM-pipeline | Ни одна система не закрывает Граф × .NET. Co-change как edge mining — только Coming (без LLM-интеграции). USES_TYPE-рёбра не упомянуты ни в одной публикации. |
| **H4.** Локальная развёртка + 187-ФЗ-ready | On-prem × RU × .NET | GigaCode / Kodify on-prem ✅, RU ✅, .NET ⚠️; Windsurf on-prem ✅, RU ❌, .NET ⚠️. Пересечение остаётся пустым. |

**Вывод.** Целевая строка «AI Junior Developer» (строка 46) — единственная во всей расширенной матрице, имеющая ✅ во всех 7 структурных характеристиках одновременно. Это формальное обоснование уникальности ниши проекта.
