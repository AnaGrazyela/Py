conta = float(input("Digite o número da sua conta: "))
saldo = float(input("Digite o seu saldo: "))
operacao = int(input("Digite o tipo de operação (1- Depósito, 2- Retirada): "))
valor = float(input("Digite o valor da operação: "))

if operacao == 1:
    saldo += valor 
elif operacao == 2:
    saldo -= valor 
else:
    print("Operação Inválida.")

print(f"Novo saldo da conta {conta}: R$ {saldo:.2f}")

