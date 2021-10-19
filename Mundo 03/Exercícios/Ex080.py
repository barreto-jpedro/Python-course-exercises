lista = [] #colocando 5 numeros digitados na ordem, sem usar o metodo sort()

for n in range(0, 5):

    num = int(input(f'Digite o {n+1}º número: '))

    if (n == 0) or num > lista[-1]:
        lista.append(num)
        print(f'Adicionado ao final da lista...')
        

    else:
        for pos in range(0, len(lista)):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Adicionado na posicao {pos} da lista... ')
                break

print(f'A lista ordenada é: {lista}')
