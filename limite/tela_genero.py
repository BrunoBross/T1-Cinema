

class TelaGenero:

	def tela_opcoes(self):
		print("----------GENERO----------")
		print("Escolha uma opcao")
		print("0 - Retornar")
		print("1 - Incluir Genero")
		print("2 - Alterar Genero")
		print("3 - Listar Genero")
		print("4 - Excluir Genero")

		opcao = int(input("Escolha uma das opcoes:"))
		return opcao

	def pega_dados_genero(self):
		print("----------DADOS GENERO----------")

		nome = input("nome: ")

		return {"nome": nome}

	def mostra_genero(self, dados_genero):
		print("NOME: ", dados_genero["nome"])
		print()

	def seleciona_genero(self):
		id_genero = input("id do genero que deseja selecionar: ")
		return id_genero

	def mostra_mensagem(self, msg):
		print(msg)
