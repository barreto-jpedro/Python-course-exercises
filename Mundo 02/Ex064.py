soma = 0
num = 0
counter = 0

while num != 999:
    num = float(input('Digite um número [999 para parar]: '))
    if num != 999:
        soma += num
        counter += 1    

print(f'Você digitou {counter} e a soma entre eles foi {soma}')
