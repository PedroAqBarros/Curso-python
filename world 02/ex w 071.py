num = int(input('Digite o valor a ser sacado: '))
v = [50, 20, 10, 1]
notas = [0]*4
i = 0
while i < 4:
    while num >= v[i]:
        notas[i] += 1
        num -= v[i]
    i += 1
print('''Em relação as notas emitidas foram usadas:
notas de R$50: {}
notas de R$20: {}
notas de R$10: {}
notas de  R$1:  {}
'''.format(notas[0], notas[1], notas[2], notas[3]))