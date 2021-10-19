dias_alugado = int(input('Por quantos dias seu carro foi alugado? '))
km_rodados = float(input('Quantos Km você percorreu? '))
valor = 60 * dias_alugado + 0.15 * km_rodados
print('O total a pagar é de R${:.2f}'.format(valor))

