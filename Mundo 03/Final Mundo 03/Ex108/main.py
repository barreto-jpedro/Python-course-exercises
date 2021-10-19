import moeda

valor = float(input(f'Digite o valor: R$'))
taxa = float(input('Qual é a taxa? (%) '))

print(f'\nDobro de {moeda.moeda(valor)} = {moeda.moeda(moeda.dobro(valor))}'
      f'\nMetade de {moeda.moeda(valor)} = {moeda.moeda(moeda.metade(valor))}'
      f'\n{moeda.moeda(valor)} acrescido em {taxa}% = {moeda.moeda(moeda.aumentar(valor,taxa))}'
      f'\n{moeda.moeda(valor)} diminuído em {taxa}% = {moeda.moeda(moeda.diminuir(valor,taxa))}'
      )
