

class TelaFilme:

	def tela_opcoes(self):

		while True:
			print("\n\033[1;96m-------==X( FILME )X==-------\033[0;0m")
			print("Escolha uma opção")
			print("0 - Retornar")
			print("1 - Incluir Filme")
			print("2 - Alterar Filme")
			print("3 - Listar Filme")
			print("4 - Excluir Filme")

			try:
				opcao = int(input("Escolha uma das opções: "))
				if 4 >= opcao >= 0:
					return opcao
				else:
					print('\n\033[1;31mDigite um número entre 0 e 4!\033[0;0m')
			except ValueError:
				print('\n\033[1;31mDigite um número!\033[0;0m')

	def pega_dados_filme(self):

		while True:

			titulo = input("Título: ")
			print('\n\033[1;96m'+titulo+'\033[0;0m\n')
			while True:
				try:
					certeza = int(input("Tem certeza do título?\n1 - Sim\n2 - Não\n3 - Cancelar\nDigite uma opção: "))
					if 3 >= certeza >= 0:
						if certeza == 1:
							return titulo
						elif certeza == 3:
							cancelar = True
							break
						elif certeza == 2:
							cancelar = False
							break
					else:
						print('\n\033[1;31mDigite um número entre 1 e 3!\033[0;0m\n')
				except ValueError:
					print('\n\033[1;31mDigite um número correto!\033[0;0m\n')
			if cancelar:
				break

	def mostra_filme(self, dados_filme):
		print(
			"TITULO: ", dados_filme["titulo"],
			"ID: ", dados_filme["id_filme"]
		)

	def seleciona_filme(self):
		return input("\nID do filme que deseja selecionar: ")

	def mostra_mensagem(self, msg):
		print(msg)
