import pytest
from app.boutique import (
    calcular_percentual_desconto,
    calcular_subtotal,
    calcular_valor_final,
    validar_preco,
    validar_quantidade,
)


@pytest.mark.unit
@pytest.mark.parametrize(
    "preco, esperado",
    [(10, 10.0), (0.01, 0.01)],
    ids=["inteiro_vira_float", "limite_menor_valor_valido"],
)
def test_validar_preco_aceita_valores_validos(preco, esperado):
    """RN01: precos numericos, finitos e maiores que zero sao aceitos."""
    # Arrange
    valor = preco

    # Act
    resultado = validar_preco(valor)

    # Assert
    assert resultado == esperado
    assert isinstance(resultado, float)


@pytest.mark.unit
@pytest.mark.parametrize(
    "preco, excecao",
    [(0, ValueError), (float("nan"), ValueError), ("10", TypeError), (True, TypeError)],
    ids=["zero", "nan", "texto", "bool"],
)
def test_validar_preco_rejeita_entradas_invalidas(preco, excecao):
    """RN01 e RN09: valor invalido levanta ValueError; tipo incorreto levanta TypeError."""
    # Arrange
    valor = preco

    # Act
    with pytest.raises(excecao):
        validar_preco(valor)

    # Assert


@pytest.mark.unit
@pytest.mark.parametrize(
    "quantidade",
    [1, 50],
    ids=["limite_minimo", "limite_maximo"],
)
def test_validar_quantidade_aceita_limites_validos(quantidade):
    """RN02: quantidades 1 e 50 sao aceitas (BVA nas bordas validas)."""
    # Arrange
    valor = quantidade

    # Act
    resultado = validar_quantidade(valor)

    # Assert
    assert resultado == valor


@pytest.mark.unit
@pytest.mark.parametrize(
    "quantidade, excecao",
    [(0, ValueError), (51, ValueError), (2.0, TypeError), (True, TypeError)],
    ids=["limite_abaixo_do_minimo", "limite_acima_do_maximo", "decimal_com_zero", "bool"],
)
def test_validar_quantidade_rejeita_entradas_invalidas(quantidade, excecao):
    """RN02 e RN09: fora de 1 a 50 levanta ValueError; tipo incorreto levanta TypeError."""
    # Arrange
    valor = quantidade

    # Act
    with pytest.raises(excecao):
        validar_quantidade(valor)

    # Assert


@pytest.mark.unit
@pytest.mark.parametrize(
    "preco, quantidade, esperado",
    [(10.00, 3, 30.00), (33.333, 3, 100.00)],
    ids=["multiplicacao_simples", "arredonda_para_duas_casas"],
)
def test_calcular_subtotal_multiplica_e_arredonda(preco, quantidade, esperado):
    """RN03: subtotal = preco x quantidade, arredondado a 2 casas decimais."""
    # Arrange
    valor_preco = preco
    valor_quantidade = quantidade

    # Act
    resultado = calcular_subtotal(valor_preco, valor_quantidade)

    # Assert
    assert resultado == esperado


@pytest.mark.unit
@pytest.mark.parametrize(
    "preco, quantidade, excecao",
    [(0, 1, ValueError), (10, 2.0, TypeError)],
    ids=["preco_zero", "quantidade_decimal"],
)
def test_calcular_subtotal_rejeita_entradas_invalidas(preco, quantidade, excecao):
    """RN09: entradas invalidas fazem o subtotal levantar a excecao correta."""
    # Arrange
    valor_preco = preco
    valor_quantidade = quantidade

    # Act
    with pytest.raises(excecao):
        calcular_subtotal(valor_preco, valor_quantidade)

    # Assert


@pytest.mark.unit
@pytest.mark.parametrize(
    "subtotal, esperado",
    [
        (50.00, 0.00),
        (200.00, 0.05),
        (400.00, 0.10),
        (800.00, 0.15),
        (99.99, 0.00),
        (100.00, 0.05),
        (499.99, 0.10),
        (500.00, 0.15),
    ],
    ids=[
        "ep_faixa_sem_desconto",
        "ep_faixa_5_por_cento",
        "ep_faixa_10_por_cento",
        "ep_faixa_15_por_cento",
        "bva_99_99_sem_desconto",
        "bva_100_00_entra_nos_5",
        "bva_499_99_ainda_10",
        "bva_500_00_entra_nos_15",
    ],
)
def test_calcular_percentual_desconto_por_faixa(subtotal, esperado):
    """RN04 a RN07: percentual de desconto correto em cada faixa e nas fronteiras."""
    # Arrange
    valor = subtotal

    # Act
    resultado = calcular_percentual_desconto(valor)

    # Assert
    assert resultado == esperado


@pytest.mark.unit
@pytest.mark.parametrize(
    "subtotal, excecao",
    [(-1, ValueError), ("100", TypeError)],
    ids=["negativo", "texto"],
)
def test_calcular_percentual_desconto_rejeita_entradas_invalidas(subtotal, excecao):
    """RN09: subtotal invalido levanta ValueError; tipo incorreto levanta TypeError."""
    # Arrange
    valor = subtotal

    # Act
    with pytest.raises(excecao):
        calcular_percentual_desconto(valor)

    # Assert


@pytest.mark.unit
@pytest.mark.parametrize(
    "preco, quantidade, esperado",
    [(99.99, 1, 99.99), (100.00, 1, 95.00), (500.00, 1, 425.00)],
    ids=["sem_desconto", "desconto_5_no_limite_100", "desconto_15_no_limite_500"],
)
def test_calcular_valor_final_aplica_desconto_correto(preco, quantidade, esperado):
    """RN08: valor final = subtotal - desconto, arredondado a 2 casas."""
    # Arrange
    valor_preco = preco
    valor_quantidade = quantidade

    # Act
    resultado = calcular_valor_final(valor_preco, valor_quantidade)

    # Assert
    assert resultado == esperado


@pytest.mark.unit
@pytest.mark.parametrize(
    "preco, quantidade, excecao",
    [(-5, 1, ValueError), (None, 1, TypeError)],
    ids=["preco_negativo", "preco_none"],
)
def test_calcular_valor_final_rejeita_entradas_invalidas(preco, quantidade, excecao):
    """RN09: entradas invalidas levantam a excecao correta no calculo final."""
    # Arrange
    valor_preco = preco
    valor_quantidade = quantidade

    # Act
    with pytest.raises(excecao):
        calcular_valor_final(valor_preco, valor_quantidade)

    # Assert
