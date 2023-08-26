import random


def jogar():  # Função principal de execução

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()

    # Definição da quantidade de lacunas para cada letra na palavra secreta
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    qtd_ = len(palavra_secreta)
    print(letras_acertadas)

    # Definição da boleana para o laço
    enforcou = False
    acertou = False
    erros = 1

    while (not enforcou and not acertou):  # Enquanto não for enforcado faça:
        chute = chama_chute()

        # Se houver na palavra a letra do chute, vai executar o próximo comando
        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            errou_chute(erros)
            erros += 1  # Caso não acerte, somará um erro
        enforcou = erros == 8  # Ao atingir o limite de erro, será enforcado
        # Ao preencher todas as lacunas "_", ganha
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):  # Resultado caso acerto
        imprime_mensagem_vencedor()
    else:  # Resultado caso esso
        imprime_mensagem_perdedor(palavra_secreta)

    print("Fim do jogo")
# Funções


def errou_chute(erros):
    chances = 7 - erros
    if (chances != 0):
        print("Você errou! Mas ainda possui {} chances...".format(chances))
    else:
        print("Acabaram as chances :'(")
    desenha_forca(erros)


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:  # Para a letra acertada:
        if (chute == letra):
            # Subistituirá "_" pela letra acertada na posição do index
            letras_acertadas[index] = letra
        index += 1


def chama_chute():  # Coleta do chute
    chute = input("Chute uma letra: ")
    chute = chute.strip().upper()  # Tratamento de entrada
    return chute


def inicializa_letras_acertadas(palavra_secreta):
    # Criação das lacunas de acordo com a quantidade de palavras
    return ["_" for letra in palavra_secreta]


def imprime_mensagem_abertura():
    print("****************************************")
    print("***Bem-vindo ao jogo da Forca \(0.0)/***")
    print("****************************************")


def carrega_palavra_secreta():
    # Abre o arquivo de palavras somente para leitura "r"
    arquivo = open("palavras.txt", "r")
    palavras = []  # Cria uma lista

    for linha in arquivo:  # Lê o arquivo e zera com o close()
        linha = linha.strip()
        palavras.append(linha)  # Lê-se por linha

    arquivo.close()

    # Gera um número aleatório entre 0 e o tamanho da lista
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()  # Seleciona a palavra
    return palavra_secreta  # Retorna a palavra_secreta


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("     _______________         ")
    print("    /               \       ")
    print("   /                 \      ")
    print("/\/                   \/\   ")
    print("\ |   XXXX     XXXX   | /   ")
    print(" \|   XXXX     XXXX   |/     ")
    print("  |   XXX       XXX   |      ")
    print("  |                   |      ")
    print("  \__      XXX      __/     ")
    print("    |\     XXX     /|       ")
    print("    | |           | |        ")
    print("    | I I I I I I I |        ")
    print("    |  I I I I I I  |        ")
    print("    \_             _/       ")
    print("      \_         _/         ")
    print("        \_______/           ")


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("    *  ___________    * ")
    print("  *   '._==_==_=_.'  *  ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("  *   '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'     *  ")
    print("     *     ) (  *       ")
    print("         _.' '._        ")
    print(" *      '-------'    *  ")


def desenha_forca(erros):
    print("  _______     ")  # Fica como base para o primeiro erro
    print(" |/      |    ")

    if (erros == 1):
        print(" |     (0_0)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |     (0_0)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |     (0_0)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |     (0_0)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |     (0_0)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |     (0_0)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |     (X_X)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


# Permite acesso ao código sem estar em Jogos.py
if (__name__ == "__main__"):
    jogar()
