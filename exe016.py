qtd = 0
qtdMaior = 0
media = 0
while True:
    idade = int(input("Digit sua idade: \n"))
    saida = int(input("[1]Continuar \n[0]Sair \n"))
    qtd+=1
    media += idade

    if idade >= 21:
        qtdMaior+=1
    if saida != 1 and saida != 0:
        print('####Opção invalida Fim da execução!!!####')
        break
    if saida == 0:
        print('Fim!!!')
        break    

print(f'\n\nQuantidades de idades: {qtd}. \nMedia entre as idade: {media / qtd} \nQuantidade de pessoas com 21 anos ou mais: {qtdMaior}')