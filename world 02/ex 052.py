from colorama import Fore, Style
Style.RESET_ALL
print()
n = int(input(Style.RESET_ALL + 'Digite um número inteiro: '))
i = 0
for c in range(1,n+1):
        if n % c == 0 :
            print(Fore.YELLOW + str(c), end=' ')
        else:
              print(Style.RESET_ALL +str(c), end=(' '))
        if n % c == 0 :
                i = i + 1
if i == 2:
    print(Style.RESET_ALL + '\nO numero {}', Style.RESET_ALL + ' é primo e pode ser dividido 2x!'.format(Fore.YELLOW + str(n)))
else:
    print(Style.RESET_ALL + '\nO numero ', Fore.YELLOW + str(n) , Style.RESET_ALL + ' não é primo e pode ser dividido {}x'.format(Fore.YELLOW + str(i)))
Style.RESET_ALL
print()