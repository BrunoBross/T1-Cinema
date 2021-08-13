

class TelaPoltrona:

	def tela_opcoes(self):

		while True:
			print("\n\033[1;96m-------==X( POLTRONA )X==-------\033[0;0m")
			print("Escolha uma opcao")
			print("0 - Retornar")
			print("1 - Incluir Poltrona")
			print("2 - Alterar Poltrona")
			print("3 - Listar Poltrona")
			print("4 - Excluir Poltrona")

			try:
				opcao = int(input("Escolha uma das opções: "))
				if 4 >= opcao >= 0:
					return opcao
				else:
					print('\033[1;31mDigite um número correto!\033[0;0m')
			except ValueError:
				print('\033[1;31mDigite um número correto!\033[0;0m')

	def pega_dados_poltrona(self):
		print("\n\033[1;96m-------==X( DADOS POLTRONA )X==-------\033[0;0m")
		aviso = '\033[1;31mDigite um número correto!\033[0;0m'
		while True:
			fileira = input("Fileira: ")
			acento = input("Acento: ")
			print(f'Poltrona: \033[1;96m{fileira}-{acento}\033[0;0m')
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
		id_poltrona = input("id do poltrona que deseja selecionar: ")
		return id_poltrona

	def mostra_mensagem(self, msg):
		print(msg)
