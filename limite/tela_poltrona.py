

class TelaPoltrona:

	def tela_opcoes(self):
		print(
				"\n-------==X( POLTRONA )X==-------"
				"\nEscolha uma opção:"
				"\n0 - Retornar"
				"\n1 - Incluir Poltrona"
				"\n2 - Alterar Poltrona"
				"\n3 - Listar Poltronas"
				"\n4 - Excluir Poltrona"
		)

		opcao = int(input("Escolha uma das opções:"))
		return opcao

	def pega_dados_poltrona(self):
		print("-------==X( DADOS POLTRONA )X==-------")

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
