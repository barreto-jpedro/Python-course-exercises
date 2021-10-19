ano = int(input('Em que ano você nasceu? '))

idade = 2021 - ano

if idade == 18:
    print('Está na hora de você se alistar!')

elif idade < 18:
    print(f'Calma! Ainda faltam {18 - idade} anos para você se alisar!')

else:
    print(f'VOCÊ DEVIA TER SE ALISTADO {idade - 18} ANOS ATRÁS!')