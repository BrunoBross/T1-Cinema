from limite.tela_sessao import TelaSessao
from entidade.sessao import Sessao


class ControladorSessaos:

	def __init__(self, controlador_sistema):
		self.__controlador_sistema = controlador_sistema
		self.__sessaos = []
		self.__tela_sessao = TelaSessao()
		self.__contador = 0

	def pega_sessao_por_id(self, id_sessao: int):
		for sessao in self.__sessaos:
			if sessao.id_sessao == id_sessao:
				return sessao
			return None

	def retornar(self):
		self.__controlador_sistema.abre_tela()

	def incluir_sessao(self):
		dados_sessao = self.__tela_sessao.pega_dados_sessao()
		sessao = Sessao(
			self.__contador+1,
			dados_sessao["horario"],
			dados_sessao["filme"],
			dados_sessao["sala"]
		)
		self.__sessaos.append(sessao)

	def alterar_sessao(self):
		self.lista_sessaos()
		id_sessao = self.__tela_sessao.seleciona_sessao()
		sessao = self.pega_sessao_por_id(id_sessao)

		if sessao is not None:
			novos_dados_sessao = self.__tela_sessao.pega_dados_sessao()
			sessao.horario = novos_dados_sessao["horario"]
			sessao.filme = novos_dados_sessao["filme"]
			sessao.sala = novos_dados_sessao["sala"]
			self.lista_sessaos()
		else:
			self.__tela_sessao.mostra_mensagem(
				"ATENCAO: sessao nao existente"
			)

	def lista_sessaos(self):
		for sessao in self.__sessaos:
			self.__tela_sessao.mostra_sessao({
				"horario": sessao.horario,
				"filme": sessao.filme,
				"sala": sessao.sala,
			})

	def excluir_sessao(self):
		self.lista_sessaos()
		id_sessao = self.__tela_sessao.seleciona_sessao()
		sessao = self.pega_sessao_por_id(int(id_sessao))

		if sessao is not None:
			self.__sessaos.remove(sessao)
			self.lista_sessaos()
		else:
			self.__tela_sessao.mostra_mensagem(
				"ATENCAO: Sessao nao existente"
			)

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
