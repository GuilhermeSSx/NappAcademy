'''
8B: Cálculo de média simples.
'''


def calculo_media(numero_1, numero_2, numero_3):
    return (numero_1 + numero_2 + numero_3) / 3


numero1 = float(input('Digite o primeiro número:  '))
numero2 = float(input('Digite o segundo número:  '))
numero3 = float(input('Digite o terceiro número:  '))

media = str(calculo_media(numero1, numero2, numero3))
print('A média é: ' + media)
