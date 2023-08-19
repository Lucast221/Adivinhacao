# Chama os arquivos dos jogos
import adivinhacao
import forca


def escolhe_jogo():
    print("****************************************")
    print("*********Escolha o jogo \(0.0)/*********")
    print("****************************************")

    jogo = int(input("(1) Adivinhação  (2) Forca: "))
    # Lê o input, associa ao jogo e executa a função jogar
    if (jogo == 1):
        print("Jogando o jogo de Adivinhacao")
        adivinhacao.jogar()
    elif (jogo == 2):
        print("Jogando o jogo da Forca")
        forca.jogar()


# Permite acesso ao código sem estar em Jogos.py
if (__name__ == "__main__"):
    escolhe_jogo()
