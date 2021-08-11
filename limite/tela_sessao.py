

class TelaSessao:

	def tela_opcoes(self):
		print(
				"\n-------==X( SESSÃO )X==-------"
				"\nEscolha uma opção:"
				"\n0 - Retornar"
				"\n1 - Incluir Sessão"
				"\n2 - Alterar Sessão"
				"\n3 - Listar Sessões"
				"\n4 - Excluir Sessão"
		)

		opcao = int(input("\nEscolha uma das opções:"))
		return opcao

	def pega_dados_sessao(self):
		print("\n-------==X( DADOS SESSÃO )X==-------")

		horario = input("\nhorario: ")

		id_filme = int(input("\nid do filme: "))

		id_sala = input("\nid_sala: ")

		return {
			"horario": horario,
			"filme": id_filme,
			"sala": id_sala
		}

	def mostra_sessao(self, dados_sessao) -> None:
		print(
			"\nID: ", dados_sessao["id_sessao"],
			"\nHORARIO: ", dados_sessao["horario"],
			"\nFILME: ", dados_sessao["filme"],
			"\nSALA: ", dados_sessao["sala"]
			)

	def seleciona_sessao(self):
		id_sessao = input("\nid da sessão que deseja selecionar: ")
		return id_sessao

	def mostra_mensagem(self, msg) -> None:
		print(msg)
