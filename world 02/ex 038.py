'''Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
O primeiro valor é maior
O segundo valor é maior
Não existe valor maior, os dois são iguais'''

n = int(input('digite um numero inteiro: '))
n1 = int(input('digite outro numero inteiro: '))
print('O primeiro é o maior numero' if n > n1 else 'O segundo é o maior numero' if n1 > n else 'Não existe valor maior, os dois são iguais' )

