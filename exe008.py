valor1 = float(input('Digite um numero: '))
valor2 = float(input('Digite outro numero: '))

if valor1 == valor2:
    print('é igual')
elif valor1 > valor2:
    print(f'Numero 1: {valor1} é Maior que o numero 2: {valor2}')
else:
    print(f'Numero 2: {valor2} é Maior que o numero 1: {valor1}')

