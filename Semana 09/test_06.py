import pytest
from seis import data_por_extenso

def test():
    assert data_por_extenso("06/10/1994") == "06 de outubro de 1994"
    with pytest.raises(KeyError) as error:
        data_por_extenso("00/00/0000")
    assert str(error.value) == "'Mês inválido'"
