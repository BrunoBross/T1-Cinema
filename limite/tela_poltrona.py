

class TelaPoltrona:

	def tela_opcoes(self):

		while True:
			print("\033[1;96m-------==X( POLTRONA )X==-------\033[0;0m")
			print("Escolha uma opcao")
			print("0 - Retornar")
			print("1 - Incluir Poltrona")
			print("2 - Alterar Poltrona")
			print("3 - Listar Poltrona")
			print("4 - Excluir Poltrona")

			try:
				opcao = int(input("Escolha uma das opções:"))
				if 4 >= opcao >= 0:
					return opcao
				else:
					print('\033[1;31mDigite um número correto!\033[0;0m')
			except ValueError:
				print('\033[1;31mDigite um número correto!\033[0;0m')

	def pega_dados_poltrona(self):
		print("\033[1;96m-------==X( DADOS POLTRONA )X==-------\033[0;0m")
		fileira = input("fileira: ")
		acento = input("acento: ")
		return {
			"fileira": fileira,
			"acento": acento
		}

	def mostra_poltrona(self, dados_poltrona):
		print(
			"FILEIRA: ", dados_poltrona["fileira"],
			"ACENTO: ", dados_poltrona["acento"],
			"ID: ", dados_poltrona["id_poltrona"]
		)

	def seleciona_poltrona(self):
		id_poltrona = input("id do poltrona que deseja selecionar: ")
		return id_poltrona

	def mostra_mensagem(self, msg):
		print(msg)
