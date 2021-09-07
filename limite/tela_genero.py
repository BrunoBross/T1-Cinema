import PySimpleGUI as sg
from limite.temas import tamanho, tamanho_janela, fonte_texto, tema, tema_aviso, fonte_titulo, cor


class TelaGenero:

	def tela_opcoes(self):
		sg.theme(tema)

		layout = [
			[sg.Text('Gerenciar Gêneros', font=fonte_titulo, text_color=cor, size=(0, 2))],
			[sg.Button('Incluir Gênero', font=fonte_texto, size=tamanho)],
			[sg.Button('Alterar Gênero', font=fonte_texto, size=tamanho)],
			[sg.Button('Listar Gêneros', font=fonte_texto, size=tamanho)],
			[sg.Button('Excluir Gênero', font=fonte_texto, size=tamanho)],
			[sg.Button('Adicionar Filme', font=fonte_texto, size=tamanho)],
			[sg.Button('Retornar', font=fonte_texto, size=tamanho)]
		]

		window = sg.Window('Gerenciador de Gêneros', layout, size=tamanho_janela, element_justification='c')

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

		sg.theme(tema_aviso)

		layout = [
			[sg.Text(msg, size=(0, 2), font=fonte_texto, text_color=cor)],
			[sg.Button('Retornar', font=fonte_texto, size=tamanho)]
		]
		window = sg.Window('Selecionar', layout, size=(400, 100), element_justification='c')
		window.Read()
		window.Close()
