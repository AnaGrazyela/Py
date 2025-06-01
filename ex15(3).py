produto = input("Digite o nome do produto: ")
compra = float(input("Digite o valor de compra: R$ "))

if compra < 10:
    lucro = 0.7
elif compra <= 30:
    lucro = 0.5
elif compra <= 50:
    lucro = 0.4
else:
    lucro = 0.3

venda = compra * (1 + lucro)

print(f"Produto: {produto}")
print(f"Valor de venda: R$ {venda:.2f}")
