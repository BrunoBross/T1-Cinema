from limite.tela_ingresso import TelaIngresso
from entidade.ingresso import Ingresso


class ControladorIngressos:

	def __init__(self, controlador_sistema):
		self.__controlador_sistema = controlador_sistema
		self.__ingressos = []
		self.__tela_ingresso = TelaIngresso()
		self.__contador = 0

	def pega_ingresso_por_id(self, id_ingresso: int):
		for ingresso in self.__ingressos:
			if ingresso.id_ingresso == id_ingresso:
				return ingresso
		return None

	def retornar(self):
		self.__controlador_sistema.abre_tela()

	def incluir_ingresso(self):
		self.__controlador_sistema.controlador_sessaos.lista_sessaos()
		dados_ingresso = self.__tela_ingresso.pega_dados_ingresso()
		id_sessao = self.__controlador_sistema.controlador_sessaos.pega_sessao_por_id(dados_ingresso["sessao"])
		dados_ingresso["sessao"] = id_sessao
		ingresso = Ingresso(
			self.__contador+1,
			dados_ingresso["fileira"],
			dados_ingresso["acento"],
			dados_ingresso["sessao"]
		)
		self.__ingressos.append(ingresso)
		self.__contador += 1

	def alterar_ingresso(self):
		self.lista_ingressos()
		id_ingresso = self.__tela_ingresso.seleciona_ingresso()
		ingresso = self.pega_ingresso_por_id(int(id_ingresso))

		if ingresso is not None:
			self.__controlador_sistema.controlador_sessaos.lista_sessaos()
			novos_dados_ingresso = self.__tela_ingresso.pega_dados_ingresso()
			ingresso.fileira = novos_dados_ingresso["fileira"]
			ingresso.acento = novos_dados_ingresso["acento"]
			ingresso.sessao = novos_dados_ingresso["sessao"]
			self.lista_ingressos()
		else:
			self.__tela_ingresso.mostra_mensagem(
				"ATENCAO: ingresso nao existente"
			)

	def lista_ingressos(self):
		self.__tela_ingresso.mostra_mensagem("-------==X( LISTA INGRESSOS )X==-------")
		for ingresso in self.__ingressos:
			self.__tela_ingresso.mostra_ingresso({
				"poltrona": ingresso.poltrona,
				"sessao_horario": ingresso.sessao.horario,
				"sessao_filme": ingresso.sessao.filme.titulo,
				"id_ingresso": ingresso.id_ingresso
			})

	def excluir_ingresso(self):
		self.lista_ingressos()
		id_ingresso = self.__tela_ingresso.seleciona_ingresso()
		ingresso = self.pega_ingresso_por_id(int(id_ingresso))

		if ingresso is not None:
			self.__ingressos.remove(ingresso)
			self.lista_ingressos()
		else:
			self.__tela_ingresso.mostra_mensagem(
				"ATENCAO: Ingresso nao existente"
			)

	def abre_tela(self):
		lista_opcoes = {
			0: self.retornar,
			1: self.incluir_ingresso,
			2: self.alterar_ingresso,
			3: self.lista_ingressos,
			4: self.excluir_ingresso
		}

		while True:
			lista_opcoes[self.__tela_ingresso.tela_opcoes()]()
