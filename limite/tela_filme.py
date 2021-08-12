

class TelaFilme:

	def tela_opcoes(self):

		aviso = '\033[1;31mDigite um número correto!\033[0;0m'
		while True:
			print("\033[1;96m----------FILME----------\033[0;0m")
			print("Escolha uma opcao")
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
					print(aviso)
			except ValueError:
				print(aviso)

	def pega_dados_filme(self):

		aviso = '\033[1;31mDigite um número correto!\033[0;0m'
		print("\033[1;96m-------==X( DADOS FILME )X==-------\033[0;0m")
		while True:
			titulo = input("título: ")
			print('\n'+titulo+'\n')
			while True:
				try:
					certeza = int(input("tem certeza do título?\n1 - sim\n2 - não\n3 - cancelar\nDigite um número: "))
					if 3 >= certeza >= 0:
						if certeza == 1:
							return {
								"titulo": titulo
							}
						elif certeza == 3:
							cancelar = True
							break
						elif certeza == 2:
							cancelar = False
							break
					else:
						print(aviso)
				except ValueError:
					print(aviso)
			if cancelar:
				break

	def mostra_filme(self, dados_filme):
		print(
			"TITULO: ", dados_filme["titulo"],
			"ID: ", dados_filme["id_filme"]
		)

	def seleciona_filme(self):
		id_filme = int(input("id do filme que deseja selecionar: "))
		return id_filme

	def mostra_mensagem(self, msg):
		print(msg)
