

class TelaIngresso:

	def tela_opcoes(self):

		while True:
			print("\033[1;96m-------==X( INGRESSO )X==-------\033[0;0m")
			print("Escolha uma opcao")
			print("0 - Retornar")
			print("1 - Incluir Ingresso")
			print("2 - Alterar Ingresso")
			print("3 - Listar Ingresso")
			print("4 - Excluir Ingresso")

			try:
				opcao = int(input("Escolha uma das opções:"))
				if 4 >= opcao >= 0:
					return opcao
				else:
					print('\033[1;31mDigite um número correto!\033[0;0m')
			except ValueError:
				print('\033[1;31mDigite um número correto!\033[0;0m')

	def pega_dados_ingresso(self):
		print("\033[1;96m-------==X( DADOS INGRESSO )X==-------\033[0;0m")
		fileira = input("fileira: ")
		acento = input("acento: ")
		id_sessao = int(input("id do sessao: "))
		return {
			"fileira": fileira,
			"acento": acento,
			"sessao": id_sessao
		}

	def mostra_ingresso(self, dados_ingresso):
		print(
			"FILEIRA: ", dados_ingresso["fileira"],
			"ACENTO: ", dados_ingresso["acento"],
			"SESSAO: ", dados_ingresso["sessao"],
			"ID: ", dados_ingresso["id_ingresso"]
		)

	def seleciona_ingresso(self):
		id_ingresso = input("id do ingresso que deseja selecionar: ")
		return id_ingresso

	def mostra_mensagem(self, msg):
		print(msg)
