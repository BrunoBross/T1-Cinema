import PySimpleGUI as sg
from limite.temas import tamanho, tamanho_janela, fonte_texto, tema, tema_aviso, fonte_titulo, cor


class TelaSessao:

	def tela_opcoes(self):
		sg.theme(tema)

		layout = [
			[sg.Text('Gerenciar Sessões', font=fonte_titulo, text_color=cor, size=(0, 2))],
			[sg.Button('Incluir Sessão', font=fonte_texto, size=tamanho)],
			[sg.Button('Alterar Sessão', font=fonte_texto, size=tamanho)],
			[sg.Button('Listar Gêneros', font=fonte_texto, size=tamanho)],
			[sg.Button('Excluir Sessão', font=fonte_texto, size=tamanho)],
			[sg.Button('Retornar', font=fonte_texto, size=tamanho)]
		]

		window = sg.Window('Gerenciador de Sessões', layout, size=tamanho_janela, element_justification='c')

		valor_escolhido = {
			'Incluir Sessão': 1, 'Alterar Sessão': 2, 'Listar Sessões': 3,
			'Excluir Sessão': 4, 'Retornar': 0
		}[window.Read()[0]]

		window.Close()
		return valor_escolhido

	def pega_dados_sessao(self, dado: str):

		print("\n\033[1;96m-------==X( DADOS SESSÃO )X==-------\033[0;0m")
		mensagem = {
			"id_filme": "Digite o ID do filme: ",
			"horario": "Horário da sessão: ",
			"id_sala": "Digite o ID da sala: ",
			"certeza": "Pressione Enter para confirmar: "
		}
		return input(f'{mensagem[dado]}')

	def mostra_sessao(self, dados_sessao):
		print(
			"FILME: ", dados_sessao["filme"], "HORÁRIO: ", dados_sessao["horario"],
			"SALA: ", dados_sessao["sala"], "ID: ", dados_sessao["id_sessao"]
		)

	def seleciona_sessao(self):
		return input("\nID da sessão que deseja selecionar: ")

	def mostra_mensagem(self, msg):

		sg.theme(tema_aviso)

		layout = [
			[sg.Text(msg, size=(0, 2), font=fonte_texto, text_color=cor)],
			[sg.Button('Retornar', font=fonte_texto, size=tamanho)]
		]
		window = sg.Window('Selecionar', layout, size=(420, 100), element_justification='c')
		window.Read()
		window.Close()
