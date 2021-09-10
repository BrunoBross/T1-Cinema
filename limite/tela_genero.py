import PySimpleGUI as sg
from limite.temas import *


class TelaGenero:

    def tela_opcoes(self):
        sg.theme(tema)

        layout = [
            [sg.Text('Gerenciar Gêneros', font=fonte_titulo, text_color=cor, size=(0, 2))],
            [sg.Button('Incluir Gênero', font=fonte_texto, size=tamanho)],
            [sg.Button('Alterar Gênero', font=fonte_texto, size=tamanho)],
            [sg.Button('Listar Gêneros', font=fonte_texto, size=tamanho)],
            [sg.Button('Excluir Gênero', font=fonte_texto, size=tamanho)],
            [sg.Button('Adicionar Filme', font=fonte_texto, size=tamanho)],
            [sg.Button('Retornar', font=fonte_texto, size=tamanho)]
        ]

        window = sg.Window('Gerenciador de Gêneros', layout, size=tamanho_janela,
                           element_justification='c', icon=icone_image, no_titlebar=title_bar, grab_anywhere=grab_any)

        valor_escolhido = {
            'Incluir Gênero': 1, 'Alterar Gênero': 2, 'Listar Gêneros': 3,
            'Excluir Gênero': 4, 'Adicionar Filme': 5, 'Retornar': 0
        }[window.Read()[0]]

        window.Close()
        return valor_escolhido

    def adiciona_filme(self, generos: list, filmes: list):
        sg.theme(tema)
        coluna_generos = [
            [sg.Listbox(values=generos, size=(30, 6), font=fonte_texto, text_color=cor)]
        ]
        coluna_filmes = [
            [sg.Listbox(values=filmes, size=(30, 6), font=fonte_texto, text_color=cor)]
        ]
        layout = [
            [sg.Text('Gêneros Cadastrados:', size=(0, 1), font=fonte_titulo, text_color=cor)],
            [sg.Column(coluna_generos, size=(400, 90), scrollable=True)],
            [sg.Text('Filmes Cadastrados:', size=(0, 1), font=fonte_titulo, text_color=cor)],
            [sg.Column(coluna_filmes, size=(400, 90), scrollable=True)],
            [sg.Button('Confirmar', font=fonte_texto, size=tamanho),
             sg.Button('Retornar', font=fonte_texto, size=tamanho)]
        ]
        window = sg.Window('generos', layout, size=tamanho_janela,
                           element_justification='c', icon=icone_image, no_titlebar=title_bar, grab_anywhere=grab_any)

        valores = window.Read()
        id_genero_e_filme = (str(valores[1][0])[6:].split('G')[0].strip(),
                             str(valores[1][1])[6:].split('T')[0].strip())
        escolha = valores[0]
        window.Close()
        if escolha == 'Confirmar' and '' not in id_genero_e_filme:
            return id_genero_e_filme
        return None, None

    def popup_lista_generos(self, generos: list):
        sg.theme(tema)
        col = [
            [sg.Text('\n'.join(generos), font=fonte_texto,
                     text_color=cor, background_color=background_listas)]
        ]
        layout = [
            [sg.Text('Gêneros Cadastrados:', size=(0, 2), font=fonte_titulo, text_color=cor)],
            [sg.Text('Lista de Gêneros:', font=fonte_texto, text_color=cor)],
            [sg.Column(col, size=(400, 150), scrollable=True, background_color=background_listas)],
            [sg.Text('')],
            [sg.Button('Retornar', font=fonte_texto, size=tamanho)]
        ]
        window = sg.Window('generos', layout, size=tamanho_janela,
                           element_justification='c', icon=icone_image, no_titlebar=title_bar, grab_anywhere=grab_any)

        window.Read()
        window.Close()

    def pega_dados_genero(self):
        sg.theme(tema)
        layout = [
            [sg.Text('Incluir Gênero:', size=(0, 2), font=fonte_titulo, text_color=cor)],
            [sg.Text('Gênero:', font=fonte_texto, text_color=cor), sg.InputText('', size=(300, 2), font=fonte_texto)],
            [sg.Text('')],
            [sg.Submit('Confirmar', font=fonte_texto), sg.Cancel('Retornar', font=fonte_texto)]
        ]
        window = sg.Window('generos', layout, size=tamanho_janela,
                           element_justification='c', icon=icone_image, no_titlebar=title_bar, grab_anywhere=grab_any)

        valores = window.Read()
        escolha = valores[0]
        user_input = valores[1][0].strip()

        window.Close()
        if escolha == 'Confirmar' and user_input != '':
            return user_input

    def seleciona_genero(self, generos: list):
        sg.theme(tema)
        layout = [
            [sg.Text('Seleciona Gênero:', size=(0, 2), font=fonte_titulo, text_color=cor)],
            [sg.Text('Selecione o gênero:', font=fonte_texto, text_color=cor)],
            [sg.Listbox(values=generos, size=(30, 6), font=fonte_texto)],
            [sg.Text('')],
            [sg.Submit('Confirmar', font=fonte_texto), sg.Cancel('Retornar', font=fonte_texto)]
        ]
        window = sg.Window('Selecionar', layout, size=tamanho_janela,
                           element_justification='c', icon=icone_image, no_titlebar=title_bar, grab_anywhere=grab_any)

        valores = window.Read()
        escolha = valores[0]

        window.Close()
        if escolha == 'Confirmar' and len(valores[1][0]):
            id_genero = str(valores[1][0])[6:].split('G')[0].strip()
            return int(id_genero)

    def altera_genero(self):
        sg.theme(tema)
        layout = [
            [sg.Text('Alterar Gênero:', size=(0, 2), font=fonte_titulo, text_color=cor)],
            [sg.Text('Novo gênero:', font=fonte_texto, text_color=cor),
             sg.InputText('', size=(300, 2), font=fonte_texto)],
            [sg.Text('')],
            [sg.Submit('Confirmar', font=fonte_texto), sg.Cancel('Retornar', font=fonte_texto)]
        ]
        window = sg.Window('generos', layout, size=tamanho_janela,
                           element_justification='c', icon=icone_image, no_titlebar=title_bar, grab_anywhere=grab_any)

        valores = window.Read()
        escolha = valores[0]
        user_input = valores[1][0].strip()

        window.Close()
        if escolha == 'Confirmar' and user_input != '':
            return user_input

    def exclui_genero(self, generos: list):
        sg.theme(tema)
        layout = [
            [sg.Text('Excluir Gênero:', size=(0, 2), font=fonte_titulo, text_color=cor)],
            [sg.Text('Selecione o gênero:', font=fonte_texto, text_color=cor)],
            [sg.Listbox(values=generos, size=(30, 6), font=fonte_texto)],
            [sg.Text('')],
            [sg.Submit('Confirmar', font=fonte_texto), sg.Cancel('Retornar', font=fonte_texto)]
        ]
        window = sg.Window('selecionar gênero', layout, size=tamanho_janela,
                           element_justification='c', icon=icone_image, no_titlebar=title_bar, grab_anywhere=grab_any)
        valores = window.Read()
        escolha = valores[0]

        window.Close()
        if escolha == 'Confirmar' and len(valores[1][0]):
            id_genero = str(valores[1][0])[6:].split('G')[0].strip()
            return int(id_genero)

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
