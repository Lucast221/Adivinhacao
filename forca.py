def jogar():

    print("****************************************")
    print("***Bem-vindo ao jogo da Forca \(0.0)/***")
    print("****************************************")

    palavra_secreta = "banana"
    # Definição da boleana para o laço
    enforcou = False
    acertou = False

    while (not enforcou and not acertou):
        # Tratamento da entrada para ser recebida em minúsculas e sem espaços
        chute = input("Chute uma letra: ")
        chute = chute.strip()
        chute = chute.lower()

        index = 1
        # Laço com tratamento de entrada
        for letra in palavra_secreta:
            if (chute.lower() == letra.lower()):
                print("Encontrei a letra {} na posição {}".format(letra, index))
            index = index + 1
        print("Jogando...")

    print("Fim do jogo")


# Permite acesso ao código sem estar em Jogos.py
if (__name__ == "__main__"):
    jogar()
