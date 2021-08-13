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

	def checa_tipo(self, dado: str):
		if dado.isalpha():
			for genero in self.__generos:
				if genero.tipo == dado:
					self.__tela_genero.mostra_mensagem(f'o genero {dado} já está cadastrado')
					return False
			return True
		self.__tela_genero.mostra_mensagem('em letras por favor')
		return False

	def retornar(self):
		self.__controlador_sistema.abre_tela()

	def incluir_genero(self):
		while True:
			tipo = self.__tela_genero.pega_dados_genero()
			if self.checa_tipo(tipo):
				genero = Genero(self.__contador+1, tipo)
				self.__generos.append(genero)
				self.__contador += 1
				self.__id_generos.append(self.__contador)

	def alterar_genero(self):
		self.lista_generos()
		id_genero = self.__tela_genero.seleciona_genero()
		genero = self.pega_genero_por_id(int(id_genero))
		if genero is not None:
			novos_dados_genero = self.__tela_genero.pega_dados_genero()
			if novos_dados_genero is not None:
				genero.tipo = novos_dados_genero["tipo"]
				self.lista_generos()
		else:
			self.__tela_genero.mostra_mensagem(
				"ATENCAO: genero nao existente"
			)

	def lista_generos(self):
		self.__tela_genero.mostra_mensagem("-------==X( LISTA GENEROS )X==-------")
		for genero in self.__generos:
			self.__tela_genero.mostra_genero({
				"tipo": genero.tipo,
				"id_genero": genero.id_genero
			})

	def excluir_genero(self):
		self.lista_generos()
		id_genero = self.__tela_genero.seleciona_genero()
		genero = self.pega_genero_por_id(int(id_genero))

		if genero is not None:
			self.__generos.remove(genero)
			self.lista_generos()
		else:
			self.__tela_genero.mostra_mensagem(
				"ATENÇÃO: Gênero não existente"
			)

	def abre_tela(self):
		lista_opcoes = {
			0: self.retornar,
			1: self.incluir_genero,
			2: self.alterar_genero,
			3: self.lista_generos,
			4: self.excluir_genero
		}

		while True:
			lista_opcoes[self.__tela_genero.tela_opcoes()]()
