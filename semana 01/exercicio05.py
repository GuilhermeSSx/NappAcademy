
lista_frases = ['Eu gosto de batatas', 'Eu estava andando de moto']
lista_frases += ['Ele estava comendo no restaurante']
lista_frases += ['O cachorro está passeando pelo parque']

for frase in lista_frases:
    lista_palavras = frase.split()
    for palavra in lista_palavras:
        if "ando" in palavra:
            print(palavra)
        elif "endo" in palavra:
            print(palavra)
        elif "indo" in palavra:
            print(palavra)


