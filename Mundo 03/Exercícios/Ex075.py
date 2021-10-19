numeros = []
pares = 0

for n in range(1, 5):
    num = int(input(f'Digite o {n}º número: '))
    numeros.insert(n, num)
    if num%2 == 0:
        pares += 1


print(f'Você digitou os valores: {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3)+1}ª posição')
else: 
    print('O valor 3 não foi digitado')

print(f'Dentre esses números, {pares} são pares')
