import PySimpleGUI as sg

sg.theme('DarkPurple4')

layout = [
    [sg.Text('Cinema', font=('Impact', 20), text_color='white', size=(0, 2))],
    [sg.Button('Ingressos', font=('Sans-Serif', 15), size=(20, 1))],
    [sg.Button('Sessões', font=('Sans-Serif', 15), size=(20, 1))],
    [sg.Button('Salas', font=('Sans-Serif', 15), size=(20, 1))],
    [sg.Button('Filmes', font=('Sans-Serif', 15), size=(20, 1))],
    [sg.Button('Gêneros', font=('Sans-Serif', 15), size=(20, 1))],
    [sg.Exit('Sair', font=('Sans-Serif', 15), size=(20, 1))]
]

window = sg.Window('Cinema', layout, size=(400, 360), grab_anywhere=True, element_justification='c')

button, values = window.Read()
