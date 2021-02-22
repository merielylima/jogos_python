import random
def jogo_adivinhacao():
    print("*************************************")
    print("  BEM VINDO AO JOGO DA ADIVINHAÇÃO")
    print("*************************************\n")

    numero_secreto = round(random.randrange(1,101))
    pontos = 1000
    total_tentativas = 0
    while (total_tentativas < 1 or total_tentativas > 3):
        total_tentativas = input("Qual o nivel de dificuldade você deseja?\n - [1] Fácil\n - [2] Médio\n - [3] Difícil\n Resposta: ")
        nivel = int(total_tentativas)
        print("----------------------------")
        if(nivel == 1):
            total_tentativas = 20
            break
        elif (nivel == 2):
            total_tentativas = 10
            break
        elif (nivel == 3):
            total_tentativas = 5
            break
        else:
            print("Você escolheu um nivel inexistente, por favor tente novamente!")
            print("----------------------------")
            total_tentativas = 0
            continue
    print("Você escolheu o nível", nivel)
    print("-------------------------------")
    # for in range(start, stop, [step])


    for rodada in range(1, total_tentativas+1):

        print("Tentativa ",rodada," de ", total_tentativas)
        print("-------------------------------")
        chute_str = input("Digite um número entre 1 e 100: ")
        chute = int(chute_str)

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("         Parabéns! Você acertou!\n         Pontuação final: ", pontos)
            break
        else:
            if(maior):
                print("Você errou! O número {} é maior do que o númerio secreto. ".format(chute))
            elif(menor):
                print("Você errou! O número {} é menor do que o númerio secreto. ".format(chute))
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
        print("-------------------------------")
    print("Fim do jogo!!!")

if(__name__ == "__main__"):
    jogo_adivinhacao()