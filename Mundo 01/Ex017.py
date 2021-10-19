from math import sqrt

cateto1 = float(input('Digite o tamanho do cateto 1: '))
cateto2 = float(input('Digite o tamanho do cateto 2: '))

hipotenusa = sqrt((cateto1**2) + (cateto2**2))

print('A hipotenusa mede: {}'.format(hipotenusa))
