from limite.tela_sala import TelaSala
from entidade.sala import Sala
from persistencia.sala_DAO import SalaDAO


class ControladorSalas:

	def __init__(self, controlador_sistema):
		self.__controlador_sistema = controlador_sistema
		self.__salas_dao = SalaDAO()
		self.__id_salas = self.__salas_dao.get_ids()
		self.__tela_sala = TelaSala()

	def pega_sala_por_id(self, id_sala: int):
		try:
			return self.__salas_dao.get(id_sala)
		except IndexError:
			return None

	def checa_id(self, id_sala: str):
		return id_sala.isdecimal() and int(id_sala) in self.__id_salas

	def retornar(self):
		self.__controlador_sistema.abre_tela()

	def checa_numero(self, numero_novo):
		for sala in self.__salas_dao.get_all():
			if numero_novo == sala.numero:
				self.__tela_sala.mostra_mensagem('Sala já existente.')
				return False
			if numero_novo == '':
				self.__tela_sala.mostra_mensagem('Número inválido.')
				return False
		return True

	def existem_salas_cadastradas(self):
		if len(self.salas) > 0:
			return True
		self.__tela_sala.mostra_mensagem(f'Não há salas cadastradas.')
		return False

	def dados_lista_salas(self):
		return [f'ID: {sala.id_sala}    Nº Sala: {sala.numero}' for sala in self.salas]

	def incluir_sala(self):

		while True:
			dados_sala = self.__tela_sala.pega_dados_sala()
			if dados_sala is not None:
				if self.checa_numero(dados_sala):
					sala = Sala(self.__salas_dao.get_last_child() + 1, dados_sala)
					self.__salas_dao.add(sala)
					self.__tela_sala.mostra_mensagem(f'A sala de Nº {sala.numero} foi adicionada!')
					break
			else:
				break

	def alterar_sala(self):

		if self.existem_salas_cadastradas():
			id_sala = self.__tela_sala.seleciona_sala(self.dados_lista_salas())
			if id_sala is not None:
				sala = self.pega_sala_por_id(int(id_sala))
				novos_dados_sala = self.__tela_sala.altera_sala()
				if novos_dados_sala is not None:
					sala_velha = sala.numero
					sala.numero = novos_dados_sala
					self.__salas_dao.add(sala)
					self.__tela_sala.mostra_mensagem(f'A sala Nº {sala_velha} foi substituida pelo Nº {sala.numero}')

	def lista_salas(self):

		if self.existem_salas_cadastradas():
			self.__tela_sala.popup_lista_salas(
				[f'ID: {sala.id_sala}    Nº Sala: {sala.numero}' for sala in self.salas]
			)

	def excluir_sala(self):

		if self.existem_salas_cadastradas():
			id_sala_ = self.__tela_sala.exclui_sala(
				[f'ID: {sala.id_sala}    Nº Sala: {sala.numero}' for sala in self.salas]
			)
			if id_sala_ is not None:
				sala = self.pega_sala_por_id(int(id_sala_))
				self.__salas_dao.remove(sala.id_sala)
				self.__tela_sala.mostra_mensagem(f'A sala de Nº {sala.numero} foi removida com sucesso')

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
		return self.__salas_dao.get_all()
