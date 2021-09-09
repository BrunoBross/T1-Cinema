import PySimpleGUI as sg
from limite.temas import *


class TelaFilme:

    def tela_opcoes(self):
        sg.theme(tema)
        layout = [
            [sg.Text('Gerenciar Filme', font=fonte_titulo, text_color=cor, size=(0, 2))],
            [sg.Button('Incluir Filme', font=fonte_texto, size=tamanho)],
            [sg.Button('Alterar Filme', font=fonte_texto, size=tamanho)],
            [sg.Button('Listar Filme', font=fonte_texto, size=tamanho)],
            [sg.Button('Excluir Filme', font=fonte_texto, size=tamanho)],
            [sg.Button('Listar Gêneros', font=fonte_texto, size=tamanho)],
            [sg.Button('Retornar', font=fonte_texto, size=tamanho)]
        ]
        window = sg.Window('Filme', layout, size=tamanho_janela,
                           element_justification='c', icon=icone_image)
        valor_escolhido = {'Incluir Filme': 1, 'Alterar Filme': 2, 'Listar Filme': 3,
                           'Excluir Filme': 4, 'Listar Gêneros': 5, 'Retornar': 0}[window.Read()[0]]

        window.Close()
        return valor_escolhido

    def popup_lista_filme(self, filmes: list):
        sg.theme(tema)
        col = [
            [sg.Text('\n'.join(filmes), font=fonte_texto, text_color=cor, background_color=background_listas)]
        ]
        layout = [
            [sg.Text('Filmes Cadastrados:', size=(0, 2), font=fonte_titulo, text_color=cor)],
            [sg.Text('Lista de Filmes:', font=fonte_texto, text_color=cor)],
            [sg.Column(col, size=(400, 150), scrollable=True, background_color=background_listas)],
            [sg.Text('')],
            [sg.Button('Retornar', font=fonte_texto, size=tamanho)]
        ]
        window = sg.Window('Filmes Cadastrados', layout, size=tamanho_janela,
                           element_justification='c', icon=icone_image)

        window.Read()
        window.Close()

    def popup_lista_filmes_por_genero(self, filmes_por_genero: list):
        sg.theme(tema)
        col = [
            [sg.Text('\n'.join(filmes_por_genero), font=fonte_texto, text_color=cor, background_color=background_listas)]
        ]
        layout = [
            [sg.Text('Filmes Cadastrados:', size=(0, 2), font=fonte_titulo, text_color=cor)],
            [sg.Text('Filmes e seus gêneros:', font=fonte_texto, text_color=cor)],
            [sg.Column(col, size=(400, 150), scrollable=True, background_color=background_listas)],
            [sg.Text('')],
            [sg.Button('Retornar', font=fonte_texto, size=tamanho)]
        ]
        window = sg.Window('Filmes Cadastrados', layout, size=tamanho_janela,
                           element_justification='c', icon=icone_image)

        window.Read()
        window.Close()

    def pega_dados_filme(self):
        sg.theme(tema)
        layout = [
            [sg.Text('Incluir Filme:', size=(0, 2), font=fonte_titulo, text_color=cor)],
            [sg.Text('Título:', font=fonte_texto, text_color=cor), sg.InputText('', size=(300, 2), font=fonte_texto)],
            [sg.Text('')],
            [sg.Submit('Confirmar', font=fonte_texto), sg.Cancel('Retornar', font=fonte_texto)]
        ]
        window = sg.Window('filmes', layout, size=tamanho_janela,
                           element_justification='c', icon=icone_image)

        valores = window.Read()
        escolha = valores[0]
        user_input = valores[1][0].strip()

        window.Close()
        if escolha == 'Confirmar' and user_input != '':
            return user_input

    def seleciona_filme(self, filmes: list):
        sg.theme(tema)
        layout = [
            [sg.Text('Seleciona Filme:', size=(0, 2), font=fonte_titulo, text_color=cor)],
            [sg.Text('Selecione o filme:', font=fonte_texto, text_color=cor)],
            [sg.Listbox(values=filmes, size=(30, 6), font=fonte_texto)],
            [sg.Text('')],
            [sg.Submit('Confirmar', font=fonte_texto), sg.Cancel('Retornar', font=fonte_texto)]
        ]
        window = sg.Window('Selecionar', layout, size=tamanho_janela,
                           element_justification='c', icon=icone_image)

        valores = window.Read()
        escolha = valores[0]

        window.Close()
        if escolha == 'Confirmar' and len(valores[1][0]):
            id_filme = str(valores[1][0])[6:].split('T')[0].strip()
            return int(id_filme)

    def altera_filme(self):
        sg.theme(tema)
        layout = [
            [sg.Text('Alterar Filme:', size=(0, 2), font=fonte_titulo, text_color=cor)],
            [sg.Text('Novo título:', font=fonte_texto, text_color=cor),
             sg.InputText('', size=(300, 2), font=fonte_texto)],
            [sg.Text('')],
            [sg.Submit('Confirmar', font=fonte_texto), sg.Cancel('Retornar', font=fonte_texto)]
        ]
        window = sg.Window('filmes', layout, size=tamanho_janela,
                           element_justification='c', icon=icone_image)

        valores = window.Read()
        escolha = valores[0]
        user_input = valores[1][0].strip()

        window.Close()
        if escolha == 'Confirmar' and user_input != '':
            return user_input

    def exclui_filme(self, filmes: list):
        sg.theme(tema)
        layout = [
            [sg.Text('Excluir Filme:', size=(0, 2), font=fonte_titulo, text_color=cor)],
            [sg.Text('Selecione o filme:', font=fonte_texto, text_color=cor)],
            [sg.Listbox(values=filmes, size=(30, 6), font=fonte_texto)],
            [sg.Text('')],
            [sg.Submit('Confirmar', font=fonte_texto), sg.Cancel('Retornar', font=fonte_texto)]
        ]
        window = sg.Window('selecionar', layout, size=tamanho_janela,
                           element_justification='c', icon=icone_image)
        valores = window.Read()
        escolha = valores[0]

        window.Close()
        if escolha == 'Confirmar' and len(valores[1][0]):
            id_filme = str(valores[1][0])[6:].split('T')[0].strip()
            return int(id_filme)

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
                           element_justification='c', icon=icone_image)

        window.Read()
        window.Close()
