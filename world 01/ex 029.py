v = float(input('Qual a velocidade do carro? '))
if v >80:
    print('Você foi multado!')
    print('A multa é de R${:.2f} '.format((v -80)*7))
else:
    print('siga com cautela')