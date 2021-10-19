import moeda

valor = float(input(f'Digite o valor: R$'))
taxa = float(input('Qual é a taxa? (%) '))

print(f'Dobro de {moeda.dinheiro(valor)} = {moeda.dobro(valor, True)}')
print(f'Metade de {moeda.dinheiro(valor)} = {moeda.metade(valor, True)}')
print(f'{moeda.dinheiro(valor)} acrescido em {taxa}% = {moeda.aumentar(valor,taxa, True)}')
print(f'{moeda.dinheiro(valor)} diminuído em {taxa}% = {moeda.diminuir(valor,taxa, True)}')
