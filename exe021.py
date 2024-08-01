def soma(a,b,c):
    resultado = a + b
    return c(resultado)

def subtracao(a,b,c):
    resultado = a - b
    return c(resultado)

def multiplicacao(a,b,c):
    resultado = a * b 
    return c(resultado)
    
def divisao(a,b,c):
    if b == 0:
        print('Não é Tem como dividir por ZERO')
    else:    
        resultado = a / b
    return c(resultado)

def resultado(a):
    print(f'o resultado é: {a}')

menu = int(input(f'SELECIONE A OPÇÃO \n[1]SOMA \n[2]SUBTRAÇÃO \n[3]MULTIPLICAÇÃO \n[4]DIVISÃO \n'))
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
if menu == 1:
    soma(valor1,valor2,resultado)
elif menu == 2:
    subtracao(valor1,valor2,resultado)
elif menu == 3:
    multiplicacao(valor1,valor2,resultado)
elif menu == 4:
    divisao(valor1,valor2,resultado)
