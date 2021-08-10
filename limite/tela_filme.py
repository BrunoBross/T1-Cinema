

class TelaFilme:

	def tela_opcoes(self) -> int:
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

	def pega_dados_filme(self) -> dict:
		print("\n-------==X( DADOS FILME )X==-------")

		titulo = input("\nTítulo do Filme: ")

		return {"titulo": titulo}

	def mostra_filme(self, dados_filme: dict):
		print(
			dados_filme["titulo"]
		)

	def seleciona_filme(self):
		id_filme = input("id do filme que deseja selecionar: ")
		return id_filme

	def mostra_mensagem(self, msg) -> None:
		print(msg)
