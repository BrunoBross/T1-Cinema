

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

	def pega_dados_sessao(self, dado: str):
		print("\033[1;96m-------==X( DADOS SESSAO )X==-------\033[0;0m")
		mensagem = {
			"id_filme": "id do filme: ", "horario": "horário: ",
			"id_sala": "id da sala: ", "certeza": "digite 1 para confirmar: "
		}
		return input(f'{mensagem[dado]}')

	def mostra_sessao(self, dados_sessao):
		print(
			"FILME: ", dados_sessao["filme"], "HORÁRIO: ", dados_sessao["horario"],
			"SALA: ", dados_sessao["sala"], "ID: ", dados_sessao["id_sessao"]
		)

	def seleciona_sessao(self):
		return input("id da sessão que deseja selecionar: ")

	def mostra_mensagem(self, msg):
		print(msg)
