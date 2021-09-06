import PySimpleGUI as sg

class TelaIngresso:

	def tela_opcoes(self):

		fonte = ('Sans-Serif', 15)
		tamanho = (20, 1)

		sg.theme('DarkPurple4')

		layout = [
			[sg.Text('Gerenciar Ingresso', font=('Impact', 20), text_color='white', size=(0, 2))],
			[sg.Button('Incluir Ingresso', font=fonte, size=tamanho)],
			[sg.Button('Lista Ingresso', font=fonte, size=tamanho)],
			[sg.Button('Excluir Ingresso', font=fonte, size=tamanho)],
			[sg.Button('Retornar', font=fonte, size=tamanho)]
		]

		window = sg.Window('Ingresso', layout, size=(400, 360), grab_anywhere=True, element_justification='c')

		button = window.Read()
		valor_escolhido = {'Incluir Ingresso': 1, 'Lista Ingresso': 2, 'Excluir Ingresso': 3, 'Retornar': 0}
		window.Close()
		return valor_escolhido[button[0]]

	def pega_dados_ingresso(self, dados: int):
		mensagem = {
			0: '\nDigite o ID da sessão: ',
			1: '\nEscolha a fileira (A-J): ',
			2: '\nEscolha o acento (1-20): '
		}
		return input(mensagem[dados])

	def mostra_ingresso(self, dados_ingresso):
		print(
			"FILEIRA:", dados_ingresso["fileira"],
			"ACENTO:", dados_ingresso["acento"],
			"FILME:", dados_ingresso["filme"],
			"SALA:", dados_ingresso["sala"],
			"HORARIO:", dados_ingresso["horario"],
			"ID:", dados_ingresso["id_ingresso"]
		)

	def seleciona_ingresso(self):
		id_ingresso = input("ID do ingresso que deseja selecionar: ")
		return id_ingresso

	def mostra_mensagem(self, msg):
		print(msg)
