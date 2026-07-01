from __future__ import annotations

from pathlib import Path

from cvcheck.include.types import CheckResult

CHECK_METADATA = {
    "name": "structure",
    "description": "Verifica se todos os 6 arquivos .md existem com sections obrigatorias",
}

CVROOT = Path(__file__).resolve().parents[2]

REQUIRED_FILES = [
    "pt-br/01-tech-produto-dados.md",
    "pt-br/02-socioambiental-tech.md",
    "pt-br/03-sumaenima.md",
    "en-us/01-tech-product-data.md",
    "en-us/02-socioenvironmental-tech.md",
    "en-us/03-sumaenima.md",
]

REQUIRED_SECTIONS = {
    "01": ["Experiência", "Formação", "Habilidades"],
    "02": ["Experiência", "Formação", "Habilidades"],
}

REQUIRED_SECTIONS_EN = {
    "01": ["Experience", "Education", "Skills"],
    "02": ["Experience", "Education", "Skills"],
}


def check() -> CheckResult:
    details = []

    for f in REQUIRED_FILES:
        path = CVROOT / f
        if not path.exists():
            details.append(f"Arquivo ausente: {f}")
            continue

        content = path.read_text(encoding="utf-8")

        if f.startswith("pt-br/03") or f.startswith("en-us/03"):
            if "## 👤" not in content and "## 🎯" not in content:
                details.append(f"{f}: 03 precisa de seccao de visao geral ou fundador")
            continue

        prefix = "en-us" if f.startswith("en-us") else "pt-br"
        suffix = f.split("/")[1][:2]
        needed = REQUIRED_SECTIONS_EN if prefix == "en-us" else REQUIRED_SECTIONS
        secs = needed.get(suffix, [])

        missing = []
        for sec in secs:
            found = False
            for variant in [f"## {sec}", f"## 💼 {sec}", f"## 🎓 {sec}", f"## 🛠️ {sec}"]:
                if variant in content:
                    found = True
                    break
            if not found:
                missing.append(sec)

        if missing:
            details.append(f"{f}: sections ausentes: {', '.join(missing)}")

    if details:
        return CheckResult.fail("structure", f"{len(details)} problema(s) de estrutura", details)

    return CheckResult.pass_("structure", f"{len(REQUIRED_FILES)} arquivos OK, sections obrigatorias presentes")
