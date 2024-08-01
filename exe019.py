while True:
    titulo = input('Digite o titulo do livro: ')
    autor = input('Digite o autor do livro: ')
    anoPublicado = int(input('Digite o ano de Publicação do livro: '))
    genero = input('Digite o genero do livro: ')
    paginas = int(input('Digite a quantidade de paginas do livro: '))

    livro = {
        'titulo': titulo,
        'autor': autor,
        'anoPublicado': anoPublicado,
        'genero': genero,
        'paginas': paginas
    }

    for chave, valor in livro.items():
        print(f'{chave} = {valor}')

    editar = input('Editar livro s/n: ')
    
    if editar == 's' or editar == 'S':
        atualizarLivro = input('Qual campo dejesa alterar: ')
        res = input('Informe o Campo Atualizado: ')
        livro.update({f'{atualizarLivro}':f'{res}'})

        for chave, valor in livro.items():
            print(f'{chave} = {valor}')
    
    saida = input('Dejesa adicionar Livro s/n: ')
    if saida == 'n' or saida == 'N':
        break
    