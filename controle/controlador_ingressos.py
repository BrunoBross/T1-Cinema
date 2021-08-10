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
		dados_ingresso = self.__tela_ingresso.pega_dados_ingresso()
		ingresso = Ingresso(
			self.__contador+1,
			dados_ingresso["sessao"],
			dados_ingresso["fileira"],
			dados_ingresso["acento"]
		)
		self.__ingressos.append(ingresso)

	def alterar_ingresso(self):
		self.lista_ingressos()
		id_ingresso = self.__tela_ingresso.seleciona_ingresso()
		ingresso = self.pega_ingresso_por_id(id_ingresso)

		if ingresso is not None:
			novos_dados_ingresso = self.__tela_ingresso.pega_dados_ingresso()
			ingresso.sessao = novos_dados_ingresso["sessao"]
			ingresso.fileira = novos_dados_ingresso["fileira"]
			ingresso.acento = novos_dados_ingresso["acento"]
			self.lista_ingressos()
		else:
			self.__tela_ingresso.mostra_mensagem(
				"ATENCAO: ingresso nao existente"
			)

	def lista_ingressos(self):
    	contador = len(self.__ingressos)
		if contador == 1:
			self.__tela_ingresso.mostra_mensagem("\n-------==X( FILME DISPONÍVEL )X==-------")
		else:
			self.__tela_ingresso.mostra_mensagem(f"\n-------==X( LISTA DE FILMES ({contador}) )X==-------")
			
		for ingresso in self.__ingressos:
			self.__tela_ingresso.mostra_ingresso({
				"sessao": ingresso.sessao,
				"fileira": ingresso.fileira,
				"acento": ingresso.acento,
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
