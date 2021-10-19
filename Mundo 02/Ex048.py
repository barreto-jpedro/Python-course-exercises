sum = 0
quantidade = 0
for n in range(3, 500, 3):
    if n % 2 == 1:
        sum += n
        quantidade += 1

print('\n\n\nSoma dos {} números impares múltiplos de 3 = {}\n\n\n'.format(quantidade, sum))
