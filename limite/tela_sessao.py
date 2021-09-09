import PySimpleGUI as sg
from limite.temas import *


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

        window = sg.Window('Gerenciador de Sessões', layout, size=tamanho_janela,
                           element_justification='c', icon=icone_image)

        valor_escolhido = {
            'Incluir Sessão': 1, 'Alterar Sessão': 2, 'Listar Sessões': 3,
            'Excluir Sessão': 4, 'Retornar': 0
        }[window.Read()[0]]

        window.Close()
        return valor_escolhido

    def pega_dados_sessao(self, filmes: list, salas: list):
        sg.theme(tema)
        horarios = ['13:20', '15:00', '16:40', '18:20', '20:00', '21:40']
        layout = [
            [sg.Text('Filme:', font=fonte_texto, text_color=cor)],
            [sg.Listbox(values=filmes, expand_y=True, no_scrollbar=True, font=fonte_texto,
                        text_color=cor, background_color=background_listas)],

            [sg.Text('Horário:', font=fonte_texto, text_color=cor)],
            [sg.Listbox(values=horarios, expand_y=True, no_scrollbar=True, font=fonte_texto,
                        text_color=cor, background_color=background_listas)],

            [sg.Text('Sala:', font=fonte_texto, text_color=cor)],
            [sg.Listbox(values=salas, expand_y=True, no_scrollbar=True, font=fonte_texto,
                        text_color=cor, background_color=background_listas)],

            [sg.Submit('Confirmar', font=fonte_texto), sg.Cancel('Retornar', font=fonte_texto)]
        ]
        window = sg.Window('incluir sessao', layout, size=tamanho_janela,
                           element_justification='c', icon=icone_image)

        valores = window.Read()
        escolha = valores[0]
        user_input = valores[1]

        window.Close()
        if escolha == 'Confirmar' and [] not in user_input.values():
            id_filme = str(user_input[0])[6:].split('T')[0].strip()
            horario = user_input[1][0]
            id_sala = str(user_input[2])[6:].split('N')[0].strip()
            return [id_filme, horario, id_sala]

    def seleciona_sessao(self):
        pass

    def mostra_mensagem(self, msg):
        sg.theme(tema_aviso)

        layout = [
            [sg.Text(msg, size=(0, 2), font=fonte_texto, text_color=cor)],
            [sg.Button('Retornar', font=fonte_texto, size=tamanho)]
        ]
        window = sg.Window('Selecionar', layout, size=(420, 100),
                           element_justification='c', icon=icone_image)
        window.Read()
        window.Close()
