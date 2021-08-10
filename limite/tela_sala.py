

class TelaSala:

	def tela_opcoes(self):
		print(
				"\n-------==X( SALA )X==-------"
				"\nEscolha uma opção:"
				"\n0 - Retornar"
				"\n1 - Incluir Sala"
				"\n2 - Alterar Sala"
				"\n3 - Listar Salas"
				"\n4 - Excluir Sala"
		)

		opcao = int(input("Escolha uma das opções:"))
		return opcao

	def pega_dados_sala(self):
		print("-------==X( DADOS SALA )X==-------")

		numero = input("numero: ")

		return {"numero": numero}

	def mostra_sala(self, dados_sala):
		print("NUMERO: ", dados_sala["numero"])
		print()

	def seleciona_sala(self):
		id_sala = input("id do sala que deseja selecionar: ")
		return id_sala

	def mostra_mensagem(self, msg):
		print(msg)
