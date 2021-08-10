

class TelaPoltrona:

	def tela_opcoes(self):
		print("----------POLTRONA----------")
		print("Escolha uma opcao")
		print("0 - Retornar")
		print("1 - Incluir Poltrona")
		print("2 - Alterar Poltrona")
		print("3 - Listar Poltrona")
		print("4 - Excluir Poltrona")

		opcao = int(input("Escolha uma das opcoes:"))
		return opcao

	def pega_dados_poltrona(self):
		print("----------DADOS POLTRONA----------")

		fileira = input("fileira: ")

		acento = input("acento: ")

		return {"fileira": fileira, "acento": acento}

	def mostra_poltrona(self, dados_poltrona):
		print("FILEIRA: ", dados_poltrona["fileira"])
		print("ACENTO: ", dados_poltrona["acento"])
		print()

	def seleciona_poltrona(self):
		id_poltrona = input("id do poltrona que deseja selecionar: ")
		return id_poltrona

	def mostra_mensagem(self, msg):
		print(msg)
