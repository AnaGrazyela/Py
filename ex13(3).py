salario = float(input("Digite seu sálario atual: R$ "))

if salario <= 1200:
    novo_salario = salario * 1.5
else:
    novo_salario = salario * 1.3

print (f"Salário reajustado {novo_salario:.2f}")