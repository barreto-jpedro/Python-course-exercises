from random import randint #5 valores sorteado. Qual o menor? Qual o maior?

print('\nOs valores sorteados foram: ', end='')

num = maior = menor = randint(0, 9) ## inicializando as variaveis
print(f'{num}', end=' ')

for n in range(0, 4):
    num = randint(0, 9)                           # Fiz diferente do cara do vídeo. Ele optou por fazer com tuplas,
    print(f'{num}', end=' ')                      # mas não tem necessidade de armazenar os dados... 

    if num >= maior:
        maior = num

    elif num <= menor:
        menor = num
print(f'\nO maior valor é: {maior}')

print(f'O menor valor é: {menor}\n')
