from random import randint


def sorteio():
    numeros = list()
    print('Sorteando os 5 valores da lista: ', end='')
    for n in range(0, 5):
        aux = randint(0, 9)
        numeros.append(aux)
        print(f'{aux} ', end='')
    print('PRONTO!')
    return numeros


def soma_pares(numeros):
    soma = 0
    for n in numeros:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {numeros}, temos: {soma}')


soma_pares(sorteio())
help(print)