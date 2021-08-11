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
		self.__controlador_sistema.controlador_filmes.lista_filmes()
		self.__controlador_sistema.controlador_salas.lista_salas()
		dados_sessao = self.__tela_sessao.pega_dados_sessao()
		id_filme = self.__controlador_sistema.controlador_filmes.pega_filme_por_id(dados_sessao["filme"])
		dados_sessao["filme"] = id_filme
		id_sala = self.__controlador_sistema.controlador_salas.pega_sala_por_id(dados_sessao["sala"])
		dados_sessao["sala"] = id_sala
		sessao = Sessao(
			self.__contador+1,
			dados_sessao["filme"],
			dados_sessao["horario"],
			dados_sessao["sala"]
		)
		self.__sessaos.append(sessao)
		self.__contador += 1

	def alterar_sessao(self):
		self.lista_sessaos()
		id_sessao = self.__tela_sessao.seleciona_sessao()
		sessao = self.pega_sessao_por_id(int(id_sessao))

		if sessao is not None:
			self.__controlador_sistema.controlador_filmes.lista_filmes()
			self.__controlador_sistema.controlador_salas.lista_salas()
			novos_dados_sessao = self.__tela_sessao.pega_dados_sessao()
			sessao.filme = novos_dados_sessao["filme"]
			sessao.horario = novos_dados_sessao["horario"]
			sessao.sala = novos_dados_sessao["sala"]
			self.lista_sessaos()
		else:
			self.__tela_sessao.mostra_mensagem(
				"ATENCAO: sessao nao existente"
			)

	def lista_sessaos(self):
		self.__tela_sessao.mostra_mensagem("-------==X( LISTA SESSAOS )X==-------")
		for sessao in self.__sessaos:
			self.__tela_sessao.mostra_sessao({
				"filme": sessao.filme.titulo,
				"horario": sessao.horario,
				"sala": sessao.sala.numero,
				"id_sessao": sessao.id_sessao
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
