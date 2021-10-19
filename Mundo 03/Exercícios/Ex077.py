lista_de_palavras = ('Lapis', 'Borracha', 'Caderno', 'Estojo',
                     'Transferidor', 'Compasso', 'Mochila', 'Canetas', 'Livro')

for palavra in lista_de_palavras:
    print(f'Na palavra {palavra}, temos as vogais: ', end='')
    for letra in palavra.strip().lower():
        if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u': ######### OUTRO JEITO ############ " if letra in 'aeiou:' "
            print(f'{letra}', end=' ')
    print('\n')

