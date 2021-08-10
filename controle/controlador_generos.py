from limite.tela_genero import TelaGenero
from entidade.genero import Genero


class ControladorGeneros:

	def __init__(self, controlador_sistema):
		self.__controlador_sistema = controlador_sistema
		self.__generos = []
		self.__tela_genero = TelaGenero()
		self.__contador = 0

	def pega_genero_por_id(self, id_genero: int):
		for genero in self.__generos:
			if genero.id_genero == id_genero:
				return genero
			return None

	def retornar(self):
		self.__controlador_sistema.abre_tela()

	def incluir_genero(self):
		dados_genero = self.__tela_genero.pega_dados_genero()
		genero = Genero(self.__contador+1, dados_genero["nome"])
		self.__generos.append(genero)

	def alterar_genero(self):
		self.lista_generos()
		id_genero = self.__tela_genero.seleciona_genero()
		genero = self.pega_genero_por_id(id_genero)

		if genero is not None:
			novos_dados_genero = self.__tela_genero.pega_dados_genero()
			genero.nome = novos_dados_genero["nome"]
			self.lista_generos()
		else:
			self.__tela_genero.mostra_mensagem(
				"ATENCAO: genero nao existente"
			)

	def lista_generos(self):
		contador = len(self.__generos)
		if contador == 1:
			self.__tela_genero.mostra_mensagem("\n-------==X( GÊNERO )X==-------")
		else:
			self.__tela_genero.mostra_mensagem(f"\n-------==X( GÊNEROS TOTAIS ({contador}) )X==-------")
		for genero in self.__generos:
			self.__tela_genero.mostra_genero({"nome": genero.nome})

	def excluir_genero(self):
		self.lista_generos()
		id_genero = self.__tela_genero.seleciona_genero()
		genero = self.pega_genero_por_id(int(id_genero))

		if genero is not None:
			self.__generos.remove(genero)
			self.lista_generos()
		else:
			self.__tela_genero.mostra_mensagem(
				"ATENCAO: Gênero nao existente"
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
