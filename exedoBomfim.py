import os
os.system('cls')
titulo=str(input('digite o titulo de um livro:  '))
autor=str(input('digiteo  nome do autor: '))
anodepublicação=int(input('digite o ano de publicação deste livro: '))
genero=str(input('digite o genero deste livro:  '))
paginas=int(input('digite a quantidade de paginas deste livro:  '))
 
 
 
Livro={
    'titulo':titulo,
    'autor': autor,
    'piblicação': anodepublicação,
    'genero': genero,
    'paginas': paginas
}
os.system('cls')
for chave,valor in Livro.items():
     print(f'{chave}={valor}')
 
pres=input('Press to continue...')
 
troca=str(input(f'deseja alterar algo no banco de dados do livro {titulo} S/N: '))
 
if troca=='s' or troca=='S' or troca=='sim':
     escolha=int(input('selecione a opção que deseja alterar:\n[1]titulo\n[2]autor\n[3]ano de Publicação\n[4]genero\n[5]paginas\n'))
elif troca=='n' or troca=='N':
     print('MEUS PARABENS SEU LIVRO FOI BUBLICADO')
else:
     print('opção invalida')
 
if escolha==1:
     novoTitulo=str(input('digite o novo titulo para este exemplar: '))
     Livro.update({'titulo':novoTitulo})
elif escolha==2:
     novoAutor=str(input('digite o novo autor para este exemplar: '))
     Livro.update({'autor':novoAutor})
elif escolha==3:
     novaPubli=str(input('digite o ano de publicação deste exemplar: '))
     Livro.update({'piblicação':novaPubli})
elif escolha==4:
     novoGenero=str(input('digite o novo genero para este exemplar: '))
     Livro.update({'genero':novoGenero})
elif escolha==5:
     novaPaginas=str(input('digite a quantidade de paginas deste exemplar: '))
     Livro.update({'paginas':novaPaginas})
else:
     print('OPÇÃO INVALIDA')
os.system('cls')
print('LIVRO ATUALIZADO')
for chave,valor in Livro.items():
     print(f'{chave}={valor}')