def area(largura, comprimento):
    return(largura * comprimento)

largura = int(input('Digite a largura do terreno: '))
comprimento = int(input('Digite o comprimento do terreno: '))

print(f'A área desse terreno é: {area(largura, comprimento)}')
