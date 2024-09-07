# Um motorista deseja calcular o consumo médio de combustível do seu carro. Crie um programa que receba a quantidade de quilômetros percorridos e a quantidade de litros de combustível consumidos, e calcule o consumo médio (km por litro).

quilo= float(input("Digite a quatidade de quilometros"))
combus= float(input("Digite a quatidade de combustivel"))
resultado = (quilo/100)*combus
print(f"O consumo medio e:{resultado}")