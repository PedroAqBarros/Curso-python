d = float(input('Qual a distancia da viagem? '))
p = d * 0.5 if d <= 200 else d * 0.45
print('O preço da passagem é R${}'.format(p))
