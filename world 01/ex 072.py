extenso = 'zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezeseis','dezesete','dezoito','dezenove','vinte'
r = 's'
while r != 'n':
    n = int(input('Digite um numero de 0 a 20: '))
    if n > 20 or n < 0:
        print('Numero invalido')
    else:
        print(extenso[n])
    r = input('deseja continuar? [s/n]')