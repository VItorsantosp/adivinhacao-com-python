import random


print("-----------------------------")
print("Bem vindo ao jogo adivinhação")
print("-----------------------------")

numero_secreto = random.randrange(1, 101)
total_de_tentativas = 3
rodada = 1
pontos = 1000

print("qual nivel de dificuldade? ")
print("(1) facil (2) medio (3) dificil")

nivel = int(input("define o nivel: "))

print(numero_secreto)


if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

for rodada in range (1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite o seu número: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou! e fez {} pontos".format(pontos))
        break
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    rodada = rodada + 1

print("Fim do jogo")