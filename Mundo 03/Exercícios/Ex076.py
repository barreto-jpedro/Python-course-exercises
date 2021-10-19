lista_de_precos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20,
                   'Compasso', 9.99, 'Mochila', 100.32, 'Canetas', 22.30, 'Livro', 34.90)

print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)

for indice in range(0, len(lista_de_precos)):
    if indice % 2 == 0:
        print(f'{lista_de_precos[indice]:.<30}', end='')
    else:
        
        print(f'R${lista_de_precos[indice]:>7.2f}')
print('_'*40)
