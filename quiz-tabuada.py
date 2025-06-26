import random


print("Bem-vindo ao Quiz de Tabuada!")

jogar_novamente="s"

while jogar_novamente.lower()== 's':
    pontos = 0

    print("\nVamos começar! Você vai responder 5 perguntas de multiplicação.")

    for i in range(5):
            primeiro=random.randint(1,10)
            segundo=random.randint(1,10)
            resultado=primeiro*segundo

            print(f"\nPergunta {i+1}:Quanto é {primeiro} x {segundo}?")
            resposta = int(input("Sua resposta: "))

            if resposta == resultado:
                print("\033[32mAcertou!\033[m")
                pontos+=1
            else:
                print(f"\033[31mErrou! A resposta correta era {resultado}.\033[m3")

    print(f"\nVocê fez {pontos} ponto(s) de 5 possíveis.")

    jogar_novamente = input("\nDeseja jogar novamente? (s/n): ")

print("\nObrigado por jogar!")
