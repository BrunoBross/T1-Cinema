

class TelaFilme:

	def tela_opcoes(self):
		print("-------==X( FILME )X==-------")
		print("Escolha uma opção:")
		print("0 - Retornar")
		print("1 - Incluir Filme")
		print("2 - Alterar Filme")
		print("3 - Listar Filmes")
		print("4 - Excluir Filme")

		opcao = int(input("Escolha uma das opções:"))
		return opcao

	def pega_dados_filme(self):
		print("-------==X( DADOS FILME )X==-------")

		titulo = input("Título do Filme: ")

		return {"titulo": titulo}

	def mostra_filme(self, dados_filme):
		print("TITULO: ", dados_filme["titulo"])
		print()

	def seleciona_filme(self):
		id_filme = input("id do filme que deseja selecionar: ")
		return id_filme

	def mostra_mensagem(self, msg):
		print(msg)
