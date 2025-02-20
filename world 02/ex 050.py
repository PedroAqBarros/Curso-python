'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.'''
soma = 0
for i in range(1,6):
    i=int(input('Digite um numero inteiro: '))
    if i % 2 == 0:
        soma = soma + i
print(soma)