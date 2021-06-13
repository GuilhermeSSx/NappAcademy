class Estoque:
    def __init__(self, preco, quantidade):
        if not isinstance(preco, float) and not isinstance(preco, int):
            raise Exception("Preço deve ser decimal ou inteiro")
        if preco < 0:
            raise Exception("Preço deve ser maior ou igual a 0")

        if not isinstance(quantidade, float) and not isinstance(quantidade, int):
            raise Exception("Quantidade deve ser decimal ou inteiro")
        if quantidade < 0:
            quantidade = 0

        self._preco = preco
        self._quantidade = quantidade

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, value):
        self._preco = value

    @property
    def quantidade(self):
        return self._quantidade

    @quantidade.setter
    def quantidade(self, value):
        self._quantidade = value

