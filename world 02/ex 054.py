from datetime import date
mnidade = 0
midade = 0
ano = date.today().year
for i in range(1,8):
    idade = int(input('em que ano a {}.a pessoa nasceu? '.format(i)))
    if ano - idade >=18:
        midade = midade + 1
    else:
        mnidade = mnidade + 1
print('Ao todo tivemos {} pessoas maiores de idade.\nE também {} menores'.format(midade,mnidade))