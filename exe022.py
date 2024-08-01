def media(notas):
    soma = 0
    if len(notas) == 0:
        return('Não é possivel dividir por zero')
    else:
        for i in range(len(notas)):
            soma += notas[i]
            media = soma / len(notas)
    return media
 
def maiorNum(notas):
    maior = 0
    if len(notas) == 0:
        return('lista vazia')
    for i in range(len(notas)):
        if notas[i] > maior:  
            maior = notas[i]
    return maior

def menorNum(notas):
    menor = 10
    if len(notas) == 0:
        return('lista vazia')
    for i in range(len(notas)):
        if notas[i] < menor:  
            menor = notas[i]
    return menor

notas = []
while True:
    nota = float(input('Digite sua nota: '))
    if nota >=0 and nota <= 10:
        notas.append(nota)
    else:
        print('A nota deve ser entre 0 e 10')
        
    saida = int(input(f'SELECEIONE UMA OPÇÃO \n[1]ADICIONAR MAIS UMA \n[2]SAIR \n'))
    
    if saida == 2:
        break

print(f"Media: {media(notas)}")
print(f"Maior Nota: {maiorNum(notas)}")
print(f"Menor Nota: {menorNum(notas)}")
print(f'Quantidade de notas {len(notas)}')
