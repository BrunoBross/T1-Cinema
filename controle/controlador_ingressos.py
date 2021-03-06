from limite.tela_ingresso import TelaIngresso
from entidade.ingresso import Ingresso
from entidade.sessao import Sessao
from persistencia.ingresso_DAO import IngressoDAO


class ControladorIngressos:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__ingressos_dao = IngressoDAO()
        self.__ingressos = self.__ingressos_dao.get_all()
        self.__ids_ingressos = self.__ingressos_dao.get_ids()
        self.__tela_ingresso = TelaIngresso()

    def pega_ingresso_por_id(self, id_ingresso: int):
        try:
            return self.__ingressos_dao.get(id_ingresso)
        except IndexError:
            return None

    def checa_id(self, id_check: str):
        if id_check.isdecimal():
            for ingresso in self.__ingressos:
                if ingresso.id_ingresso == int(id_check):
                    return True
        return False

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def incluir_ingresso(self):

        material = [self.__ingressos_dao.get_last_child() + 1]
        control_sessao = self.__controlador_sistema.controlador_sessaos
        if len(control_sessao.sessaos) < 1:
            self.__tela_ingresso.mostra_mensagem('Não há sessão disponível, crie uma antes.')
            return

        # aqui pega a sessao
        id_sessao = self.__tela_ingresso.pega_sessao(
            [
                f'ID: {sessao.id_sessao} | Horario: {sessao.horario} | Sala: {sessao.sala.numero} | Filme: {sessao.filme.titulo} '
                for sessao in self.__controlador_sistema.controlador_sessaos.sessaos]
        )

        if id_sessao is None or not control_sessao.checa_id(id_sessao):
            return
        material.append(control_sessao.pega_sessao_por_id(int(id_sessao)))

        # aqui pega o acento e poltrona
        while True:
            poltrona = self.__tela_ingresso.pega_poltrona()

            if self.checa_ingresso(id_sessao, poltrona):
                material.append(poltrona)
                self.__ingressos_dao.add(Ingresso(material[0], material[1], material[2]))
                return
            self.__tela_ingresso.mostra_mensagem('Essa poltrona já foi vendida.')

    def checa_ingresso(self, sessao_dado: Sessao, poltrona_dado: str):
        if len(self.__ingressos) < 1:
            return True
        for sessao in self.__controlador_sistema.controlador_sessaos.sessaos:
            if str(sessao.id_sessao) == sessao_dado:
                for ingresso in self.__ingressos:
                    if ingresso.poltrona == poltrona_dado and ingresso.sessao.id_sessao == sessao.id_sessao:
                        return False
        return True

    def existem_ingressos_cadastrados(self):
        if len(self.ingressos) > 0:
            return True
        self.__tela_ingresso.mostra_mensagem('\nNão há ingressos cadastrados.')
        return False

    def lista_ingressos(self):
        if self.existem_ingressos_cadastrados():
            self.__tela_ingresso.popup_lista_ingresso(self.dados_lista_ingressos())

    def dados_lista_ingressos(self):
        return [
            f'Poltrona: {ingresso.poltrona} | Filme: {ingresso.sessao.filme.titulo} | Sala: {ingresso.sessao.sala.numero} | Horário: {ingresso.sessao.horario} | ID: {ingresso.id_ingresso}'
            for ingresso in self.__ingressos]

    def excluir_ingresso(self):

        if len(self.__ingressos) > 0:

            id_ingresso = self.__tela_ingresso.excluir_ingresso(self.dados_lista_ingressos())
            if id_ingresso is not None:
                ingresso = self.pega_ingresso_por_id(int(id_ingresso))
                self.__ingressos_dao.remove(ingresso.id_ingresso)
                self.__tela_ingresso.mostra_mensagem('O ingresso foi removido com sucesso')
            else:
                self.__tela_ingresso.mostra_mensagem(
                    'Não há ingressos cadastrados'
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
