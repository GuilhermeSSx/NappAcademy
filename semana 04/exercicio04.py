from datetime import datetime


def dias_pos_copa():
    data_atual = datetime.today()
    data_copa = datetime.strptime("2014-07-08", "%Y-%m-%d")
    diff_dias = data_atual - data_copa
    return diff_dias.days

if __name__ == "__main__":
    print('A quantidade de dias após a copa são: ', dias_pos_copa())