salario = float(input('Digite o sau salário:'))

if salario <= 1250:
    salario = salario * 1.15
else:
    salario = salario * 1.1

print('O seu novo salário é: R${:.2f}'.format(salario))