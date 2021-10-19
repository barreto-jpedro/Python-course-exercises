from random import randrange

num = randrange(6)

var1 = int(input('Em qual número entre 0 e 5 estou pensando? '))

if (var1 == num):
    print('PARABÉNS!!!')
else:
    var1 = input('ERROU!!')
