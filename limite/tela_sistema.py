import PySimpleGUI as sg


class TelaSistema:

    def tela_opcoes(self):
        
        fonte = ('Sans-Serif', 15)
        tamanho = (20, 1)

        sg.theme('DarkPurple4')

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
