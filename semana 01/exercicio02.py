
lista_nomes = ['Ana', 'Maria', 'José', 'Pedro', 'Elena', 'Helena', 'elen']
vogais = ['A', 'E', 'I', 'O', 'U']


for nome in lista_nomes:
    for vogal in vogais:
        if nome[0].upper() == vogal:
            print(nome)