# Boutique Pink - Engenharia de Testes (QTS - AT1)

Regras de negócio de uma loja de roupas (cálculo de subtotal, desconto e valor final),
com testes unitários em Pytest e 100% de cobertura de linhas e ramificações.

## Estrutura do Projeto

```text
boutique-pink/
├── app/
│   ├── __init__.py
│   └── boutique.py          # Regras de negócio
├── tests/
│   ├── __init__.py
│   └── test_boutique.py     # Testes unitários (AAA, EP, BVA, Error Guessing)
├── PRD.md                   # Especificação das regras
├── AGENTS.md                # Regras de contexto para a IA
├── AI_USAGE.md              # Relatório de transparência de IA
├── pyproject.toml
└── README.md
```

## Como Executar

### 1. Instalar as dependências com o `uv`

```bash
uv sync
```

### 2. Executar os testes

```bash
uv run pytest -v
```

### 3. Medir a cobertura (linhas e ramificações)

```bash
uv run pytest --cov=app --cov-branch --cov-report=term-missing
```

## Regras principais

- Preço numérico, finito e maior que zero; quantidade inteira de 1 a 50.
- Desconto: abaixo de R$ 100 → 0%; R$ 100 a 299,99 → 5%; R$ 300 a 499,99 → 10%;
  a partir de R$ 500 → 15%.
- Entradas de tipo incorreto levantam `TypeError`; valores inválidos levantam `ValueError`.

Detalhes em [`PRD.md`](PRD.md). Uso de IA em [`AI_USAGE.md`](AI_USAGE.md).