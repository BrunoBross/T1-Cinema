

class TelaGenero:

	def tela_opcoes(self):

		aviso = '\033[1;31mDigite um número correto!\033[0;0m'

		while True:
			print("\n\033[1;96m-------==X( GÊNERO )X==-------\033[0;0m")
			print("Escolha uma opção")
			print("0 - Retornar")
			print("1 - Incluir Genero")
			print("2 - Alterar Genero")
			print("3 - Listar Genero")
			print("4 - Excluir Genero")

			try:
				opcao = int(input("Escolha uma das opções: "))
				if 4 >= opcao >= 0:
					return opcao
				else:
					print(aviso)
			except ValueError:
				print(aviso)

	def pega_dados_genero(self):

		aviso = '\033[1;31mDigite um número correto!\033[0;0m'
		print("\n\033[1;96m-------==X( DADOS GÊNERO )X==-------\033[0;0m")
		while True:
			tipo = input("tipo: ")
			print('\n'+tipo+'\n')
			while True:
				try:
					certeza = int(input("tem certeza do tipo de gênero?\n1 - sim\n2 - não\n3 - cancelar\nDigite um número: "))
					if 3 >= certeza >= 0:
						if certeza == 1:
							return tipo
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

	def mostra_genero(self, dados_genero):
		print(
			"TIPO: ", dados_genero["tipo"],
			"ID: ", dados_genero["id_genero"]
		)

	def seleciona_genero(self):
		return int(input("id do genero que deseja selecionar: "))

	def mostra_mensagem(self, msg):
		print(msg)
