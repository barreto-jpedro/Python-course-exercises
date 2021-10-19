num = int(input('Digite um número para descobrir se ele é primo: '))

sum = 0

for n in range(1, num+1):
    if num % n == 0:
        sum += 1

print(f'Soma>{sum} ')
if sum == 2:
    print(f'O numero {num} é primo!!')
else:
    print(f'O numero {num} NÃO é primo!!')
