

class TelaGenero:

	def tela_opcoes(self):
		print("\033[1;96m----------GENERO----------\033[0;0m")
		print("Escolha uma opcao")
		print("0 - Retornar")
		print("1 - Incluir Genero")
		print("2 - Alterar Genero")
		print("3 - Listar Genero")
		print("4 - Excluir Genero")

		opcao = int(input("Escolha uma das opcoes:"))
		return opcao

	def pega_dados_genero(self):
		print("\033[1;96m-------==X( DADOS GENERO )X==-------\033[0;0m")
		tipo = input("tipo: ")
		return {
			"tipo": tipo
		}

	def mostra_genero(self, dados_genero):
		print(
			"TIPO: ", dados_genero["tipo"],
			"ID: ", dados_genero["id_genero"]
		)

	def seleciona_genero(self):
		id_genero = input("id do genero que deseja selecionar: ")
		return id_genero

	def mostra_mensagem(self, msg):
		print(msg)
