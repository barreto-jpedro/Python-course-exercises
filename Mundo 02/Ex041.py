print('Descubra em qual categoria você se encaixa!')

idade = int(input('Digite a sua idade: '))

if idade < 9:
    print('Você será alocado na categoria MIRIM')

elif 9 <= idade and idade < 14:
    print('Você será alocado na categoria INFANTIL')

elif 14 <= idade and idade < 19:
    print('Você será alocado na categoria JUNIOR')

elif 19 <= idade and idade < 20:
    print('Você será alocado na categoria SENIOR')

else:
    print('Você será alocado na categoria MASTER')
