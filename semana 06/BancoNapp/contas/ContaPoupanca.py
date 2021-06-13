from BancoNapp.contas.Conta import Conta


class ContaPoupanca(Conta):
    """
    Classe representa a conta corrente de pessoa física.
    Limite padrão da conta: R$ 500,00
    Args:
        Conta ([type]): [description]
    """
    def __init__(self,  **kwargs):
        """
        Construtor da classe ContaPoupanca.
        Extrai do dicionário kwargs a profissao do correntista.
        """
        super(ContaPoupanca, self).__init__(**kwargs)
        self.profissao = kwargs.get('profissao', '')
        self.limite = kwargs.get('limite', 0)

    def rendimento_aniversario(self, valor):
        if valor < 0 or valor > 1:
            raise ValueError('Os juros precisam ser entre 0 (0%) e 1 (100%).')
        self.saldo += self.saldo*valor