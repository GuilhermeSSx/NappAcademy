def juros_compostos(valor_inicial, juros, tempo):
    """
    Calculadora de juros compostos
    Args:
        valor_inicial (float): Valor inicial.
        juros (float): Porcentagem dos juros, entre 0% e 100%.
        tempo (int): Tempo em meses.
    """
    juros = juros/100
    valor_final = valor_inicial * (1+juros)**tempo
    return round(valor_final, 2)