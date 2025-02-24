# Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

continuar = 'S'
soma = quantidade = media = maior = menor = 0

while continuar in 'Ss':
    numero = int(input('Digite um número: '))
    soma += numero
    quantidade += 1
    
    if quantidade == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    
    continuar = input('Quer continuar? [S/N] ').strip().upper()[0]

media = soma / quantidade
print(f'Você digitou {quantidade} números e a média foi {media:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')