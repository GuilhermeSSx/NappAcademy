from datetime import date, datetime


def quantos_dias_vida(data_nascimento):
    data_atual = date.today()
    dias_vida = data_atual - datetime.strptime(data_nascimento, '%Y-%m-%d').date()
    return dias_vida.days

if __name__ == "__main__":
    print('Seus dias de vida são: ', quantos_dias_vida('1998-07-23'))