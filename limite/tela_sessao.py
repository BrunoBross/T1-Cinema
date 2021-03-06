import PySimpleGUI as sg
from limite.temas import *


class TelaSessao:

    def tela_opcoes(self):
        sg.theme(tema)

        layout = [
            [sg.Text('Gerenciar Sessões', font=fonte_titulo, text_color=cor, size=(0, 2))],
            [sg.Button('Incluir Sessão', font=fonte_texto, size=tamanho)],
            [sg.Button('Alterar Sessão', font=fonte_texto, size=tamanho)],
            [sg.Button('Listar Sessões', font=fonte_texto, size=tamanho)],
            [sg.Button('Excluir Sessão', font=fonte_texto, size=tamanho)],
            [sg.Button('Retornar', font=fonte_texto, size=tamanho)]
        ]

        window = sg.Window('Gerenciador de Sessões', layout, size=tamanho_janela,
                           element_justification='c', icon=icone_image, no_titlebar=title_bar, grab_anywhere=grab_any)

        valor_escolhido = {
            'Incluir Sessão': 1, 'Alterar Sessão': 2, 'Listar Sessões': 3,
            'Excluir Sessão': 4, 'Retornar': 0
        }[window.Read()[0]]

        window.Close()
        return valor_escolhido

    def popup_lista_sessaos(self, sessaos: list):
        sg.theme(tema)
        col = [
            [sg.Text('\n'.join(sessaos), font=fonte_texto, text_color=cor, background_color=background_listas)]
        ]
        layout = [
            [sg.Text('Sessões Cadastradas:', size=(0, 2), font=fonte_titulo, text_color=cor)],
            [sg.Text('Lista de sessões:', font=fonte_texto, text_color=cor)],
            [sg.Column(col, size=(400, 150), scrollable=True, background_color=background_listas)],
            [sg.Text('')],
            [sg.Button('Retornar', font=fonte_texto, size=tamanho)]
        ]
        window = sg.Window('Sessoes', layout, size=tamanho_janela,
                           element_justification='c', icon=icone_image, no_titlebar=title_bar, grab_anywhere=grab_any)

        window.Read()
        window.Close()

    def pega_dados_sessao(self, filmes: list, salas: list):
        sg.theme(tema)
        horarios = ['13:20', '15:00', '16:40', '18:20', '20:00', '21:40']
        layout = [
            [sg.Text('Filme:', font=fonte_texto, text_color=cor)],
            [sg.Spin(values=filmes, font=fonte_texto,
                     text_color=cor, background_color=background_listas)],
            [sg.Text('')],
            [sg.Text('Horário:', font=fonte_texto, text_color=cor)],
            [sg.Spin(values=horarios, font=fonte_texto,
                     text_color=cor, background_color=background_listas)],
            [sg.Text('')],
            [sg.Text('Sala:', font=fonte_texto, text_color=cor)],
            [sg.Spin(values=salas, font=fonte_texto,
                     text_color=cor, background_color=background_listas)],
            [sg.Text('')],
            [sg.Submit('Confirmar', font=fonte_texto), sg.Cancel('Retornar', font=fonte_texto)]
        ]
        window = sg.Window('Incluir sessao', layout, size=tamanho_janela,
                           element_justification='c', icon=icone_image, no_titlebar=title_bar, grab_anywhere=grab_any)

        valores = window.Read()
        escolha = valores[0]
        user_input = valores[1]

        window.Close()
        if escolha == 'Confirmar':
            id_filme = str(user_input[0])[4:].split('T')[0].strip()
            horario = user_input[1]
            id_sala = str(user_input[2])[4:].split('N')[0].strip()
            return [id_filme, horario, id_sala]

    def seleciona_sessao(self, sessaos: list):
        sg.theme(tema)
        layout = [
            [sg.Text('Seleciona Sessão:', size=(0, 2), font=fonte_titulo, text_color=cor)],
            [sg.Text('Selecione a sessão:', font=fonte_texto, text_color=cor)],
            [sg.Listbox(values=sessaos, size=(30, 6), font=fonte_texto)],
            [sg.Text('')],
            [sg.Submit('Confirmar', font=fonte_texto), sg.Cancel('Retornar', font=fonte_texto)]
        ]
        window = sg.Window('Selecionar', layout, size=tamanho_janela,
                           element_justification='c', icon=icone_image, no_titlebar=title_bar, grab_anywhere=grab_any)

        valores = window.Read()
        escolha = valores[0]
        selecionado = valores[1][0]

        window.Close()
        if escolha == 'Confirmar' and len(selecionado):
            id_sessao = (str(selecionado).split(' | ID: ')[1])[:-2]
            return id_sessao

    def altera_sessao(self, filmes: list, salas: list):
        sg.theme(tema)
        horarios = ['13:20', '15:00', '16:40', '18:20', '20:00', '21:40']
        layout = [
            [sg.Text('Filme:', font=fonte_texto, text_color=cor)],
            [sg.Listbox(values=filmes, expand_y=True, no_scrollbar=True, font=fonte_texto,
                        text_color=cor, background_color=background_listas)],
            [sg.Text(' ')],
            [sg.Text('Horário:', font=fonte_texto, text_color=cor)],
            [sg.Listbox(values=horarios, expand_y=True, no_scrollbar=True, font=fonte_texto,
                        text_color=cor, background_color=background_listas)],
            [sg.Text(' ')],
            [sg.Text('Sala:', font=fonte_texto, text_color=cor)],
            [sg.Listbox(values=salas, expand_y=True, no_scrollbar=True, font=fonte_texto,
                        text_color=cor, background_color=background_listas)],
            [sg.Text(' ')],
            [sg.Submit('Confirmar', font=fonte_texto), sg.Cancel('Retornar', font=fonte_texto)]
        ]
        window = sg.Window('Alterar sessao', layout, size=tamanho_janela,
                           element_justification='c', icon=icone_image, no_titlebar=title_bar, grab_anywhere=grab_any)

        valores = window.Read()
        escolha = valores[0]
        user_input = valores[1]

        id_filme = ''
        horario = ''
        id_sala = ''
        window.Close()
        if escolha == 'Confirmar':
            if user_input[0]:
                id_filme = str(user_input[0])[6:].split('T')[0].strip()
            if user_input[1]:
                horario = user_input[1][0]
            if user_input[2]:
                id_sala = str(user_input[2])[6:].split('N')[0].strip()
            return [id_filme, horario, id_sala]

    def exclui_sessao(self, sessaos: list):
        sg.theme(tema)
        layout = [
            [sg.Text('Excluir Sessão:', size=(0, 2), font=fonte_titulo, text_color=cor)],
            [sg.Text('Selecione a sessão:', font=fonte_texto, text_color=cor)],
            [sg.Listbox(values=sessaos, size=(30, 6), font=fonte_texto)],
            [sg.Text('')],
            [sg.Submit('Confirmar', font=fonte_texto), sg.Cancel('Retornar', font=fonte_texto)]
        ]
        window = sg.Window('Selecionar', layout, size=tamanho_janela,
                           element_justification='c', icon=icone_image, no_titlebar=title_bar, grab_anywhere=grab_any)
        valores = window.Read()
        escolha = valores[0]
        selecionado = valores[1][0]

        window.Close()
        if escolha == 'Confirmar' and len(selecionado):
            id_sessao = (str(selecionado).split(' | ID: ')[1])[:-2]
            return id_sessao

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
