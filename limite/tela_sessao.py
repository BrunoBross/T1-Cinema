

class TelaSessao:

	def tela_opcoes(self):
		print("-------==X( SESSÃO )X==-------")
		print("Escolha uma opção:")
		print("0 - Retornar")
		print("1 - Incluir Sessão")
		print("2 - Alterar Sessão")
		print("3 - Listar Sessões")
		print("4 - Excluir Sessão")

		opcao = int(input("Escolha uma das opções:"))
		return opcao

	def pega_dados_sessao(self):
		print("-------==X( DADOS SESSÃO )X==-------")

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
