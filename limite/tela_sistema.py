class TelaSistema:

	def tela_opcoes(self):

		while True:
			print("\033[1;96m-------==X( CINEMA )X==-------\033[0;0m")
			print("Escolha uma opção:")
			print("0 - Finalizar sistema")
			print("1 - Poltronas")
			print("2 - Sessões")
			print("3 - Ingressos")
			print("4 - Salas")
			print("5 - Filmes")
			print("6 - Gêneros")

			try:
				opcao = int(input("Escolha uma das opções:"))
				return opcao
			except ValueError:
				print('\033[1;31mDigite um número correto!\033[0;0m')
				#TelaSistema.tela_opcoes(self)

