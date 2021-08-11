from entidade.sessao import Sessao
from entidade.poltrona import Poltrona


class Ingresso:

    def __init__(self, id_ingresso: int, sessao: Sessao, fileira: str, acento: str):

        if isinstance(id_ingresso, int):
            self.__id_ingresso = id_ingresso

        if isinstance(sessao, Sessao):
            self.__sessao = sessao

        if isinstance(fileira, str) and isinstance(acento, str):
            self.__poltrona = Poltrona(fileira, acento)

    @property
    def id_ingresso(self):
        return self.__id_ingresso

    @property
    def sessao(self):
        return self.__sessao

    @sessao.setter
    def sessao(self, sessao: Sessao):

        if isinstance(sessao, Sessao):
            self.__sessao = sessao

    @property
    def poltrona(self):
        return self.__poltrona

    @poltrona.setter
    def poltrona(self, fileira: str, acento: str):

        if isinstance(fileira, str) and isinstance(acento, str):
            self.__poltrona = Poltrona(fileira, acento)
