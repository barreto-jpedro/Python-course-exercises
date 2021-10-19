from random import randint

num = int(input(('Adivinhe qual número de 0 a 10 eu estou pensando: ')))

aleatorio = randint(0, 10)

while num != aleatorio:
    if num < aleatorio:
        print('Mais...', end='')
    else:
        print('Menos...', end='')

    num = int(input('Tente outra vez: '))


print('PARABÉNS!! VOCÊ ACERTOU!!')
