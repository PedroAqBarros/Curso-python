import random

def par_ou_impar():
    vitorias = 0

    while True:
        jogador_valor = int(input("Digite um valor: "))
        jogador_escolha = input("Par ou Ímpar? [P/I] ").strip().upper()
        computador_valor = random.randint(0, 10)
        total = jogador_valor + computador_valor

        print(f"Você jogou {jogador_valor} e o computador jogou {computador_valor}. Total de {total} ", end="")
        print("DEU PAR" if total % 2 == 0 else "DEU ÍMPAR")

        if (jogador_escolha == 'P' and total % 2 == 0) or (jogador_escolha == 'I' and total % 2 != 0):
            print("Você VENCEU!")
            vitorias += 1
        else:
            print("Você PERDEU!")
            break

        print("Vamos jogar novamente...")

    print(f"GAME OVER! Você venceu {vitorias} vezes.")

if __name__ == "__main__":
    par_ou_impar()