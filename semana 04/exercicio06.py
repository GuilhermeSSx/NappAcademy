def calculo_porcentagem_entre_0_e_1(valor, porcentagem):
    """
    Cálculo de porcentagem onde o valor mínimo é 0
    e o valor máximo é 1.
    Args:
        valor (float): Valor inicial
        porcentagem (integer): Porcentagem entre 0 e 1
    Raises:
        ValueError: Caso a porcentagem não respeite o limite entre 0 e 1.
    Returns:
        float: Valor calculado da porcentagem do valor inicial
    """
    if porcentagem < 0 or porcentagem >1:
        raise ValueError("Porcentagem precisa estar entre 0 e 1")
    return valor * porcentagem