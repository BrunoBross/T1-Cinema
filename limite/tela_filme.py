from entidade.filme import Filme
import PySimpleGUI as sg
from limite.temas import tamanho, tamanho_janela, fonte_texto, tema, tema_aviso, fonte_titulo, cor


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

        window = sg.Window('Filme', layout, size=tamanho_janela, element_justification='c')

        button = window.Read()
        valor_escolhido = {'Incluir Filme': 1, 'Alterar Filme': 2, 'Listar Filme': 3,
                           'Excluir Filme': 4, 'Listar Gêneros': 5, 'Retornar': 0}
        window.Close()
        return valor_escolhido[button[0]]

    def popup_nenhum_registro(self):
        sg.theme(tema_aviso)
        popup = sg.Window('Aviso', [[sg.Text('Não existem', font=fonte_texto, size=tamanho)],
                                    [sg.Text('filmes cadastrados!', font=fonte_texto, size=tamanho)],
                                    [sg.Button('Retornar', font=fonte_texto, size=tamanho)]],
                          size=tamanho_janela, element_justification='c')
        popup.Read()

    def popup_lista_filme(self, filmes: list):

        sg.theme(tema)

        col = [
            [sg.Text('\n'.join(filmes), font=fonte_texto, text_color=cor)]
        ]
        layout = [
            [sg.Text('Filmes Cadastrados:', size=(0, 2), font=('Impact', 20), text_color=cor)],
            [sg.Column(col, size=(400, 150), scrollable=True)],
            [sg.Text('')],
            [sg.Button('Retornar', font=fonte_texto, size=tamanho)]
        ]
        window = sg.Window('Filmes Cadastrados', layout, size=tamanho_janela, element_justification='c')
        window.Read()
        window.Close()

    def lista_generos_do_filme(self, lista: list, filme: Filme):
        print(f'\n\t{filme.titulo}:')
        for genero in lista:
            print(f'* {genero.tipo}')

    def pega_dados_filme(self):

        sg.theme(tema)

        layout = [
            [sg.Text('Incluir Filmes:', size=(0, 2), font=('Impact', 20), text_color=cor)],
            [sg.Text('Título:', font=fonte_texto, text_color=cor), sg.InputText('', size=(300, 2), font=fonte_texto)],
            [sg.Text('')],
            [sg.Submit('Confirmar', font=fonte_texto), sg.Cancel('Retornar', font=fonte_texto)]
        ]
        window = sg.Window('Filmes Cadastrados', layout, size=tamanho_janela, element_justification='c')
        values = window.Read()
        window.Close()
        if values[0] == 'Confirmar' and values[1][0] != '':
            return values[1][0]
        else:
            window.Close()

    def seleciona_filme(self, filmes: list):
        sg.theme(tema)
        layout = [
            [sg.Text('Seleciona Filme:', size=(0, 2), font=('Impact', 20), text_color=cor)],
            [sg.Text('Selecione o filme:', font=fonte_texto, text_color=cor)],
            [sg.Listbox(values=filmes, size=(30, 6), font=fonte_texto)],
            [sg.Text('')],
            [sg.Submit('Confirmar', font=fonte_texto), sg.Cancel('Retornar', font=fonte_texto)]
        ]
        window = sg.Window('Selecionar', layout, size=tamanho_janela, element_justification='c')
        values = window.Read()
        if values[0] == 'Confirmar' and len(values[1][0]) != 0 and str(values[1][0])[6].isdecimal():
            window.Close()
            return str(values[1][0])[6]
        window.Close()
        return None

    def altera_filme(self):

        sg.theme(tema)

        layout = [
            [sg.Text('Alterar Filme:', size=(0, 2), font=('Impact', 20), text_color=cor)],
            [sg.Text('Novo título:', font=fonte_texto, text_color=cor),
             sg.InputText('', size=(300, 2), font=fonte_texto)],
            [sg.Text('')],
            [sg.Submit('Confirmar', font=fonte_texto), sg.Cancel('Retornar', font=fonte_texto)]
        ]
        window = sg.Window('Filmes Cadastrados', layout, size=tamanho_janela, element_justification='c')
        valores = window.Read()
        escolha = valores[0]
        user_input = valores[1][0]

        if escolha == 'Confirmar' and user_input != '':
            window.Close()
            return user_input
        window.Close()

    def exclui_filme(self, filmes: list):
        sg.theme(tema)
        layout = [
            [sg.Text('Excluir Filme:', size=(0, 2), font=('Impact', 20), text_color=cor)],
            [sg.Text('Selecione o filme:', font=fonte_texto, text_color=cor)],
            [sg.Listbox(values=filmes, size=(30, 6), font=fonte_texto)],
            [sg.Text('')],
            [sg.Submit('Confirmar', font=fonte_texto), sg.Cancel('Retornar', font=fonte_texto)]
        ]
        window = sg.Window('Selecionar', layout, size=tamanho_janela, element_justification='c')
        values = window.Read()
        escolha = values[0]
        window.Close()
        if escolha == 'Confirmar' and len(values[1][0]):
            id_filme = str(values[1][0])[6:].split('T')[0].strip()
            return int(id_filme)
        window.Close()

    def mostra_filme(self, dados_filme):
        print(
            "TITULO: ", dados_filme["titulo"],
            "ID: ", dados_filme["id_filme"]
        )

    def mostra_mensagem(self, msg):

        sg.theme(tema_aviso)

        layout = [
            [sg.Text(msg, size=(0, 2), font=fonte_texto, text_color=cor)],
            [sg.Button('Retornar', font=fonte_texto, size=tamanho)]
        ]
        window = sg.Window('Selecionar', layout, size=(400, 100), element_justification='c')
        window.Read()
        window.Close()
