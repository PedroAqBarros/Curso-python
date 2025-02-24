tg = 0
p1k = 0
pmb = ''
precomb = float('')

while True:
    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: R$"))
    
    tg += preco
    
    if preco > 1000:
        p1k += 1
    
    if preco < precomb:
        precomb = preco
        pmb = nome
    
    cc = input("Deseja continuar? [S/N] ").strip().upper()
    if cc == 'N':
        break

print(f"\nTotal gasto na compra: R${tg:.2f}")
print(f"Quantidade de produtos que custam mais de R$1000: {p1k}")
print(f"Produto mais barato: {pmb} que custa R${precomb:.2f}")