import PySimpleGUI as sg

class TelaSala:

	def tela_opcoes(self):

		fonte = ('Sans-Serif', 15)
		tamanho = (20, 1)

		sg.theme('DarkPurple4')

		layout = [
			[sg.Text('Gerenciar Sala', font=('Impact', 20), text_color='white', size=(0, 2))],
			[sg.Button('Incluir Sala', font=fonte, size=tamanho)],
			[sg.Button('Alterar Sala', font=fonte, size=tamanho)],
			[sg.Button('Lista Sala', font=fonte, size=tamanho)],
			[sg.Button('Excluir Sala', font=fonte, size=tamanho)],
			[sg.Button('Retornar', font=fonte, size=tamanho)]
		]

		window = sg.Window('Sala', layout, size=(400, 360), grab_anywhere=True, element_justification='c')

		button = window.Read()
		valor_escolhido = {'Incluir Sala': 1, 'Alterar Sala': 2, 'Lista Sala': 3, 'Excluir Sala': 4, 'Retornar': 0}
		window.Close()
		return valor_escolhido[button[0]]

	def pega_dados_sala(self):

		while True:
			numero = input("Número da Sala: ")
			print(f'\n\033[1;96mSala Nª: {numero}\033[0;0m\n')
			while True:
				try:
					certeza = int(input('Tem certeza disso? \n1- Sim \n2- Não \n3- Cancelar \nDigite uma opção: '))
					if 3 >= certeza >= 1:
						if certeza == 1:
							return numero
						elif certeza == 3:
							cancelar = True
							break
						elif certeza == 2:
							cancelar = False
							break
					else:
						print('\n\033[1;31mDigite um número entre 1 e 3!\033[0;0m\n')
				except ValueError:
					print('\n\033[1;31mDigite um número correto!\033[0;0m\n')
			if cancelar:
				break

	def mostra_sala(self, dados_sala):
		print(
			"NUMERO: ", dados_sala["numero"],
			"ID: ", dados_sala["id_sala"]
		)

	def seleciona_sala(self):
		return input("\nID da sala que deseja selecionar: ")

	def mostra_mensagem(self, msg):
		print(msg)
