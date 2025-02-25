tabela = (
    "Botafogo", "Flamengo", "Grêmio", "São Paulo", "Fluminense",
    "Palmeiras", "Bragantino", "Athletico-PR", "Fortaleza", "Atlético-MG",
    "Cruzeiro", "Internacional", "Corinthians", "Cuiabá", "Goiás",
    "Bahia", "Santos", "Vasco da Gama", "Coritiba", "América-MG"
)
print(f'5 primeiros colocados {tabela[:5]}')
print(f'4 ultimos {tabela[-4:]}')
print(f'Ordem afabetica: {sorted(tabela)}')
print(f'A chapecoense está na posição {tabela.index('Bahia')+1}')