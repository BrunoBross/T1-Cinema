from limite.tela_filme import TelaFilme
from entidade.filme import Filme


class ControladorFilmes:

	def __init__(self, controlador_sistema):
		self.__controlador_sistema = controlador_sistema
		self.__filmes = []
		self.__id_filmes = []
		self.__tela_filme = TelaFilme()
		self.__contador = 0

	def pega_filme_por_id(self, id_filme: int):
		for filme in self.__filmes:
			if filme.id_filme == id_filme:
				return filme
		return None

	def checa_id(self, id_filme: str):
		if id_filme.isdecimal():
			if int(id_filme) in self.__id_filmes:
				return True
			else:
				return False
		else:
			return False

	def retornar(self):
		self.__controlador_sistema.abre_tela()

	def incluir_filme(self):
		dados_filme = self.__tela_filme.pega_dados_filme()
		if dados_filme is not None:
			filme = Filme(self.__contador+1, dados_filme)
			self.__filmes.append(filme)
			self.__contador += 1
			self.__id_filmes.append(self.__contador)

	def alterar_filme(self):
		if len(self.__filmes) < 1:
			self.__tela_filme.mostra_mensagem('Não existem filmes cadastrados')
			return
		self.lista_filmes()
		id_filme = self.__tela_filme.seleciona_filme()
		if self.checa_id(id_filme):
			filme = self.pega_filme_por_id(int(id_filme))
			if filme is not None:
				novos_dados_filme = self.__tela_filme.pega_dados_filme()
				if novos_dados_filme is not None:
					filme.titulo = novos_dados_filme
					self.lista_filmes()
			else:
				self.__tela_filme.mostra_mensagem("ATENÇÃO: filme não existente")
		else:
			self.__tela_filme.mostra_mensagem(f'"{id_filme}" não é válido, operação cancelada')

	def lista_filmes(self):
		self.__tela_filme.mostra_mensagem("\n\033[1;96m-------==X( LISTA FILMES )X==-------\033[0;0m")
		for filme in self.__filmes:
			self.__tela_filme.mostra_filme({
				"titulo": filme.titulo,
				"id_filme": filme.id_filme
			})

	def excluir_filme(self):
		if len(self.__filmes) < 1:
			self.__tela_filme.mostra_mensagem('Não existem filmes cadastrados')
			return
		while True:
			self.lista_filmes()
			id_filme = self.__tela_filme.seleciona_filme()
			if self.checa_id(id_filme):
				filme = self.pega_filme_por_id(int(id_filme))
				if filme is not None:
					titulo = filme.titulo
					quantidade = len(self.__filmes)
					self.__filmes.remove(filme)
					if quantidade+1 == len(self.__filmes):
						self.__tela_filme.mostra_mensagem(f'O filme {titulo} foi removido do sistema')
				else:
					self.__tela_filme.mostra_mensagem("ATENÇÃO: Filme não existente")
			else:
				self.__tela_filme.mostra_mensagem('\t\tTente novamente!')

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

	@property
	def id_filmes(self):
		return self.__id_filmes

	@property
	def filmes(self):
		return self.__filmes
