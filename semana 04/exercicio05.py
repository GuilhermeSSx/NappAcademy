import csv
from datetime import date, datetime


def find_born_monday(lista):
    """
    Função que recebe a lista com todos os registros carregados de um
    arquivo CSV via Reader e busca os clientes nascidos em uma segunda-feira.
    Args:
        lista (List): Lista de tuplas
    Returns:
        List: Lista com os nomes de pessoas que nasceram
        em uma segunda feira.
    """
    list_names = []
    for indice in lista:
        if len(indice[4]) == 10:
            birthday_convert_date = datetime.strptime(indice[4], "%Y-%m-%d").date()
            if birthday_convert_date.isoweekday() == 1: # numero indice da segunda feira
                list_names.append(indice[0])
        else:
            if len(indice[5]) == 10:
                birthday_convert_date = datetime.strptime(indice[5], "%Y-%m-%d").date()
                if birthday_convert_date.isoweekday() == 1:
                    list_names.append(indice[0])
    return list_names


def carregar_arquivo(path):
    """
    Função que recebe a string com o arquivo, abre o arquivo CSV
    com o reader e carrega os dados em uma lista retornada.
    Args:
        path (String): Nome do arquivo
    Returns:
        (List): Lista com todos os registros
    """
    local_list = []
    with open(path, newline='\n') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for line in reader:
            local_list.append(line)
    return local_list


if __name__ == "__main__":
    path = 'usernames.csv'
    lista = []
    lista = carregar_arquivo(path)
    nascidos_segunda_feira = find_born_monday(lista)
    print(nascidos_segunda_feira)