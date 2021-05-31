from datetime import date, datetime, timedelta


def idade_pessoa(data_nascimento):
    data_atual = datetime.today()
    dias_ano = 365.2425
    idade = (data_atual.date() - datetime.strptime(data_nascimento, '%Y-%m-%d').date()) / dias_ano
    return idade.days

if __name__ == "__main__":
    print('A sua idade é:', idade_pessoa('1998-07-23'))

    