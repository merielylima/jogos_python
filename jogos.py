import forca
import adivinhacao

print("************************************")
print("     BEM VINDO A ABA DE JOGOS")
print("************************************\n")

def jogos():
    jogo = 0
    while (jogo < 1 or jogo > 2):

        print("Escolha um jogo!\n\n[1] Forca\n[2] Adivinhação\n")
        jogo = int(input("Resposta: "))
        print("----------------------------")
        if (jogo == 1):
            print("Você escolheu o jogo da forca!\n")
            forca.jogo_forca()
            break
        elif (jogo == 2):
            print("Você escolheu o jogo da Adivinhação!\n")
            adivinhacao.jogo_adivinhacao()
            break
        else:
            print("Você escolheu um jogo inexistente, por favor tente novamente!")
            print("----------------------------")
            jogo = 0
            continue

inicia = True
while inicia == True:
    jogos()
    jogar = input("\n\nDeseja jogar novamente? [S/N]: ").upper()

    if jogar == "S":
        jogos()
    else:
        print("Você saiu dos jogos")
        inicia = False
