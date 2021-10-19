num = -1
por_extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
               'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

num = int(input('Digite um número entre 0 e 20: '))

while num < 0 or num > 20:
    print('ERRADO! TENTE NOVAMENTE.')
    num = int(input('Digite um número entre 0 e 20: '))
    

print(f'O número {num} escrito por extenso é: {por_extenso[num]}')
