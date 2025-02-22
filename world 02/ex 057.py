sexo = str(input('Qual seu sexo? [m/f]')).strip().lower()
while sexo != 'm' and sexo != 'f':
    print('Sexo inválido, tente novamente')
    sexo = str(input('Qual seu sexo? [m/f]')).strip().lower()
print('Sexo registrado')