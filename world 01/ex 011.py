l = float(input('qual a largura em M da parede? '))
a = float(input('qual a altura em M da parede? '))
ar = l * a
t = ar / 2
print('A area total é de {}, será nescessario {} litros de tinta para pintar considerando que cada litro pinta uma area de 2m².'.format(ar, t))