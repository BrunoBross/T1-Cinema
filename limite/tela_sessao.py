

class TelaSessao:

	def tela_opcoes(self):

		aviso = '\033[1;31mDigite um número correto!\033[0;0m'

		while True:
			print("\033[1;96m----------SESSAO----------\033[0;0m")
			print("Escolha uma opcao")
			print("0 - Retornar")
			print("1 - Incluir Sessao")
			print("2 - Alterar Sessao")
			print("3 - Listar Sessao")
			print("4 - Excluir Sessao")

			try:
				opcao = int(input("Escolha uma das opções: "))
				if 4 >= opcao >= 0:
					return opcao
				else:
					print(aviso)
			except ValueError:
				print(aviso)

	def pega_dados_sessao(self):
		print("\033[1;96m-------==X( DADOS SESSAO )X==-------\033[0;0m")
		id_filme = int(input("id do filme: "))
		horario = input("horário: ")
		id_sala = int(input("id da sala: "))
		return {
			"filme": id_filme,
			"horario": horario,
			"sala": id_sala
		}

	def mostra_sessao(self, dados_sessao):
		print(
			"FILME: ", dados_sessao["filme"],
			"HORÁRIO: ", dados_sessao["horario"],
			"SALA: ", dados_sessao["sala"],
			"ID: ", dados_sessao["id_sessao"]
		)

	def seleciona_sessao(self):
		id_sessao = int(input("id da sessão que deseja selecionar: "))
		return id_sessao

	def mostra_mensagem(self, msg):
		print(msg)
