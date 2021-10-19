lista = []

for num in range(0, 5):
    lista.append(float(input(f'Digite o {num+1}º número: ')))

    if num == 0:
        maior = menor = lista[0]
    else:
        if lista[num] >= maior:
            maior = lista[num]

        elif lista[num] <= menor:
            menor = lista[num]

print(f'Você digitou os seguintes valores: {lista}')


print(f'O maior valor da lista é {maior}. ELe está na posição: ', end='')
for pos, numero in enumerate(lista):
    if numero == maior:
        print(f'{pos+1}', end='...')

print(f'\nO menor valor da lista é {menor}. ELe está na posição: ', end='')
for pos, numero in enumerate(lista):
    if numero == menor:
        print(f'{pos+1}', end='...')
