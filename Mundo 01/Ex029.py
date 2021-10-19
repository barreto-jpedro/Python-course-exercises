velocidade = float(input('Digite a velocidade do carro em Km/h: '))


if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Você foi multado!')
    print('O valor da sua multa é de: R${:.2f}'.format(multa))
