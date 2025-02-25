produtos = ('banana', 4.99, 'laranja', 13.99, 'maçã', 5.50, 'brinjela', 70.00)
print('='*40)
lista = ('lista de produtos')
listac = lista.center(40, '-')
print(listac)
print('='*40)
for i in range(0, len(produtos), 2):
    print(produtos[i],f' R$ {produtos[i+1]:>5.2f}'.rjust(40 - len(produtos[i]) - 1, '.'))