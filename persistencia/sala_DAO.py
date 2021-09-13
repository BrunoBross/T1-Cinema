from persistencia.DAO import DAO
from entidade.sala import Sala


class SalaDAO(DAO):
    def __init__(self):
        super().__init__('dados/salas.pkl')

    def add(self, sala: Sala):
        if sala is not None and isinstance(sala, Sala):
            super().add(sala.id_sala, sala)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
