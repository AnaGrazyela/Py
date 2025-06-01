num = int(input("Digite um número de 1 à 12: "))
meses = [
    "janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
]

if 1 <= num <= 12:
    print(f" O mês é {meses[num - 1]}") # o "f" ele será para string IMPORTANTE!
else:
    print("Este número é inválido")