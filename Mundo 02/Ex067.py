while True:
    num = int(input('Digite um numero positivo para ver a sua tabuada: '))
    if num < 0:
        break

    for counter in range(0, 11):
        print('-'*5, f'{num} x {counter} = {num * counter}', '-'*5)

print('\nO programa terminou porque você digitou um NÚMERO NEGATIVO.\n')

