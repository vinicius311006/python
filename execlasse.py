class Veiculo:
    def __init__(self,marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0

    def mostrar_informacoes(self):
        print(f'A marca: {self.marca}')
        print(f'O modelo: {self.modelo}')
        print(f'O ano: {self.ano}')
        print(f'Velocidade {self.velocidade}')


    def aumentar_velocidade(self):
        if self.velocidade <= 150:
            self.velocidade += 10
        else:
            print('Passou do limite de 150 Km/h')


    def diminuir_velocidade(self):
        if self.velocidade > 0:
            self.velocidade -= 15
        else:
           print('A velocidade ja esta em Zero')
           if self.velocidade < 0:
                self.velocidade = 0



marca = input("Informe a Marca do veiculo: ")
modelo = input("Informe o Modelo do veiculo: ")
ano = int(input("Informe o Ano do veiculo: "))

veiculo1 = Veiculo(marca, modelo, ano)
veiculo2 = Veiculo("Lamborghini", "Urus", 2019)
veiculo3 = Veiculo("Ferrari", "F19", 2017)

#Aumentar velocidade
# veiculo1.aumentar_velocidade()
# veiculo1.aumentar_velocidade()
# veiculo1.aumentar_velocidade()

veiculo2.aumentar_velocidade()
# veiculo2.aumentar_velocidade()
# veiculo2.aumentar_velocidade()
# veiculo2.aumentar_velocidade()
# veiculo2.aumentar_velocidade()
# veiculo2.aumentar_velocidade()
# veiculo2.aumentar_velocidade()

#Diminuir velocidade
veiculo2.diminuir_velocidade()
# veiculo3.diminuir_velocidade()

#Mostra informação
veiculo1.mostrar_informacoes()
veiculo2.mostrar_informacoes()
veiculo3.mostrar_informacoes()