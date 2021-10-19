from random import randint
from operator import itemgetter

dados = {'jogador1': randint(1, 6),
         'jogador2': randint(1, 6),
         'jogador3': randint(1, 6),
         'jogador4': randint(1, 6)}

print('Valores sorteados: ')

for k, v in dados.items():
    print(f'O {k} tirou {v} no dado')

print(f'\n{" == RANKING DOS JOGADORES == ":^40}')

n = 0

for k in sorted(dados, key=itemgetter(1), reverse=True):
    n += 1
    print(f'O {n}º colocado foi {k} e tirou {dados[k]} no dado')

print('-='*30)
