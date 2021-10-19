print('Digite o ano de nascimento de 7 pessoas: ')

contador =0

for n in range(0, 7):
    ano = int(input('-> '))
    if ano < 2000:
        contador += 1

print(f'Dessas 7 pessoas, {contador} são maiores de idade.')