import pytest

def situacao_escolar(nota_final, ausencias=0):
    if ausencias < 0 or ausencias > 80:
        raise Exception('Ausências entre 0 e 80')
    if nota_final < 0 or nota_final > 10:
        raise Exception('Nota Final entre 0 e 10')
    if ausencias > 40:
        return 'Reprovado por falta'
    if nota_final < 5:
        return 'Reprovado por nota'
    if nota_final < 7:
        return 'Reprovado, em regime de recuperação'
    return 'Aprovado'


assert situacao_escolar(10, 2) == 'Aprovado'
assert situacao_escolar(5, 5) == 'Reprovado, em regime de recuperação'
assert situacao_escolar(4, 35) == 'Reprovado por nota'
assert situacao_escolar(10, 45) == 'Reprovado por falta'
with pytest.raises(Exception) as error:
    situacao_escolar(10, 85)
assert str(error.value) == 'Ausências entre 0 e 80'
with pytest.raises(Exception) as error:
    situacao_escolar(11, 11)
assert str(error.value) == 'Nota Final entre 0 e 10'
