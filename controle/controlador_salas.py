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
		if id_sala.isdecimal() and int(id_sala) in self.__id_salas:
			return True
		return False

	def retornar(self):
		self.__controlador_sistema.abre_tela()

	def checa_numero(self, numero_novo):
		for sala in self.__salas:
			if numero_novo == sala.numero:
				self.__tela_sala.mostra_mensagem('Sala já existente')
				return False
			if numero_novo == '':
				self.__tela_sala.mostra_mensagem('Número inválido')
				return False
		return True

	def incluir_sala(self):
		dados_sala = self.__tela_sala.pega_dados_sala()
		if dados_sala is not None:
			if self.checa_numero(dados_sala):
				sala = Sala(self.__contador+1, dados_sala)
				self.__salas.append(sala)
				self.__contador += 1
				self.__id_salas.append(self.__contador)

	def alterar_sala(self):
		tela = self.__tela_sala

		if len(self.__salas) < 1:
			tela.mostra_mensagem('não existem salas')
			return
		self.lista_salas()
		while True:
			id_sala = tela.seleciona_sala()
			print(id_sala, self.checa_id(id_sala))
			if self.checa_id(id_sala):
				sala = self.pega_sala_por_id(int(id_sala))
				if sala is not None:
					novos_numero = tela.pega_dados_sala()
					if self.checa_numero(novos_numero):
						sala.numero = novos_numero
						break

	def lista_salas(self):
		self.__tela_sala.mostra_mensagem("\n\033[1;96m-------==X( LISTA SALAS )X==-------\033[0;0m")
		for sala in self.__salas:
			self.__tela_sala.mostra_sala({
				"numero": sala.numero,
				"id_sala": sala.id_sala
			})

	def excluir_sala(self):
		if len(self.__salas) < 1:
			self.__tela_sala.mostra_mensagem('Não existem salas cadastradas')
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
						self.__tela_sala.mostra_mensagem(f'"A Sala {numero}" foi removida do sistema')
					break
			else:
				self.__tela_sala.mostra_mensagem('\t\tTente novamente')

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

	@property
	def salas(self):
		return self.__salas
