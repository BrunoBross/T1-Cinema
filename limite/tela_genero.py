

class TelaGenero:

	def tela_opcoes(self):
		print("-------==X( GÊNERO )X==-------")
		print("Escolha uma opção:")
		print("0 - Retornar")
		print("1 - Incluir Gênero")
		print("2 - Alterar Gênero")
		print("3 - Listar Gêneros")
		print("4 - Excluir Gênero")

		opcao = int(input("Escolha uma das opções:"))
		return opcao

	def pega_dados_genero(self):
		print("-------==X( DADOS GÊNERO )X==-------")

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
