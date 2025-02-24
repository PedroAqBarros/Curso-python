while True:
    num = int(input("Digite um número para ver a sua tabuada (número negativo para sair): "))
    if num < 0:
        break
    print(f"Tabuada de {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
    print("-" * 20)
print("Programa encerrado.")