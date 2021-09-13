from limite.tela_filme import TelaFilme
from entidade.filme import Filme
from persistencia.filme_DAO import FilmeDAO


class ControladorFilmes:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__filmes_dao = FilmeDAO()
        self.__filmes = self.__filmes_dao.get_all()
        self.__id_filmes = []
        self.__tela_filme = TelaFilme()
        self.__contador = 0

    def pega_filme_por_id(self, id_filme: int):
        for filme in self.__filmes:
            if filme.id_filme == id_filme:
                return filme
        return None

    def existem_filmes_cadastrados(self):
        if len(self.filmes) > 0:
            return True
        self.__tela_filme.mostra_mensagem('\nNão há filmes cadastrados.')
        return False

    def checa_titulo(self, dado: str):
        for filme in self.__filmes:
            if filme.titulo == dado:
                self.__tela_filme.mostra_mensagem(f'O filme "{dado}" já está cadastrado.')
                return False
        return True

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def incluir_filme(self):
        dados_filme = self.__tela_filme.pega_dados_filme()
        if dados_filme is not None:
            if self.checa_titulo(dados_filme):
                filme = Filme(self.__contador + 1, dados_filme)
                self.__filmes_dao.add(filme)
                self.__contador += 1
                self.__id_filmes.append(self.__contador)

    def alterar_filme(self):
        if self.existem_filmes_cadastrados():
            id_filme = self.__tela_filme.seleciona_filme(self.dados_lista_filmes())
            if id_filme is not None:
                filme = self.pega_filme_por_id(int(id_filme))
                novos_dados_filme = self.__tela_filme.altera_filme()
                if novos_dados_filme is not None:
                    filme.titulo = novos_dados_filme

    def dados_lista_filmes(self):
        return [f'ID: {filme.id_filme}    Título: {filme.titulo}'
                for filme in self.__filmes]

    def dados_lista_filme_por_genero(self):
        generos = [genero for genero in self.__controlador_sistema.controlador_generos.generos if
                   len(genero.filmes) > 0]
        filmes = [genero.filmes for genero in generos]
        filmes_por_genero = []
        for genero, filmes_lista in zip(generos, filmes):
            filmes_por_genero.append(f'{genero.tipo}:')
            for filme in filmes_lista:
                filmes_por_genero.append(f'   {filme.titulo}')
        return filmes_por_genero

    def lista_filmes(self):
        if self.existem_filmes_cadastrados():
            self.__tela_filme.popup_lista_filme(self.dados_lista_filmes())

    def excluir_filme(self):
        if self.existem_filmes_cadastrados():
            id_filme = self.__tela_filme.exclui_filme(self.dados_lista_filmes())
            if id_filme is not None:
                filme = self.pega_filme_por_id(int(id_filme))
                nome = filme.titulo
                self.__filmes_dao.remove(filme.id_filme)
                self.__tela_filme.mostra_mensagem(f'\nO filme "{nome}"\nfoi removido com sucesso')

    def listar_generos_por_id(self):
        if self.existem_filmes_cadastrados() and self.__controlador_sistema.controlador_generos.existem_generos_cadastrados():
            self.__tela_filme.popup_lista_filmes_por_genero(self.dados_lista_filme_por_genero())

    def abre_tela(self):
        lista_opcoes = {
            0: self.retornar,
            1: self.incluir_filme,
            2: self.alterar_filme,
            3: self.lista_filmes,
            4: self.excluir_filme,
            5: self.listar_generos_por_id
        }

        while True:
            lista_opcoes[self.__tela_filme.tela_opcoes()]()

    @property
    def id_filmes(self):
        return self.__id_filmes

    @property
    def filmes(self):
        return self.__filmes

    @property
    def tela(self):
        return self.__tela_filme
