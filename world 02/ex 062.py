p = int(input('Primeiro termo: '))
r = int(input('razão: '))
t = p
c = 1
tot = 0
mais = 10
while mais != 0:
    tot += mais
    while c <= tot:
        print('{} ->'.format(t), end=(''))
        t += r
        c += 1
    if c > tot:
        print('PAUSA')
        mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados'.format(tot))
