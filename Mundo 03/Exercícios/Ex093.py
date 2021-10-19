dados = dict()
n_gols = list()
dados['nome'] = str(input('Nome do jogador: '))
dados['total'] = 0

for n in range(0, int(input('Quantas partidas ele jogou? '))):
    n_gols.append(int(input(f'Quantos gols ele fez na partida {n+1}? ')))
    dados['total'] += n_gols[n]

dados['gols'] = n_gols

print('-='*50)
print(dados)
print('-='*50)

for k, v in dados.items():
    print(f'O campo {k} tem o valor: {v}')
print('-='*50)

print(f'O jogador {dados["nome"]} jogou {len(n_gols)} partidas')

for n in range(0, len(n_gols)):
    print(f'Na partida {n+1}, fez {n_gols[n]}')

print(f'foi um total de {dados["total"]} gols.')

print('')
