

class TelaIngresso:

	def tela_opcoes(self):

		while True:
			print("\n\033[1;96m-------==X( INGRESSO )X==-------\033[0;0m")
			print("Escolha uma opção")
			print("0 - Retornar")
			print("1 - Incluir Ingresso")
			print("2 - Alterar Ingresso")
			print("3 - Listar Ingresso")
			print("4 - Excluir Ingresso")

			try:
				opcao = int(input("Escolha uma das opções: "))
				if 4 >= opcao >= 0:
					return opcao
				else:
					print('\033[1;31mDigite um número entre 0 e 4!\033[0;0m')
			except ValueError:
				print('\033[1;31mDigite um número!\033[0;0m')

	def pega_dados_ingresso(self, dados: int):
		mensagem = {
			0: '\nDigite o ID da sessão: ',
			1: '\nEscolha a fileira: ',
			2: '\nEscolha o acento (1-20): '
		}
		return input(mensagem[dados])



	def mostra_ingresso(self, dados_ingresso):
		print(
			"FILEIRA:", dados_ingresso["fileira"],
			"ACENTO:", dados_ingresso["acento"],
			"FILME:", dados_ingresso["filme"],
			"SALA:", dados_ingresso["sala"],
			"HORARIO:", dados_ingresso["horario"],
			"ID:", dados_ingresso["id_ingresso"]
		)

	def seleciona_ingresso(self):
		id_ingresso = input("ID do ingresso que deseja selecionar: ")
		return id_ingresso

	def mostra_mensagem(self, msg):
		print(msg)
