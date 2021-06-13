from ecommerce.classes.Cliente import Cliente
from ecommerce.classes.Produto import Produto
from ecommerce.classes.ProdutoPedido import ProdutoPedido


class Pedido:
    formas_aceitas = ['dinheiro', 'cartão', 'pix']

    def __init__(self, cliente):
        if not isinstance(cliente, Cliente):
            raise TypeError('Não é possível instanciar um Pedido sem um cliente')
        self._cliente = cliente
        self._itens = {}

    @property
    def itens(self):
        return self._itens

    @itens.setter
    def itens(self, value):
        self._itens = value

    @property
    def cliente(self):
        return self._cliente

    def __str__(self):
        return f'Pedido de {self._cliente}'

    def __repr__(self):
        return f'Pedido de {self._cliente}'

    def add_item(self, produto):
        if not isinstance(produto, Produto):
            raise TypeError('Não foi passado um objeto produto')
        if produto.ean not in self._itens:
            self._itens[produto.ean] = ProdutoPedido(produto, 1)
        else:
            self._itens[produto.ean].quantidade += 1

    def quantidade_produto_no_pedido(self, ean):
        if ean in self._itens:
            return self._itens[ean].quantidade
        return 0

    def nota_fiscal(self):
        nota_produtos = []
        set_produtos = []
        for item in self._itens:
            set_produtos.append(str(item))
        set_produtos = set(set_produtos)
        for produto in set_produtos:
            quantidade = self.quantidade_produto_no_pedido(str(produto))
            nota_produtos.append((produto, quantidade))
        return nota_produtos

    def valor_total_pagar(self):
        total_pagar = 0
        for ean in self._itens:
            total_pagar += self._itens[ean].produto.preco * self._itens[ean].quantidade
        return total_pagar

    def checkout(self, forma_pagamento=None):
        if not forma_pagamento:
            raise Exception('Informe um meio de pagamento')
        if forma_pagamento.lower() in self.formas_aceitas:
            dados_checkout = (self.nota_fiscal(), self.valor_total_pagar())
            return dados_checkout
        raise Exception('Forma de pagamento não aceita')
