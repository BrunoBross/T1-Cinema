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
		self.__tela_filme.mostra_mensagem(f'\nNão há filmes cadastrados.')
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
		dados_filme = self.__tela_filme.pega_dados_filme()
		if dados_filme is not None:
			filme = Filme(self.__contador+1, dados_filme)
			self.__filmes.append(filme)
			self.__contador += 1
			self.__id_filmes.append(self.__contador)

	def alterar_filme(self):
		if self.existem_filmes_cadastrados():
			id_filme = self.__tela_filme.seleciona_filme(self.dados_lista_filmes())
			if id_filme is not None:
				filme = self.pega_filme_por_id(int(id_filme))
				novos_dados_filme = self.__tela_filme.altera_filme()
				if novos_dados_filme is not None:
					filme.titulo = novos_dados_filme

	def dados_lista_filmes(self):
		return [f'ID: {filme.id_filme}    Título: {filme.titulo}' for filme in self.filmes]

	def lista_filmes(self):
		if self.existem_filmes_cadastrados():
			self.__tela_filme.popup_lista_filme(self.dados_lista_filmes())

	def excluir_filme(self):
		if self.existem_filmes_cadastrados():
			id_filme = self.__tela_filme.exclui_filme(self.dados_lista_filmes())
			if id_filme is not None:
				filme = self.pega_filme_por_id(int(id_filme))
				nome = filme.titulo
				self.__filmes.remove(filme)
				self.__tela_filme.mostra_mensagem(f'\nO filme "{nome}"\nfoi removido com sucesso')

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
