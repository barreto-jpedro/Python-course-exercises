lista = [] 
teste_cinco = False
quer_continuar = 'S'

while quer_continuar == 'S':
    lista.append(int(input(f'\nDigite o um número: ')))
    quer_continuar = str(input('Quer continuar? [S/N]')).strip().upper()

    if lista[-1] == 5:
        teste_cinco = True

lista.sort(reverse=True)

if teste_cinco == True:
    print(f'\n\tO numero 5 faz parte da lista. ')
else:
    print(f'\n\tO numero 5 NÃO faz parte da lista. ')
print(f'\tA lista em ordem decrescente é: {lista}')
print(f'\tVocê digitou {len(lista)} elementos\n')

#print(f'A lista ordenada é: {lista}')
