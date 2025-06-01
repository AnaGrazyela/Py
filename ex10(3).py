nota1 = float(input("Digite sua nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))
nota4 = float(input("Digite sua quarta nota:  "))
media = (nota1+nota2+nota3+nota4)/4

print(f"Média {media:.2f}")
if media >= 7:
    print("Aprovado!")
else:
    print("Reprovado!")