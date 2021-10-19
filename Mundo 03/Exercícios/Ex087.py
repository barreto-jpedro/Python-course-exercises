matriz = [[], [], []]
soma_pares = 0
soma_terceira_linha = 0
maior_valor_2_linha = 0


for i in range(0, 3):
    for j in range(0, 3):
        num = int(input(f'Digite um valor para: [{i}, {j}]: '))
        matriz[i].append(num)

        if i == 1 and j == 0:  # inicializa o maior numero da segunda linha
            maior_valor_2_linha = num

        if num > maior_valor_2_linha and i == 1:   # pega o maior numero da segunda linha da matriz
            maior_valor_2_linha = num

        if num % 2 == 0:  # soma os numeros pares
            soma_pares += num
            print('NUMERO PAR')

        if j == 2:  # identifica a terceira linha da matriz
            soma_terceira_linha += num


for i in range(0, 3):  # printa a atriz
    print('\n')
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^5}]', end='')

print('\n')

print(f'A soma dos valores pares é: {soma_pares}')
print(f'A soma dos valores da terceira coluna é: {soma_terceira_linha}')
print(f'O maior valor da segunda linha é: {maior_valor_2_linha}')
