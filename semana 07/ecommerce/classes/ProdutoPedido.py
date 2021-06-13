from ecommerce.classes.Produto import Produto

class ProdutoPedido:
    def __init__(self, produto, quantidade):
        if not isinstance(produto, Produto):
            raise Exception("Produto não informado")

        if not isinstance(quantidade, float) and not isinstance(quantidade, int):
            raise Exception("Quantidade deve ser decimal ou inteiro")
        if quantidade < 0:
            quantidade = 0

        self._produto = produto
        self._quantidade = quantidade

    @property
    def produto(self):
        return self._produto

    @produto.setter
    def preco(self, value):
        self._produto = value

    @property
    def quantidade(self):
        return self._quantidade

    @quantidade.setter
    def quantidade(self, value):
        self._quantidade = value

    def __str__(self):
        return f"{self._quantidade:5} [{self._produto.ean:5}] {self._produto.preco}"

