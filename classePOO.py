class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def mudar_nome(self):
        self.nome = input('Qual seu nome:')
        print(f'{self.nome}, Seja bem Vindo! ')

    def mudar_idade(self):
        self.idade = int(input('Qual sua idade: '))

    def mudar_cpf(self):
        self.cpf = int(input('Qual o seu CPF: '))    

class Aluno(Pessoa):
    def __init__(self, nome, idade, cpf, matricula):

        super().__init__(nome, idade, cpf)
        self.matricula = matricula

    def exibir_informacacoes(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')   
        print(f'CPF: {self.cpf}')
        print(f'Matricula: {self.matricula}')

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cpf, cargo):
        super().__init__(nome, idade, cpf)
        self.cargo = cargo
        self.salario = 1530.00

    def mudar_salario(self):
        self.salario = float(input('Qual o novo salario: '))          

    def exibir_informacacoes(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'CPF: {self.cpf}')
        print(f'Cargo: {self.cargo}')
        print(f'Salario: {self.salario}')

nomePessoa = input('Qual o seu nome: ')
idadePessoa = int(input('Qual a sua idade: '))
cpfPessoa = int(input('Qual o seu CPF: '))     

# adicionando objeto
eu = Pessoa(nomePessoa, idadePessoa, cpfPessoa)

voce = Pessoa(input('Qual o seu Nome: '), int(input('Qual sua idade: ')), int(input('Qual o seu CPF: ')) )

nos = Pessoa('sandro', 18, 123456789)


# Imprimindo os objetos
print(f'o Nome é: {eu.nome}')
print(f'a Idade é: {eu.idade}')
print(f'o CPF é: {eu.cpf}')

print(f'o Nome é: {voce.nome}')
print(f'o Nome é: {nos.nome}')


#Chamndo od Metodos
eu.mudar_nome()
print(f'o nome alterado é {eu.nome}')

eu.mudar_idade()
print(f'a idade alterada é {eu.idade}')

eu.mudar_cpf()
print(f'o CPF alterado é {eu.cpf}')

#classe aluno
aluno1 = Aluno('Ana', 20, 123456789, 2022001)

aluno1.exibir_informacacoes()
aluno1.mudar_idade

#classe funcionario
funcionario1 = Funcionario('José', 30, 987654321, 'Analista')

funcionario1.mudar_nome()
funcionario1.mudar_salario()
funcionario1.exibir_informacacoes()
