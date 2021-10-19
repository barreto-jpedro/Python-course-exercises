lista = []
num = 0

while True:
    num = float(input('\nDigite um valor: '))

    if num not in lista:
        lista.append(num)
    else:
        print('%¨&%  VALOR REPETIDO! Não irei adiionar novamente...  %¨&%\n')

    finalizar = str(
        input('Deseja digitar outro valor? [S/N] ')).strip().upper()

    if finalizar == 'N':
        break

print('_'*30, '\n')

print(f'Você digitou os valores: {sorted(lista)}')
