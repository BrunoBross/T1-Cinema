import PySimpleGUI as sg
from limite.temas import *
from time import sleep


class TelaSistema:

    def tela_opcoes(self):

        sg.theme(tema)

        # menu_superior = [
        #     ['Menu', ['Créditos']]
        # ]

        layout = [
            # [sg.Menu(menu_superior)],
            [sg.Text('Cinema', font=fonte_titulo, text_color=cor, size=(0, 2))],
            [sg.Button('Ingressos', font=fonte_texto, size=tamanho)],
            [sg.Button('Sessões', font=fonte_texto, size=tamanho)],
            [sg.Button('Salas', font=fonte_texto, size=tamanho)],
            [sg.Button('Filmes', font=fonte_texto, size=tamanho)],
            [sg.Button('Gêneros', font=fonte_texto, size=tamanho)],
            # [sg.Button('Créditos', font=fonte_texto, size=tamanho)],      # botao de creditos
            [sg.Exit('Sair', font=fonte_texto, size=tamanho)]

        ]

        window = sg.Window('Cinema', layout, size=tamanho_janela_inicio, element_justification='c', icon=icone_image, no_titlebar=title_bar, grab_anywhere=grab_any)

        button = window.Read()
        valor_escolhido = {'Ingressos': 1, 'Sessões': 2, 'Salas': 3, 'Filmes': 4, 'Gêneros': 5, 'Créditos': 6, 'Sair': 0}
        window.Close()
        return valor_escolhido[button[0]]

    def creditos(self):

        sg.theme(tema)

        layout = [
            [sg.Text('Créditos', font=fonte_titulo, text_color=cor, size=(0, 2))],
            [sg.Text('Bruno Barreto & Gabriel Avila', size=(0, 2), font=fonte_texto, text_color=cor)],
            [sg.Image(bruno_image, size=(100, 100)), sg.Text('  '), sg.Image(gabriel_image, size=(100, 100))],
            [sg.Text('')],
            [sg.Button('Retornar', font=fonte_texto, size=tamanho)]
        ]
        window = sg.Window('Créditos', layout, size=(tamanho_janela), element_justification='c', icon=icone_image, no_titlebar=title_bar, grab_anywhere=grab_any)
        window.Read()
        window.Close()
