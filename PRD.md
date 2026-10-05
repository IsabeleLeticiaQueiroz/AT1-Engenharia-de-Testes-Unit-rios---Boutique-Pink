# PRD - Boutique Pink

## 1. Visão geral

A Boutique Pink é um sistema simples de cálculo de compras de uma loja de roupas. O sistema calcula o valor total de uma compra com base no preço e na quantidade dos produtos, aplicando descontos conforme o valor da compra.

## 2. Escopo

**Dentro do escopo:**

* Informar o preço de um produto.
* Informar a quantidade comprada.
* Calcular o subtotal.
* Aplicar descontos conforme o valor da compra.
* Calcular o valor final.

**Fora do escopo:**

* Cadastro de clientes e produtos.
* Controle de estoque.
* Pagamentos reais.
* Banco de dados.
* Interface gráfica ou site.
* Sistema de entregas.

## 3. Regras de negócio

|  ID  | Descrição                                                                                                                                                                                                                   |
| :--: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| RN01 | O preço deve ser numérico (`int` ou `float`), finito e maior que zero. Valores booleanos não são aceitos.                                                                                                                   |
| RN02 | A quantidade deve ser um número inteiro entre 1 e 50.                                                                                                                                                                       |
| RN03 | O subtotal deve ser calculado multiplicando o preço pela quantidade, com arredondamento para duas casas decimais.                                                                                                           |
| RN04 | Subtotais inferiores a R$ 100,00 não recebem desconto.                                                                                                                                                                      |
| RN05 | Subtotais entre R$ 100,00 e R$ 299,99 recebem 5% de desconto.                                                                                                                                                               |
| RN06 | Subtotais entre R$ 300,00 e R$ 499,99 recebem 10% de desconto.                                                                                                                                                              |
| RN07 | Subtotais iguais ou superiores a R$ 500,00 recebem 15% de desconto.                                                                                                                                                         |
| RN08 | O valor final deve ser calculado pela fórmula `valor final = subtotal − desconto`, com arredondamento para duas casas decimais.                                                                                             |
| RN09 | Entradas de tipo incorreto (texto, `None`, `bool` ou quantidade decimal, como `2.0`) levantam `TypeError`. Entradas numéricas inválidas (zero, negativo, `NaN`, infinito ou quantidade fora de 1–50) levantam `ValueError`. |

## 4. Requisitos não funcionais

* Python 3.12 ou superior, gerenciado com uv.
* Type Hints em todas as funções.
* Tratamento defensivo de entradas inválidas (RN09).
* Testes unitários com Pytest (AAA, EP, BVA e Error Guessing).
* Cobertura medida com pytest-cov (`--cov-branch`).

## 5. Critérios de aceite

* [x] Calcular corretamente o subtotal.
* [x] Aplicar o desconto correspondente ao valor da compra.
* [x] Retornar o valor final com o desconto aplicado.
* [x] Rejeitar preços iguais ou inferiores a zero.
* [x] Rejeitar quantidades inválidas.
* [x] Todos os testes unitários devem passar.
* [x] `uv run pytest -v` com todos os testes passando.
* [x] `uv run pytest --cov=app --cov-branch --cov-report=term-missing` com 100% de linhas e ramos.
