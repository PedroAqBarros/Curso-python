totf = 0
totidade = 0
midade = 0
nomemidade = ''
for i in range(1,5):
    nome = input('Qual nome da {}.a pessoa? '.format(i)).strip().lower()
    idade = int(input('Quantos anos você tem? '))
    sexo = input('Qual seu sexo? [m/f]').strip().lower()
    totidade = totidade + idade
    if sexo == 'f':
        if idade < 20:
            totf = totf + 1
    if sexo == 'm':
        if idade > midade:
            midade = idade
            nomemidade = nome
print('A media de idade do grupo é de {} anos.\nO homem mais velho tem {} anos e se chama {}.\nAo todo são {} mulheres com menos de 20 anos'.format(totidade/4,midade,nomemidade,totf))