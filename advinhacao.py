import random

def jogar_advinhacao():
    print_inicio()

    numero_secreto = int(random.random() * 100)
    total_tentativas = 0
    pontos = 1000

    print("\033[32m     DIGITE: \033[0m[\033[31m1\033[0m]\033[32m fácil \033[0m")
    print("\033[32m             \033[0m[\033[31m2\033[0m]\033[32m normal \033[0m")
    print("\033[32m             \033[0m[\033[31m3\033[0m]\033[32m dificil \033[0m")

    nivel = int(input("\033[31m    DIGITE O NIVEL:   \033[0m"))

    if(nivel == 1):
        total_tentativas = 10
    elif(nivel == 2):
        total_tentativas = 5
    elif(nivel == 3):
        total_tentativas = 3

    while (total_tentativas > 0):

        print(f"\033[42m \033[30m      TENTATIVA NÚMERO: {total_tentativas}     \033[0m \033[0m")
        chute = int(input("Digite um número entre [ 1 - 100 ]: "))
        print(f"você digitou o número: {chute}")

        if(chute <= 0 or chute >= 101):
            print("Você não digitou número entre [ 1 - 100 ], tente novamente! ")
            continue

        acertou = chute == numero_secreto
        menor = chute > numero_secreto
        maior = chute < numero_secreto

        if (acertou):
            print("Você Acertou!")
            break
        elif(maior):
            print("Você chutou um número menor!")
            pontos_perdidos = abs(abs(numero_secreto - chute) - 20)
            pontos = pontos - pontos_perdidos
        elif(menor):
            print("Você chutou um número maior!")
            pontos_perdidos = abs(abs(chute - numero_secreto) - 20)
            pontos = pontos - pontos_perdidos

        total_tentativas = total_tentativas - 1

    print_final(numero_secreto, pontos)
    
    for rodada in range(1, 10, 2):
        print(rodada)
    valor = 34.34888
    print(f"R$ {valor:08.2f}")

def print_inicio():
    print("\033[31m*\033[0m" * 31)
    print("\033[32m BEM VINDO JOGO DE ADVINHAÇÃO \033[0m")
    print("\033[31m*\033[0m" * 31)

def print_final(numero_secreto, pontos):
    print("\033[31m*\033[0m" * 31)
    print("\033[32m          FIM DO JOGO!           \033[0m")
    print(f"\033[32m    O NÚMERO SECRETO ERA: {numero_secreto}       \033[0m")
    print(f"\033[32m       PONTOS: {pontos}       \033[0m")
    print("\033[31m*\033[0m" * 31)

if(__name__ == "__main__"):
    jogar_advinhacao()