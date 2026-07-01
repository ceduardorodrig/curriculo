#!/usr/bin/env bash
set -euo pipefail

CVROOT="$(cd "$(dirname "$0")/.." && pwd)"
HOOKS_DIR="$CVROOT/.git/hooks"

echo "🔧 Instalando hooks cvcheck..."

# ── pre-push ────────────────────────────────────────────────────────
cat > "$HOOKS_DIR/pre-push" << 'HOOK'
#!/usr/bin/env bash
set -euo pipefail

CVROOT="$(cd "$(dirname "$0")/../.." && pwd)"

echo ""
echo "🔍 cvcheck: executando verificacoes pre-push..."
echo ""

cd "$CVROOT"
python -m cvcheck --quiet

EXIT_CODE=$?

if [ $EXIT_CODE -ne 0 ]; then
    echo ""
    echo "❌ cvcheck: FALHA NA VERIFICACAO. Push bloqueado."
    echo "   Corrija as falhas acima ou use 'git push --no-verify' para ignorar (nao recomendado)."
    echo ""
    exit 1
fi

echo "✅ cvcheck: todas as verificacoes passaram. Push permitido."
echo ""
HOOK

chmod +x "$HOOKS_DIR/pre-push"
echo "  ✅ pre-push hook instalado em $HOOKS_DIR/pre-push"

# ── pre-commit (opcional, só estrutura e links rápidos) ─────────────
cat > "$HOOKS_DIR/pre-commit" << 'HOOK'
#!/usr/bin/env bash
set -euo pipefail

CVROOT="$(cd "$(dirname "$0")/../.." && pwd)"

cd "$CVROOT"
python -m cvcheck --only structure --only links --quiet 2>/dev/null || true
HOOK

chmod +x "$HOOKS_DIR/pre-commit"
echo "  ✅ pre-commit hook instalado em $HOOKS_DIR/pre-commit"

echo ""
echo "🎯 Hooks cvcheck instalados com sucesso!"
echo "   - pre-commit: verifica estrutura e links"
echo "   - pre-push: verificacao completa (bloqueia se falhar)"
echo ""
