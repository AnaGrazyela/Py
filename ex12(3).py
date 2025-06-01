print("Calculadora")
print("1- soma")
print("2- subtração")
print("3- multiplicação")
print("4- divisão")

operacao = int(input("Escolha a operação: "))
n1 = float(input("Digite seu primeiro número: "))
n2 = float(input("Digite seu segundo número: "))

if operacao == 1:
    resultado = n1 + n2
    print(f"Resultado {resultado}")
elif operacao == 2:
    resultado = n1 - n2
    print(f"Resultado {resultado}")
elif operacao == 3:
    resultado = n1 * n2
    print(f"Resultado {resultado}")
elif operacao == 4:
    if n2 != 0:
        resultado = n1/n2
        print(f"Resultado {resultado}")
    else:
        print("Erro! A operação é divisivel por 0.")
else:
    print("Operação Invalida.")
