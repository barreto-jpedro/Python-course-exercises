def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco*taxa/100)
    return res if formato is False else dinheiro(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco*taxa/100)
    return res if formato is False else dinheiro(res)


def dobro(preco=0, formato=False):
    res = preco*2
    return res if formato is False else dinheiro(res)


def metade(preco=0, formato=False):
    res = preco/2
    return res if formato is False else dinheiro(res)


def dinheiro(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(preco=0, aumento=0, reducao=0):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{dinheiro(preco)}')
    print(f'Dobro do preço: \t{dobro(preco,True)}')
    print(f'Metade do preço: \t{metade(preco,True)}')
    print(f'Aumento de {aumento}% no preço: \t{aumentar(preco,aumento,True)}')
    print(f'Reducao de {reducao}% no preço: \t{diminuir(preco,reducao,True)}')
    print('-' * 30)
