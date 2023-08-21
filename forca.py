def jogar():

    print("****************************************")
    print("***Bem-vindo ao jogo da Forca \(0.0)/***")
    print("****************************************")

    palavra_secreta = "banana".upper()  # Tratamento de entrada
    qtd_ = len(palavra_secreta)
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]
    # Definição da boleana para o laço
    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while (not enforcou and not acertou):  # Enquanto não for enforcado faça:
        chute = input("Chute uma letra: ")
        chute = chute.strip().upper()  # Tratamento de entrada

        # Se houver na palavra a letra do chute, vai executar o próximo comando
        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:  # Para a letra acertada:
                if (chute == letra):
                    # Subistituirá "_" pela letra acertada na posição do index
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1  # Caso não acerte, somará um erro

        enforcou = erros == qtd_  # Ao atingir o limite de erro, será enforcado
        # Ao preencher todas as lacunas "_", ganha
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
        chances = qtd_ - erros
        print("Você possui {} chances...".format(chances))

    if (acertou):  # Resultado
        print("Parabéns, você conseguiu!!")
    else:  # Resultado
        print("Você foi enforcado :´(")

    print("Fim do jogo")


# Permite acesso ao código sem estar em Jogos.py
if (__name__ == "__main__"):
    jogar()
