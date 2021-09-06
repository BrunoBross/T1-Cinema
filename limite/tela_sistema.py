class TelaSistema:

    def tela_opcoes(self):
        # while True:

        # print("\n\033[1;96m-------==X( CINEMA )X==-------\033[0;0m")
        # print("Escolha uma opção:")
        # print("0 - Finalizar sistema")
        # print("1 - Ingressos")
        # print("2 - Sessões")
        # print("3 - Salas")
        # print("4 - Filmes")
        # print("5 - Gêneros")
        # #print("6 - Poltronas")
        while True:
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

            button = window.Read()
            valor_escolhido = {'Ingressos': 1, 'Sessões': 2, 'Salas': 3, 'Filmes': 4, 'Gêneros': 5, 'Sair': 0}
            window.Close()
            return valor_escolhido[button[0]]

    # try:
    # 	opcao = int(input("Escolha uma das opções: "))
    # 	if 5 >= opcao >= 0:
    # 		return opcao
    # 	else:
    # 		print('\n\033[1;31mDigite um número entre 0 e 5!\033[0;0m')
    # except ValueError:
    # 	print('\n\033[1;31mDigite um número!\033[0;0m')
