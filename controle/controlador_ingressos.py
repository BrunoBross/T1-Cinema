from limite.tela_ingresso import TelaIngresso
from entidade.ingresso import Ingresso


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
            self.__tela_ingresso.mostra_mensagem('\033[1;31mNão existem sessões cadastradas.\033[0;0m')
            return

        while True:
            control_sessao.lista_sessaos()
            id_sessao = self.__tela_ingresso.pega_dados_ingresso(0)
            if control_sessao.checa_id(id_sessao):
                material.append(control_sessao.pega_sessao_por_id(int(id_sessao)))
                break

        while True:
            fileira = self.__tela_ingresso.pega_dados_ingresso(1)
            if fileira.isalpha() and len(fileira) == 1:
                material.append(fileira)
                break
            else:
                self.__tela_ingresso.mostra_mensagem('\033[1;31mFileira inválida.\033[0;0m')

        while True:
            acento = self.__tela_ingresso.pega_dados_ingresso(2)
            if acento.isdecimal() and 20 >= int(acento) >= 1:
                material.append(acento)
                break
            else:
                self.__tela_ingresso.mostra_mensagem('\033[1;31mAcento inválido.\033[0;0m')

        self.__ingressos.append(Ingresso(material[0], material[1], material[2], material[3]))
        self.__contador += 1


    def alterar_ingresso(self):
        self.lista_ingressos()
        id_ingresso = self.__tela_ingresso.seleciona_ingresso()
        ingresso = self.pega_ingresso_por_id(int(id_ingresso))

        if ingresso is not None:
            self.__controlador_sistema.controlador_sessaos.lista_sessaos()
            novos_dados_ingresso = self.__tela_ingresso.pega_dados_ingresso()
            ingresso.fileira = novos_dados_ingresso["fileira"]
            ingresso.acento = novos_dados_ingresso["acento"]
            ingresso.sessao = novos_dados_ingresso["sessao"]
            self.lista_ingressos()
        else:
            self.__tela_ingresso.mostra_mensagem(
                "\033[1;31mATENÇÃO: ingresso não existente\033[0;0m"
            )


    def lista_ingressos(self):
        self.__tela_ingresso.mostra_mensagem("\n\033[1;96m-------==X( LISTA INGRESSOS )X==-------\033[0;0m")
        for ingresso in self.__ingressos:
            self.__tela_ingresso.mostra_ingresso({
                "poltrona": ingresso.poltrona,
                "sessao_horario": ingresso.sessao.horario,
                "sessao_filme": ingresso.sessao.filme.titulo,
                "id_ingresso": ingresso.id_ingresso
            })


    def excluir_ingresso(self):
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


    def abre_tela(self):
        lista_opcoes = {
            0: self.retornar,
            1: self.incluir_ingresso,
            2: self.alterar_ingresso,
            3: self.lista_ingressos,
            4: self.excluir_ingresso
        }

        while True:
            lista_opcoes[self.__tela_ingresso.tela_opcoes()]()
