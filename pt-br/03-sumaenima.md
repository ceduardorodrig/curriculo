# Sumaenima — StênioBOT

**Plataforma de Etnografia com IA Local, Privada e Open-Source**

[sumaenima.com](https://sumaenima.com) (em desenvolvimento) | [github.com/ceduardorodrig](https://github.com/ceduardorodrig)

---

## Visão Geral

**Founder & Product Owner:** Carlos Eduardo Rodrigues

Sumaenima é meu projeto de vida. Existe há quase 10 anos como entidade criativa independente, atravessando toda minha carreira em paralelo aos empregos formais. Nasceu de uma convicção: pesquisa qualitativa — especialmente com comunidades tradicionais, indígenas e grupos vulneráveis — não deveria depender de infraestrutura de big tech para processar dados sensíveis. Mas por falta de recursos, seguiu como projeto paralelo durante anos — até que em 2024 comecei a construir a **StênioBOT**.

O sonho é captar recursos para ter equipe e construir um **Bureau de Dados** com alma antropológica: uma estrutura que produza projetos como o Tô no Mapa, visualizações de dados e pesquisa etnográfica em escala — unindo ciência, território e tecnologia de forma soberana.

**StênioBOT** é uma plataforma de etnografia assistida por IA que roda 100% offline, em hardware local, sem enviar dados para nuvem. Quatro módulos integrados que cobrem o ciclo completo da pesquisa qualitativa: da coleta em campo à análise e visualização.

---

## O Problema

Pesquisadores, ONGs e instituições que trabalham com dados sensíveis enfrentam um dilema:
- Serviços cloud (Google, OpenAI, AWS) são caros e exigem envio de dados para servidores externos
- Alternativas locais são fragmentadas, mal documentadas e exigem conhecimento técnico profundo
- LGPD e comitês de ética restringem cada vez mais o uso de soluções cloud para dados de pesquisa

Não existe uma plataforma integrada, local, privada e acessível para pesquisa qualitativa assistida por IA.

---

## A Solução — StênioBOT

### Módulos

#### StênioREC — Transcrição em Tempo Real
- Transcrição local via **Whisper large-v3-turbo** com detecção de atividade de voz (VAD)
- Purificação de transcrições via **Gemma 3 (1B)** em pipeline paralelo (Neural Flow)
- Exportação em tempo real para Google Docs no modo colaborativo
- Drafts sub-500ms com refinamento assíncrono

#### StênioPANEL — Visão Computacional para Workshops
- Scanner de post-its e painéis físicos com **GroundingDINO + SAM 2**
- OCR via **PaddleOCR** para extração de texto manuscrito
- Geração automática de esquemas `.canvas` compatíveis com Obsidian

#### StênioDIVE — Mineração Semântica
- Crawler de wikilinks, tags e notas conectando transcrições (REC) e boards visuais (PANEL)
- Grafo interativo de conexões semânticas entre documentos
- Embeddings e busca semântica local

#### DataVis — Visualizações Interativas
- Dados climáticos em tempo real (PM2.5, matriz energética, enchentes)
- Visualizações com física de partículas e dados dinâmicos
- Painéis para tomada de decisão baseada em evidências

### Funcionalidades Transversais

- **SaaS**: Assinaturas via Mercado Pago, planos por volume de processamento
- **Autenticação**: Google OAuth com armazenamento criptografado de tokens
- **CMS**: Blog + documentação com editor WYSIWYG (TipTap) e biblioteca de imagens
- **ERP**: Organizações, membros, leads, contratos, faturas, projetos
- **Observabilidade**: Grafana + Loki + Promtail, logs estruturados, health endpoints

---

## Stack Tecnológica

| Camada | Tecnologia |
|--------|-----------|
| **Backend** | FastAPI (async) + Python 3.12+ + SQLAlchemy 2.0 (asyncpg) |
| **Frontend** | React 19 + Vite 8 + TypeScript 6 + Material Web Components (MD3) + Tailwind |
| **Banco** | PostgreSQL 16 + Alembic (migrations) |
| **Cache/Queue** | Valkey 8 (Redis-compatível) · Streams, Pub/Sub, arq job queues |
| **AI Áudio** | Whisper large-v3-turbo (transformers/PyTorch) + Gemma 3 (1B) |
| **AI Visão** | GroundingDINO + SAM 2 + PaddleOCR + Gemma 4B |
| **Infra** | Docker Swarm multi-nó · Docker Compose · NVIDIA GPU |
| **Rede** | Tailscale Funnel · Nginx reverse proxy |
| **Pagamentos** | Mercado Pago SDK |
| **Analytics** | Umami (self-hosted, privacy-first) |
| **Monitoramento** | Grafana + Loki + Promtail |

### Métricas do Projeto

- **~7,9 milhões** de linhas de código
- **334 commits**
- **23,8 mil** arquivos
- **202 commits** do fundador + **133** de agentes de IA assistidos
- Arquitetura: **3 nós** (Core + Edge primário + Edge standby), **6+ serviços**

---

## Arquitetura do Sistema

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

Comunicação 100% via Valkey: Streams para chunks de áudio, Pub/Sub para resultados, arq queues para jobs batch, e mutex distribuído para serialização de GPU.

### Nós Físicos

| Nó | Hardware | Função | Localização |
|----|----------|--------|-------------|
| **psicopompo** | Xeon E-2246G 6C/12T · RTX 5050 · 46GB RAM · CachyOS (Arch) | Core — Workers IA, PostgreSQL, Valkey, API | Casa (CGNAT) |
| **ybyra** | 1GB RAM · Ubuntu | Edge primário — nginx, SPA, Umami | Oracle Cloud |
| **kuaray** | i5-4200U · 6GB RAM · Linux Mint | Edge standby — failover warm | Casa (CGNAT) |

---

## Infraestrutura — Homelab Mnemocine

Prova de conceito rodando em hardware real, sem dependência de cloud comercial:

- **psicopompo**: Dell workstation Frankenstein — absolute sleeper. Servidor principal com CachyOS (Arch), GPU RTX 5050 para inferência local, 46GB RAM, armazenamento Btrfs em 4 discos (~3.6TB total)
- **kuaray**: Notebook Dell velho reaproveitado rodando Linux Mint com 21 containers — porque tecnologia útil não se descarta
- **Rede**: Tailscale mesh VPN como backbone, bypass de CGNAT, funnels públicos para serviços expostos
- **Serviços**: 30+ containers em produção cobrindo AI, banco, cache, DNS, monitoramento, automação residencial, streaming e backup
- **Monitoramento**: Grafana + Loki + Promtail com dashboards personalizados

---

## Founders

**Carlos Eduardo Rodrigues** · Antropólogo (UnB), founder e PO.

Há quase 10 anos combinando pesquisa etnográfica, tecnologia e dados — com a Sumaenima como fio condutor de tudo que faz. Construiu a Plataforma Tô no Mapa (integrada ao MPF) enquanto estava no ISPN. Viveu na pele o potencial transformador da tecnologia no socioambiental, e também o burnout de usar comunicação a serviço de terceiros.

Monografia: *"Uma Assemblage de Projetos de Vida: mudanças organizacionais na Fazenda Canadá, Cavalcante-GO"* (UnB, 2023). Coautor em Land Use Policy (Elsevier, 2026). Prêmio Mercosul de Jornalismo Científico. Documentarista ("RUA PARA QUE(M)?"). Arquiteto do homelab Mnemocine.

Híbrido por natureza — capaz de traduzir necessidades de pesquisa qualitativa em requisitos de sistema, e arquitetura técnica em impacto socioambiental.

---

## Potencial de Mercado

- **Pesquisa de mercado e UX**: empresas que precisam de análise qualitativa de entrevistas e workshops sem depender de ferramentas cloud estrangeiras
- **ONGs e institutos de pesquisa**: organizações do Sul Global que trabalham com dados sensíveis de comunidades
- **Universidades**: programas de pós-graduação que precisam de ferramentas de análise qualitativa para seus pesquisadores
- **Governo**: órgãos como MPF, FUNAI, ICMBio que lidam com dados territoriais e culturais sigilosos
- **Saúde**: pesquisas clínicas e etnográficas sujeitas aLGPD e comitês de ética

---

## Próximos Passos

1. Finalizar versão beta para testes com instituições parceiras
2. Programa de aceleração para escala
3. Expansão do módulo DataVis com datasets climáticos do Cerrado e Amazônia
4. Versão mobile para coleta em campo offline-first
5. Marketplace de modelos de IA especializados para pesquisa qualitativa

---

**Contato:** [ceduardorodrig@gmail.com](mailto:ceduardorodrig@gmail.com) · +55 (61) 9-9803-3546
