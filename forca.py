import random

def jogo_forca():
    apresentacao() # mostra mensagem antes de inicio
    palavra_secreta = carrega_palavra()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = len(letras_acertadas)

    while(not enforcou and not acertou):

        chute = entrar_chute()

        if chute in palavra_secreta:
            chute_certo(chute, letras_acertadas, palavra_secreta)
        else:
            erros = erros - 1
            print("Ops, você errou! Faltam apenas {} tentativas.".format(erros))
            desenha_forca(erros)

        enforcou = erros == 0
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)
    if (acertou):
        vencedor()
    elif(enforcou):
        perdedor(palavra_secreta)
    print("Fim do jogo...")

def apresentacao():
    print("************************************")
    print("     BEM VINDO AO JOGO DA FORCA")
    print("************************************\n")
def carrega_palavra():

    arquivo = open("palavras.txt", "r")  # Lê o arquivo
    palavras = []  # cria uma lista vazia
    for linha in arquivo:  # para cada palavra(linha) do arquivo, faça:
        linha = linha.strip()  # limpar o \n
        palavras.append(linha)  # armazenha as palavras(linha) na lista palavras
    arquivo.close()  # fecha o arquivo
    # print(palavras)  # imprime as palavras contidas no arquivo

    numero = random.randrange(0, len(palavras))  # sorteia uma das palavras(linhas) do arquivo
    palavra_secreta = palavras[numero].upper()  # palavra escolhida

    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    print("----------------------------------\n")
    return ["_" for letra in palavra] # adiciona a linha para cada letra da palavra secreta

def entrar_chute():
    chute = input("\nQual a letra? ")
    chute = chute.strip().upper()  # ignorar os espaços
    return chute

def chute_certo(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            print("Muito bem, você encontrou a letra {} na posição {}".format(letra, index + 1))
            letras_acertadas[index] = letra
        index = index + 1

def vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (     ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      ( )   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")
    if (erros == 8):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")
    if (erros == 8):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")
    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "main"):
    jogo_forca()
