'''Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer
 e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.'''

n = int(input('Digite um numero inteiro: '))
e = int(input('escolha qual será a base de conversão.\n Digite: [1] para binário, [2] para octal e [3] para hexadecimal.\n'))

if e == 1:
    print('{} convertido para binario é {}'.format(n,bin(n)))
elif e == 2:
    print('{} convertido para oct é {}'.format(n,oct(n)))
else:
    print('{} convertido para hex é {}'.format(n,hex(n)))