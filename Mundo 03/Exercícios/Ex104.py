def leiaInt(msg):
    while True:
        var = input(msg)
        if var.isnumeric():
            return int(var)
        else:
            print('ERRO! digite um número válido.')


#Programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número: {n}')