from entidade.sessao import Sessao

class Ingresso:

	def __init__(self, id_ingresso: int, sessao: Sessao, fileira: str, acento: str):

		if isinstance(id_ingresso, int):
			self.__id_ingresso = id_ingresso

		if isinstance(sessao, Sessao):
			self.__sessao = sessao

		if isinstance(fileira, str):
			self.__fileira = fileira

		if isinstance(acento, str):
			self.__acento = acento

	@property
	def id_ingresso(self):
		return self.__id_ingresso

	@property
	def sessao(self):
		return self.__sessao

	@sessao.setter
	def sessao(self, sessao: Sessao):

		if isinstance(sessao, Sessao):
			self.__sessao = sessao

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
