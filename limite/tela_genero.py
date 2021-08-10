

class TelaGenero:

	def tela_opcoes(self) -> int:
		print(
			"\n-------==X( GÊNERO )X==-------"
			"\ndEscolha uma opção:"
			"\n0 - Retornar"
			"\n1 - Incluir Gênero"
			"\n2 - Alterar Gênero"
			"\n3 - Listar Gêneros"
			"\n4 - Excluir Gênero"
			)

		opcao = int(input("\nEscolha uma das opções:"))
		return opcao

	def pega_dados_genero(self) -> dict:
		print("\n-------==X( DADOS GÊNERO )X==-------")

		nome = input("\nnome: ")

		return {"nome": nome}

	def mostra_genero(self, dados_genero) -> None:
		print("\nNOME: ", dados_genero["nome"])

	def seleciona_genero(self):
		id_genero = input("\nid do genero que deseja selecionar: ")
		return id_genero

	def mostra_mensagem(self, msg) -> None:
		print(msg)
