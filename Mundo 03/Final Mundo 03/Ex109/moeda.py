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
