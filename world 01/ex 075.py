tupla = (int(input('Digite um numero inteiro: ')),
         int(input('Digite um numero inteiro: ')),
         int(input('Digite um numero inteiro: ')),
         int(input('Digite um numero inteiro: ')))
print(f'o valor nove aparece {tupla.count(9)}')
print(f'Posição do primeiro vlr 3 é a {tupla.index(3) + 1}a. pos')
print('Os pares são', end=' ')
for i, n in enumerate(tupla):
    if n % 2 == 0:
        print(n, end=', ')