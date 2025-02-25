from random import randint
n1 = randint(0,10); n2 = randint(0,10); n3 = randint(0,10); n4 = randint(0,10); n5 = randint(0,10); 
tupla = (n1,n2,n3,n4,n5)
maior = 0
menor = n1
print(tupla)
for i in range(0,5):
    if maior < tupla[i]:
        maior = tupla[i]
    if menor > tupla[i] :
        menor = tupla[i]
print(f'maior é {maior} e menor é {menor}')