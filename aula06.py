aluno = {
    'nome':'vinicius',
    'idade': 17,
    'serie': 3,
    'ativo': True
}

# print(aluno)
# print(aluno['nome'])
# print(f'{aluno['nome']} tem {aluno['idade']} anos')
# print(aluno.keys())
# print(aluno.values())
# print(aluno.items())

for chave in aluno:
    print(chave)

for chave, valor in aluno.items():
    print(f'{chave} = {valor}')


del aluno['idade']
print(aluno)

aluno.update({'responstavel': 'vinicius'})


maisAluno = {
    'endereço': 'rua 1',
    'telefone': 1699999000,
    'cep': 1480000
}

aluno.update(maisAluno)
print(aluno)