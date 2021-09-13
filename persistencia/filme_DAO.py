from persistencia.DAO import DAO
from entidade.filme import Filme


class FilmeDAO(DAO):
    def __init__(self):
        super().__init__('dados/filmes.pkl')

    def add(self, filme: Filme):
        if filme is not None and isinstance(filme, Filme):
            super().add(filme.id_filme, filme)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
