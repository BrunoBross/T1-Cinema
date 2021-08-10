

class Genero:

	def __init__(self, id_genero: int, nome: str):

		if isinstance(id_genero, int):
			self.__id_genero = id_genero

		if isinstance(nome, str):
			self.__nome = nome

	@property
	def id_genero(self):
		return self.__id_genero

	@property
	def nome(self):
		return self.__nome

	@nome.setter
	def nome(self, nome: str):

		if isinstance(nome, str):
			self.__nome = nome
