from limite.tela_ingresso import TelaIngresso
from entidade.ingresso import Ingresso
from entidade.sessao import Sessao


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

        while True:
            id_sessao = self.__tela_ingresso.pega_sessao(
                [f'ID: {sessao.id_sessao}    Título: {sessao.titulo}' for sessao in self.__ingressos]
            )
            if control_sessao.checa_id(id_sessao):
                material.append(control_sessao.pega_sessao_por_id(int(id_sessao)))
                break


        while True:
            control_sessao.lista_sessaos()

            id_sessao = self.__tela_ingresso.pega_dados_ingresso(0)
            if control_sessao.checa_id(id_sessao):
                material.append(control_sessao.pega_sessao_por_id(int(id_sessao)))
                break

        while True:
            fileira = self.__tela_ingresso.pega_dados_ingresso(1)
            if fileira.isalpha() and len(fileira) == 1:
                if fileira.lower() in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']:
                    material.append(fileira.lower())
                    break
            else:
                self.__tela_ingresso.mostra_mensagem('Fileira inválida.')

        while True:
            acento = self.__tela_ingresso.pega_dados_ingresso(2)
            if acento.isdecimal() and 20 >= int(acento) >= 1:
                material.append(acento)
                break
            else:
                self.__tela_ingresso.mostra_mensagem('Acento inválido.')
        if self.checa_ingresso(material[1], material[2], material[3]):
            self.__ingressos.append(Ingresso(material[0], material[1], material[2], material[3]))
            self.__contador += 1
            return
        self.__tela_ingresso.mostra_mensagem('Ingresso já vendido.')

    def checa_ingresso(self, sessao_dado: Sessao, fileira_dado: str, acento_dado: str):
        if len(self.__ingressos) < 1:
            return True
        for sessao in self.__controlador_sistema.controlador_sessaos.sessaos:
            if sessao == sessao_dado:
                for ingresso in self.__ingressos:
                    if ingresso.fileira == fileira_dado:
                        if ingresso.acento == acento_dado:
                            return False
        return True

    def lista_ingressos(self):

        if len(self.__ingressos) > 0:
            for ingresso in self.__ingressos:
                self.__tela_ingresso.mostra_ingresso({
                    "fileira": ingresso.fileira,
                    "acento": ingresso.acento,
                    "filme": ingresso.sessao.filme.titulo,
                    "sala": ingresso.sessao.sala.numero,
                    "horario": ingresso.sessao.horario,
                    "id_ingresso": ingresso.id_ingresso
                })
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
