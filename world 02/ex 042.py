'''Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
EQUILÁTERO: todos os lados iguais
ISÓSCELES: dois lados iguais, um diferente
ESCALENO: todos os lados diferentes'''

l1 = float(input('digite o primeiro lado: '))
l2 = float(input('digite o segundo lado: '))
l3 = float(input('digite o terceiro lado: '))
tri = bool((l1 < l2 + l3) and (l2 < l1 + l3) and ( l3 < l1 + l2))
eq = bool((l1 == l2) and (l2 == l3))
es = bool((l1 != l2) and (l2 != l3) and (l1 != l3))
print("pode formar um triangulo? ", 'sim' if tri == True else 'não')
if tri == True and eq == True:
    print('o triangulo é equilatero')
elif es == True:
    print('o triangulo é escaleno')
else:
    print('o triangulo é isosceles')
