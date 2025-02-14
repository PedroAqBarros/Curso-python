nome = str(input('Digite seu nome completo: ')).strip().lower().split()
if nome[0:] == 'silva':
    print('verdadeiro')
else:
    print('falso')