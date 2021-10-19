
preco_casa = float(input('Qual é o valor da casa? '))
salario = float(input('Qual é o seu salário? '))
tempo = float(input('Por quanto tempo você vai pagar suas prestações? '))

prestacao = preco_casa / tempo

prestacao = round(prestacao,2)

if prestacao <= 0.3 * salario:
    print(' PARABÉNS! Você pode comprar a casa!')
    print(f'O valor da parcela será de R${prestacao}')
else:
    print('Infelizmente, você não pode comprar esta casa...')
 