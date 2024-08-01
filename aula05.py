# x = [] #lista
# y = () #tupla
# z = {} #dicionario

pessoa = {
    'nome':'vinicius',
    'idade': 17,
    'aluno': True
}
print(pessoa['nome'])
print(f'O(a) {pessoa["nome"]} tem {pessoa["idade"]} anos')


time = []
for i in range(4):
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    altura = float(input('Digite sua altura: '))
    atleta = {
        'nome': nome,
        'idade': idade,
        'altura': altura
    }
    time.append(atleta)
print(time[1]['nome'])    

for atleta in time:
    print(f'{atleta['nome']} tem {atleta['idade']} anos e mede {atleta['altura']} cm')