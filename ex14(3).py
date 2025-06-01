idade = int(input("Digite a sua idade: "))

if 0 <= idade <= 2:
    print("Você é um recém nascido")
elif 3 <= idade <= 11:
    print("Você é uma criança")
elif 12 <= idade <= 19:
    print("Você é um Adolescente")
elif 20 <= idade <= 55:
    print("Você é um adulto")
else:
    print("Você é um idoso(a)")