from limite.tela_filme import TelaFilme
from entidade.filme import Filme


class ControladorFilmes:

	def __init__(self, controlador_sistema):
		self.__controlador_sistema = controlador_sistema
		self.__filmes = []
		self.__tela_filme = TelaFilme()
		self.__contador = 0

	def pega_filme_por_id(self, id_filme: int):
		for filme in self.__filmes:
			if filme.id_filme == id_filme:
				return filme
		return None

	def retornar(self):
		self.__controlador_sistema.abre_tela()

	def incluir_filme(self):
		dados_filme = self.__tela_filme.pega_dados_filme()
		filme = Filme(
			self.__contador+1,
			dados_filme["titulo"]
		)
		self.__filmes.append(filme)
		self.__contador += 1

	def alterar_filme(self):
		self.lista_filmes()
		id_filme = self.__tela_filme.seleciona_filme()
		filme = self.pega_filme_por_id(int(id_filme))

		if filme is not None:
			novos_dados_filme = self.__tela_filme.pega_dados_filme()
			filme.titulo = novos_dados_filme["titulo"]
			self.lista_filmes()
		else:
			self.__tela_filme.mostra_mensagem(
				"ATENCAO: filme nao existente"
			)

	def lista_filmes(self):
		self.__tela_filme.mostra_mensagem("-------==X( LISTA FILMES )X==-------")
		for filme in self.__filmes:
			self.__tela_filme.mostra_filme({
				"titulo": filme.titulo,
				"id_filme": filme.id_filme
			})

	def excluir_filme(self):
		self.lista_filmes()
		id_filme = self.__tela_filme.seleciona_filme()
		filme = self.pega_filme_por_id(int(id_filme))

		if filme is not None:
			self.__filmes.remove(filme)
			self.lista_filmes()
		else:
			self.__tela_filme.mostra_mensagem(
				"ATENCAO: Filme nao existente"
			)

	def abre_tela(self):
		lista_opcoes = {
			0: self.retornar,
			1: self.incluir_filme,
			2: self.alterar_filme,
			3: self.lista_filmes,
			4: self.excluir_filme
		}

		while True:
			lista_opcoes[self.__tela_filme.tela_opcoes()]()
