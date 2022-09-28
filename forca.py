import random

def jogar_forca():

    print_inicio()
    palavra_secreta = gerar_palavra_secreta()
    forca = ["|_|" for letra in palavra_secreta]
    enforcou = False
    venceu = False
    error = 0
    total_tentativas = definir_nivel()
    
    
    while(not enforcou and not venceu):

        chute = input("Qual a letra?: ").lower().strip()
        posicao = 0
        print(f"\033[32mTENTATIVA: {total_tentativas}\033[0m")
        if chute not in palavra_secreta:
            error = error + 1
            gerar_forca(error)
            total_tentativas = total_tentativas - 1
            
        else:
            for letra in palavra_secreta:

                if chute == letra:
                    print("você acertou")
                    print(f"encontrado {chute} na posicao {posicao}")
                    forca[posicao] = f"|{chute}|"
                posicao = posicao + 1

        if "|_|" not in forca:
            venceu = True
        if total_tentativas == 0:
            enforcou = True

        print(forca)

        if venceu:
            print_venceu()
        elif enforcou:
            print_perdeu(palavra_secreta)

    print_final(palavra_secreta)

#FUNÇÕES PARA O PROGRAMA DO JOGO DA FORCA
def print_inicio():
    print("\033[31m*\033[0m" * 31)
    print("\033[32m BEM VINDO JOGO DE FORCA! \033[0m")
    print("\033[31m*\033[0m" * 31)

def print_final(palavra_secreta):
    print("\033[31m*\033[0m" * 31)
    print("\033[32m          FIM DO JOGO!           \033[0m")
    print(f"\033[32m    O NÚMERO SECRETO ERA: {palavra_secreta}       \033[0m")
    print("\033[31m*\033[0m" * 31)

def gerar_palavra_secreta():
    
    arquivo = open("palavras.txt", "w")
    arquivo.write("banana\n")
    arquivo.write("laranja\n")
    arquivo.write("mechirica\n")
    arquivo.write("acerola\n")
    arquivo.write("melancia\n")
    arquivo.write("morango\n")
    arquivo.write("jabuticaba\n")
    arquivo.write("ameixa\n")
    arquivo.close()

    lista_palavra_secreta = []
    arquivo_lido = open("palavras.txt", "r")

    for linha in arquivo_lido:
        lista_palavra_secreta.append(linha.strip())

    arquivo_lido.close()

    palavra_secreta = lista_palavra_secreta[random.randrange(0, len(lista_palavra_secreta))]
    return palavra_secreta

def print_venceu():
    print("\033[33m CONGRATULATIONS YOU WIN \033[0m")
    print("\033[33m                         \033[0m")
    print("\033[33m       ___________       \033[0m")
    print("\033[33m      '._==_==_=_.'      \033[0m")
    print("\033[33m      .-\\:      /-.     \033[0m")
    print("\033[33m     | (|:.     |) |     \033[0m")
    print("\033[33m      '-|:.     |-'      \033[0m")
    print("\033[33m        \\::.    /       \033[0m")
    print("\033[33m         '::. .'         \033[0m")
    print("\033[33m           ) (           \033[0m")
    print("\033[33m         _.' '._         \033[0m")
    print("\033[33m        '-------'        \033[0m")

def print_perdeu(palavra_secreta):
    print(f"\033[31m   {palavra_secreta}        \033[0m")
    print("\033[31m     OH MY GODS YOU BE HANGED   \033[0m")
    print("\033[31m                                \033[0m")
    print("\033[31m    _______________             \033[0m")
    print("\033[31m   /               \\           \033[0m")
    print("\033[31m  /                 \\          \033[0m")
    print("\033[31m//                   \\/\\      \033[0m")
    print("\033[31m\\|   XXXX     XXXX   | /       \033[0m")
    print("\033[31m |   XXXX     XXXX   |/         \033[0m")
    print("\033[31m |   XXX       XXX   |          \033[0m")
    print("\033[31m |                   |          \033[0m")
    print("\033[31m \\__      XXX      __/         \033[0m")
    print("\033[31m   |\\     XXX     /|           \033[0m")
    print("\033[31m   | |           | |            \033[0m")
    print("\033[31m   | I I I I I I I |            \033[0m")
    print("\033[31m   |  I I I I I I  |            \033[0m")
    print("\033[31m   \\_             _/           \033[0m")
    print("\033[31m     \\_         _/             \033[0m")
    print("\033[31m       \\_______/               \033[0m")

def gerar_forca(error):
    print(f"\033[35mYOU HAVE {error}\033[0m")
    print("\033[35m  _______            \033[0m")
    print("\033[35m |/      |          \033[0m")

    if error == 1:
        print("\033[35m |                  \033[0m")
        print("\033[35m |                  \033[0m")
        print("\033[35m |                  \033[0m")
        print("\033[35m |                  \033[0m")

    elif error == 2:
        print("\033[35m |      (_)         \033[0m")
        print("\033[35m |                  \033[0m")
        print("\033[35m |                  \033[0m")
        print("\033[35m |                  \033[0m")

    elif error == 3:
        print("\033[35m |      (_)          \033[0m")
        print("\033[35m |      \\|/         \033[0m")
        print("\033[35m |                   \033[0m")
        print("\033[35m |                   \033[0m")

    elif error == 4:
        print("\033[35m |      (_)          \033[0m")
        print("\033[35m |      \\|/         \033[0m")
        print("\033[35m |       |           \033[0m")
        print("\033[35m |                   \033[0m")

    elif error == 5:
        print("\033[35m |      (_)          \033[0m")
        print("\033[35m |      \\|/         \033[0m")
        print("\033[35m |       |           \033[0m")
        print("\033[35m |      / \\         \033[0m")

    print("\033[35m |                   \033[0m")
    print("\033[35m_|___                \033[0m")

def definir_nivel():
    print("\033[32m     DIGITE: \033[0m[\033[31m1\033[0m]\033[32m fácil \033[0m")
    print("\033[32m             \033[0m[\033[31m2\033[0m]\033[32m normal \033[0m")
    print("\033[32m             \033[0m[\033[31m3\033[0m]\033[32m dificil \033[0m")

    nivel = int(input("\033[31m    DIGITE O NIVEL:   \033[0m"))

    if (nivel == 1):
        total_tentativas = 10
    elif (nivel == 2):
        total_tentativas = 5
    elif (nivel == 3):
        total_tentativas = 3
    return total_tentativas

if(__name__ == "__main__"):
    jogar_forca()