salario = float(input('Qual é o salário do funcionário? R$'))
salario_aumentado = salario * 1.15
print('Um funcionario que ganhava R${}, com 15% de aumento, passa a receber: R${:.2f}.'.format(salario, salario_aumentado))