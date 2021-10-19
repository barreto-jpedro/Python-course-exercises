num = int(input('Digite um numero inteiro: ')) 

print(' [1] Binário\n [2] Octal\n [3] hexadecimal')

escolha = int (input('Escolha para qual base deseja convertê-lo: '))

if escolha == 1:
    print('O número {}, em binário, é dado por: {}'.format(num, bin(num)[2:]))

elif escolha == 2:
    print('O número {}, em octal, é dado por: {}'.format(num, oct(num)[2:]))

elif escolha == 3:
    print('O número {}, em hexadecimal, é dado por: {}'.format(num, hex(num)[2:]))

else:
    print('Você escolheu uma base invalida. Reinicie o programa.')