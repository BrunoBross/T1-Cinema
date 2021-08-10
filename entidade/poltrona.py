

class Poltrona:

	def __init__(self, id_poltrona: int, fileira: str, acento: str):

		if isinstance(id_poltrona, int):
			self.__id_poltrona = id_poltrona

		if isinstance(fileira, str):
			self.__fileira = fileira

		if isinstance(acento, str):
			self.__acento = acento

	@property
	def id_poltrona(self):
		return self.__id_poltrona

	@property
	def fileira(self):
		return self.__fileira

	@fileira.setter
	def fileira(self, fileira: str):

		if isinstance(fileira, str):
			self.__fileira = fileira

	@property
	def acento(self):
		return self.__acento

	@acento.setter
	def acento(self, acento: str):

		if isinstance(acento, str):
			self.__acento = acento
