from random import randint

print('Vamos jogar par ou impar!!!')

impar = 1
par = 0

counter = 0

while True:
    opcao = str(input('Você quer par ou impar? [P/I] ')).strip().upper()
    usuario = int(input('Digite um número: '))
    
    computador = randint(0,1)
    
    resultado = (usuario + computador) % 2
    
    print(f'Você jogou {usuario} e o computador jogou {computador}. A soma deu {usuario + computador}')

    if (resultado == impar and opcao == 'I') or (resultado == par and opcao == 'P'):
        counter += 1
        print(f'\nParabéns! Você venceu pela {counter}ª vez. Vamos de novo!\n')
    
    else:
        print('\nInfelizmente, você perdeu!\n')
        break

