num1 = float(input('Digite o primeiro lado: '))
num2 = float(input('Digite o segundo  lado: '))
num3 = float(input('Digite o terceiro lado: '))


if num1 >= num2:
    if num1 >= num3:
        maior = num1

        if num3 >= num2:
            menor = num2
            meio = num3
        else:
            menor = num3
            meio = num2
    else:
        maior = num3
        menor = num2
        meio = num1

else:
    if num2 >= num3:
        maior = num2
        if num1 >= num3:
            menor = num3
            meio = num1
        else:
            menor = num1
            meio = num3
    else:
        maior = num3
        menor = num1
        meio = num2


if (menor + meio) > maior:
    print('Este triângulo EXISTE!')

else:
    print('Este triângulo NÃO existe!')
