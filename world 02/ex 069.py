total_maiores_18 = 0
total_homens = 0
total_mulheres_menos_20 = 0

while True:
    print("Cadastro de Pessoa")
    idade = int(input("Idade: "))
    sexo = ''
    while sexo not in 'MF':
        sexo = input("Sexo [M/F]: ").strip().upper()
    
    if idade > 18:
        total_maiores_18 += 1
    if sexo == 'M':
        total_homens += 1
    if sexo == 'F' and idade < 20:
        total_mulheres_menos_20 += 1
    
    continuar = ''
    while continuar not in 'SN':
        continuar = input("Quer continuar? [S/N]: ").strip().upper()
    if continuar == 'N':
        break

print(f"Total de pessoas com mais de 18 anos: {total_maiores_18}")
print(f"Ao todo temos {total_homens} homens cadastrados")
print(f"E temos {total_mulheres_menos_20} mulheres com menos de 20 anos")