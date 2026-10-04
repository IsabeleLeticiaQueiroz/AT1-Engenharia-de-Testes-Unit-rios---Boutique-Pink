import math

# Constantes de negocio
QUANTIDADE_MINIMA = 1
QUANTIDADE_MAXIMA = 50
LIMITE_FAIXA_5 = 100.00
LIMITE_FAIXA_10 = 300.00
LIMITE_FAIXA_15 = 500.00


def _validar_valor_positivo(valor: float, nome: str) -> float:
    """Valida que o valor e numerico (int ou float), finito e maior que zero (RN01 e RN09)."""
    # bool e subclasse de int, por isso precisa ser checado antes
    if isinstance(valor, bool) or not isinstance(valor, (int, float)):
        raise TypeError(f"{nome} deve ser numerico (int ou float).")
    if not math.isfinite(valor):
        raise ValueError(f"{nome} deve ser um numero finito.")
    if valor <= 0:
        raise ValueError(f"{nome} deve ser maior que zero.")
    return float(valor)


def validar_preco(preco: float) -> float:
    """Valida o preco unitario de um produto (RN01 e RN09)."""
    return _validar_valor_positivo(preco, "O preco")


def validar_quantidade(quantidade: int) -> int:
    """Valida que a quantidade e um inteiro entre 1 e 50 (RN02 e RN09)."""
    if isinstance(quantidade, bool) or not isinstance(quantidade, int):
        raise TypeError("A quantidade deve ser um numero inteiro.")
    if quantidade < QUANTIDADE_MINIMA or quantidade > QUANTIDADE_MAXIMA:
        raise ValueError(
            f"A quantidade deve estar entre {QUANTIDADE_MINIMA} e {QUANTIDADE_MAXIMA}."
        )
    return quantidade


def calcular_subtotal(preco: float, quantidade: int) -> float:
    """Calcula o subtotal: preco x quantidade, arredondado a 2 casas (RN03)."""
    preco_valido = validar_preco(preco)
    quantidade_valida = validar_quantidade(quantidade)
    return round(preco_valido * quantidade_valida, 2)


def calcular_percentual_desconto(subtotal: float) -> float:
    """Retorna o percentual de desconto conforme a faixa do subtotal (RN04 a RN07).

    - abaixo de 100,00: 0%
    - de 100,00 ate 299,99: 5%
    - de 300,00 ate 499,99: 10%
    - a partir de 500,00: 15%
    """
    valor = _validar_valor_positivo(subtotal, "O subtotal")
    if valor < LIMITE_FAIXA_5:
        return 0.00
    if valor < LIMITE_FAIXA_10:
        return 0.05
    if valor < LIMITE_FAIXA_15:
        return 0.10
    return 0.15


def calcular_valor_final(preco: float, quantidade: int) -> float:
    """Calcula o valor final: subtotal - desconto, arredondado a 2 casas (RN08)."""
    subtotal = calcular_subtotal(preco, quantidade)
    percentual = calcular_percentual_desconto(subtotal)
    desconto = round(subtotal * percentual, 2)
    return round(subtotal - desconto, 2)