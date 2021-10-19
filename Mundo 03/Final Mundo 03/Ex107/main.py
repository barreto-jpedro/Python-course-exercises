import moeda 

valor = float(input(f'Digite o valor: R$'))
taxa = float(input('valorual a taxa? (%) '))

print(f'\nDobro de R${valor} = R${moeda.dobro(valor)}'
      f'\nMetade de R${valor} = R${moeda.metade(valor):.2f}'
      f'\nR${valor} acrescido em {taxa}% = R${moeda.aumentar(valor,taxa):.2f}'
      f'\nR${valor} diminuído em {taxa}% = R${moeda.diminuir(valor,taxa):.2f}'
      )
