p = int(input('Primeiro termo: '))
r = int(input('razão: '))
t = p
c = 1
while c <= 10:
    print('{} ->'.format(t), end=(''))
    t += r
    c += 1
print('FIM')