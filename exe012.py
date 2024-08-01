numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite outro numero: '))

if numero1 == numero2:
    print('é igual')
elif numero1 > numero2:
    print(f'são diferente e o numero 1: {numero1} é maior')
else:
    print(f'são diferente e o numero 2: {numero2} é maior')       