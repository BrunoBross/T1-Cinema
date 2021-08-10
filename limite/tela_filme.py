

class TelaFilme:

	def tela_opcoes(self):
		print(
			"\n-------==X( FILME )X==-------"
			"\nEscolha uma opção:"
			"\n0 - Retornar"
			"\n1 - Incluir Filme"
			"\n2 - Alterar Filme"
			"\n3 - Listar Filmes"
			"\n4 - Excluir Filme"
		)

		opcao = int(input("\nEscolha uma das opções:"))
		return opcao

	def pega_dados_filme(self):
		print("\n-------==X( DADOS FILME )X==-------")

		titulo = input("\nTítulo do Filme: ")

		return {"titulo": titulo}

	def mostra_filme(self, dados_filme):
		print("\n-------==X( LISTA FILME(S) )X==-------")
		print("\nTITULO: ", dados_filme["titulo"])
		print()

	def seleciona_filme(self):
		id_filme = input("id do filme que deseja selecionar: ")
		return id_filme

	def mostra_mensagem(self, msg) -> None:
		print(msg)
