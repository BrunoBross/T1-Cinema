

class TelaSala:

	def tela_opcoes(self):
		print("\033[1;96m-------==X( SALA )X==-------\033[0;0m")
		print("Escolha uma opcao")
		print("0 - Retornar")
		print("1 - Incluir Sala")
		print("2 - Alterar Sala")
		print("3 - Listar Sala")
		print("4 - Excluir Sala")

		opcao = int(input("Escolha uma das opcoes:"))
		return opcao

	def pega_dados_sala(self):
		print("\033[1;96m-------==X( DADOS SALA )X==-------\033[0;0m")
		numero = input("numero: ")
		return {
			"numero": numero
		}

	def mostra_sala(self, dados_sala):
		print(
			"NUMERO: ", dados_sala["numero"],
			"ID: ", dados_sala["id_sala"]
		)

	def seleciona_sala(self):
		id_sala = input("id do sala que deseja selecionar: ")
		return id_sala

	def mostra_mensagem(self, msg):
		print(msg)
