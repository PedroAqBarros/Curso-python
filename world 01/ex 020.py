import random
a1 = str(input('Digite o nome do aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o anome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))
lista= [a1, a2, a3, a4] 
random.shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)
