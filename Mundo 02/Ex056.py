Nomes = []
Idades = []
Sexos = []

for n in range(0,4): ## inicializando os vetores
    print(f'----- {n+1}ª PESSOA -----')
    Nomes.insert(n, input('Nome: '))
    Idades.insert(n, int(input('Idade: ')))
    Sexos.insert(n,  str((input('Sexo [M/F]: ').upper())))


################################################################################
                    ## Calculando a media das idades ##

soma = 0

for n in range(0,4): 
    soma += Idades[n]

media = soma/4

print(f'A média de idade do grupo é de {media} anos')

################################################################################
                        ## Calculado o mais velho ##

maior = Idades[0]
posicao = 0

for i in range(0, 4):
    if Idades[i] > maior:
        maior = Idades[i]                       
        posicao = i

print('A pessoa mais velha tem {} anos e se chama: {}'.format(maior, Nomes[posicao]) )

################################################################################
         ## Calculando o numero de mulheres com menos de 20 anos ##

meninas = 0

for i in range (0,4):
    if Sexos[i] == 'F' and Idades[i] < 20:
        meninas += 1
print(f'Neste grupo, {meninas} tem menos de 20 anos.')
