'''Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe,
 de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
   se é a hora exata de se alistar ou se já passou do tempo do alistamento.
 Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''
from datetime import date

ano = int(input('digite o ano de seu nascimento: '))
idade = date.today().year - ano
if idade < 18:
    print('ainda faltam {} ano/s para se alistar'.format((18-idade)))
elif  idade > 18:
    print('já se atrasaram {} ano/s'.format(idade-18))
else:
    print('está no ano de alistamento')