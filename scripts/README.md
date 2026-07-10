# Scripts de Validação

Este diretório substitui o antigo `cvcheck/`. A validação agora é feita
pelo **StênioKernel** unificado, localizado em:

```
/mnt/NVME_PCI/sumaenimahub/SUMAENIMA-HUB/scripts/steniocheck
```

## Uso

```bash
# Rodar todas as verificações do perfil resume
./scripts/stenio_check

# Auto-teste do kernel
./scripts/stenio_check --self-test

# Listar drivers disponíveis
./scripts/stenio_check 2>&1 | grep resume_
```

O perfil `resume` inclui 10 drivers que validam:
- Datas PT-BR
- Ortografia (PT e EN)
- Paridade bilíngue
- Siglas com definição
- Imagens com alt text
- Conteúdo solto
- Sumário (TOC)
- Tom consistente

## CI (GitHub Actions)

O workflow `.github/workflows/ci.yml` roda a mesma validação em todo push. Ele faz checkout
do **SUMAENIMA-HUB** (repositório privado do kernel) via SSH deploy key e executa:

```bash
PYTHONPATH=<sumaenima-hub>/scripts \
  python3 -m steniocheck --tag resume --scope static --format github
```

O mesmo código do kernel roda localmente e no CI — governança unificada.

### Segurança do CI

O acesso ao SUMAENIMA-HUB usa **SSH deploy key read-only**, sem expor credenciais da conta
do usuário. A chave privada está armazenada como secret criptografado do GitHub Actions
(`STENIOCHECK_SSH_KEY`) e nunca aparece em logs ou no código fonte.
