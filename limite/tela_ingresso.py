import PySimpleGUI as sg
from limite.temas import *


class TelaIngresso:

    def tela_opcoes(self):

        sg.theme(tema)

        layout = [
            [sg.Text('Gerenciar Ingresso', font=fonte_titulo, text_color=cor, size=(0, 2))],
            [sg.Button('Incluir Ingresso', font=fonte_texto, size=tamanho)],
            [sg.Button('Lista Ingresso', font=fonte_texto, size=tamanho)],
            [sg.Button('Excluir Ingresso', font=fonte_texto, size=tamanho)],
            [sg.Button('Retornar', font=fonte_texto, size=tamanho)]
        ]

        window = sg.Window('Ingresso', layout, size=tamanho_janela, element_justification='c', icon=icone_image,
                           no_titlebar=title_bar, grab_anywhere=grab_any)

        button = window.Read()
        valor_escolhido = {'Incluir Ingresso': 1, 'Lista Ingresso': 2, 'Excluir Ingresso': 3, 'Retornar': 0}
        window.Close()
        return valor_escolhido[button[0]]

    def pega_sessao(self, sessoes: list):

        sg.theme(tema)

        layout = [
            [sg.Text('Incluir Ingresso:', size=(0, 2), font=fonte_titulo, text_color=cor)],
            [sg.Text('Selecione a Sessão:', font=fonte_texto, text_color=cor)],
            [sg.Listbox(values=sessoes, size=(80, 6), font=fonte_texto)],
            [sg.Submit('Confirmar', font=fonte_texto), sg.Cancel('Retornar', font=fonte_texto)]
        ]
        window = sg.Window('Selecionar', layout, size=(500, 380), element_justification='c', icon=icone_image,
                           no_titlebar=title_bar, grab_anywhere=grab_any)
        values = window.Read()
        window.Close()
        if values[0] == 'Confirmar' and str(values[1][0]).replace('[', '').replace(']', '') != '':
            # pega o ID e da um replace pra garantir que nao vai ter espaço em branco
            value = str(values[1][0][0][4:6]).replace(' ', '')
            return value
        else:
            return None

    def pega_poltrona(self):

        sg.theme(tema)

        # colunas de poltronas
        coluna1 = [
            [sg.Button('H-1', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('G-1', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('F-1', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('E-1', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('D-1', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('C-1', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('B-1', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('A-1', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')]
        ]
        coluna2 = [
            [sg.Button('H-2', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('G-2', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('F-2', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('E-2', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('D-2', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('C-2', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('B-2', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('A-2', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')]
        ]
        coluna3 = [
            [sg.Button('H-3', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('G-3', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('F-3', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('E-3', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('D-3', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('C-3', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('B-3', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('A-3', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')]
        ]
        coluna4 = [
            [sg.Button('H-4', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('G-4', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('F-4', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('E-4', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('D-4', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('C-4', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('B-4', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('A-4', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')]
        ]
        coluna5 = [
            [sg.Button('H-5', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('G-5', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('F-5', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('E-5', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('D-5', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('C-5', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('B-5', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('A-5', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')]
        ]
        coluna6 = [
            [sg.Button('H-6', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('G-6', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('F-6', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('E-6', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('D-6', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('C-6', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('B-6', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('A-6', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')]
        ]
        coluna7 = [
            [sg.Button('H-7', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('G-7', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('F-7', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('E-7', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('D-7', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('C-7', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('B-7', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('A-7', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')]
        ]
        coluna8 = [
            [sg.Button('H-8', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('G-8', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('F-8', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('E-8', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('D-8', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('C-8', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('B-8', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('A-8', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')]
        ]
        coluna9 = [
            [sg.Button('H-9', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('G-9', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('F-9', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('E-9', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('D-9', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('C-9', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('B-9', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')],
            [sg.Button('A-9', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')]
        ]
        coluna10 = [
            [sg.Button('H-10', image_filename=poltrona_image, image_size=(30, 30), font='impact',
                       button_color='white')],
            [sg.Button('G-10', image_filename=poltrona_image, image_size=(30, 30), font='impact',
                       button_color='white')],
            [sg.Button('F-10', image_filename=poltrona_image, image_size=(30, 30), font='impact',
                       button_color='white')],
            [sg.Button('E-10', image_filename=poltrona_image, image_size=(30, 30), font='impact',
                       button_color='white')],
            [sg.Button('D-10', image_filename=poltrona_image, image_size=(30, 30), font='impact',
                       button_color='white')],
            [sg.Button('C-10', image_filename=poltrona_image, image_size=(30, 30), font='impact',
                       button_color='white')],
            [sg.Button('B-10', image_filename=poltrona_image, image_size=(30, 30), font='impact',
                       button_color='white')],
            [sg.Button('A-10', image_filename=poltrona_image, image_size=(30, 30), font='impact', button_color='white')]
        ]

        layout = [
            [sg.Text('Selecione Sua Poltrona:', font=fonte_texto)],
            [sg.Column(coluna1), sg.Column(coluna2), sg.Column(coluna3), sg.Column(coluna4), sg.Column(coluna5),
             sg.Column(coluna6), sg.Column(coluna7), sg.Column(coluna8), sg.Column(coluna9), sg.Column(coluna10)],
            [sg.Text('\n\n\n\n')],
            [sg.Text('TELA', background_color='red', size=(15, 2), justification='c', font=('Sans-Serif', 15, 'bold'),
                     text_color='white')]
        ]
        window = sg.Window('Selecionar Poltrona', layout, size=(560, 490), element_justification='c', icon=icone_image,
                           no_titlebar=title_bar, grab_anywhere=grab_any)
        values = window.Read()
        window.Close()
        return values[0]

    def popup_lista_ingresso(self, dados_ingressos: list):
        sg.theme(tema)

        col = [
            [sg.Text('\n'.join(dados_ingressos), font=fonte_texto, text_color=cor, background_color=background_listas)]
        ]

        layout = [
            [sg.Text('Ingressos Cadastrados:', size=(0, 2), font=fonte_titulo, text_color=cor)],
            [sg.Text('Lista de Ingressos:', font=fonte_texto, text_color=cor)],
            [sg.Column(col, size=(400, 150), scrollable=True, background_color=background_listas)],
            [sg.Text('')],
            [sg.Button('Retornar', font=fonte_texto, size=tamanho)]
        ]
        window = sg.Window('Ingressos Cadastrados', layout, size=tamanho_janela, element_justification='c',
                           icon=icone_image, no_titlebar=title_bar, grab_anywhere=grab_any)

        window.Read()
        window.Close()

    def pega_dados_ingresso(self, sessoes: list):

        mensagem = {
            0: self.pega_sessao(),
            1: self.pega_poltrona()
        }
        return mensagem[dados]

    def excluir_ingresso(self, ingressos: list):

        sg.theme(tema)
        layout = [
            [sg.Text('Excluir Ingresso:', size=(0, 2), font=fonte_titulo, text_color=cor)],
            [sg.Text('Selecione o Ingresso:', font=fonte_texto, text_color=cor)],
            [sg.Listbox(values=ingressos, size=(30, 6), font=fonte_texto)],
            [sg.Text('')],
            [sg.Submit('Confirmar', font=fonte_texto), sg.Cancel('Retornar', font=fonte_texto)]
        ]
        window = sg.Window('Selecionar Ingresso', layout, size=tamanho_janela, element_justification='c',
                           icon=icone_image, no_titlebar=title_bar, grab_anywhere=grab_any)
        values = window.Read()
        escolha = values[0]

        window.Close()
        if escolha == 'Confirmar':
            value = str((values[1])[0]).replace('{', '').replace("'", '').replace(' ', '').replace('[', '').replace(']', '')
            return value[-2:].replace(':', '')

    def seleciona_ingresso(self):
        id_ingresso = input("ID do ingresso que deseja selecionar: ")
        return id_ingresso

    def mostra_mensagem(self, msg):
        sg.theme(tema_aviso)

        layout = [
            [sg.Text(msg, size=(0, 2), font=fonte_texto, text_color=cor)],
            [sg.Button('Retornar', font=fonte_texto, size=tamanho)]
        ]
        window = sg.Window('Selecionar', layout, size=(420, 100), element_justification='c', icon=icone_image,
                           no_titlebar=title_bar, grab_anywhere=grab_any)
        window.Read()
        window.Close()
