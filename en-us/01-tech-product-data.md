# Carlos Eduardo Rodrigues

**Data & Product Architect** | Anthropology meets Local AI Engineering

[ceduardorodrig@gmail.com](mailto:ceduardorodrig@gmail.com) | +55 (61) 9-9803-3546 | Brasília-DF, Brazil

[linkedin.com/in/c-eduardo-rodrigues](https://linkedin.com/in/c-eduardo-rodrigues) | [github.com/ceduardorodrig](https://github.com/ceduardorodrig)

---

## Profile

Data and product architect who bridges open-source technology and qualitative research. Proven track record designing local AI pipelines (Whisper, LLMs), orchestrating multi-node Docker Swarm clusters, and building data products from scratch. Ingenious use of repurposed hardware and free software to deliver private, offline, cost-effective AI solutions — with zero dependency on big tech infrastructure. Anthropology degree from UnB as the foundation for human-centered product design.

---

## Experience

### Sumaenima — Founder & Product Owner
*2016 — present · Brasília-DF / Remote*

Sumaenima is my life project. It has existed for nearly 10 years as an independent creative entity, running alongside formal employment throughout my entire career. What keeps me going is the dream of one day raising resources to build a team and create a **Data Bureau** with an anthropological soul — more projects like Tô no Mapa and data visualizations that unite science, territory, and technology.

**StênioBOT** (2024–present): an AI-assisted ethnography platform running 100% local inference. Four integrated modules:

- **StênioREC**: real-time transcription (Whisper large-v3-turbo) with voice activity detection, Gemma 3 purification pipeline, and Google Docs export
- **StênioPANEL**: physical workshop scanner with computer vision (GroundingDINO + SAM 2 + PaddleOCR), generating Obsidian-compatible `.canvas` schemas
- **StênioDIVE**: cross-semantic mining of wikilinks, tags, and notes connecting transcripts and visual boards in an interactive graph
- **DataVis**: interactive climate visualizations with particle physics and real-time data

Stack: FastAPI (async) + React 19 + TypeScript 6 + PostgreSQL 16 + Valkey 8 + Docker Swarm (3 nodes). SaaS with Mercado Pago billing, Google OAuth, and Grafana/Loki observability. Fully offline, private, LGPD-compliant.

### IPAM — Amazon Environmental Research Institute
*2022 — 2025 · Brasília-DF, Brazil*

**Communication Analyst** (2024–2025) · **Communication Assistant** (2023–2024) · **Trainee** (2022–2023)

- Implemented Agile/Scrum as Scrum Master for the communications team, structuring sprints, ceremonies, and delivery metrics
- Managed audience data and performance across 5 social networks, reaching **2+ million users** combined
- Administered Google Ad Grants (US$ 10K/month) and Meta Ads campaigns with segmentation, A/B testing, and continuous optimization
- Co-directed **"Manaus Extrema"** documentary, premiered at INPA during 2024 PROTEJA Talks
- **Mercosur Scientific Journalism and Dissemination Award — 1st place, Social Networks category** (2024)
- Served as CIPA (Internal Accident and Harassment Prevention Commission) president for two terms

### ISPN — Institute for Society, Population and Nature
*2017 — 2021 · Brasília-DF, Brazil*

**Junior Technical Advisor** (2019–2021) · **Trainee** (2017–2019)

- **Tô no Mapa**: the project that defined my hybrid career. Started as an ethnographic field researcher conducting requirements gathering with traditional communities, and helped transform a data collection initiative into the **Tô no Mapa Platform** — now integrated with Brazil's Federal Public Ministry, empowering thousands of communities to self-map their territories
- Created the Institute's first public communications strategy in years
- Produced maps (QGIS), reports, graphic materials, and photographic coverage during field expeditions
- Organized large-scale socio-environmental events: Acampamento Terra Livre, Encontro e Feira dos Povos do Cerrado, Latin American Agroecology Congress

### Participatory Fauna Monitoring Network (Rede de Monitoria)
*2020 — 2022 · Cavalcante-GO, Brazil*

**Communications Specialist**

- Connected with a senior manager from the **World Bank** to structure a wildlife corridor between Chapada dos Veadeiros National Park and the Kalunga Historical Site
- Organized and facilitated the network's inaugural meeting, bringing together ICMBio, UnB, NGOs, and rural landowners
- Produced the complete executive report (conception, writing, photography, layout)

---

## Infrastructure & Homelab (Mnemocine)

Personal 4-server infrastructure orchestrated via Docker Swarm, proving distributed architecture concepts with heterogeneous hardware and free software:

| Server | Hardware | Role |
|--------|----------|------|
| **psicopompo** | Dell Frankenstein · Xeon E-2246G 6C/12T · RTX 5050 · 46GB RAM · CachyOS (Arch) | Core — AI, database, Swarm manager |
| **ybyra** | Oracle Cloud · 1GB RAM | Primary edge — nginx, SPA, umami |
| **ybytu** | Oracle Cloud · 1GB RAM | Cloud — DNS, dashboard, sync |
| **kuaray** | Repurposed Dell laptop · i5-4200U · 6GB RAM · Linux Mint | Secondary edge — media, home automation |

- **Tailscale** mesh network as backbone (CGNAT bypass, public funnels)
- **30+ containers** in production (PostgreSQL, Valkey, nginx, AdGuard, Home Assistant, *arr stack)
- Monitoring with **Grafana + Loki + Promtail**
- Automated backups with Borg + pg_dump
- Daily driver: Arch Linux (CachyOS) for years

---

## Education

**University of Brasília (UnB)** — Bachelor's Degree in Social Sciences / Anthropology (2016–2023)

- **Thesis:** *"Uma Assemblage de Projetos de Vida: mudanças organizacionais na Fazenda Canadá, Cavalcante-GO"* (2023). Advisor: Prof. Henyo Trindade Barretto Filho. Ethnography on land subdivision, memory, and life projects in Chapada dos Veadeiros.
- Directed the ethnographic documentary "RUA PARA QUE(M)?" (85min) about Brasília's neo-fanfarre movement, produced in collaboration with the Anthropology Department, NEAz-UnB, and HONK! BSB.

---

## Publications

- **Co-author** — Moser, P. et al. *"Institutional Invisibility Threatens the Lands and Livelihoods of Traditional Communities in the Northern Brazilian Cerrado"* — Submitted to **Land Use Policy** (Elsevier, 2026)
- **Documentary** — *RUA PARA QUE(M)?* (85min, 2020) — Direction, photography, editing. Published by Sumaenima. 1k+ views on YouTube.
- **Documentary** — *Manaus Extrema* (2024) — Co-direction. Premiered at INPA / PROTEJA Talks 2024.

---

## Skills

| Category | Technologies |
|----------|-------------|
| **Backend** | FastAPI, Python, SQLAlchemy, asyncpg, REST APIs, WebSockets |
| **Frontend** | React, TypeScript, Vite, Tailwind, Material Web Components |
| **Database** | PostgreSQL, Alembic, SQL, data modeling |
| **Infrastructure** | Docker Swarm, Nginx, Tailscale, Linux (Arch), GPU passthrough |
| **AI/ML** | Whisper (transcription), LLMs (Gemma), GroundingDINO, SAM 2, embeddings |
| **Observability** | Grafana, Loki, Promtail, health endpoints |
| **Methods** | Agile/Scrum (Scrum Master), ethnographic research, UX Research, OKRs |
| **Tools** | Git, Adobe Creative Suite, QGIS, Google Earth Engine |

---

## Languages

- **Portuguese** — Native
- **English** — Fluent (reading, writing, technical and academic conversation)
