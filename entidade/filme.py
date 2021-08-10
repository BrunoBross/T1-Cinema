

class Filme:

	def __init__(self, id_filme: int, titulo: str):

		if isinstance(id_filme, int):
			self.__id_filme = id_filme

		if isinstance(titulo, str):
			self.__titulo = titulo

	@property
	def id_filme(self):
		return self.__id_filme

	@property
	def titulo(self):
		return self.__titulo

	@titulo.setter
	def titulo(self, titulo: str):

		if isinstance(titulo, str):
			self.__titulo = titulo