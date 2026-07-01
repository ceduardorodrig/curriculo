# Carlos Eduardo Rodrigues

**Arquiteto de Dados & Produto** | Antropologia + Engenharia de IA Local

[ceduardorodrig@gmail.com](mailto:ceduardorodrig@gmail.com) | +55 (61) 9-9803-3546 | Brasília-DF

[linkedin.com/in/c-eduardo-rodrigues](https://linkedin.com/in/c-eduardo-rodrigues) | [github.com/ceduardorodrig](https://github.com/ceduardorodrig)

---

## Perfil

Arquiteto de dados e produto que constrói pontes entre tecnologia open-source e pesquisa qualitativa. Experiência comprovada em projetar pipelines de IA local (Whisper, LLMs), orquestrar clusters Docker Swarm multi-nó e gerenciar produtos de dados do zero. Uso engenhoso de hardware reaproveitado e software livre para entregar soluções de IA privadas, offline e economicamente viáveis — sem depender de infraestrutura de big tech. Formação em Antropologia pela UnB como base para design de produto centrado em humanos.

---

## Experiência

### Sumaenima — Founder & Product Owner
*2024 — presente · Brasília-DF / Remoto*

Fundador e PO da StênioBOT, plataforma de etnografia assistida por IA com inferência 100% local. Quatro módulos integrados:

- **StênioREC**: transcrição em tempo real (Whisper large-v3-turbo) com detecção de atividade de voz, purificação via Gemma 3 e exportação para Google Docs
- **StênioPANEL**: scanner de workshops físicos com visão computacional (GroundingDINO + SAM 2 + PaddleOCR), gerando esquemas compatíveis com Obsidian
- **StênioDIVE**: mineração semântica cruzada de wikilinks, tags e notas, conectando transcrições e boards visuais em grafo interativo
- **DataVis**: visualizações climáticas interativas com física de partículas e dados em tempo real

Stack: FastAPI (async) + React 19 + TypeScript 6 + PostgreSQL 16 + Valkey 8 + Docker Swarm (3 nós). SaaS com assinaturas via Mercado Pago, autenticação Google OAuth e observabilidade Grafana/Loki. Plataforma 100% offline, privada e LGPD-compliant.

### IPAM — Amazon Environmental Research Institute
*2022 — presente · Brasília-DF*

**Communication Analyst** (2024–presente) · **Communication Assistant** (2023–2024) · **Trainee** (2022–2023)

- Implementei metodologia Agile/Scrum como Scrum Master na equipe de comunicação, estruturando sprints, rituais e métricas de entrega
- Gerenciei dados de audiência e performance de 5 redes sociais, atingindo alcance consolidado de **2+ milhões de usuários**
- Administrei campanhas de Google Ad Grants (US$ 10K/mês em créditos) e Meta Ads com segmentação, testes A/B e otimização contínua
- Codiretor do documentário **"Manaus Extrema"**, estreou no INPA durante o PROTEJA Talks 2024
- **Prêmio Mercosul de Jornalismo e Divulgação Científica — 1º lugar na categoria Redes Sociais** (2024)
- Presidi a CIPA (Comissão Interna de Prevenção de Acidentes e Assédio) por dois mandatos

### ISPN — Institute for Society, Population and Nature
*2017 — 2021 · Brasília-DF*

**Junior Technical Advisor** (2019–2021) · **Trainee** (2017–2019)

- **Tô no Mapa**: projeto que definiu minha trajetória híbrida. Comecei como pesquisador etnográfico em campo, realizando levantamento de requisitos com comunidades tradicionais, e ajudei a transformar uma iniciativa de coleta de dados na **Plataforma Tô no Mapa** — hoje integrada ao Ministério Público Federal, empoderando milhares de comunidades a automapecar seus territórios
- Criei a primeira estratégia de comunicação pública do Instituto em anos
- Produzi mapas (QGIS), relatórios, materiais gráficos e cobertura fotográfica em expedições de campo
- Organizei eventos socioambientais de grande porte: Acampamento Terra Livre, Encontro e Feira dos Povos do Cerrado, Congresso Latino-Americano de Agroecologia

### Participatory Fauna Monitoring Network (Rede de Monitoria)
*2020 — 2022 · Cavalcante-GO*

**Communications Specialist**

- Conectei com gerente sênior do **World Bank** para estruturar um corredor ecológico entre o Parque Nacional da Chapada dos Veadeiros e o Sítio Histórico Kalunga
- Organizei e facilitei a reunião inaugural da rede, reunindo ICMBio, UnB, ONGs e proprietários rurais
- Produzi relatório executivo completo (concepção, redação, fotografia, diagramação)

---

## Infraestrutura & Homelab (Mnemocine)

Infraestrutura pessoal de 4 servidores orquestrados via Docker Swarm, provando conceitos de arquitetura distribuída com hardware heterogêneo e software livre:

| Servidor | Hardware | Papel |
|----------|----------|-------|
| **psicopompo** | Dell Frankenstein · Xeon E-2246G 6C/12T · RTX 5050 · 46GB RAM · CachyOS (Arch) | Core — IA, banco, Swarm manager |
| **ybyra** | Oracle Cloud · 1GB RAM | Edge primário — nginx, SPA, umami |
| **ybytu** | Oracle Cloud · 1GB RAM | Cloud — DNS, dashboard, sincronização |
| **kuaray** | Dell notebook reaproveitado · i5-4200U · 6GB RAM · Linux Mint | Edge secundário — multimídia, automação |

- Rede mesh **Tailscale** como backbone (bypass de CGNAT, funnels públicos)
- **30+ containers** em produção (PostgreSQL, Valkey, nginx, AdGuard, Home Assistant, *arr stack)
- Monitoramento com **Grafana + Loki + Promtail**
- Backup automatizado com Borg + pg_dump
- Desktop principal: Arch Linux (CachyOS) — daily driver há anos

---

## Formação

**Universidade de Brasília (UnB)** — Bacharelado em Ciências Sociais / Antropologia (2016–2023)

Pesquisa etnográfica sobre neorruralistas e comunidades tradicionais. Direção do documentário etnográfico "RUA PARA QUE(M)?" (85min) sobre o movimento neo-fanfarrista de Brasília, produzido em colaboração com o Departamento de Antropologia, NEAz-UnB e HONK! BSB.

---

## Publicações

- **Coautor** — Moser, P. et al. *"Institutional Invisibility Threatens the Lands and Livelihoods of Traditional Communities in the Northern Brazilian Cerrado"* — Submetido a **Land Use Policy** (Elsevier, 2026)
- **Documentário** — *RUA PARA QUE(M)?* (85min, 2020) — Direção, fotografia, edição. Publicado pela Sumaenima. YouTube: 1k+ views.
- **Documentário** — *Manaus Extrema* (2024) — Codireção. Estreia no INPA / PROTEJA Talks 2024.

---

## Skills

| Categoria | Tecnologias |
|-----------|-------------|
| **Backend** | FastAPI, Python, SQLAlchemy, asyncpg, REST APIs, WebSockets |
| **Frontend** | React, TypeScript, Vite, Tailwind, Material Web Components |
| **Banco de Dados** | PostgreSQL, Alembic, SQL, modelagem de dados |
| **Infraestrutura** | Docker Swarm, Nginx, Tailscale, Linux (Arch), GPU passthrough |
| **AI/ML** | Whisper (transcrição), LLMs (Gemma), GroundingDINO, SAM 2, embeddings |
| **Observabilidade** | Grafana, Loki, Promtail, health endpoints |
| **Métodos** | Agile/Scrum (Scrum Master), pesquisa etnográfica, UX Research, OKRs |
| **Ferramentas** | Git, Adobe Creative Suite, QGIS, Google Earth Engine |

---

## Idiomas

- **Português** — Nativo
- **Inglês** — Fluente (leitura, escrita, conversação técnica e acadêmica)
