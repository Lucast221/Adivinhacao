import random

print("****************************************")
print("Bem-vindo ao jogo de adivinhação \(0.0)/")
print("****************************************")

numero_secreto = random.randrange(0,101)
total_tentativas = 0
pontos = 1000

print("Temos três níveis")
print("(1) Fácil  (2) Médio  (3) Difícil")

nivel = int(input("Qual o nível de dificulde? "))

if(nivel == 1):
    total_tentativas = 20
elif(nivel == 2):
        total_tentativas = 10
else:
    total_tentativas = 5
    

for rodada in range(1,total_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_tentativas))
    chute_str = input("Digite sua aposta entre 1 e 100: ")
    print("Você escolheu o número:",chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Não são aceitos valores menores que 1 nem maiores que 100!")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print("Você acertou!!")
       
        break
    else:
        if maior:
            print("Você errou :( Seu número foi maior do que deveria.")
        elif menor:
            print("Você errou :( Seu número foi menor do que deveria.")

        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - (5 * pontos_perdidos)
else:
    pontos = 0
    print("Sua pontuação foi de: {} Pontos!".format(pontos))

print("O número secreto era",numero_secreto)
print("Fim do jogo!")