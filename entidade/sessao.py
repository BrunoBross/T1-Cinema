from entidade.filme import Filme
from entidade.sala import Sala

class Sessao:

	def __init__(self, id_sessao: int, horario: str, filme: Filme, sala: Sala):

		if isinstance(id_sessao, int):
			self.__id_sessao = id_sessao

		if isinstance(horario, str):
			self.__horario = horario

		if isinstance(filme, Filme):
			self.__filme = filme

		if isinstance(sala, Sala):
			self.__sala = sala

	@property
	def id_sessao(self):
		return self.__id_sessao

	@property
	def horario(self):
		return self.__horario

	@horario.setter
	def horario(self, horario: str):

		if isinstance(horario, str):
			self.__horario = horario

	@property
	def filme(self):
		return self.__filme

	@filme.setter
	def filme(self, filme: Filme):

		if isinstance(filme, Filme):
			self.__filme = filme

	@property
	def sala(self):
		return self.__sala

	@sala.setter
	def sala(self, sala: Sala):

		if isinstance(sala, Sala):
			self.__sala = sala
