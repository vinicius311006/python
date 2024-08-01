jose = 0
maria = 0
marcia = 0
branco = 0
votantes = int(input('Digite quantos vão votar: \n'))

for i in range(votantes):
    voto = int(input(f'[11]jose \n[22]Maria \n[33]Marcia \n'))
    if voto == 11:
        jose+=1
    elif voto == 22:
         maria+=1
    elif voto == 33:
         marcia+=1
    else:
        branco+=1
        print('Votou Branco')

print(f'jose {jose} votos \n maria {maria} votos \n marcia {marcia} votos')
if jose > maria and jose > marcia:
   print(f'Jose ganhou com {jose} votos')
elif maria > jose and maria > marcia:
   print(f'Maria ganhou com {maria} votos')
elif marcia > jose and marcia > maria:
   print(f'marcia ganhou com {marcia} votos')
else:
    print('EMPATE!!!')   
print(f'votos em brancos foi {branco}')   