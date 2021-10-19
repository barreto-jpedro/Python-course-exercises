primeiro_termo = float(input('Digite o primeiro termo da sua PA: '))
razao = float(input('Digite a razão da sua PA: '))


decimo_termo = primeiro_termo+(razao*9)

print(f'Decimo termo: {decimo_termo}')

while primeiro_termo <= decimo_termo:
    print(f'{primeiro_termo} -> ', end='')
    primeiro_termo += razao

print('FIM')
