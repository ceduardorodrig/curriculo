from __future__ import annotations

import os
import sys
from pathlib import Path

from cvcheck.include.types import CheckResult

CHECK_METADATA = {
    "name": "sec_scope_guard",
    "description": "Impede runs parciais que escondem falhas (--only)",
}

CVROOT = Path(__file__).resolve().parents[2]


def check() -> CheckResult:
    is_restricted = False
    reasons = []

    argv = [a.lower() for a in sys.argv[1:]]

    if "--only" in argv:
        idx = argv.index("--only")
        if idx + 1 < len(argv):
            is_restricted = True
            reasons.append(f"--only {sys.argv[idx + 1]}")

    for tag in ["--tag", "--scope"]:
        if tag in argv:
            is_restricted = True
            reasons.append(tag)

    if not is_restricted:
        return CheckResult.pass_("sec_scope_guard", "Escopo completo — todos os drivers serao executados")

    is_tty = sys.stdin.isatty()
    has_api_keys = any(k in os.environ for k in ["GEMINI_API_KEY", "ANTHROPIC_API_KEY", "OPENAI_API_KEY"])

    if not is_tty and has_api_keys:
        return CheckResult.fail(
            "sec_scope_guard",
            "RUN PARCIAL BLOQUEADO: Agentes de IA estao PROIBIDOS de runs de escopo reduzido.",
            [
                "Sempre execute 'python -m cvcheck' completo antes de concluir ou commit/push.",
                f"Razoes: {', '.join(reasons)}",
                "Para desenvolvimento local interativo, use --only sem variaveis de API key.",
            ],
        )

    return CheckResult.warn(
        "sec_scope_guard",
        f"Run parcial detectado: {', '.join(reasons)}. Runs completas sao obrigatorias antes de commit/push.",
    )
