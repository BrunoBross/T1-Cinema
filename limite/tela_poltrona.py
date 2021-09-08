import PySimpleGUI as sg
from limite.temas import tamanho, tamanho_janela, fonte_texto, tema, tema_aviso, fonte_titulo, cor


class TelaPoltrona:

    def tela_opcoes(self):

        sg.theme(tema)

        layout = [
            [sg.Text('Gerenciar Poltrona', font=fonte_titulo, text_color=cor, size=(0, 2))],
            [sg.Button('Incluir Poltrona', font=fonte_texto, size=tamanho)],
            [sg.Button('Alterar Poltrona', font=fonte_texto, size=tamanho)],
            [sg.Button('Lista Poltrona', font=fonte_texto, size=tamanho)],
            [sg.Button('Excluir Poltrona', font=fonte_texto, size=tamanho)],
            [sg.Button('Retornar', font=fonte_texto, size=tamanho)]
        ]

        window = sg.Window('Poltrona', layout, size=tamanho_janela, element_justification='c')

        button = window.Read()
        valor_escolhido = {'Incluir Poltrona': 1, 'Alterar Poltrona': 2, 'Lista Poltrona': 3,
                           'Excluir Poltrona': 4, 'Retornar': 0}
        window.Close()
        return valor_escolhido[button[0]]

    def pega_dados_poltrona(self):
        print("\n\033[1;96m-------==X( DADOS POLTRONA )X==-------\033[0;0m")
        aviso = '\n\033[1;31mDigite um número correto!\033[0;0m'
        while True:
            fileira = input("Fileira: ")
            acento = input("Acento: ")
            print(f'\nPoltrona: \033[1;96m{fileira}-{acento}\033[0;0m\n')
            while True:
                try:
                    certeza = int(input("Tem certeza da poltrona?\n1 - Sim\n2 - Não\n3 - Cancelar\nDigite um número: "))
                    if 3 >= certeza >= 0:
                        if certeza == 1:
                            return {
                                "fileira": fileira,
                                "acento": acento
                            }
                        elif certeza == 3:
                            cancelar = True
                            break
                        elif certeza == 2:
                            cancelar = False
                            break
                    else:
                        print(aviso)
                except ValueError:
                    print(aviso)
            if cancelar:
                break

    def mostra_poltrona(self, dados_poltrona):
        print(
            "FILEIRA: ", dados_poltrona["fileira"],
            "ACENTO: ", dados_poltrona["acento"],
            "ID: ", dados_poltrona["id_poltrona"]
        )

    def seleciona_poltrona(self):
        id_poltrona = input("ID da poltrona que deseja selecionar: ")
        return id_poltrona

    def mostra_mensagem(self, msg):

        sg.theme(tema_aviso)

        layout = [
            [sg.Text(msg, size=(0, 2), font=fonte_texto, text_color=cor)],
            [sg.Button('Retornar', font=fonte_texto, size=tamanho)]
        ]
        window = sg.Window('Selecionar', layout, size=(420, 100), element_justification='c')
        window.Read()
        window.Close()
