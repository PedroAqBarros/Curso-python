f = str(input('Digite uma frase qualquer: ')).strip().lower()
p = f.split()
j = ''.join(p)
fi = j[::-1]
if j == fi:
    print(f, ' Ao contrario é: ', fi, ' e é um palindromo')
else:
    print(f, ' não é um palindromo e ao contrario fica: ', fi)