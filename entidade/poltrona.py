

class Poltrona:

	def __init__(self, fileira: str, acento: str):

		if isinstance(fileira, str) and isinstance(acento, str):
			self.__codigo = fileira+acento

	@property
	def codigo(self):
		return self.__codigo

	@codigo.setter
	def codigo(self, fileira: str, acento: str):

		if isinstance(fileira, str) and isinstance(acento, str):
			self.__codigo = fileira+acento
