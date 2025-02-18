p = float(input('Qual o preço do produto? R$'))
pag = int(input('Qual a forma de pagamento?\n DIGITE:\n [1]: a vista\n [2]a vista cartão\n [3]ate 2x cartao\n [4]3x ou mais cartao\n'))
total = int
parcela = int
if pag == 1:
    p = p - p *10/100
    print('o preço final do produto é R$',p)
elif pag == 2:
    p = p - p *5/100
    print('o preço final do produto é R$',p)
elif pag == 3:
    p = p
    print('sua compra em 2x s/juros custará R$',p)
else:
    p = p + p *20/100
    parcela = int(input('em quantas x? '))
    total = p / parcela
    print('sua compra em {}x c/juros custará R${} por mês e o preco final será: R${}'.format(parcela,total,p))