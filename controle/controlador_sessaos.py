from limite.tela_sessao import TelaSessao
from entidade.sessao import Sessao
from controle.controlador_filmes import ControladorFilmes


class ControladorSessaos:

	def __init__(self, controlador_sistema):
		self.__controlador_sistema = controlador_sistema
		self.__sessaos = []
		self.__id_sessaos = []
		self.__tela_sessao = TelaSessao()
		self.__contador = 0

	def pega_sessao_por_id(self, id_sessao: int):
		for sessao in self.__sessaos:
			if sessao.id_sessao == id_sessao:
				return sessao
		return None

	def existem_sessaos_cadastrados(self):
		if len(self.sessaos) > 0:
			return True
		self.__tela_sessao.mostra_mensagem('\n\033[1;31mNão há sessões disponíveis, crie um antes.\033[0;0m')
		return False

	def checa_id(self, id_sessao: str):
		if id_sessao.isdecimal():
			if int(id_sessao) in self.__id_sessaos:
				return True
			else:
				return False
		else:
			return False

	def retornar(self):
		self.__controlador_sistema.abre_tela()

	def incluir_sessao(self):

		control_filme = self.__controlador_sistema.controlador_filmes
		control_sala = self.__controlador_sistema.controlador_salas
		control_genero = self.__controlador_sistema.controlador_generos
		tela = self.__tela_sessao

		material = [self.__contador+1]
		nao_possui = ''
		tem_filme = False
		if len(control_filme.filmes) > 0:
			nao_possui += 'nao possui filme.'
			tem_filme = True
		if len(control_sala.salas) > 0 and tem_filme:
			while True:
				if control_filme.filme_com_genero_existe:
					control_genero.lista_filmes_por_genero()
				else:
					control_filme.lista_filmes()
				id_filme = tela.pega_dados_sessao("id_filme")
				if control_filme.checa_id(id_filme):
					filme = control_filme.pega_filme_por_id(int(id_filme))
					material.append(filme)
					tela.mostra_mensagem(f'\nO filme \033[1;96m"{filme.titulo}"\033[0;0m foi adicionado a esta sessão.')
					break

			while True:
				horario = tela.pega_dados_sessao("horario")
				tela.mostra_mensagem(f'\nDeseja confirmar \033[1;96m"{horario}"\033[0;0m como horário?')
				certeza = tela.pega_dados_sessao("certeza")
				if certeza == '':
					material.append(horario)
					break
			while True:
				control_sala.lista_salas()
				id_sala = tela.pega_dados_sessao("id_sala")
				if control_sala.checa_id(id_sala):
					sala = control_sala.pega_sala_por_id(int(id_sala))
					material.append(sala)
					tela.mostra_mensagem(f'\nA sala \033[1;96m"{sala.numero}"\033[0;0m foi adicionada à sessão.')
					break
			sessao = Sessao(material[0], material[1], material[2], material[3])
			self.__sessaos.append(sessao)
			self.__contador += 1
			self.__id_sessaos.append(self.__contador)

		else:

			self.__tela_sessao.mostra_mensagem("\n\033[1;96m-------==X( INCLUIR SESSÃO )X==-------\033[0;0m")

			if not tem_filme:
				self.__tela_sessao.mostra_mensagem('\n\033[1;31mNão há filme disponível, adicione um antes.\033[0;0m')
			else:
				self.__tela_sessao.mostra_mensagem('\n\033[1;31mNão há sala disponível, crie uma antes.\033[0;0m')

	def alterar_sessao(self):
		if self.existem_sessaos_cadastrados():

			tela = self.__tela_sessao
			tela.mostra_mensagem("\n\033[1;96m-------==X( ALTERAR SESSÕES )X==-------\033[0;0m")
			while True:
				self.lista_sessaos()
				id_sessao = tela.seleciona_sessao()
				if self.checa_id(id_sessao):
					sessao = self.pega_sessao_por_id(int(id_sessao))
					break
				else:
					tela.mostra_mensagem("\033[1;31mTente novamente\033[0;0m")
			control_filme = self.__controlador_sistema.controlador_filmes
			control_sala = self.__controlador_sistema.controlador_salas
			while True:
				control_filme.lista_filmes()
				id_filme = tela.pega_dados_sessao("id_filme")
				if control_filme.checa_id(id_filme):
					filme = control_filme.pega_filme_por_id(int(id_filme))
					sessao.filme = filme
					tela.mostra_mensagem(f'\nO filme "{filme.titulo}" foi adicionado a esta sessão')
					break
			while True:
				horario = tela.pega_dados_sessao("horario")
				tela.mostra_mensagem(f'\nDeseja confirmar "{horario}" como horário?')
				certeza = tela.pega_dados_sessao("certeza")
				if certeza == '':
					sessao.horario = horario
					tela.mostra_mensagem(f'{horario} adicionado a sessão como horário.')
					break
			while True:
				control_sala.lista_salas()
				id_sala = tela.pega_dados_sessao("id_sala")
				if control_sala.checa_id(id_sala):
					sala = control_sala.pega_sala_por_id(int(id_sala))
					sessao.sala = sala
					tela.mostra_mensagem(f'\nA sala {sala.numero} foi adicionada à sessão.')
					break

	def lista_sessaos(self):
		self.__tela_sessao.mostra_mensagem("\n\033[1;96m-------==X( LISTA SESSÕES )X==-------\033[0;0m")

		if len(self.sessaos) > 0:
			for sessao in self.__sessaos:
				self.__tela_sessao.mostra_sessao({
					"filme": sessao.filme.titulo,
					"horario": sessao.horario,
					"sala": sessao.sala.numero,
					"id_sessao": sessao.id_sessao
				})
		else:
			self.__tela_sessao.mostra_mensagem('\n\033[1;31mNão há sessões disponíveis, crie uma antes.\033[0;0m')

	def excluir_sessao(self):
		self.__tela_sessao.mostra_mensagem("\n\033[1;96m-------==X( EXCLUIR SESSÕES )X==-------\033[0;0m")

		if len(self.__sessaos) < 1:
			self.__tela_sessao.mostra_mensagem('\n\033[1;31mNão há sessões disponíveis, crie uma antes.\033[0;0m')
			return
		while True:
			self.lista_sessaos()
			id_filme = self.__tela_sessao.seleciona_sessao()
			if self.checa_id(id_filme):
				filme = self.pega_sessao_por_id(int(id_filme))
				if filme is not None:
					titulo = filme.titulo
					quantidade = len(self.__sessaos)
					self.__sessaos.remove(filme)
					if quantidade+1 == len(self.__sessaos):
						self.__tela_sessao.mostra_mensagem(f'O filme {titulo} foi removido do sistema.')
				else:
					self.__tela_sessao.mostra_mensagem("\033[1;31mATENÇÃO: Filme não existente\033[0;0m")
			else:
				self.__tela_sessao.mostra_mensagem('\t\tTente novamente.')

	def abre_tela(self):
		lista_opcoes = {
			0: self.retornar,
			1: self.incluir_sessao,
			2: self.alterar_sessao,
			3: self.lista_sessaos,
			4: self.excluir_sessao
		}

		while True:
			lista_opcoes[self.__tela_sessao.tela_opcoes()]()

	@property
	def id_sessaos(self):
		return self.__id_sessaos

	@property
	def sessaos(self):
		return self.__sessaos
