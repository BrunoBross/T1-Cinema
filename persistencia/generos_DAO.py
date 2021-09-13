from persistencia.DAO import DAO
from entidade.genero import Genero


class GeneroDAO(DAO):
    def __init__(self):
        super().__init__('dados/generos.pkl')

    def add(self, genero: Genero):
        if genero is not None and isinstance(genero, Genero):
            super().add(genero.id_genero, genero)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
