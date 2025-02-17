s = float(input('Qual o seu salario? R$'))
print('O seu salario agora é :R$',s + s * 10/100 if s > 1250 else s + s * 15/100)