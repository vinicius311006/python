import random
tentativa = 0
numero = random.randint(0,100)
while True:
    tentativa+=1
    palpite = int(input('Digite seu palpite: '))

    if numero == palpite:
        print(f'Parabens você Acertou o numero {numero} aleatorio com {tentativa} tentativas')
        saida = (input(f'Dejesa jogar novamente\n [S]Continuar\n [N]Sair\n'))
        if saida == 'n' or saida == 'N':
            break 
        else:
            numero = random.randint(0,100)
            tentativa = 0
    elif numero < palpite:
        print('O Numero é Menor')
    else :
        print('O Numero é Maior')