pessoas = list()
dados = list()

while True:
    dados.append(input('Nome: '))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])

    if len(pessoas) == 1:
        menor = maior = dados[1]

    else:
        if dados[-1] >= maior:
            maior = dados[-1]
        elif dados[-1] <= menor:
            menor = dados[-1]

        dados.clear()

    quer_continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if(quer_continuar == 'N'):
        break

print(f'\n\tVocê cadastrou {len(pessoas)} pessoas.\n')

print(f'\tO maior peso foi {maior}kg.\n\tPessoas com esse peso: ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]}', end=', ')

print(f'\n\n\tO menor peso foi {menor}kg.\n\tPessoas com esse peso: ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]}', end=', ')