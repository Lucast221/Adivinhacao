import random

# Cria uma função jogar para ser chamada em Jogos.py


def jogar():

    print("****************************************")
    print("Bem-vindo ao jogo de adivinhação \(0.0)/")
    print("****************************************")
    # Gera o número secreto
    numero_secreto = random.randrange(0, 101)
    total_tentativas = 0
    pontos = 1000

    print("Temos três níveis")
    print("(1) Fácil  (2) Médio  (3) Difícil")
    # Lê o input e associa à um nível com uma quantidade de tentativas
    nivel = int(input("Qual o nível de dificulde? "))

    if (nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5
    # Cria um laço de repetição que vai executar de 1 até a quantidade de tentativas dos níveis + 1, para que seja incluida no range
    for rodada in range(1, total_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_tentativas))
        chute_str = input("Digite sua aposta entre 1 e 100: ")
        print("Você escolheu o número:", chute_str)
        chute = int(chute_str)
        # Limitação das entradas de 1 à 100
        if (chute < 1 or chute > 100):
            print("Não são aceitos valores menores que 1 nem maiores que 100!")
            continue  # Repete o código caso o número não estiver dentro da entrada permitida
        # Determinação dos valores
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print("Você acertou!!")

            break  # Ao acertar, para o jogo
        else:
            if maior:
                print("Você errou :( Seu número foi maior do que deveria.")
            elif menor:
                print("Você errou :( Seu número foi menor do que deveria.")
            # Calcula os pontos a cada rodada
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - (5 * pontos_perdidos)
    else:
        pontos = 0
        # Caso não acertar, transforma os pontos para zero e retorna para o usuário
        print("Sua pontuação foi de: {} Pontos!".format(pontos))

    print("O número secreto era", numero_secreto)
    print("Fim do jogo!")


# Permite acesso ao código sem estar em Jogos.py
if (__name__ == "__main__"):
    jogar()
