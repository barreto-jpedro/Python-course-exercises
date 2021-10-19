from typing import no_type_check


def cadastro_jogador(nome='<desconhecido>', n_gols = 0):    
    print(f'O jogador {nome} fez {n_gols} gol(s) no campeonato.')



nome = input('Nome do jogador: ')
n_gols = input('Número de gols: ')

if n_gols.isnumeric():
    n_gols = int(n_gols)
else:
    n_gols = 0

cadastro_jogador(nome, n_gols)