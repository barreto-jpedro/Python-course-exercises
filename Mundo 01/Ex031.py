dist = float(input('Qual é a distância da sua viagem em quilometros? '))

if dist > 200:
    valor = 0.45 * dist

else:
    valor = 0.5 * dist

print('O valor a ser pago será de: {:.2f}'.format(valor))
