from persistencia.DAO import DAO
from entidade.sessao import Sessao


class SessaoDAO(DAO):
    def __init__(self):
        super().__init__('dados/sessaos.pkl')

    def add(self, sessao: Sessao):
        if sessao is not None and isinstance(sessao, Sessao):
            super().add(sessao.id_sessao, sessao)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
