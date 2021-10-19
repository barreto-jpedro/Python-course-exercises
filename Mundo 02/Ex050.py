print('Digite 6 números.')

sum = 0

for n in range (1,7):
    num = int(input('\n->'))
    if num % 2 == 0:
        sum += num
print('\n\n\nSoma dos números pares  digitados é: {}\n\n\n'.format(sum))

