'''Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma 
casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação
 mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''

c = float(input('digite o valor da casa: '))
s = float(input('digite o salario: '))
a = int(input('Em quantos anos pretende pagar: '))
if s * 0.3 >= c / (a * 12):
    print('empréstimo concedido')   
else:
    print('empréstimo negado')