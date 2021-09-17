from limite.tela_genero import TelaGenero
from entidade.genero import Genero
from persistencia.generos_DAO import GeneroDAO


class ControladorGeneros:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__generos_dao = GeneroDAO()
        self.__id_generos = []
        self.__tela_genero = TelaGenero()
        self.__contador = self.__generos_dao.get_last_child()

    def pega_genero_por_id(self, id_genero: int):
        for genero in self.__generos_dao.get_all():
            if genero.id_genero == id_genero:
                return genero
        return None

    def existem_generos_cadastrados(self):
        if len(self.generos) > 0:
            return True
        self.__tela_genero.mostra_mensagem('Não há gêneros disponíveis')
        return False

    def checa_tipo(self, dado: str):
        for genero in self.__generos_dao.get_all():
            if genero.tipo == dado:
                self.__tela_genero.mostra_mensagem(f'O gênero "{dado}" já está cadastrado.')
                return False
        return True

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def incluir_genero(self):
        dados_genero = self.__tela_genero.pega_dados_genero()
        if dados_genero is not None:
            if self.checa_tipo(dados_genero):
                genero = Genero(self.__contador + 1, dados_genero)
                self.__generos_dao.add(genero)
                self.__contador += 1
                self.__id_generos.append(self.__contador)

    def dados_lista_genero(self):
        return [f'ID: {genero.id_genero}     Gênero: {genero.tipo};' for genero in self.generos]

    def alterar_genero(self):
        if self.existem_generos_cadastrados():
            id_genero = self.__tela_genero.seleciona_genero(self.dados_lista_genero())
            if id_genero is not None:
                genero = self.pega_genero_por_id(id_genero)
                novos_dados_genero = self.__tela_genero.altera_genero()
                if self.checa_tipo(novos_dados_genero):
                    genero.tipo = novos_dados_genero

    def adiciona_filme(self):
        if self.existem_generos_cadastrados() and self.__controlador_sistema.controlador_filmes.existem_filmes_cadastrados():
            id_genero, id_filme = self.__tela_genero.adiciona_filme(self.dados_lista_genero(),
                                                                    self.__controlador_sistema.controlador_filmes.dados_lista_filmes())
            if id_genero is not None:
                filme = self.__controlador_sistema.controlador_filmes.pega_filme_por_id(int(id_filme))
                genero = self.pega_genero_por_id(int(id_genero))
                if genero not in filme.generos:
                    filme.generos.append(genero)
                    genero.filmes.append(filme)

    def lista_generos(self):
        if self.existem_generos_cadastrados():
            self.__tela_genero.popup_lista_generos(self.dados_lista_genero())

    def excluir_genero(self):
        if self.existem_generos_cadastrados():
            id_genero = self.__tela_genero.seleciona_genero(self.dados_lista_genero())
            if id_genero is not None:
                genero = self.pega_genero_por_id(id_genero)
                nome = genero.tipo
                self.__generos_dao.remove(genero)
                self.__tela_genero.mostra_mensagem(f'Gênero {nome} removido com sucesso')

    def abre_tela(self):
        lista_opcoes = {
            0: self.retornar,
            1: self.incluir_genero,
            2: self.alterar_genero,
            3: self.lista_generos,
            4: self.excluir_genero,
            5: self.adiciona_filme
        }

        while True:
            lista_opcoes[self.__tela_genero.tela_opcoes()]()

    @property
    def generos(self):
        return self.__generos_dao.get_all()
