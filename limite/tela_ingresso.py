

class TelaIngresso:

	def tela_opcoes(self):
		print(
				"\n-------==X( INGRESSO )X==-------"
				"\nEscolha uma opção:"
				"\n0 - Retornar"
				"\n1 - Incluir Ingresso"
				"\n2 - Alterar Ingresso"
				"\n3 - Listar Ingressos"
				"\n4 - Excluir Ingresso"
		)

		opcao = int(input("Escolha uma das opções:"))
		return opcao

	def pega_dados_ingresso(self):
		print("-------==X( DADOS INGRESSO )X==-------")

		sessao = input("sessao: ")

		fileira = input("fileira: ")

		acento = input("acento: ")

		return {"sessao": sessao, "fileira": fileira, "acento": acento}

	def mostra_ingresso(self, dados_ingresso):
		print("SESSAO: ", dados_ingresso["sessao"])
		print("FILEIRA: ", dados_ingresso["fileira"])
		print("ACENTO: ", dados_ingresso["acento"])
		print()

	def seleciona_ingresso(self):
		id_ingresso = input("id do ingresso que deseja selecionar: ")
		return id_ingresso

	def mostra_mensagem(self, msg):
		print(msg)
