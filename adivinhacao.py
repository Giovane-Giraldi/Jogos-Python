import random

def jogar():

    print("********************************")
    print("bem vindo ao jogo de adivinhação")
    print("********************************")

    numero_secreto = random.randrange(1,101)
    tentativas = 0
    pontos = 1000

    print("qual nível de dificuldade" )
    print("(1)Fácil (2)Médio (3)Difícil (4)impossível")
    nivel = int(input("defina o nível:"))

    if(nivel == 1):
        tentativas = 20
    elif(nivel == 2):
        tentativas = 15
    elif(nivel == 3):
        tentativas = 10
    elif(nivel == 4):
        tentativas = 5
    else:
        jogar()
    for rodada in range(1,tentativas + 1):
        print("tentativa {} de {}".format(rodada,tentativas))
        chute = input("Digite um número entre 1 e 100:")
        print("voce digitou", chute )
        chute = int(chute)

        if (chute < 1 or chute > 100):
             print("você deve digitar um número entre 1 e 100")
             continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
           print("voce acertou, você fez {} pontos".format(pontos))
           break
        else:

            if(maior):
                print("voce errou!o seu chute foi maior do que o número secreto")

            elif(menor):
                print("voce errou!o seu chute foi menor do que o número secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos




    print("fim de jogo")

if(__name__ =="__main__"):
    jogar()
