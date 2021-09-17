from limite.tela_sessao import TelaSessao
from entidade.sessao import Sessao
from persistencia.sessao_DAO import SessaoDAO


class ControladorSessaos:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__sessaos_dao = SessaoDAO()
        self.__id_sessaos = []
        self.__tela_sessao = TelaSessao()
        self.__contador = self.__sessaos_dao.get_last_child()

    def pega_sessao_por_id(self, id_sessao: int):
        for sessao in self.__sessaos_dao.get_all():
            if sessao.id_sessao == id_sessao:
                return sessao
        return None

    def checa_id(self, id_sessao: str):
        if id_sessao.isdecimal() and int(id_sessao) in self.__id_sessaos:
            return True
        return False

    def existem_sessaos_cadastrados(self):
        if len(self.sessaos) > 0:
            return True
        self.__tela_sessao.mostra_mensagem('\nNão há sessões cadastradas')
        return False

    def checa_atributos(self, dados: list):
        for sessao in self.__sessaos_dao.get_all():
            if str(sessao.sala.id_sala) == dados[2] and str(sessao.filme.id_filme) == dados[0] and sessao.horario in dados:
                self.__tela_sessao.mostra_mensagem('Sessão já cadastrada!')
                return False
        return True

    def checa_horario_e_sala(self, dados: list):
        for sessao in self.__sessaos_dao.get_all():
            if sessao.horario in dados and str(sessao.sala.id_sala) in dados:
                self.__tela_sessao.mostra_mensagem(f'A sala Nº {dados[2]} já está ocupada\nno horário das {dados[1]}')
                return False
        return True

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def incluir_sessao(self):
        filmes = self.__controlador_sistema.controlador_filmes
        salas = self.__controlador_sistema.controlador_salas

        if filmes.existem_filmes_cadastrados() and salas.existem_salas_cadastradas():
            dados_sessao = self.__tela_sessao.pega_dados_sessao(
                filmes.dados_lista_filmes(),
                salas.dados_lista_salas()
            )
            if dados_sessao is not None:
                if self.checa_atributos(dados_sessao):
                    if self.checa_horario_e_sala(dados_sessao):
                        filme = filmes.pega_filme_por_id(int(dados_sessao[0]))
                        sala = salas.pega_sala_por_id(int(dados_sessao[2]))
                        horario = dados_sessao[1]
                        sessao = Sessao(self.__contador + 1, filme, horario, sala)
                        self.__sessaos_dao.add(sessao)
                        self.__contador += 1
                        self.__id_sessaos.append(self.__contador)

    def alterar_sessao(self):
        filmes = self.__controlador_sistema.controlador_filmes
        salas = self.__controlador_sistema.controlador_salas

        if self.existem_sessaos_cadastrados():
            id_sessao = self.__tela_sessao.seleciona_sessao(self.dados_lista_sessaos())
            if id_sessao is not None:
                novos_dados_sessao = self.__tela_sessao.altera_sessao(filmes.dados_lista_filmes(),
                                                                      salas.dados_lista_salas())
                if novos_dados_sessao is not None:
                    if self.checa_horario_e_sala(novos_dados_sessao):
                        sessao = self.pega_sessao_por_id(int(id_sessao))
                        for ingresso in self.__controlador_sistema.controlador_ingressos.ingressos:
                            if ingresso.sessao == sessao:
                                self.__tela_sessao.mostra_mensagem('Não é possível alterar está sessão'
                                                                   '\ningressos já foram vendidos')
                                return
                        if novos_dados_sessao[0] != '':
                            filme = filmes.pega_filme_por_id(int(novos_dados_sessao[0]))
                            if sessao.filme is not filme:
                                sessao.filme = filme
                        if novos_dados_sessao[1] != '':
                            if sessao.horario != novos_dados_sessao[1]:
                                sessao.horario = novos_dados_sessao[1]
                        if novos_dados_sessao[2] != '':
                            sala = salas.pega_sala_por_id(int(novos_dados_sessao[2]))
                            if sessao.sala is not sala:
                                sessao.sala = sala

    def dados_lista_sessaos(self):
        return [f'Filme: {sessao.filme.titulo} | Sala Nº {sessao.sala.numero} '
                f'| Horário: {sessao.horario} | ID: {sessao.id_sessao} '
                for sessao in self.__sessaos_dao.get_all()]

    def lista_sessaos(self):
        if self.existem_sessaos_cadastrados():
            self.__tela_sessao.popup_lista_sessaos(self.dados_lista_sessaos())

    def excluir_sessao(self):
        if self.existem_sessaos_cadastrados():
            id_sessao = self.__tela_sessao.exclui_sessao(self.dados_lista_sessaos())
            if id_sessao is not None:
                sessao = self.pega_sessao_por_id(int(id_sessao))
                self.__sessaos_dao.remove(sessao.id_sessao)

    def abre_tela(self):
        lista_opcoes = {
            0: self.retornar,
            1: self.incluir_sessao,
            2: self.alterar_sessao,
            3: self.lista_sessaos,
            4: self.excluir_sessao
        }

        while True:
            lista_opcoes[self.__tela_sessao.tela_opcoes()]()

    @property
    def id_sessaos(self):
        return self.__id_sessaos

    @property
    def sessaos(self):
        return self.__sessaos_dao.get_all()
