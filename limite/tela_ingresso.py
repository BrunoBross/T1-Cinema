

class TelaIngresso:

	def tela_opcoes(self):
		print("----------INGRESSO----------")
		print("Escolha uma opcao")
		print("0 - Retornar")
		print("1 - Incluir Ingresso")
		print("2 - Alterar Ingresso")
		print("3 - Listar Ingresso")
		print("4 - Excluir Ingresso")

		opcao = int(input("Escolha uma das opcoes:"))
		return opcao

	def pega_dados_ingresso(self):
		print("----------DADOS INGRESSO----------")

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
