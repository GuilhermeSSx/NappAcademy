from ecommerce.classes.Produto import Produto
from ecommerce.classes.Pedido import Pedido
from ecommerce.classes.Estoque import Estoque


class Loja:
    def __init__(self, nome):
        self._nome = nome
        self._estoque = {}

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def estoque(self):
        return self._estoque

    def __str__(self):
        return self.nome

    def __repr__(self):
        return 'Nome da Loja => ' + self.nome

    def add_estoque(self, ean, preco, quantidade):
        if ean not in self._estoque:
            self._estoque[ean] = Estoque(preco, quantidade)
        else:
            self._estoque[ean].quantidade += quantidade
            self._estoque[ean].preco = preco

    def quantidade_produtos(self, ean):
        if ean in self._estoque:
            return self._estoque[ean].quantidade
        return 0

    def comprar(self, ean):
        if ean in self._estoque and self._estoque[ean].quantidade > 0:
            self._estoque[ean].quantidade -= 1
            produto = Produto(preco=self._estoque[ean].preco, ean=ean)
            return produto
        return None

    def devolver_carrinho(self, pedido):
        if isinstance(pedido, Pedido):
            for item in pedido.itens:
                if isinstance(item, Produto):
                    self.add_estoque(item.ean, item.preco, 1)
            pedido.itens = []
            return pedido
