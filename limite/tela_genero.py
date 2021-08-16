

class TelaGenero:

	def tela_opcoes(self):

		while True:
			print("\n\033[1;96m-------==X( GÊNERO )X==-------\033[0;0m")
			print("Escolha uma opção")
			print("0 - Retornar")
			print("1 - Incluir Gênero")
			print("2 - Alterar Gênero")
			print("3 - Listar Gêneros")
			print("4 - Excluir Gênero")
			print("5 - Adiciona Filme")

			try:
				opcao = int(input("Escolha uma das opções: "))
				if 5 >= opcao >= 0:
					return opcao
				else:
					print('\n\033[1;31mDigite um número entre 0 e 5!\033[0;0m')
			except ValueError:
				print('\n\033[1;31mDigite um número!\033[0;0m')

	def lista_filmes_por_genero(self, generos: list):
		print('\n\033[1;96m-------==X( GÊNEROS E FILMES )X==-------\033[0;0m')
		for genero in generos:
			print(f'\n{genero.tipo:}:')
			for filme in genero.filmes:
				print(f'\t- {filme.titulo} / ID = {filme.id_filme},' if filme != generos[-1] else f'\t- {filme.titulo} / ID = {filme.id_filme}')

	def pega_dados_genero(self):

		aviso = '\n\033[1;31mDigite um número correto!\033[0;0m'
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
							return False
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
		return input("id do gênero que deseja selecionar: ")

	def mostra_mensagem(self, msg):
		print(msg)
