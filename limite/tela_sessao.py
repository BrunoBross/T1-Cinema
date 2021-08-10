

class TelaSessao:

	def tela_opcoes(self):
		print("----------SESSAO----------")
		print("Escolha uma opcao")
		print("0 - Retornar")
		print("1 - Incluir Sessao")
		print("2 - Alterar Sessao")
		print("3 - Listar Sessao")
		print("4 - Excluir Sessao")

		opcao = int(input("Escolha uma das opcoes:"))
		return opcao

	def pega_dados_sessao(self):
		print("----------DADOS SESSAO----------")

		horario = input("horario: ")

		filme = input("filme: ")

		sala = input("sala: ")

		return {"horario": horario, "filme": filme, "sala": sala}

	def mostra_sessao(self, dados_sessao):
		print("HORARIO: ", dados_sessao["horario"])
		print("FILME: ", dados_sessao["filme"])
		print("SALA: ", dados_sessao["sala"])
		print()

	def seleciona_sessao(self):
		id_sessao = input("id do sessao que deseja selecionar: ")
		return id_sessao

	def mostra_mensagem(self, msg):
		print(msg)
