dados = dict()
pessoas = list()
quer_continuar = 'S'
soma_idades = 0

while quer_continuar == 'S':
    dados['nome'] = input('Nome: ')  # Nome

    while True:  # Sexo
        dados['sexo'] = input('Sexo: [F/M]').strip().upper()
        if (dados['sexo'] != 'M') and (dados['sexo'] != 'F'):
            print('ERRO! Por favor, digite novamente: ')
        else:
            break

    dados['idade'] = int(input('Idade: '))  # Idade
    soma_idades += dados['idade']

    while True:  # Quer continuar?
        quer_continuar = input('Quer continuar? [S/N] ').strip().upper()
        if quer_continuar == 'S':
            break
        elif quer_continuar == 'N':
            break
        else:
            print('ERRO! Responda apenas S ou N.')

    pessoas.append(dados.copy())

media = soma_idades/len(pessoas)

print(f'\nA)  Ao todo temos {len(pessoas)} pessoas cadastradas.')
print(f'B)  A média de idade é: {media} anos.')
print(f'C)  As mulheres cadastradas são: ', end='')

for n in pessoas:
    for k, v in n.items():
        if k == 'sexo' and v == 'F':
            print(n['nome'], end='; ')

print('\nAs pessoas que estão acima da média são: ')

for n in pessoas:
    if n['idade'] > media:
        for k, v in n.items():
            print(f'{k} = {v}; ', end='')
        print('')

print('>>ENCERRADO<<')