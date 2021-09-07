import PySimpleGUI as sg
from limite.temas import tamanho, tamanho_janela, fonte_texto, tema, tema_aviso, fonte_titulo, cor
from limite import tela_ingresso


class TelaSistema:

    def tela_opcoes(self):

        tela_ingresso.TelaIngresso.pega_poltrona(self)

        sg.theme(tema)

        layout = [
            [sg.Text('Cinema', font=fonte_titulo, text_color=cor, size=(0, 2))],
            [sg.Button('Ingressos', font=fonte_texto, size=tamanho)],
            [sg.Button('Sessões', font=fonte_texto, size=tamanho)],
            [sg.Button('Salas', font=fonte_texto, size=tamanho)],
            [sg.Button('Filmes', font=fonte_texto, size=tamanho)],
            [sg.Button('Gêneros', font=fonte_texto, size=tamanho)],
            [sg.Exit('Sair', font=fonte_texto, size=tamanho)]
        ]

        window = sg.Window('Cinema', layout, size=tamanho_janela, element_justification='c')

        button = window.Read()
        valor_escolhido = {'Ingressos': 1, 'Sessões': 2, 'Salas': 3, 'Filmes': 4, 'Gêneros': 5, 'Sair': 0}
        window.Close()
        return valor_escolhido[button[0]]
