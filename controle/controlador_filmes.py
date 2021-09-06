from limite.tela_filme import TelaFilme
from entidade.filme import Filme


class ControladorFilmes:

	def __init__(self, controlador_sistema):
		self.__controlador_sistema = controlador_sistema
		self.__filmes = []
		self.__id_filmes = []
		self.__tela_filme = TelaFilme()
		self.__contador = 0
		self.__filme_com_genero_existe = [False]

	def pega_filme_por_id(self, id_filme: int):
		for filme in self.__filmes:
			if filme.id_filme == id_filme:
				return filme
		return None

	def existem_filmes_cadastrados(self):
		if len(self.filmes) > 0:
			return True
		self.__tela_filme.mostra_mensagem('\n\033[1;31mNão há filmes disponíveis, crie um antes.\033[0;0m')
		return False

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
		self.__tela_filme.mostra_mensagem("\n\033[1;96m-------==X( INCLUIR FILMES )X==-------\033[0;0m")
		dados_filme = self.__tela_filme.pega_dados_filme()
		if dados_filme is not None:
			filme = Filme(self.__contador+1, dados_filme)
			self.__filmes.append(filme)
			self.__contador += 1
			self.__id_filmes.append(self.__contador)

	def alterar_filme(self):
		tela = self.__tela_filme

		tela.mostra_mensagem("\n\033[1;96m-------==X( ALTERAR FILMES )X==-------\033[0;0m")

		if self.existem_filmes_cadastrados():
			while True:
				if len(self.__filmes) > 0:
					self.lista_filmes()
					id_filme = tela.seleciona_filme()
					if self.checa_id(id_filme):
						filme = self.pega_filme_por_id(int(id_filme))
						if filme is not None:
							tela.mostra_mensagem("\n\033[1;96m-------==X( NOVO TÍTULO FILME )X==-------\033[0;0m")
							novos_dados_filme = tela.pega_dados_filme()
							if novos_dados_filme is not None:
								filme.titulo = novos_dados_filme
								self.lista_filmes()
							else:
								return
						else:
							tela.mostra_mensagem("\n\033[1;31mATENÇÃO: filme não existente.\033[0;0m")
					else:
						tela.mostra_mensagem(f'\n\033[1;31m"{id_filme}" não é um ID válido, tente novamente.\033[0;0m')
				else:
					self.lista_filmes()

	def lista_filmes(self):
		self.__tela_filme.popup_lista_filme(
			[f'ID: {filme.id_filme}    Título: {filme.titulo}' for filme in self.filmes]
		)

	def excluir_filme(self):
		tela = self.__tela_filme

		tela.mostra_mensagem("\n\033[1;96m-------==X( EXCLUIR FILMES )X==-------\033[0;0m")

		if self.existem_filmes_cadastrados():
			self.lista_filmes()
			while True:

				id_filme = tela.seleciona_filme()
				if self.checa_id(id_filme):
					filme = self.pega_filme_por_id(int(id_filme))
					if filme is not None:
						titulo = filme.titulo
						self.__filmes.remove(filme)
						tela.mostra_mensagem(f'\nO filme \033[1;96m{titulo}\033[0;0m foi \033[1;31mremovido\033[0;0m do sistema.')
						return
					else:
						tela.mostra_mensagem("\n\033[1;31mATENÇÃO: Filme não existente.\033[0;0m")
				else:
					tela.mostra_mensagem('\n\033[1;31mDigite um ID válido!\033[0;0m')

	def listar_generos_por_id(self):
		tela = self.__tela_filme

		if self.existem_filmes_cadastrados():
			if not self.__filme_com_genero_existe[0]:
				tela.mostra_mensagem('\n\033[1;31mNenhum filme com gênero registrado.\033[0;0m')
				return
			while True:
				self.lista_filmes()
				id_filme = tela.seleciona_filme()
				if self.checa_id(id_filme):
					filme = self.pega_filme_por_id(int(id_filme))
					generos = filme.generos
					tela.lista_generos_do_filme(generos, filme)
					return
				tela.mostra_mensagem('\n\033[1;31mID inválido, tente novamente.\033[0;0m')

	def abre_tela(self):
		lista_opcoes = {
			0: self.retornar,
			1: self.incluir_filme,
			2: self.alterar_filme,
			3: self.lista_filmes,
			4: self.excluir_filme,
			5: self.listar_generos_por_id
		}

		while True:
			lista_opcoes[self.__tela_filme.tela_opcoes()]()

	@property
	def id_filmes(self):
		return self.__id_filmes

	@property
	def filmes(self):
		return self.__filmes

	@property
	def tela(self):
		return self.__tela_filme

	@property
	def filme_com_genero_existe(self):
		return self.__filme_com_genero_existe

	@filme_com_genero_existe.setter
	def filme_com_genero_existe(self, valor: bool):
		self.__filme_com_genero_existe.insert(0, valor)
