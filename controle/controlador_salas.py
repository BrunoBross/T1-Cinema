from limite.tela_sala import TelaSala
from entidade.sala import Sala


class ControladorSalas:

	def __init__(self, controlador_sistema):
		self.__controlador_sistema = controlador_sistema
		self.__salas = []
		self.__id_salas = []
		self.__tela_sala = TelaSala()
		self.__contador = 0

	def pega_sala_por_id(self, id_sala: int):
		for sala in self.__salas:
			if sala.id_sala == id_sala:
				return sala
		return None

	def checa_id(self, id_sala: str):
		if id_sala.isdecimal():
			if int(id_sala) in self.__id_salas:
				return True
			else:
				return False
		else:
			return False

	def retornar(self):
		self.__controlador_sistema.abre_tela()

	def incluir_sala(self):
		dados_sala = self.__tela_sala.pega_dados_sala()
		if dados_sala is not None:
			sala = Sala(self.__contador+1, dados_sala)
			self.__salas.append(sala)
			self.__contador += 1
			self.__id_salas.append(self.__contador)

	def alterar_sala(self):
		if len(self.__salas) < 1:
			self.__tela_sala.mostra_mensagem('não existem salas')
			return
		self.lista_salas()
		id_sala = self.__tela_sala.seleciona_sala()
		while True:
			if self.checa_id(id_sala):
				sala = self.pega_sala_por_id(int(id_sala))

				if sala is not None:
					novos_dados_sala = self.__tela_sala.pega_dados_sala()
					sala.numero = novos_dados_sala
					break

	def lista_salas(self):
		self.__tela_sala.mostra_mensagem("-------==X( LISTA SALAS )X==-------")
		for sala in self.__salas:
			self.__tela_sala.mostra_sala({
				"numero": sala.numero,
				"id_sala": sala.id_sala
			})

	def excluir_sala(self):
		if len(self.__salas) < 1:
			self.__tela_sala.mostra_mensagem('não existem salas cadastradas')
			return
		while True:
			self.lista_salas()
			id_sala = self.__tela_sala.seleciona_sala()
			if self.checa_id(id_sala):
				sala = self.pega_sala_por_id(int(id_sala))
				if sala is not None:
					numero = sala.numero
					quantidade = len(self.__salas)
					self.__salas.remove(sala)
					if quantidade == len(self.__salas):
						self.__tela_sala.mostra_mensagem(f'"sala {numero}" removida do sistema')
					break
			else:
				self.__tela_sala.mostra_mensagem('\t\ttente novamente')

	def abre_tela(self):
		lista_opcoes = {
			0: self.retornar,
			1: self.incluir_sala,
			2: self.alterar_sala,
			3: self.lista_salas,
			4: self.excluir_sala
		}

		while True:
			lista_opcoes[self.__tela_sala.tela_opcoes()]()

	@property
	def id_salas(self):
		return self.__id_salas
