numeros = [[], []]
num = 0
for n in range(1, 8):
    num = int(input(f'Digite o {n}º número: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else: 
        numeros[1].append(num)       
    

numeros[0].sort()
numeros[1].sort()

print(f'Numeros: {numeros}') 

print(f'Números pares: ', end='')
print(numeros[1])

print(f'Números impares: ', end='')
print(numeros[0])
    


