soma = 0
num = 0
counter = 0
opcao = 'S'
menor = 0 
maior = 0 


while opcao == 'S':
    num = float(input('Digite um número: '))
    if num >= maior or counter == 0:
        maior = num

    if num <= menor or counter == 0:
        menor = num

    soma += num
    counter += 1
    opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()
    

print(f'Você digitou {counter} e a media entre eles foi {soma/counter}')
print(f'O maior valor foi {maior} e o menor foi: {menor}')
