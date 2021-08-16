

class TelaSessao:

	def tela_opcoes(self):

		while True:
			print("\n\033[1;96m-------==X( SESSÃO )X==-------\033[0;0m")
			print("Escolha uma opção")
			print("0 - Retornar")
			print("1 - Incluir Sessão")
			print("2 - Alterar Sessão")
			print("3 - Listar Sessões")
			print("4 - Excluir Sessão")

			try:
				opcao = int(input("Escolha uma das opções: "))
				if 4 >= opcao >= 0:
					return opcao
				else:
					print('\n\033[1;31mDigite um número entre 0 e 4!\033[0;0m')
			except ValueError:
				print('\n\033[1;31mDigite um número!\033[0;0m')

	def pega_dados_sessao(self, dado: str):

		print("\n\033[1;96m-------==X( DADOS SESSÃO )X==-------\033[0;0m")
		mensagem = {
			"id_filme": "Digite o ID do filme: ", "horario": "Horário da sessão: ",
			"id_sala": "Digite o ID da sala: ", "certeza": "Pressione Enter para confirmar: "
		}
		return input(f'{mensagem[dado]}')

	def mostra_sessao(self, dados_sessao):
		print(
			"FILME: ", dados_sessao["filme"], "HORÁRIO: ", dados_sessao["horario"],
			"SALA: ", dados_sessao["sala"], "ID: ", dados_sessao["id_sessao"]
		)

	def seleciona_sessao(self):
		return input("\nID da sessão que deseja selecionar: ")

	def mostra_mensagem(self, msg):
		print(msg)
