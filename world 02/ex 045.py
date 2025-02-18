from random import choice
p = int(input('escolha \n [1]pedra [2]papel ou [3]tesoura\n'))
pedra = 1
papel = 2
tesoura = 3
pc = choice([pedra, papel, tesoura])


while p == pc:
    if pc == 1:
        print('eu também escolhi pedra')
    elif pc == 2:
        print('eu também escolhi papel')
    else:
        print('eu também escolhi tesoura')
    p = int(input('empatamos escolha novamente\n escolha \n [1]pedra [2]papel ou [3]tesoura\n'))
    pc = choice([pedra, papel, tesoura])

if p == 1 and pc == 3:
    print('Eu escolhi tesoura')
    print('Você ganhou!!')
elif p == 1 and pc == 2:
    print('Eu escolhi papel')
    print('Você perdeu :( ')
elif p == 2 and pc == 3:
    print('Eu escolhi tesoura')
    print('Você perdeu :( ')
elif p == 2 and pc == 1:
    print('Eu escolhi pedra')
    print('Você ganhou!!')
elif p == 3 and pc == 1:
    print('Eu escolhi pedra')
    print('Você perdeu :( ')
elif p == 3 and pc == 2:
    print('Eu escolhi papel')
    print('Você ganhou!!')
else:
    print('opção invalida', p, pc)