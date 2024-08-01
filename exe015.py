contador = 0
maior = 0
menor = 0
soma = 0
while True:
    numero = int(input('Digite um numero'))
    if numero >= 0:
        soma+=numero
        contador+=1
        if numero > maior:
            maior = numero
        if menor == 0 or numero<menor:
            menor = numero    
    else:
        break    
print(f'Numero: {soma}')
print(f'Maior: {maior}')
print(f'Menor: {menor}')
print(f'Media: {soma / contador}')

