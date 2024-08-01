# #função
# def mensagem():
#     print('ola mundo')
#     print('vinicius')

# mensagem()    

# def hello(meu_nome):
#     print(f'Ola {meu_nome}, seja bem vindo!')

# hello('vinicius')    

# def soma(a,b):
#     resultado = a + b
#     return resultado
# valor1 = int(input('Digite o primeiro valor: '))
# valor2 = int(input('Digite o segundo valor: '))
# print(f'A soma dos valore é: {soma(valor1,valor2)}')

vinicius = lambda a,b: a + b
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
print(f'A soma dos valore é: {vinicius(valor1,valor2)}')
