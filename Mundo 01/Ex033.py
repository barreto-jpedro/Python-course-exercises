num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo  número: '))
num3 = float(input('Digite o terceiro número: '))


if num1 >= num2:
    if num1 >= num3:
        maior = num1

        if num3 >= num2:
            menor = num2
        else:
            menor = num3
    else:
        maior = num3
        menor = num2

else:
    if num2 >= num3:
        maior = num2
        if num1 >= num3:
            menor = num3
        else:
            menor = num1
    else:
        maior = num3
        menor = num1


print('O menor número é: {}'.format(menor))
print('O maior número é: {}'.format(maior))


