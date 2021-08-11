

class TelaFilme:

	def tela_opcoes(self):

		while True:
			print("\033[1;96m----------FILME----------\033[0;0m")
			print("Escolha uma opcao")
			print("0 - Retornar")
			print("1 - Incluir Filme")
			print("2 - Alterar Filme")
			print("3 - Listar Filme")
			print("4 - Excluir Filme")

			try:
				opcao = int(input("Escolha uma das opções:"))
				if 4 >= opcao >= 0:
					return opcao
				else:
					print('\033[1;31mDigite um número correto!\033[0;0m')
			except ValueError:
				print('\033[1;31mDigite um número correto!\033[0;0m')

	def pega_dados_filme(self):
		print("\033[1;96m-------==X( DADOS FILME )X==-------\033[0;0m")
		titulo = input("titulo: ")
		return {
			"titulo": titulo
		}

	def mostra_filme(self, dados_filme):
		print(
			"TITULO: ", dados_filme["titulo"],
			"ID: ", dados_filme["id_filme"]
		)

	def seleciona_filme(self):
		id_filme = input("id do filme que deseja selecionar: ")
		return id_filme

	def mostra_mensagem(self, msg):
		print(msg)
