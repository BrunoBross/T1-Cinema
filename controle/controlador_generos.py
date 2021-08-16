from limite.tela_genero import TelaGenero
from entidade.genero import Genero


class ControladorGeneros:

	def __init__(self, controlador_sistema):
		self.__controlador_sistema = controlador_sistema
		self.__generos = []
		self.__id_generos = []
		self.__tela_genero = TelaGenero()
		self.__contador = 0

	def pega_genero_por_id(self, id_genero: int):
		for genero in self.__generos:
			if genero.id_genero == id_genero:
				return genero
		return None

	def existem_generos_cadastrados(self):
		if len(self.generos) > 0:
			return True
		self.__tela_genero.mostra_mensagem('\n\033[1;31mNão há gêneros disponíveis, crie um antes.\033[0;0m')
		return False

	def checa_id(self, dado: str):
		if dado.isdecimal() and int(dado) in self.__id_generos:
			return True
		return False

	def checa_tipo(self, dado: str):
		if not dado:
			return None
		if dado.isalpha():
			for genero in self.__generos:
				if genero.tipo == dado:
					self.__tela_genero.mostra_mensagem(f'\nO gênero {dado} já está cadastrado.')
					return False
			return True
		self.__tela_genero.mostra_mensagem('\nEm letras por favor.')
		return False

	def retornar(self):
		self.__controlador_sistema.abre_tela()

	def incluir_genero(self):
		while True:
			tipo = self.__tela_genero.pega_dados_genero()
			if not tipo:
				self.__tela_genero.mostra_mensagem('\noperação cancelada')
				break
			if self.checa_tipo(tipo):
				genero = Genero(self.__contador+1, tipo)
				self.__generos.append(genero)
				self.__contador += 1
				self.__id_generos.append(self.__contador)
				break

	def alterar_genero(self):
		if self.existem_generos_cadastrados():
			self.lista_generos()
			id_genero = self.__tela_genero.seleciona_genero()
			if self.checa_id(id_genero):
				while True:
					tipo = self.__tela_genero.pega_dados_genero()
					checagem = self.checa_tipo(tipo)
					if checagem is not None:
						if checagem:
							self.pega_genero_por_id(int(id_genero)).tipo = tipo
							break
					else:
						self.__tela_genero.mostra_mensagem('\nOperação cancelada.')
						return

	def adiciona_filme(self):
		control_filme = self.__controlador_sistema.controlador_filmes
		tela = self.__tela_genero
		if self.existem_generos_cadastrados() and self.__controlador_sistema.controlador_filmes.existem_filmes_cadastrados():
			self.lista_generos()
			id_genero = tela.seleciona_genero()
			if self.checa_id(id_genero):
				genero = self.pega_genero_por_id(int(id_genero))
				while True:
					control_filme.lista_filmes()
					id_filme = control_filme.tela.seleciona_filme()
					if control_filme.checa_id(id_filme):
						filme = control_filme.pega_filme_por_id(int(id_filme))
						if filme not in filme.generos and filme not in genero.filmes:
							filme.generos.append(genero)
							genero.filmes.append(filme)
						tela.mostra_mensagem(f'\n{filme.titulo} é do gênero {genero.tipo}')
						control_filme.filme_com_genero_existe.insert(0, True)
						return
					else:
						tela.mostra_mensagem('\nID inválido, tente novamente')
			else:
				tela.mostra_mensagem('\nID inválido, operação cancelada.')

	def lista_generos(self):
		self.__tela_genero.mostra_mensagem("-------==X( LISTA GÊNEROS )X==-------")
		for genero in self.__generos:
			self.__tela_genero.mostra_genero({
				"tipo": genero.tipo,
				"id_genero": genero.id_genero
			})

	def lista_filmes_por_genero(self):
		if not self.__controlador_sistema.controlador_filmes.filme_com_genero_existe[0]:
			self.__tela_genero.mostra_mensagem('\nNão existem filmes com gêneros cadastrados.')
			return
		todos_generos = self.generos
		generos_com_filmes = [genero for genero in todos_generos if len(genero.filmes) > 0]
		self.__tela_genero.lista_filmes_por_genero(generos_com_filmes)

	def excluir_genero(self):
		self.lista_generos()
		id_genero = self.__tela_genero.seleciona_genero()
		if self.checa_id(id_genero):
			genero = self.pega_genero_por_id(int(id_genero))
			self.__generos.remove(genero)
			self.__tela_genero.mostra_mensagem(f'\nGênero {genero.tipo} removido com sucesso.')

	def abre_tela(self):
		lista_opcoes = {
			0: self.retornar,
			1: self.incluir_genero,
			2: self.alterar_genero,
			3: self.lista_generos,
			4: self.excluir_genero,
			5: self.adiciona_filme
		}

		while True:
			lista_opcoes[self.__tela_genero.tela_opcoes()]()

	@property
	def generos(self):
		return self.__generos
