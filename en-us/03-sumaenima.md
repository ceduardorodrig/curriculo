# Sumaenima — StênioBOT

**Ethnography Platform with Local, Private, Open-Source AI**

[sumaenima.com](https://sumaenima.com) (in development) | [github.com/ceduardorodrig](https://github.com/ceduardorodrig)

---

## Overview

**Founder & Product Owner:** Carlos Eduardo Rodrigues

Sumaenima was born from a conviction: qualitative research — especially with traditional communities, Indigenous peoples, and vulnerable groups — should never depend on big tech infrastructure to process sensitive data.

StênioBOT is an **AI-assisted ethnography platform** running 100% offline on local hardware, with zero data sent to the cloud. Four integrated modules cover the complete qualitative research cycle: from field collection to analysis and visualization.

---

## The Problem

Researchers, NGOs, and institutions working with sensitive data face a dilemma:
- Cloud services (Google, OpenAI, AWS) are expensive and require sending data to external servers
- Local alternatives are fragmented, poorly documented, and require deep technical expertise
- Data protection regulations (LGPD, GDPR) and ethics committees increasingly restrict cloud solutions for research data

There is no integrated, local, private, and accessible platform for AI-assisted qualitative research.

---

## The Solution — StênioBOT

### Modules

#### StênioREC — Real-Time Transcription
- Local transcription via **Whisper large-v3-turbo** with voice activity detection (VAD)
- Transcription purification via **Gemma 3 (1B)** in a parallel Neural Flow pipeline
- Real-time export to Google Docs in collaborative mode
- Sub-500ms drafts with asynchronous refinement

#### StênioPANEL — Computer Vision for Workshops
- Physical post-it and board scanning with **GroundingDINO + SAM 2**
- OCR via **PaddleOCR** for handwritten text extraction
- Automatic generation of `.canvas` schemas compatible with Obsidian

#### StênioDIVE — Semantic Mining
- Cross-linking crawler connecting transcripts (REC) and visual boards (PANEL)
- Interactive knowledge graph of semantic connections between documents
- Local embeddings and semantic search

#### DataVis — Interactive Visualizations
- Real-time climate data (PM2.5, energy matrix, flood data)
- Particle physics visualizations with dynamic data
- Evidence-based decision-making dashboards

### Cross-Cutting Features

- **SaaS**: Mercado Pago subscription billing, volume-based plans
- **Auth**: Google OAuth with encrypted token storage
- **CMS**: Blog + documentation with TipTap WYSIWYG editor and image library
- **ERP**: Organizations, members, leads, contracts, invoices, projects
- **Observability**: Grafana + Loki + Promtail, structured logging, health endpoints

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | FastAPI (async) + Python 3.12+ + SQLAlchemy 2.0 (asyncpg) |
| **Frontend** | React 19 + Vite 8 + TypeScript 6 + Material Web Components (MD3) + Tailwind |
| **Database** | PostgreSQL 16 + Alembic (migrations) |
| **Cache/Queue** | Valkey 8 (Redis-compatible) · Streams, Pub/Sub, arq job queues |
| **AI Audio** | Whisper large-v3-turbo (transformers/PyTorch) + Gemma 3 (1B) |
| **AI Vision** | GroundingDINO + SAM 2 + PaddleOCR + Gemma 4B |
| **Infra** | Docker Swarm multi-node · Docker Compose · NVIDIA GPU |
| **Network** | Tailscale Funnel · Nginx reverse proxy |
| **Payments** | Mercado Pago SDK |
| **Analytics** | Umami (self-hosted, privacy-first) |
| **Monitoring** | Grafana + Loki + Promtail |

### Project Metrics

- **~7,9 million** lines of code
- **334 commits**
- **23,800+** files
- **202 commits** by founder + **133** by assisted AI agents
- Architecture: **3 nodes** (Core + Primary Edge + Standby Edge), **6+ services**

---

## System Architecture

```
Browser Client (SPA)
        |
    HTTPS/WSS
        |
+-------------------+       Valkey 8 (Streams, Pub/Sub, arq queues)
|   API Worker      |<------+-------------------------+
| (CPU only)        |       |                         |
| FastAPI + React   |       |                         |
| Auth, Payments,   |       |                         |
| WS, Canvas, CMS   |       |                         |
+-------------------+       |                         |
        |                  |                         |
        +------------------+                         |
        |                                            |
+------------------+                    +-------------------+
| Audio Worker     |                    | Vision Worker     |
| (GPU required)   |                    | (GPU required)    |
| Whisper + Gemma  |                    | GroundingDINO     |
| 1B               |                    | + SAM 2 +         |
| Stream consumer  |                    | PaddleOCR +       |
| + arq batch jobs |                    | Gemma 4B          |
+------------------+                    +-------------------+
```

Communication is 100% via Valkey: Streams for audio chunks, Pub/Sub for results, arq queues for batch jobs, and distributed mutex for GPU serialization.

### Physical Nodes

| Node | Hardware | Role | Location |
|------|----------|------|----------|
| **psicopompo** | Xeon E-2246G 6C/12T · RTX 5050 · 46GB RAM · CachyOS (Arch) | Core — AI Workers, PostgreSQL, Valkey, API | Home (CGNAT) |
| **ybyra** | 1GB RAM · Ubuntu | Primary edge — nginx, SPA, Umami | Oracle Cloud |
| **kuaray** | i5-4200U · 6GB RAM · Linux Mint | Standby edge — warm failover | Home (CGNAT) |

---

## Infrastructure — Mnemocine Homelab

Proof of concept running on real hardware with zero commercial cloud dependency:

- **psicopompo**: Dell Frankenstein workstation — absolute sleeper. Main server running CachyOS (Arch), RTX 5050 for local inference, 46GB RAM, Btrfs storage across 4 drives (~3.6TB total)
- **kuaray**: Old repurposed Dell laptop running Linux Mint with 21 containers — because useful technology shouldn't be thrown away
- **Network**: Tailscale mesh VPN as backbone, CGNAT bypass, public funnels for exposed services
- **Services**: 30+ containers in production covering AI, database, cache, DNS, monitoring, home automation, streaming, and backup
- **Monitoring**: Grafana + Loki + Promtail with custom dashboards

---

## Founder

**Carlos Eduardo Rodrigues** · Anthropologist (UnB), founder and PO.

Nearly a decade combining ethnographic research, technology, and data. Built the Tô no Mapa Platform (integrated with Brazil's Federal Public Ministry). Co-author in Land Use Policy (Elsevier, 2026). Mercosur Scientific Journalism Award winner. Documentary filmmaker. Architect of the Mnemocine homelab.

A hybrid by nature — able to translate qualitative research needs into system requirements, and technical architecture into socio-environmental impact.

---

## Market Potential

- **Market & UX Research**: companies needing qualitative analysis of interviews and workshops without relying on foreign cloud tools
- **NGOs and research institutes**: Global South organizations working with sensitive community data
- **Universities**: graduate programs needing qualitative analysis tools for researchers
- **Government**: agencies like the Federal Public Ministry, FUNAI, ICMBio dealing with confidential territorial and cultural data
- **Healthcare**: clinical and ethnographic research subject to LGPD/GDPR and ethics committees

---

## Next Steps

1. Finalize beta version for partner institution testing
2. Accelerator program for scale
3. Expand DataVis module with Cerrado and Amazon climate datasets
4. Mobile version for offline-first field collection
5. Marketplace of specialized AI models for qualitative research

---

**Contact:** [ceduardorodrig@gmail.com](mailto:ceduardorodrig@gmail.com) · +55 (61) 9-9803-3546
