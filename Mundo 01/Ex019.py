from random import choice

pessoa1 = input('Digite o nome da pessoa 1: ')
pessoa2 = input('Digite o nome da pessoa 2: ')
pessoa3 = input('Digite o nome da pessoa 3: ')
pessoa4 = input('Digite o nome da pessoa 4: ')

lista = [pessoa1, pessoa2, pessoa3, pessoa4]

sorteado = choice(lista)

print('O aluno escolhido foi {}'.format(sorteado))
