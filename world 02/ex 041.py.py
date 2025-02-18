from datetime import date
ano = int(input('Digite o ano de seu nascimento: '))
idade = date.today().year - ano
print('Sua categoria é MIRIN' if idade <=9 else 'Sua categoria é INFANTIL' if idade > 9 and idade <= 14 else 
      'Sua categoria é JUNIOR' if idade > 14 and idade <= 19 else 'Sua categoria é SENIOR' if idade > 19 and idade <= 25 else 'Sua categoria é MASTER')