print('Digite as notas das dus primeiras provas: ')

nota1 = int(input('Primeira nota: '))
nota2 = int(input('Segunda nota: '))

media = (nota1 + nota2) / 2

print(f'Sua média final foi: {media}')

if media > 7:
    print('PARABÉNS!! Você foi aprovado.')

elif 5 < media and media < 6.9:
    print('Você está de recuperação.')

else:
    print('Você foi REPROVADO.')
