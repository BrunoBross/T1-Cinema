# macaco

controlador = input('Nome do controlador:  ')
atributos = input('Atributos da entidade:  ').split()
control = controlador.lower()[:-1]
file = open(f'controlador_{controlador.lower()}.py', 'w+')
#imports
file.write(f'from limite.tela_{controlador.lower()[:-1]} import Tela{controlador[:-1]}\nfrom entidade.{controlador.lower()[:-1]} import {controlador[:-1]}')

#construtor
file.write(f'\n\n\nclass Controlador{controlador}:\n\n\tdef __init__(self, controlador_sistema):\n\t\tself.__controlador_sistema = controlador_sistema\n\t\tself.__{controlador.lower()} = []\n\t\tself.__tela_{controlador.lower()[:-1]} = Tela{controlador[:-1]}()')

#pega por codigo
file.write(f'\n\n\tdef pega_{control}_por_codigo(self, codigo: int):\n\t\tfor {control} in self.__{controlador.lower()}:\n\t\t\tif {control}.codigo == codigo:\n\t\t\t\treturn {control}\n\t\t\treturn None')

#retornar (0)
file.write(f'\n\n\tdef retornar(self):\n\t\tself.__controlador_sistema.abre_tela()')

#incluir (1)
file.write(f'\n\n\tdef incluir_{control}(self):\n\t\tdados_{control} = self.__tela_{control}.pega_dados_{control}()\n\t\t{control} = {controlador[:-1]}(')
for atributo in atributos[:-1]:
    file.write(f'\n\t\t\tdados_{control}["{atributo}"],')
file.write(f'\n\t\t\tdados_{control}["{atributos[-1]}"]\n\t\t)')

#alterar (2)
file.write(f'\n\n\tdef alterar_{control}(self):\n\t\tself.lista_{controlador.lower()}()')
file.write(f'\n\t\t{atributos[0]}_{control} = self.__tela_{control}.seleciona_{control}()')
file.write(f'\n\t\t{control} = self.pega_{control}_por_{atributos[0]}({atributos[0]}_{control})')
file.write(f'\n\n\t\tif {control} is not None:\n\t\t\tnovos_dados_{control} = self.__tela_{control}.pega_dados_{control}()')
for atributo in atributos:
    file.write(f'\n\t\t\t{control}.{atributo} = novos_dados_{control}["{atributo}"]')
file.write(f'\n\t\t\tself.lista_{controlador.lower()}()')
file.write(f'\n\t\telse:\n\t\t\tself.__tela_{control}.mostra_mensagem("ATENÇÃO: {control} não existente")')

#listar (3)
file.write(f'\n\n\tdef lista_{controlador.lower()}(self):\n\t\tfor {control} in self.__{controlador.lower()}:')
file.write(f'\n\t\t\tself.__tela_{control}.mostra_{control}('+'{')
for atributo in atributos:
    if atributo != atributos[-1]:
        file.write(f'\n\t\t\t\t"{atributo}": {control}.{atributo},')
    else:
        file.write(f'\n\t\t\t\t"{atributo}": {control}.{atributo}')
file.write('\n\t\t\t})')

#excluir (4)
file.write(f'\n\n\tdef excluir_{control}(self):\n\t\tself.lista_{controlador.lower()}()\n\t\tcodigo_{control} = self.__tela_{control}.seleciona_{control}()\n\t\t{control} = self.pega_{control}_por_codigo(int(codigo_{control}))')
file.write(f'\n\n\t\tif {control} is not None:\n\t\t\tself.__{controlador.lower()}.remove({control})\n\t\t\tself.lista_{controlador.lower()}()')
file.write(f'\n\t\telse:\n\t\t\tself.__tela_{control}.mostra_mensagem("ATENÇÃO: {controlador[:-1]} não existente")')

#abre tela
file.write('\n\n\tdef abre_tela(self):\n\t\tlista_opcoes = {'+f'\n\t\t\t0: self.retornar,\n\t\t\t1: self.incluir_{control},\n\t\t\t2: self.alterar_{control},\n\t\t\t3: self.lista_{controlador.lower()},\n\t\t\t4: self.excluir_{control}\n\t\t'+'}')
file.write(f'\n\n\t\twhile True:\n\t\t\tlista_opcoes[self.__tela_{control}.tela_opcoes()]()\n')

