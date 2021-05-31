from massa_dados import list_spend_money

def spend_by_login(login):
    for registro in list_spend_money:
        if registro[1] == login:
            print(registro)
  
def sum_by_login(login):
    lista_registros = []
    total = 0
    for registro in list_spend_money:
        if registro[1] == login:
            lista_registros.append(registro[3])
    for valor in lista_registros:
        if type(valor) == str and valor != '' or type(valor) == float:
            total += float(valor)
    return total

if __name__ == "__main__":
    login = 'justin16'
    spend_by_login(login)
    print('A soma total é: ')
    print(round(sum_by_login(login), 2))
