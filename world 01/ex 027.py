nome = input('digite seu nome completo: ').strip()
print('seu primeiro nome é {}.'.format(nome[0:nome.find(' ')]))
ultimapos= nome.rfind(' ')
print('Seu ultimo nome é {}.'.format(nome[ultimapos+1:]))
