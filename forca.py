
import random



def jogar():

    imprime_mensagem_abertura()
    palavra_secreta =carrega_palavra_secreta()
    letras_certas = inicializa_palavra_secreta(palavra_secreta)
    print(letras_certas)

    enforcou = False
    acertou = False
    erros = 0


    #ENQUANTO N ACERTOU NEM ENFORCOU
    while(not enforcou and not acertou):

        chute = pede_chute()
         
        if(chute in palavra_secreta):
            marca_letra_certa(chute, letras_certas,palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 8
        acertou = "_" not in letras_certas
        print(letras_certas)
        print ("erros {}/8".format(erros) )

    if (acertou):
            imprime_mensagem_vitoria()
        
    else:
            imprime_mensagem_derrota(palavra_secreta)



def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def imprime_mensagem_vitoria():

        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("     .-\:        /-.    ")
        print("     |(|:.     ; |) |    ")
        print("     '-|:.    ;  |-'     ")
        print("        \::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")


def imprime_mensagem_derrota(palavra_secreta):

        print("VOCÊ MORREU!")
        print("A palavra era {}".format(palavra_secreta))
        print("███████████████████████████")
        print("███████▀▀▀░░░░░░░▀▀▀███████")
        print("████▀░░░░░░░░░░░░░░░░░▀████")
        print("███│░░░░░░░░░░░░░░░░░░░│███")
        print("██▌│░░░░░░░░░░░░░░░░░░░│▐██")
        print("██░└┐░░░░░░░░░░░░░░░░░┌┘░██")
        print("██░░└┐░░░░░░░░░░░░░░░┌┘░░██")
        print("██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██")
        print("██▌░│██████▌░░░▐██████│░▐██")
        print("███░│▐███▀▀░░▄░░▀▀███▌│░███")
        print("██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██")
        print("██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██")
        print("████▄─┘██▌░░░░░░░▐██└─▄████")
        print("█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████")
        print("████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████")
        print("█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████")
        print("███████▄░░░░░░░░░░░▄███████")
        print("██████████▄▄▄▄▄▄▄██████████")
        print("███████████████████████████")


def marca_letra_certa(chute, letras_certas,palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute.upper() == letra.upper()):
            letras_certas[index] = letra
        index += 1

def inicializa_palavra_secreta(palavra):
    lista =  ["_" for letra in palavra]
    return lista


def pede_chute():
    chute = input("Qual letra?")
    chute = chute.strip().upper()
    return chute

def imprime_mensagem_abertura():
    print("********************************")
    print("***bem vindo ao jogo de forca***")
    print("********************************")

def carrega_palavra_secreta():
    arquivo = open("dados/palavra.txt", "r")
    palavra = []

    for linha in arquivo:
        linha = linha.strip()
        palavra.append(linha)

    arquivo.close()

    numero = random.randrange(0,len(palavra))
    palavra_secreta = palavra[numero].upper()
    return palavra_secreta






if(__name__ == "__main__"):
    jogar()






