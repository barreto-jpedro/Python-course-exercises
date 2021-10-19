from random import randint
numeros = list()

print('-'*50)
print(f'{"GERADOR DE JOGOS PARA A MEGA SENA":^50}')
print('-'*50)

n_de_jogos = int(input('Quantos jogos você deseja? '))



for n in range(0, n_de_jogos):
    for n in range(1,7):
        numeros.append(randint(1,60))    
        
    numeros.sort()
    print(f'Jogo {n}: {numeros}')
    numeros.clear()

print('\nBOA SORTE!!\n')        
