from limite.tela_ingresso import TelaIngresso
from entidade.ingresso import Ingresso
from entidade.sessao import Sessao
from controle import controlador_sessaos


class ControladorIngressos:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__ingressos = []
        self.__tela_ingresso = TelaIngresso()
        self.__contador = 0

    def pega_ingresso_por_id(self, id_ingresso: int):
        for ingresso in self.__ingressos:
            if ingresso.id_ingresso == id_ingresso:
                return ingresso
        return None

    def checa_id(self, id_check: str):
        if id_check.isdecimal() and int(id_check) in self.__ingressos:
            return True
        return False

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def incluir_ingresso(self):

        material = [self.__contador + 1]
        control_sessao = self.__controlador_sistema.controlador_sessaos
        if len(control_sessao.sessaos) < 1:
            self.__tela_ingresso.mostra_mensagem('Não há sessão disponível, crie uma antes.')
            return

        # aqui pega a sessao
        while True:
            id_sessao = self.__tela_ingresso.pega_sessao(
                [
                    f'ID: {sessao.id_sessao} | Horario: {sessao.horario} | Sala: {sessao.sala.numero} | Filme: {sessao.filme.titulo}'
                    for sessao in self.__controlador_sistema.controlador_sessaos.sessaos]
            )
            if control_sessao.checa_id(id_sessao):
                material.append(control_sessao.pega_sessao_por_id(int(id_sessao)))
                break

        # aqui pega o acento e poltrona
        while True:
            poltrona = self.__tela_ingresso.pega_poltrona()
            material.append(poltrona)
            break

        if self.checa_ingresso(id_sessao, poltrona):
            self.__ingressos.append(Ingresso(material[0], material[1], material[2]))
            self.__contador += 1
            return
        self.__tela_ingresso.mostra_mensagem('Ingresso já vendido.')

    def checa_ingresso(self, sessao_dado: Sessao, poltrona_dado: str):
        if len(self.__ingressos) < 1:
            return True
        for sessao in self.__controlador_sistema.controlador_sessaos.sessaos:
            if sessao == sessao_dado:
                for ingresso in self.__ingressos:
                    if ingresso.poltrona == poltrona_dado:
                        return False
        return True

    def lista_ingressos(self):

        if len(self.__ingressos) > 0:
            for ingresso in self.__ingressos:
                self.__tela_ingresso.mostra_ingresso(

                    f'Poltrona: {ingresso.poltrona}'
                    f' | Filme: {ingresso.sessao.filme.titulo}'
                    f' | Sala: {ingresso.sessao.sala.numero}'
                    f' | Horário: {ingresso.sessao.horario}'
                    f' | ID: {ingresso.id_ingresso}')

        else:
            self.__tela_ingresso.mostra_mensagem('Não há ingresso disponível, crie um antes.')

    def excluir_ingresso(self):

        if len(self.__ingressos) > 0:

            self.lista_ingressos()
            id_ingresso = self.__tela_ingresso.seleciona_ingresso()
            ingresso = self.pega_ingresso_por_id(int(id_ingresso))

            if ingresso is not None:
                self.__ingressos.remove(ingresso)
                self.lista_ingressos()
            else:
                self.__tela_ingresso.mostra_mensagem(
                    "ATENCAO: Ingresso nao existente"
                )
        else:
            self.__tela_ingresso.mostra_mensagem('Não há ingresso disponível, crie um antes.')

    def abre_tela(self):
        lista_opcoes = {
            0: self.retornar,
            1: self.incluir_ingresso,
            2: self.lista_ingressos,
            3: self.excluir_ingresso
        }

        while True:
            lista_opcoes[self.__tela_ingresso.tela_opcoes()]()

    @property
    def ingressos(self):
        return self.__ingressos
