import pytest

def soma_numeros(*args):
    soma = 0
    for item in args:
        try:
            soma = soma + item
        except TypeError:
            raise TypeError('Incompatibilidade de tipos. Verificar parâmetros')
    return soma


assert soma_numeros(1,2,3,4,5) == 15
with pytest.raises(TypeError) as error:
    soma_numeros(1,2,3,"4",5)
assert str(error.value) == 'Incompatibilidade de tipos. Verificar parâmetros'
