jogadores = list()
dados = dict()
_historico_de_gols = list()

quer_continuar = 'S'

while quer_continuar == 'S':
    total = 0
    dados['nome'] = str(input('Nome do jogador: '))

    for n in range(0, int(input('Quantas partidas ele jogou? '))):
        _historico_de_gols.append(
            int(input(f'Quantos gols ele fez na partida {n+1}? ')))
        total += _historico_de_gols[n]

    dados['historico_de_gols'] = _historico_de_gols[:]
    dados['total'] = total

    jogadores.append(dados.copy())
    _historico_de_gols.clear()

    while True:  # Quer continuar?
        quer_continuar = input('Quer continuar? [S/N] ').strip().upper()
        if quer_continuar == 'S':
            break
        elif quer_continuar == 'N':
            break
        else:
            print('ERRO! Responda apenas S ou N.')


print('-='*50)
print(f'{"cod:":<5}', f'{"Nome":<20}', f'{"Gols":<16}', f'{"Total"}')
print('_'*100)


for counter, value in enumerate(jogadores):
    print(f'  {counter}   ', end='')
    for info in value.values():
        print(f'{str(info):<20}', end='')
    print('')

print('\n', '-='*50, '\n')


while True:
    opcao = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if opcao == 999:
        break

    print(f'\t - LEVANTAMENTO DO JOGADOR {jogadores[opcao]["nome"]}')
    for counter, value in enumerate(jogadores[opcao]['historico_de_gols']):
        print(f'\tNo jogo {counter+1} fez {value} gols')

print('\n')

print('>>>>>>>>Fim do programa<<<<<<<<')

print('\n')
