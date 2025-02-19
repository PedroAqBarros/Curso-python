Ppeso = 1
Lpeso = 1
pessoaL = 1
pessoaP = 1
for i in range(1,6):
    peso = float(input('quantos kg tem a {}.a pessoa? '.format(i)))
    if i == 1:
        Ppeso = peso
        Lpeso = peso
    else:
        if peso > Ppeso:
            Ppeso = peso
            pessoaP = i
        if peso < Lpeso:
            Lpeso = peso
            pessoaL = i
print('A pessoa mais pesada foi a {}.a , pesando {:.2f} kg'.format(pessoaP,Ppeso))
print('A pessoa mais pesada foi a {}.a , pesando {:.2f} kg'.format(pessoaL,Lpeso))