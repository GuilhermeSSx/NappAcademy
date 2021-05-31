from massa_dados import list_spend_money


def spend_by_login(login, limit=1000):
    for registro in list_spend_money:
        try:
            if registro[1] == login and float(registro[3]) <= limit:
                print(registro)
        except ValueError:
            pass

def sum_by_login(login, limit=600):
    lista_registros = []
    total = 0
    for registro in list_spend_money:
        if registro[1] == login:
            lista_registros.append(registro[3])
        for valor in lista_registros:
            if type(valor) == str and valor != '' or type(valor) == float:
                if float(valor) <= limit:
                    total += float(valor)
    return total

if __name__ == "__main__":
    login = 'justin16'
    spend_by_login(login, 1200)
    print('A soma total até 600: ')
    print(sum_by_login(login))
    print('A soma total até 1200: ')
    print(sum_by_login(login, 1200))