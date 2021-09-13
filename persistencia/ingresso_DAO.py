from persistencia.DAO import DAO
from entidade.ingresso import Ingresso


class IngressoDAO(DAO):
    def __init__(self):
        super().__init__('dados/ingressos.pkl')

    def add(self, ingresso: Ingresso):
        if ingresso is not None and isinstance(ingresso, Ingresso):
            super().add(ingresso.id_ingresso, ingresso)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
