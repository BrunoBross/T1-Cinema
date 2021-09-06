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
        layout = [
            [sg.Text('Filmes Cadastrados:', font=('Impact', 20), text_color='white')],
            [sg.Text('\n'.join(filmes), text_color='white')]
        ]
        window = sg.Window('Filmes Cadastrados', layout, size=(400, 60+len(filmes)*17))
        window.Read()

    def lista_generos_do_filme(self, lista: list, filme: Filme):
        print(f'\n\t{filme.titulo}:')
        for genero in lista:
            print(f'* {genero.tipo}')

    def pega_dados_filme(self):
        while True:
            titulo = input("Título: ")
            print('\n\033[1;96m' + titulo + '\033[0;0m\n')
            while True:
                try:
                    certeza = int(input("Tem certeza do título?\n1 - Sim\n2 - Não\n3 - Cancelar\nDigite uma opção: "))
                    if 3 >= certeza >= 0:
                        if certeza == 1:
                            return titulo
                        elif certeza == 3:
                            return None
                        elif certeza == 2:
                            break
                    else:
                        print('\n\033[1;31mDigite um número entre 1 e 3!\033[0;0m\n')
                except ValueError:
                    print('\n\033[1;31mDigite um número correto!\033[0;0m\n')

    def mostra_filme(self, dados_filme):
        print(
            "TITULO: ", dados_filme["titulo"],
            "ID: ", dados_filme["id_filme"]
        )

    def seleciona_filme(self):
        return input("\nID do filme que deseja selecionar: ")

    def mostra_mensagem(self, msg):
        print(msg)
