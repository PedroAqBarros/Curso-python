n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
escolha = 0
while escolha != 5:
    escolha = int(input('[1]somar\n[2]multiplicar\n[3]maior\n[4]novos números\n[5]sair\nEscolha uma opção: '))
    if escolha == 1:
        print('A soma dos dois numeros é {:.2}'.format(n1+n2))
    elif escolha == 2:
        print('A multiplicação dos dois numeros é {:.2}'.format(n1*n2))
    elif escolha == 3:
        if n1 > n2 and n1 != n2:
            print('O maior número é {}'.format(n1))
        elif n1 == n2:
            print('Os números são iguais')
        else:
            print('O maior número é {}'.format(n2))
    elif escolha == 4:
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número: '))
    elif escolha == 5:
        print('Fim')
    else:
        print('Opção inválida')