import pytest

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

meses = dict(
    zip(list(range(1, 13)), lista_meses)
)

def data_por_extenso(data):
    """
    Recebe uma data no formado dd/MM/aaaa e retorna por extenso.
    Entrada '10/12/2020'
    Saída '10 de dezembro de 2020'

    Args:
        data ([str]): Data no formado dd/MM/aaaa

    Returns:
        [str]: Data por extenso
    """
    data = data.split('/')
    try:
        return data[0] + ' de ' + meses[int(data[1])] + ' de ' + data[2]
    except KeyError:
        raise KeyError('Mês inválido')


def test():
    assert data_por_extenso("06/10/1994") == "06 de outubro de 1994"
    with pytest.raises(KeyError) as error:
        data_por_extenso("00/00/0000")
    assert str(error.value) == "'Mês inválido'"
