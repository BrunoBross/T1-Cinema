import PySimpleGUI as sg


class TelaGenero:

	def tela_opcoes(self):
		sg.theme('DarkPurple4')
		fonte = ('Sans-Serif', 15)
		tamanho = (20, 1)

		layout = [
			[sg.Text('Gerenciar Gêneros', font=('Impact', 20), text_color='white', size=(0, 2))],
			[sg.Button('Incluir Gênero', font=fonte, size=tamanho)],
			[sg.Button('Alterar Gênero', font=fonte, size=tamanho)],
			[sg.Button('Listar Gêneros', font=fonte, size=tamanho)],
			[sg.Button('Excluir Gênero', font=fonte, size=tamanho)],
			[sg.Button('Adicionar Filme', font=fonte, size=tamanho)],
			[sg.Button('Retornar', font=fonte, size=tamanho)]
		]

		window = sg.Window('Gerenciador de Gêneros', layout, size=(400, 360), element_justification='c')

		valor_escolhido = {
			'Incluir Gênero': 1, 'Alterar Gênero': 2, 'Listar Gêneros': 3,
			'Excluir Gênero': 4, 'Adicionar Filme': 5, 'Retornar': 0
		}[window.Read()[0]]

		window.Close()
		return valor_escolhido

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
