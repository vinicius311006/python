# Vinicius Nascimento
def adicionar():
    nome = input('Digite o nome do Novo Produto: ')
    preco = float(input('Informe o Preço do Novo Produto: '))
    qtd = int(input('Informe a Quantidade de estoque do Novo Produto: '))

    for produto in estoque:
        if produto['nome'] == nome:
            produto['preco'] = preco
            produto['qtd'] += qtd
            print(f'Produto {nome} já existente. Atualizado quantidade e preço.')
            return
    
    produto = {
        'nome': nome,
        'preco': preco,
        'qtd': qtd
    }
    estoque.append(produto)
    print(f'Produto {nome} adicionado ao estoque com sucesso.')


def vender():
    if len(estoque) == 0:
        return print('lista vazia')
    
    nomeProduto = input('Informe o nome do produto para selecionar: ')
    venderQdt = int(input('Informe a quantidade de venda: '))

    for i in range(len(estoque)):
        if nomeProduto == estoque[i]['nome']:
            if estoque[i]['qtd'] < venderQdt:
                print(f'Esse Produto tem apenas {estoque[i]["qtd"]} unidades em estoque.')
                return
            else:
                estoque[i]['qtd'] -= venderQdt 
                print(f'Você vendeu {venderQdt} unidades do produto {estoque[i]["nome"]}.')
                return
    print('Produto inválido')
                

def total():
    if len(estoque) == 0:
        return print('lista vazia')
    
    for i in range(len(estoque)):
        total = estoque[i]['preco'] * estoque[i]['qtd']    
        print(f'Produto {estoque[i]['nome']} tem um Toltal de: {total} Reais')

def relatorio():
    if len(estoque) == 0:
        return print('lista vazia')
    
    for i in range(len(estoque)):
        print(f'{estoque[i]}')

estoque = []
while True:
    print('\n \n1 - Adicionar')
    print('2 - Vender')
    print('3 - Total')
    print('4 - Listar produtos')
    print('5 - Sair')
    op = int(input('Escolha uma opção: '))
    if op == 1:
        adicionar()
    elif op == 2:
        vender()
    elif op == 3:
        total()
    elif op == 4:
        relatorio()
    elif op == 5:
        print('Saindo...')
        break         
    else:
        print('opção inválida')
