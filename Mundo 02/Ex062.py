primeiro_termo = float(input('Digite o primeiro termo da sua PA: '))
razao = float(input('Digite a razão da sua PA: '))
n_de_termos = int(input(('Quantos termos você quer ver? ')))


while n_de_termos != 0:
    n = 0
    while n != n_de_termos:
        print(f'{primeiro_termo} -> ', end='')
        primeiro_termo += razao
        n += 1
    print('PAUSA')
    n_de_termos = int(input(('Quantos termos você quer ver? ')))


print('FIM')
    
