print("Conversão de Temperatura")
print("1 - Celsius para fahrenheit")
print("2 - fahrenheit para Celsius")
opcao = int(input("Escolha a opção (1 ou 2): "))

temp = float(input("Digite a temperatura: "))

if opcao == 1:
    fahrenheit = (9 * temp + 160) / 5
    print(f"{temp:.2f}° = {fahrenheit:.2f}°F")
elif opcao == 2:
    celsius = (temp - 32) * (5/9)
    print(f"{temp:.2f}°F = {celsius:.2f}°C")
else:
    print("Opção Inválida!")