

tela = input('Insira o nome da classe da entidade:   ')
atributos = input('Atributos da entidade:  ').split()
tel = tela.lower()
a = open(f'tela_{tel}.py', 'w+')

#classe
a.write(f'\n\n\nclass Tela{tela}:')

#tela opções
a.write(f'\n\n\tdef tela_opcoes(self):\n\t\tprint("----------{tela.upper()}----------")\n\t\tprint("Escolha uma opção")\n\t\tprint("0 - Retornar")\n\t\tprint("1 - Incluir {tela}")\n\t\tprint("2 - Alterar {tela}")\n\t\tprint("3 - Listar {tela}")\n\t\tprint("4 - Excluir {tela}")')
a.write(f'\n\n\t\topcao = int(input("Escolha uma das opções:"))\n\t\treturn opcao')

#pega dados
a.write(f'\n\n\tdef pega_dados_{tel}(self):\n\t\tprint("----------DADOS {tel.upper()}----------")')
for atributo in atributos:
    a.write(f'\n\t\t{atributo} = input("{atributo}: ")')
a.write('\n\n\t\treturn {')
for atributo in atributos[:-1]:
    a.write(f'"{atributo}": {atributo}, ')
a.write(f'"{atributos[-1]}": {atributos[-1]}'+'}')

#mostra
a.write(f'\n\n\tdef mostra_{tel}(self, dados_{tel}):')
for atributo in atributos:
    a.write(f'\n\t\tprint("{atributo.upper()}: ", dados_{tel}["{atributo}"])')
a.write('\n\t\tprint()')

#seleciona
a.write(f'\n\n\tdef seleciona_{tel}(self):\n\t\t{atributos[0]} = input("{atributos[0]} do {tel} que deseja selecionar: ")\n\t\treturn {atributos[0]}')

#mostra mensagem
a.write('\n\n\tdef mostra_mensagem(self, msg):\n\t\tprint(msg)')
