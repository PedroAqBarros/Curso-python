n = int(input('digite um numero: '))
i = 0
for t in range(1,11):
    i = i + 1
    t = n * t
    print(' {} * {} = {} '.format(n, i, t))