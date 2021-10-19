def maior(*numeros):
    cont = len(numeros)
    if cont == 0:
        print('Não foi passado nenhum numero')
    else:
        maior = numeros[0]

        for n in numeros:
            if n > maior:
                maior = n

    print(f'Você digitou {cont} valores.\nO maior deles é: {maior}')
    print('-='*20)


maior(2, 9, 4, 5, 7, 1)
maior(5,2,7)

