frase = str(input('digite qualquer coisa: ')).lower().strip()
print('a letra "a" aparece {} vezes'.format(frase.count('a')))
print('a letra "a" aparece a primeira vez na posição {}'.format(frase.find('a')))
print('a letra "a" aparece a ultima vez na posição {}'.format(frase.rfind('a')))