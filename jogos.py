import forca
import advinhacao

def escolher_jogos():
    jogo = retornar_opcao()

    if(jogo == 1):
        print("JOGO FORCA")
        forca.jogar_forca()
    elif(jogo == 2):
        print("JOGO ADVINHACAO")
        advinhacao.jogar_advinhacao()


def retornar_opcao():
    print("\033[31m*\033[0m" * 31)
    print("\033[32m ESCOLHA UM JOGO \033[0m")
    print("\033[31m*\033[0m" * 31)

    print("\033[32m     DIGITE: \033[0m[\033[31m1\033[0m]\033[32m FORCA \033[0m")
    print("\033[32m             \033[0m[\033[31m2\033[0m]\033[32m ADVINHAÇÃO \033[0m")

    return int(input("\033[31m    DIGITE O NUMERO DO JOGO:   \033[0m"))

if(__name__ == "__main__"):
    escolher_jogos()