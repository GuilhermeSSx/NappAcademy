import csv
path = 'usernames.csv'


def buscar_cartao_expira_2030_v1(path, parametro='322'):
    """
    Função abre o arquivo .csv, realiza a leitura via DictReader e busca
    a string 'parâmetro' como substring do campo 'Cartão de Crédito'.

    Args:
        path (String): String com o nome do arquivo
        parametro (str, optional): Substring a ser encontrada. Padrão '322'.

    Returns:
        List: Lista de dicionários
    """
    lista_completa = []
    lista_nomes = []
    with open(path, newline='\n') as csvfile:
        reader = csv.DictReader(csvfile)
        for line in reader:
            lista_completa.append(line)
    for item in lista_completa:
        try:
            if parametro in item.get('credit_card'):
                lista_nomes.append(item['name'])
        except KeyError:
            print(KeyError)
    return lista_nomes


def find_start_subtring_credit_card(path, parametro='303'):
    """
    Função abre o arquivo .csv, realiza a leitura via DictReader busca
    a string 'parâmetro' como início do campo 'Cartão de Crédito' .

    Args:
        path (String): String com o nome do arquivo
        parametro (str, optional): Substring a ser encontrada. Padrão '303'.

    Returns:
        List: Lista de dicionários
    """
    lista_completa = []
    lista_nomes = []
    with open(path, newline='\n') as csvfile:
        reader = csv.DictReader(csvfile)
        for line in reader:
            lista_completa.append(line)
    for item in lista_completa:
        try:
            if parametro in item.get('credit_card')[0:3]:
                lista_nomes.append(item['name'])
        except KeyError:
            print(KeyError)
    return lista_nomes


if __name__ == "__main__":
    print('--- Refatoração do Exercicio 01 ---')
    print(buscar_cartao_expira_2030_v1(path))
    print(buscar_cartao_expira_2030_v1(path, '222'))
    print('\n--- Refatoração do Exercicio 02 ---')
    print(find_start_subtring_credit_card(path))
    print(find_start_subtring_credit_card(path, '222'))