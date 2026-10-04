# AGENTS.md

## Projeto

Boutique Pink: sistema de cálculo de compras de uma loja de roupas, feito em Python 3.12+.
A fonte da verdade das regras de negócio é o arquivo `PRD.md`.
A IA nunca deve inventar, alterar ou remover regras que não estejam no PRD.

## Regras de código

- O código de negócio fica na pasta `app/` e os testes na pasta `tests/`.
- Todas as funções devem ter Type Hints nos parâmetros e no retorno.
- Cada função deve ter uma docstring curta citando a regra que implementa (ex.: RN05).
- As funções devem ser simples, puras e determinísticas: sem leitura de arquivos, sem
  aleatoriedade e sem usar data ou hora do sistema.
- Validar as entradas conforme a RN09:
  - `TypeError` para tipo incorreto (texto, `None`, `bool`, quantidade decimal como `2.0`).
  - `ValueError` para valor inválido (zero, negativo, `NaN`, infinito, quantidade fora de 1 a 50).
- Usar apenas a biblioteca padrão do Python no código de negócio.

## Regras de teste

- Usar Pytest, com testes na pasta `tests/`.
- Estruturar cada teste no padrão AAA, com os comentários `# Arrange`, `# Act` e `# Assert`.
- Marcar todos os testes com `@pytest.mark.unit`.
- Usar `@pytest.mark.parametrize` (com `ids`) para testar vários valores na mesma função.
- Aplicar as técnicas de teste:
  - Particionamento de Equivalência (EP): um caso por faixa de desconto.
  - Análise do Valor Limite (BVA): 99,99 / 100,00 / 499,99 / 500,00
    para o desconto, e 0 / 1 / 50 / 51 para a quantidade.
  - Error Guessing: `None`, texto, `bool`, `NaN`, infinito, números negativos e zero.
- Meta: 100% de cobertura de linhas e de ramificações (`--cov-branch`).


## Comandos

- Instalar dependências: `uv sync`
- Rodar os testes: `uv run pytest -v`
- Medir a cobertura: `uv run pytest --cov=app --cov-branch --cov-report=term-missing`

## Proibido

- Alterar o `PRD.md` sem avisar o autor do projeto.
- Apagar ou enfraquecer testes só para aumentar a cobertura.
- Escrever teste sem `assert` real.
- Adicionar regras de negócio que não estejam no PRD.
- Adicionar dependências externas ao código de negócio.