palavras = ('aprender', 'programar', 'linguagem', 'python')
for i in range(0, len(palavras)):
    print(f'a palavra {palavras[i]} contem as vogal: ', end=' ')
    if palavras[i].find('a') != -1: 
        print('a', end=' ')
    if palavras[i].find('e') != -1: 
        print('e', end=' ')
    if palavras[i].find('i') != -1: 
        print('i', end=' ')
    if palavras[i].find('o') != -1: 
        print('o', end=' ')
    if palavras[i].find('u') != -1: 
        print('u', end=' ')
    print('\n')
