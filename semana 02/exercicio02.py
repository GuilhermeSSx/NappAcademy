from massa_dados import list_spend_money

def spend_by_gender(gender):
    for registro in list_spend_money:
        if registro[2] == gender:
            print(registro)

def sum_by_gender(gender):
    lista_genero =[]
    total = 0
    for registro in list_spend_money:
        if registro[2] == gender:
            lista_genero.append(registro[3])
        for valor in lista_genero:
            if type(valor) == str and valor != '' or type(valor) == float:
                total += float(valor)
    return total

if __name__ == "__main__":
    gender = 'M'
    spend_by_gender(gender)
    print('A soma total é: ')
    print(round(sum_by_gender(gender), 2))
    