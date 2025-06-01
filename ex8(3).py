negativo = 0 

for i in range(5):
    num = float(input(f"Digite o {i+1}° numero: "))
    if num < 0:
        negativo += 1

print (f"Quantidades de negativos é {negativo}")

