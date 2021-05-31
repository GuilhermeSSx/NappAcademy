from datetime import datetime, timedelta


def data_2_semanas():
    data_inicial = datetime.today()
    data_futura = data_inicial + timedelta(weeks= 2, days= 3)
    return data_futura.date()

if __name__ == "__main__":
    print('A data inicial após 2 semanas e 3 dias é: ', data_2_semanas())