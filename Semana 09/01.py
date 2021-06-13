import pytest

def juros_simples(capital, taxa=0.1, n_periodos=2):
    if capital <= 0:
        raise Exception('Capital precisa ser maior que zero.')
    if taxa < 0 or taxa > 1:
        raise Exception('Taxa precisa estar entre 0 e 1.')
    if n_periodos <= 0:
        raise Exception('Período precisa ser maior que zero.')
    return capital + capital * taxa * n_periodos


assert juros_simples(100, 0.2, n_periodos=6) == 220
assert juros_simples(200, 0.4, n_periodos=12) == 1160
with pytest.raises(Exception) as error:
    juros_simples(-20, 0.4, n_periodos=12)
assert str(error.value) == 'Capital precisa ser maior que zero.'
with pytest.raises(Exception) as error:
    juros_simples(20, -0.4, n_periodos=12)
assert str(error.value) == 'Taxa precisa estar entre 0 e 1.'
with pytest.raises(Exception) as error:
    juros_simples(20, 0.4, n_periodos=-12)
assert str(error.value) == 'Período precisa ser maior que zero.'
