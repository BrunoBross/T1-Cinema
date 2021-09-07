import PySimpleGUI as sg
from limite.temas import tamanho, fonte, tema

class TelaSistema:

    def tela_opcoes(self):

        sg.theme(tema)

        layout = [
            [sg.Text('Cinema', font=('Impact', 20), text_color='white', size=(0, 2))],
            [sg.Button('Ingressos', font=fonte, size=tamanho)],
            [sg.Button('Sessões', font=fonte, size=tamanho)],
            [sg.Button('Salas', font=fonte, size=tamanho)],
            [sg.Button('Filmes', font=fonte, size=tamanho)],
            [sg.Button('Gêneros', font=fonte, size=tamanho)],
            [sg.Exit('Sair', font=fonte, size=tamanho)]
        ]

        window = sg.Window('Cinema', layout, size=(400, 360), grab_anywhere=True, element_justification='c')

        button = window.Read()
        valor_escolhido = {'Ingressos': 1, 'Sessões': 2, 'Salas': 3, 'Filmes': 4, 'Gêneros': 5, 'Sair': 0}
        window.Close()
        return valor_escolhido[button[0]]
