

class Sala:

	def __init__(self, id_sala: int, numero: str):

		if isinstance(id_sala, int):
			self.__id_sala = id_sala

		if isinstance(numero, str):
			self.__numero = numero

	@property
	def id_sala(self):
		return self.__id_sala

	@property
	def numero(self):
		return self.__numero

	@numero.setter
	def numero(self, numero: str):

		if isinstance(numero, str):
			self.__numero = numero
