import PySimpleGUI as sg
from limite.temas import *


class TelaSala:

	def tela_opcoes(self):

		sg.theme(tema)

		layout = [
			[sg.Text('Gerenciar Sala', font=fonte_titulo, text_color=cor, size=(0, 2))],
			[sg.Button('Incluir Sala', font=fonte_texto, size=tamanho)],
			[sg.Button('Alterar Sala', font=fonte_texto, size=tamanho)],
			[sg.Button('Lista Sala', font=fonte_texto, size=tamanho)],
			[sg.Button('Excluir Sala', font=fonte_texto, size=tamanho)],
			[sg.Button('Retornar', font=fonte_texto, size=tamanho)]
		]

		window = sg.Window('Sala', layout, size=tamanho_janela, element_justification='c', icon=icone_image, no_titlebar=title_bar, grab_anywhere=grab_any)

		button = window.Read()
		valor_escolhido = {'Incluir Sala': 1, 'Alterar Sala': 2, 'Lista Sala': 3, 'Excluir Sala': 4, 'Retornar': 0}
		window.Close()
		return valor_escolhido[button[0]]

	def popup_lista_salas(self, salas: list):

		sg.theme(tema)

		col = [
			[sg.Text('\n'.join(salas), font=fonte_texto, text_color=cor, background_color=background_listas)]
		]
		layout = [
			[sg.Text('Salas Cadastradas', size=(0, 2), font=fonte_titulo, text_color=cor)],
			[sg.Text('Lista de Salas:', font=fonte_texto, text_color=cor)],
			[sg.Column(col, size=(400, 150), scrollable=True, background_color=background_listas)],
			[sg.Text('')],
			[sg.Button('Retornar', font=fonte_texto, size=tamanho)]
		]
		window = sg.Window('Salas Cadastradas', layout, size=tamanho_janela, element_justification='c', icon=icone_image, no_titlebar=title_bar, grab_anywhere=grab_any)
		window.Read()
		window.Close()


	def pega_dados_sala(self):

		sg.theme(tema)

		salas = []
		for _ in range(1, 26):
			salas.append(_)

		layout = [
			[sg.Text('Incluir Sala', size=(0, 2), font=fonte_titulo, text_color=cor)],
			[sg.Text('Número da Sala:', font=fonte_texto, text_color=cor), sg.Spin(values=salas, font=fonte_texto, text_color=cor, background_color=background_listas)],
			[sg.Text('')],
			[sg.Submit('Confirmar', font=fonte_texto), sg.Cancel('Retornar', font=fonte_texto)]
		]
		window = sg.Window('Cadastrar Salas', layout, size=tamanho_janela, element_justification='c', icon=icone_image, no_titlebar=title_bar, grab_anywhere=grab_any)
		values = window.Read()
		window.Close()
		if values[0] == 'Confirmar' and values[1][0] != '':
			return str(int(values[1][0]))
		else:
			window.Close()
			return None

	def seleciona_sala(self, salas: list):

		sg.theme(tema)

		col = [sg.Listbox(values=salas, size=(30, 6), font=fonte_texto)]

		layout = [
			[sg.Text('Seleciona Sala', size=(0, 2), font=fonte_titulo, text_color=cor)],
			[sg.Text('Selecione a Sala:', font=fonte_texto, text_color=cor)],
			[col],
			[sg.Text('')],
			[sg.Submit('Confirmar', font=fonte_texto), sg.Cancel('Retornar', font=fonte_texto)]
		]
		window = sg.Window('Selecionar Sala', layout, size=tamanho_janela, element_justification='c', icon=icone_image, no_titlebar=title_bar, grab_anywhere=grab_any)
		values = window.Read()
		window.Close()
		if values[0] == 'Confirmar' and len(values[1][0]) != 0 and str(values[1][0])[6].isdecimal():
			value = (str(values[1][0][0])[4:6]).replace(' ', '')
			return value

	def altera_sala(self):

		sg.theme(tema)

		layout = [
			[sg.Text('Alterar Sala', size=(0, 2), font=fonte_titulo, text_color=cor)],
			[sg.Text('Novo Número:', font=fonte_texto, text_color=cor), sg.Slider(range=(1, 25), orientation='h', size=(30, 20))],
			[sg.Text('')],
			[sg.Submit('Confirmar', font=fonte_texto), sg.Cancel('Retornar', font=fonte_texto)]
		]
		window = sg.Window('Alterar Sala', layout, size=tamanho_janela, element_justification='c', icon=icone_image, no_titlebar=title_bar, grab_anywhere=grab_any)
		values = window.Read()
		window.Close()
		if values[0] == 'Confirmar':
			return str(int(values[1][0]))

	def exclui_sala(self, salas: list):

		sg.theme(tema)

		layout = [
			[sg.Text('Excluir Sala', size=(0, 2), font=fonte_titulo, text_color=cor)],
			[sg.Text('Selecione a Sala:', font=fonte_texto, text_color=cor)],
			[sg.Listbox(values=salas, size=(30, 6), font=fonte_texto)],
			[sg.Text('')],
			[sg.Submit('Confirmar', font=fonte_texto), sg.Cancel('Retornar', font=fonte_texto)]
		]
		window = sg.Window('Excluir Sala', layout, size=tamanho_janela, element_justification='c', icon=icone_image, no_titlebar=title_bar, grab_anywhere=grab_any)
		values = window.Read()
		window.Close()
		if values[0] == 'Confirmar' and len(values[1][0]) != 0 and str(values[1][0])[6].isdecimal():
			return str(values[1][0])[6]
		else:
			window.Close()

	def mostra_sala(self, dados_sala):
		print(
			"NUMERO: ", dados_sala["numero"],
			"ID: ", dados_sala["id_sala"]
		)


	def mostra_mensagem(self, msg):

		sg.theme(tema_aviso)
		if '\n' in msg:
			tamanho_da_janela_de_aviso = (420, 150)
			tamanho_caixa_de_texto = (0, 4)
		else:
			tamanho_da_janela_de_aviso = (420, 100)
			tamanho_caixa_de_texto = (0, 2)
		layout = [
			[sg.Text(msg, size=tamanho_caixa_de_texto, font=fonte_texto, text_color=cor)],
			[sg.Button('Retornar', font=fonte_texto, size=tamanho)]
		]
		window = sg.Window('Selecionar', layout, size=tamanho_da_janela_de_aviso,
						   element_justification='c', icon=icone_image, no_titlebar=title_bar, grab_anywhere=grab_any)

		window.Read()
		window.Close()

