from random import randint

print('\n\nVAMOS JOGAR JOKENPÔ?\n')
print('[1] - Pedra\n[2] - Papel\n[3] - Tesoura\n')


jogador = int(input('Você escolhe primeiro: '))
computador = randint(1, 3)
lista = ('PEDRA', 'PAPEL', 'TESOURA')

print('\nVocê escolheu {} e o computador escolheu {}.\n'.format(lista[jogador-1], lista[computador-1]))

if jogador == 1:
    if computador == 1:
        print('EMPATOU! Reinicie o programa e jogue novamente. \n\n')
    elif computador == 2:
        print('VOCÊ PERDEU! Reinicie o programa e tente novamente. \n\n')
    else:
        print('PARABÉNS!!!! VOCÊ VENCEU!!!\n\n')


elif jogador == 2:
    if computador == 1:
        print(' PARABÉNS!!!! VOCÊ VENCEU!!!\n\n')
    elif computador == 2:
        print('EMPATOU! Reinicie o programa e jogue novamente. \n\n')
    else:
        print('VOCÊ PERDEU! Reinicie o programa e tente novamente. \n\n')

elif jogador == 3:
    if computador == 1:
        print('VOCÊ PERDEU! Reinicie o programa e tente novamente. \n\n')
    elif computador == 2:
        print(' PARABÉNS!!!! VOCÊ VENCEU!!!\n\n')
    else:
        print('EMPATOU! Reinicie o programa e jogue novamente. \n\n')

else:
    print('ESCOLHA INVÁLIDA! Reinicie o programa e tente novamente. \n\n')
