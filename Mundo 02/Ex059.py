#### Calculadora ####
num1 = float(input('Primeiro valor: '))
num2 = float(input('Segundo valor: '))

opcao = 0

while opcao != 5:
    print('\n[1] - Somar\n[2] - Multiplicar\n[3] - Maior\n[4] - Novos números\n[5] - Sair do programa')
    opcao = int(input('\n>>>> Qual é a sua opção? '))
    
    if opcao == 1: 
        print(f'\n{num1} + {num2} = {num1 + num2}\n')

    elif opcao == 2:
        print(f'\n{num1} x {num2} = {num1 * num2}\n')

    elif opcao == 3:
        if num1 == num2:
            print(f'\n{num1} É IGUAL A {num2}\n')
            
        elif num1 > num2:
            print(f'\n{num1} É MAIOR QUE {num2}\n')

        else:
            print(f'\n{num2} É MAIOR QUE {num1}\n')
            
    elif opcao == 4:
        num1 = float(input('Primeiro novo valor: '))
        num2 = float(input('Segundo novo valor: '))
    
    elif opcao == 5:
        print('\nO programa foi encerrado.\n')

    else:
        print('\nErro! Opção inválida!!\n')
        

