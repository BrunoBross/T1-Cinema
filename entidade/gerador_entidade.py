

classe = input('nome da classe: '  )# Livro
atributos = [atributo.strip() for atributo in input('digite os atributos: ').split(',')  ]# numero: int, biblioteca: Biblioteca
a = open(f'{classe.lower()}.py', 'w+')

# construtor
a.write(f'\n\nclass {classe}:\n')
a.write(f'\n\tdef __init__(self, {", ".join(atributos)}):')
for atributo in atributos:
    nome = atributo.split(':')[0]
    tipo = atributo.split(':')[1].strip()
    a.write(f'\n\n\t\tif isinstance({nome}, {tipo}):\n\t\t\tself.__{nome} = {nome}')

# setters e getters
for atributo in atributos:
    nome = atributo.split(':')[0]
    tipo = atributo.split(':')[1].strip()
    a.write \
        (f'\n\n\t@property\n\tdef {nome}(self):\n\t\treturn self.__{nome}\n\n\t@{nome}.setter\n\tdef {nome}(self, {atributo}):\n\t\t\nif isinstance({nome}, {tipo}):\n\t\t\tself.__{nome} = {nome}\n')
