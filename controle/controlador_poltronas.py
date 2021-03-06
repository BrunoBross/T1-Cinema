from limite.tela_poltrona import TelaPoltrona
from entidade.poltrona import Poltrona


class ControladorPoltronas:

	def __init__(self, controlador_sistema):
		self.__controlador_sistema = controlador_sistema
		self.__poltronas = []
		self.__tela_poltrona = TelaPoltrona()
		self.__contador = 0

	def pega_poltrona_por_id(self, id_poltrona: int):
		for poltrona in self.__poltronas:
			if poltrona.id_poltrona == id_poltrona:
				return poltrona
		return None

	def retornar(self):
		self.__controlador_sistema.abre_tela()

	def incluir_poltrona(self):
		dados_poltrona = self.__tela_poltrona.pega_dados_poltrona()
		poltrona = Poltrona(
			self.__contador+1,
			dados_poltrona["fileira"],
			dados_poltrona["acento"]
		)
		self.__poltronas.append(poltrona)
		self.__contador += 1

	def alterar_poltrona(self):
		self.lista_poltronas()

		if len(self.__poltronas) > 0:

			id_poltrona = self.__tela_poltrona.seleciona_poltrona()
			poltrona = self.pega_poltrona_por_id(int(id_poltrona))

			if poltrona is not None:
				novos_dados_poltrona = self.__tela_poltrona.pega_dados_poltrona()
				poltrona.fileira = novos_dados_poltrona["fileira"]
				poltrona.acento = novos_dados_poltrona["acento"]
				self.lista_poltronas()
			else:
				self.__tela_poltrona.mostra_mensagem(
					"ATENÇÃO: poltrona não existente"
				)
		else:
			pass # já está mostrando a mensagem na listagem de poltronas, por isso que não estou printando novamente

	def lista_poltronas(self):
		self.__tela_poltrona.mostra_mensagem("\n\033[1;96m-------==X( LISTA POLTRONAS )X==-------\033[0;0m")

		if len(self.__poltronas) > 0:
			for poltrona in self.__poltronas:
				self.__tela_poltrona.mostra_poltrona({
					"fileira": poltrona.fileira,
					"acento": poltrona.acento,
					"id_poltrona": poltrona.id_poltrona
				})
		else:
			self.__tela_poltrona.mostra_mensagem('\033[1;31mNão há poltronas disponíveis, crie uma antes.\033[0;0m')

	def excluir_poltrona(self):

		self.lista_poltronas()

		if len(self.__poltronas) > 0:

			id_poltrona = self.__tela_poltrona.seleciona_poltrona()
			poltrona = self.pega_poltrona_por_id(int(id_poltrona))

			if poltrona is not None:
				self.__poltronas.remove(poltrona)
				self.lista_poltronas()
			else:
				self.__tela_poltrona.mostra_mensagem(
					"ATENÇÃO: poltrona não existente"
				)
		else:
			pass # já está mostrando a mensagem na listagem de poltronas, por isso que não estou printando novamente

	def abre_tela(self):
		lista_opcoes = {
			0: self.retornar,
			1: self.incluir_poltrona,
			2: self.alterar_poltrona,
			3: self.lista_poltronas,
			4: self.excluir_poltrona
		}

		while True:
			lista_opcoes[self.__tela_poltrona.tela_opcoes()]()

	@property
	def poltronas(self):
		return self.__poltronas