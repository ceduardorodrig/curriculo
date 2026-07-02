from __future__ import annotations

import re
from pathlib import Path

from cvcheck.include.types import CheckResult

CHECK_METADATA = {
    "name": "parity",
    "description": "Verifica se todos arquivos PT tem versao EN e vice-versa (exceto sub-versoes)",
}

CVROOT = Path(__file__).resolve().parents[2]

HEADING_RE = re.compile(r"^##\s+(.+)$", re.MULTILINE)

KNOWN_MAPPINGS = {
    "Perfil": "Profile",
    "Experiência": "Experience",
    "Formação": "Education",
    "Habilidades": "Skills",
    "Publicações": "Publications",
    "Idiomas": "Languages",
    "Prêmios": "Awards",
    "Infraestrutura — Sumænimá & Mnemocine": "Infrastructure — Sumænimá & Mnemocine",
    "Infraestrutura — Homelab Mnemocine": "Infrastructure — Mnemocine Homelab",
    "Visão Geral": "Overview",
    "O Problema": "The Problem",
    "A Solução — StênioBOT": "The Solution — StênioBOT",
    "Design & Experiência": "Design & Experience",
    "Escala do Ecossistema": "Ecosystem Scale",
    "Fundador": "Founder",
    "Próximos Passos": "Next Steps",
    "Stack Tecnológica": "Tech Stack",
    "StênioKernel — Kernel de Governança para Agentes de IA": "StênioKernel — AI Agent Governance Kernel",
    "Idiomas": "Languages",
}


def _strip_emoji(name: str) -> str:
    return re.sub(r"[^\w\s/–—\-&\u00C0-\u024F]", "", name).strip()


FILE_MAPPINGS = {
    "socioambiental-tech": "socioenvironmental-tech",
    "socioambiental-nichado": "socioenvironmental-nichado",
    "tech-produto-dados": "tech-product-data",
    "sumaenima": "sumaenima",
}


def _file_suffix(name: str) -> str:
    m = re.match(r"\d{2}-(.+)\.md$", name)
    return m.group(1) if m else ""


def _find_pairs(pt_dir: Path, en_dir: Path) -> tuple[list, list, list]:
    pt_files = sorted(pt_dir.glob("*.md"))
    en_files = sorted(en_dir.glob("*.md"))

    en_map: dict[str, Path] = {}
    for f in en_files:
        suffix = _file_suffix(f.name)
        if suffix:
            en_map[suffix] = f

    pairs = []
    pt_orphans = []

    for pt_f in pt_files:
        pt_suffix = _file_suffix(pt_f.name)
        if not pt_suffix:
            continue
        en_suffix = FILE_MAPPINGS.get(pt_suffix, pt_suffix)
        if en_suffix in en_map:
            pairs.append((pt_f, en_map[en_suffix]))
        else:
            pt_orphans.append(pt_f)

    en_orphans = []
    for en_f in en_files:
        en_suffix = _file_suffix(en_f.name)
        if not en_suffix:
            continue
        # Check if any PT file maps to this EN suffix
        pt_has = False
        for pt_s, en_s in FILE_MAPPINGS.items():
            if en_s == en_suffix:
                pt_has = True
                break
        if not pt_has:
            en_orphans.append(en_f)

    return pairs, pt_orphans, en_orphans


def check() -> CheckResult:
    details = []
    pt_dir = CVROOT / "pt-br"
    en_dir = CVROOT / "en-us"

    pairs, pt_orphans, en_orphans = _find_pairs(pt_dir, en_dir)

    for pt_f in pt_orphans:
        details.append(f"{pt_f.relative_to(CVROOT)}: existe em PT mas sem versao EN correspondente")
    for en_f in en_orphans:
        details.append(f"{en_f.relative_to(CVROOT)}: existe em EN mas sem versao PT correspondente")

    for pt_file, en_file in pairs:
        pt_rel = pt_file.relative_to(CVROOT)
        en_rel = en_file.relative_to(CVROOT)

        pt_heads = {_strip_emoji(m.group(1)) for m in HEADING_RE.finditer(pt_file.read_text(encoding="utf-8"))}
        en_heads = {_strip_emoji(m.group(1)) for m in HEADING_RE.finditer(en_file.read_text(encoding="utf-8"))}

        pt_ignored = {"Sobre", "About", "Contato", "Contact", "Narrativa", "Narrative",
                       "O Fio da Meada", "The Thread", "Sumaenima  Mnemocine"}
        pt_filtered = {h for h in pt_heads if h not in pt_ignored and not h.startswith("Vers")}
        en_filtered = {h for h in en_heads if h not in pt_ignored and not h.startswith("Vers")}

        pt_mapped = {KNOWN_MAPPINGS.get(h, h) for h in pt_filtered}
        en_mapped = {KNOWN_MAPPINGS.get(h, h) for h in en_filtered}

        pt_only = pt_mapped - en_mapped
        en_only = en_mapped - pt_mapped

        if pt_only:
            details.append(f"{pt_rel}: sections sem equivalente EN: {', '.join(sorted(pt_only)[:5])}")
        if en_only:
            details.append(f"{en_rel}: sections sem equivalente PT: {', '.join(sorted(en_only)[:5])}")

    if details:
        return CheckResult.fail("parity", f"{len(details)} divergencia(s) entre PT e EN", details)

    return CheckResult.pass_("parity", f"{len(pairs)} pares conferidos, sections equivalentes")
