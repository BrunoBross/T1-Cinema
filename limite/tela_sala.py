

class TelaSala:

	def tela_opcoes(self):

		while True:
			print("\n\033[1;96m-------==X( SALA )X==-------\033[0;0m")
			print("Escolha uma opcao")
			print("0 - Retornar")
			print("1 - Incluir Sala")
			print("2 - Alterar Sala")
			print("3 - Listar Sala")
			print("4 - Excluir Sala")

			try:
				opcao = int(input("Escolha uma das opções: "))
				if 4 >= opcao >= 0:
					return opcao
				else:
					print('\033[1;31mDigite um número entre 0 e 4!\033[0;0m')
			except ValueError:
				print('\033[1;31mDigite um número!\033[0;0m')

	def pega_dados_sala(self):
		aviso = '\033[1;31mDigite um número correto!\033[0;0m'
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
						print(aviso)
				except ValueError:
					print(aviso)
			if cancelar:
				break

	def mostra_sala(self, dados_sala):
		print(
			"NUMERO: ", dados_sala["numero"],
			"ID: ", dados_sala["id_sala"]
		)

	def seleciona_sala(self):
		return input("id do sala que deseja selecionar: ")

	def mostra_mensagem(self, msg):
		print(msg)
