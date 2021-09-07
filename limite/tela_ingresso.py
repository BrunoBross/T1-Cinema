import PySimpleGUI as sg
from limite.temas import tamanho, tamanho_janela, fonte_texto, tema, tema_aviso, fonte_titulo, cor


class TelaIngresso:

	def tela_opcoes(self):

		sg.theme(tema)

		layout = [
			[sg.Text('Gerenciar Ingresso', font=fonte_titulo, text_color=cor, size=(0, 2))],
			[sg.Button('Incluir Ingresso', font=fonte_texto, size=tamanho)],
			[sg.Button('Lista Ingresso', font=fonte_texto, size=tamanho)],
			[sg.Button('Excluir Ingresso', font=fonte_texto, size=tamanho)],
			[sg.Button('Retornar', font=fonte_texto, size=tamanho)]
		]

		window = sg.Window('Ingresso', layout, size=tamanho_janela, element_justification='c')

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
		sg.theme(tema_aviso)

		layout = [
			[sg.Text(msg, size=(0, 2), font=fonte_texto, text_color=cor)],
			[sg.Button('Retornar', font=fonte_texto, size=tamanho)]
		]
		window = sg.Window('Selecionar', layout, size=(400, 100), element_justification='c')
		window.Read()
		window.Close()
