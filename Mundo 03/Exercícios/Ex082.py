lista = []
lista_pares = []
lista_impares = []
quer_continuar = 'S'

while quer_continuar == 'S':
    num = int(input(f'\nDigite o um número: '))
    lista.append(num)
    
    if num % 2 == 0:
        lista_pares.append(num)
    else:
        lista_impares.append(num)

    quer_continuar = str(input('Quer continuar? [S/N] ')).strip().upper()

print(f'\nOs números digitados foram: {lista}')
print(f'os números PARES digitados foram: {lista_pares}')
print(f'os números IMPARES digitados foram: {lista_impares}\n')
