nome = input('Digite seu Nome: ')
salarioFixo = float(input('Digite seu salario Fixo'))
totalVendas = float(input('Digite o valor de vendas do mês'))


comisao = totalVendas * 15 / 100
salarioFinal = salarioFixo + comisao

print(f'{nome} seu salario fixo é: {salarioFixo} você fez {totalVendas} de vendas no mês \nseu salario final é {salarioFinal}')   