nomes = []
for i in range(8):
     nomes.append(input('digite um Nome: '))

buscador = input('Buscador de pessoa: ')
if buscador in nomes:
    print(f'Pessoa encontarda na posição: {nomes.index(buscador)}')
else:
    print('Pessoa não encontrada')
          