from massa_dados import list_spend_money

def spend_by_subname(name):
    for registro in list_spend_money:
        if 'Brown' in registro[0]:
            print(registro)

def sum_by_subname(name):
    lista_subnomes = []
    total = 0
    for registro in list_spend_money:
        if 'Brown' in registro[0]:
            lista_subnomes.append(registro[3])
        for valor in lista_subnomes:
            if type(valor) == str and valor != '' or type(valor) == float:
                total += float(valor)    
    return total

if __name__ == "__main__":
    name = 'Brown'
    spend_by_subname(name)
    print(f'A soma total é: \n{sum_by_subname(name):.2f}')