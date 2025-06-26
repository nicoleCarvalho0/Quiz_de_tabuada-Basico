import random

computador=random.randint(1,100)
print("="*50)
print("Bem-vindo ao Jogo de Adivinhação!".center(50))
print("="*50)

for tentativas in range(6):
     if tentativas < 5:
        jogador=int(input("Digite um numero de (1 ate 100):"))
        if jogador == computador:
            print("Acertou!!Parabens!! ")
            print(f"Parabéns! Você acertou o número {computador} em {tentativas} tentativas!")
            break
        else:
            if jogador> computador:
                print("O número é menor. Tente novamente!")
            else:
                print("O número é maior. Tente novamente!")
     else:
        print(f"Voce errou!!Que pena !!O numero secreto era {computador}!!")


