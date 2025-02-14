d = int(input('quantos dias foi alugado? '))
km = float(input('quantos km foram rodados? '))
a = (d * 60) + (km * 0.15)
print('o total a pagar é R${}'.format(a))