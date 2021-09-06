from entidade.filme import Filme
import PySimpleGUI as sg
from limite.temas import tamanho, fonte, tema


class TelaFilme:

    def tela_opcoes(self):
        sg.theme(tema)

        layout = [
            [sg.Text('Gerenciar Filme', font=('Impact', 20), text_color='white', size=(0, 2))],
            [sg.Button('Incluir Filme', font=fonte, size=tamanho)],
            [sg.Button('Alterar Filme', font=fonte, size=tamanho)],
            [sg.Button('Listar Filme', font=fonte, size=tamanho)],
            [sg.Button('Excluir Filme', font=fonte, size=tamanho)],
            [sg.Button('Listar Gêneros', font=fonte, size=tamanho)],
            [sg.Button('Retornar', font=fonte, size=tamanho)]
        ]

        window = sg.Window('Filme', layout, size=(400, 360), grab_anywhere=True, element_justification='c')

        button = window.Read()
        valor_escolhido = {'Incluir Filme': 1, 'Alterar Filme': 2, 'Listar Filme': 3, 'Excluir Filme': 4,
                           'Listar Gêneros': 5, 'Retornar': 0}
        window.Close()
        return valor_escolhido[button[0]]

    def popup_lista_filme(self, filmes: list):
        sg.theme(tema)
        if len(filmes) <= 0:
            col = [
                [sg.Text('Não há filmes cadastrados.', font=fonte, text_color='white')]
            ]
        else:
            col = [
                [sg.Text('\n'.join(filmes), font=fonte, text_color='white')]
            ]
        layout = [
            [sg.Text('Filmes Cadastrados:', size=(0, 2), font=('Impact', 20), text_color='white')],
            [sg.Column(col, size=(400, 200), scrollable=True)],
            [sg.Button('Retornar', font=fonte, size=tamanho)]
        ]
        window = sg.Window('Filmes Cadastrados', layout, size=(400, 360), element_justification='c')
        window.Read()
        window.Close()

    def lista_generos_do_filme(self, lista: list, filme: Filme):
        print(f'\n\t{filme.titulo}:')
        for genero in lista:
            print(f'* {genero.tipo}')

    def pega_dados_filme(self):

        sg.theme(tema)
        layout = [
            [sg.Text('Incluir Filmes:', size=(0, 2), font=('Impact', 20), text_color='white')],
            [sg.Text('Título:', font=fonte, text_color='white'), sg.InputText('', size=(100, 2), font=fonte)],
            [sg.Text('')],
            [sg.Text('Confirmar?', font=fonte, text_color='white')],
            [sg.Submit('Sim', font=fonte), sg.Cancel('Não', font=fonte)]
        ]
        window = sg.Window('Filmes Cadastrados', layout, size=(400, 360), element_justification='c')
        values = window.Read()
        window.Close()
        if values[0] == 'Sim':
            return values[1][0]
        else:
            window.Close()

    def mostra_filme(self, dados_filme):
        print(
            "TITULO: ", dados_filme["titulo"],
            "ID: ", dados_filme["id_filme"]
        )

    def seleciona_filme(self):
        return input("\nID do filme que deseja selecionar: ")

    def mostra_mensagem(self, msg):
        print(msg)
