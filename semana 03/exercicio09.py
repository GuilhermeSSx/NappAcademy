import csv
path='usernames.csv'

class buscar_nomes_cartao:
    """
    lista nomes com string OO
    """
    def __init__(self, parametro='322'):
        """
        Construtor de objetos para listar nomes com substring
        e inicio do campo do cartão.

        Args:
            parametro (int): numero do cartãopen_code
        """
        self.parametro = parametro
        self.busca_cartao_string = self.busca_cartao_OO_v1()
        self.busca_cartao_incial = self.busca_cartao_OO_v2()
    
    def busca_cartao_OO_v1(self):
        """
        Metódo para buscar cartões por string
        """
        lista_completa = []
        lista_nomes = []
        with open(path, newline='\n') as csvfile:
            reader = csv.DictReader(csvfile)
            for line in reader:
                lista_completa.append(line)
        for item in lista_completa:
            try:
                if self.parametro in item.get('credit_card'):
                    lista_nomes.append(item['name'])
            except KeyError:
                print(KeyError)
        return lista_nomes

    def busca_cartao_OO_v2(self):
        """
        Metódo para buscar cartões pela inicial do cartão
        """
        lista_completa = []
        lista_nomes = []
        with open(path, newline='\n') as csvfile:
            reader = csv.DictReader(csvfile)
            for line in reader:
                lista_completa.append(line)
        for item in lista_completa:
            try:
                if self.parametro in item.get('credit_card')[0:3]:
                    lista_nomes.append(item['name'])
            except KeyError:
                print(KeyError)
        return lista_nomes

print('--- Exercicio 01 e 02 em OO sem parametro ---')
buscar1 = buscar_nomes_cartao()
print(buscar1.busca_cartao_string)
print(buscar1.busca_cartao_incial)
print('\n--- Exercicio 01 e 02 em OO passando parametro ---')
buscar2 = buscar_nomes_cartao('222')
print(buscar2.busca_cartao_string)
print(buscar2.busca_cartao_incial)

