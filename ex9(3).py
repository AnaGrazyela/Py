time1 = input("Digite o primeiro time: ")
gols1 = int(input("Quantos gols o time fez: "))
time2 = input("Digite o segundo time: ")
gols2 = int(input("Quantos gols o time fez: "))


if gols1 < gols2:
    print(f"O time {time2} ganhou.")
elif gols2 < gols1:
    print(f"O time {time1} ganhou.")
else:
    print("Empate")