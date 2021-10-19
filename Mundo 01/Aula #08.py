import math

num = int(input('Digite um número: '))
raiz = math.sqrt(num)

print('A raiz de {} é igual a {}'.format(num, raiz))
print('A raiz de {} arredondada é igual a {}'.format(num, math.ceil(raiz)))#arredondou pra cima
print('A raiz de {} arredondada é igual a {}'.format(num, math.floor(raiz)))#arredondou pra baixo

###

from math import sqrt

num = int(input('Digite um número: '))
raiz = sqrt(num)

print('A raiz de {} é igual a {}'.format(num, raiz))
print('A raiz de {} arredondada é igual a {}'.format(num, ceil(raiz)))#arredondou pra cima
