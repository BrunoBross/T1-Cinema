class TelaSistema:

	def tela_opcoes(self):

		while True:
			print("\n\033[1;96m-------==X( CINEMA )X==-------\033[0;0m")
			print("Escolha uma opção:")
			print("0 - Finalizar sistema")
			print("1 - Ingressos")
			print("2 - Sessões")
			print("3 - Salas")
			print("4 - Filmes")
			print("5 - Gêneros")
			print("6 - Poltronas")

			try:
				opcao = int(input("Escolha uma das opções: "))
				if 6 >= opcao >= 0:
					return opcao
				else:
					print('\n\033[1;31mDigite um número entre 0 e 6!\033[0;0m')
			except ValueError:
				print('\n\033[1;31mDigite um número!\033[0;0m')
