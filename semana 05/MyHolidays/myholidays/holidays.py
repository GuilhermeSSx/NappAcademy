from datetime import date, datetime

class MyCalendar:
	def __init__(self, *args):
		self.datas = []
		self.add_holiday(*args)

	def validar_data(self, data):
		if isinstance(data, date):
			return data
		elif isinstance(data, str):
			try:
				return datetime.strptime(data, '%d/%m/%Y').date()
			except:
				return None

	def add_holiday(self, *args):
		for data in args:
			data_arg = self.validar_data(data)
			if data_arg:
				self.datas.append(data_arg)
		self.datas = list(set(self.datas))

	def check_holiday(self, data):
		return self.validar_data(data) in self.datas