from entidade.filme import Filme


class Genero:

	def __init__(self, id_genero: int, tipo: str):

		if isinstance(id_genero, int):
			self.__id_genero = id_genero

		if isinstance(tipo, str):
			self.__tipo = tipo

		self.__filmes = []

	@property
	def id_genero(self):
		return self.__id_genero

	@property
	def tipo(self):
		return self.__tipo

	@tipo.setter
	def tipo(self, tipo: str):

		if isinstance(tipo, str):
			self.__tipo = tipo

	@property
	def filmes(self):
		return self.__filmes

	@filmes.setter
	def filmes(self, filme: Filme):

		if isinstance(filme, Filme):
			self.__filmes.append(Filme)
