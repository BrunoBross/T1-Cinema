from limite.tela_sistema import TelaSistema
from controle.controlador_ingressos import ControladorIngressos
from controle.controlador_sessaos import ControladorSessaos
from controle.controlador_salas import ControladorSalas
from controle.controlador_filmes import ControladorFilmes
from controle.controlador_generos import ControladorGeneros
from controle.controlador_poltronas import ControladorPoltronas


class ControladorSistema:

	def __init__(self):
		self.__controlador_ingressos = ControladorIngressos(self)
		self.__controlador_sessaos = ControladorSessaos(self)
		self.__controlador_salas = ControladorSalas(self)
		self.__controlador_filmes = ControladorFilmes(self)
		self.__controlador_generos = ControladorGeneros(self)
		self.__controlador_poltronas = ControladorPoltronas(self)
		self.__tela_sistema = TelaSistema()

	@property
	def controlador_ingressos(self):
		return self.__controlador_ingressos

	@property
	def controlador_sessaos(self):
		return self.__controlador_sessaos

	@property
	def controlador_salas(self):
		return self.__controlador_salas

	@property
	def controlador_filmes(self):
		return self.__controlador_filmes

	@property
	def controlador_generos(self):
		return self.__controlador_generos

	@property
	def controlador_poltronas(self):
		return self.__controlador_poltronas

	def inicializa_sistema(self):
		self.abre_tela()

	def gerencia_ingressos(self):
		self.__controlador_ingressos.abre_tela()

	def gerencia_sessaos(self):
		self.__controlador_sessaos.abre_tela()

	def gerencia_salas(self):
		self.__controlador_salas.abre_tela()

	def gerencia_filmes(self):
		self.__controlador_filmes.abre_tela()

	def gerencia_generos(self):
		self.__controlador_generos.abre_tela()

	def gerencia_poltronas(self):
		self.__controlador_poltronas.abre_tela()

	def encerra_sistema(self):
		print('\033[1;31mAté logo ;(\033[0;0m')
		exit(0)

	def abre_tela(self):
		lista_opcoes = {
			1: self.gerencia_ingressos,
			2: self.gerencia_sessaos,
			3: self.gerencia_salas,
			4: self.gerencia_filmes,
			5: self.gerencia_generos,
			0: self.encerra_sistema
		}

		while True:
			opcao_escolhida = self.__tela_sistema.tela_opcoes()
			funcao_escolhida = lista_opcoes[opcao_escolhida]
			funcao_escolhida()
