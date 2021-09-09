from limite.tela_sessao import TelaSessao
from entidade.sessao import Sessao


class ControladorSessaos:

	def __init__(self, controlador_sistema):
		self.__controlador_sistema = controlador_sistema
		self.__sessaos = []
		self.__id_sessaos = []
		self.__tela_sessao = TelaSessao()
		self.__contador = 0

	def pega_sessao_por_id(self, id_sessao: int):
		for sessao in self.__sessaos:
			if sessao.id_sessao == id_sessao:
				return sessao
		return None

	def existem_sessaos_cadastrados(self):
		if len(self.sessaos) > 0:
			return True
		self.__tela_sessao.mostra_mensagem('\nNão há sessões cadastradas')
		return False

	def checa_atributos(self, dados: list):
		for sessao in self.__sessaos:
			if sessao.sala in dados and sessao.filme in dados and sessao.horario in dados:
				self.__tela_sessao.mostra_mensagem('Sessão já cadastrada!')
				return False
		return True

	def retornar(self):
		self.__controlador_sistema.abre_tela()

	def incluir_sessao(self):
		dados_sessao = self.__tela_sessao.pega_dados_sessao(
			self.__controlador_sistema.controlador_filmes.dados_lista_filmes(),
			self.__controlador_sistema.controlador_salas.dados_lista_salas()
		)
		if dados_sessao is not None:
			if self.checa_atributos(dados_sessao):
				sessao = Sessao(self.__contador+1, dados_sessao[0], dados_sessao[1], dados_sessao[2])
				self.__sessaos.append(sessao)
				self.__contador += 1
				self.__id_sessaos.append(self.__contador)

	def alterar_sessao(self):
		pass

	def lista_sessaos(self):
		pass

	def excluir_sessao(self):
		pass

	def abre_tela(self):
		lista_opcoes = {
			0: self.retornar,
			1: self.incluir_sessao,
			2: self.alterar_sessao,
			3: self.lista_sessaos,
			4: self.excluir_sessao
		}

		while True:
			lista_opcoes[self.__tela_sessao.tela_opcoes()]()

	@property
	def id_sessaos(self):
		return self.__id_sessaos

	@property
	def sessaos(self):
		return self.__sessaos
