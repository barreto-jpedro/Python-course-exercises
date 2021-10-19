print('=' * 50, '\n' , 'Banco Mais que Exatas', '\n' , '=' * 50)
print('Cédulas disponíveis: \n\tR$50,00\n\tR$20,00\n\tR$10,00\n\tR$1,00')

valor = int(input('Digite o valor que para retirar o dinheiro: '))

print(f'Totade de {valor // 50} cédulas de R$50,00')
print(f'Totade de {(valor % 50)//20} cédulas de R$20,00')
print(f'Totade de {((valor % 50)%20)//10} cédulas de R$10,00')
print(f'Totade de {(((valor % 50)%20)%10)} cédulas de R$1,00')
