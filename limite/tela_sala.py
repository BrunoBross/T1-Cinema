import PySimpleGUI as sg
from limite.temas import tamanho, tamanho_janela, fonte_texto, tema, tema_aviso, fonte_titulo, cor


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

		window = sg.Window('Sala', layout, size=tamanho_janela, element_justification='c')

		button = window.Read()
		valor_escolhido = {'Incluir Sala': 1, 'Alterar Sala': 2, 'Lista Sala': 3, 'Excluir Sala': 4, 'Retornar': 0}
		window.Close()
		return valor_escolhido[button[0]]

	def popup_lista_salas(self, salas: list):

		sg.theme(tema)

		col = [
			[sg.Text('\n'.join(salas), font=fonte_texto, text_color=cor)]
		]
		layout = [
			[sg.Text('Salas Cadastradas:', size=(0, 2), font=('Impact', 20), text_color=cor)],
			[sg.Column(col, size=(400, 150), scrollable=True)],
			[sg.Text('')],
			[sg.Button('Retornar', font=fonte_texto, size=tamanho)]
		]
		window = sg.Window('Salas Cadastradas', layout, size=tamanho_janela, element_justification='c')
		window.Read()
		window.Close()


	def pega_dados_sala(self):

		sg.theme(tema)

		layout = [
			[sg.Text('Incluir Sala:', size=(0, 2), font=('Impact', 20), text_color=cor)],
			[sg.Text('Número da Sala:', font=fonte_texto, text_color=cor), sg.Slider(range=(1, 25), orientation='h', size=(30, 20))],
			[sg.Text('')],
			[sg.Submit('Confirmar', font=fonte_texto), sg.Cancel('Retornar', font=fonte_texto)]
		]
		window = sg.Window('Filmes Cadastrados', layout, size=tamanho_janela, element_justification='c')
		values = window.Read()
		window.Close()
		if values[0] == 'Confirmar' and values[1][0] != '':
			return str(int(values[1][0]))
		else:
			window.Close()
			return None

	def seleciona_sala(self, salas: list):

		sg.theme(tema)

		layout = [
			[sg.Text('Seleciona Sala:', size=(0, 2), font=('Impact', 20), text_color=cor)],
			[sg.Text('Selecione a Sala:', font=fonte_texto, text_color=cor)],
			[sg.Listbox(values=salas, size=(30, 6), font=fonte_texto)],
			[sg.Text('')],
			[sg.Submit('Confirmar', font=fonte_texto), sg.Cancel('Retornar', font=fonte_texto)]
		]
		window = sg.Window('Selecionar', layout, size=tamanho_janela, element_justification='c')
		values = window.Read()
		window.Close()
		if values[0] == 'Confirmar' and len(values[1][0]) != 0 and str(values[1][0])[6].isdecimal():
			print(values)
		else:
			window.Close()

	def altera_sala(self):

		sg.theme(tema)

		layout = [
			[sg.Text('Alterar Sala:', size=(0, 2), font=('Impact', 20), text_color=cor)],
			[sg.Text('Novo Número:', font=fonte_texto, text_color=cor), sg.InputText('', size=(300, 2), font=fonte_texto)],
			[sg.Text('')],
			[sg.Submit('Confirmar', font=fonte_texto), sg.Cancel('Retornar', font=fonte_texto)]
		]
		window = sg.Window('Salas Cadastradas', layout, size=tamanho_janela, element_justification='c')
		values = window.Read()
		if values[0] == 'Confirmar' and values[1][0] != '':
			window.Close()
			return values[1][0]
		else:
			window.Close()

	def exclui_sala(self, salas: list):

		sg.theme(tema)

		layout = [
			[sg.Text('Excluir Sala:', size=(0, 2), font=('Impact', 20), text_color=cor)],
			[sg.Text('Selecione a Sala:', font=fonte_texto, text_color=cor)],
			[sg.Listbox(values=salas, size=(30, 6), font=fonte_texto)],
			[sg.Text('')],
			[sg.Submit('Confirmar', font=fonte_texto), sg.Cancel('Retornar', font=fonte_texto)]
		]
		window = sg.Window('Selecionar', layout, size=tamanho_janela, element_justification='c')
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

		layout = [
			[sg.Text(msg, size=(0, 2), font=fonte_texto, text_color=cor)],
			[sg.Button('Retornar', font=fonte_texto, size=tamanho)]
		]
		window = sg.Window('Selecionar', layout, size=(400, 100), element_justification='c')
		window.Read()
		window.Close()
