num1 = int(input('Digite um número para calcular o seu fatorial: '))

n = 1
resultado = 1


while num1 >= n:   
    resultado = resultado * n
    n += 1


print(f'\nO fatorial de {num1} é {resultado}')


