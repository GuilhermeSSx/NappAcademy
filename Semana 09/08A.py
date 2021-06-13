'''
8A: Cálculo de média simples.
'''


def calculo_media():
    numero_1 = float(input('Digite o primeiro número:  '))
    numero_2 = float(input('Digite o segundo número:  '))
    numero_3 = float(input('Digite o terceiro número:  '))
    media = (numero_1 + numero_2 + numero_3) / 3
    print('A média é: ' + str(media))


calculo_media()
