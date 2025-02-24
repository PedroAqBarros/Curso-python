count = 0
total = 0

while True:
    number = int(input("Digite um número (999 para parar): "))
    if number == 999:
        break
    count += 1
    total += number

print(f"Você digitou {count} números e a soma entre eles é {total}.")