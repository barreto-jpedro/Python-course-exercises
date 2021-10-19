def fatorial(num, show=False):
    """

    Essa função foi criada para calcular o fatorial de um número.
    :param n: O número a ser alculado
    :param show: mostrar ou não a conta
    :return: O valor fatorial do numero n
    """
    _fatorial = 1
    for n in range(1, num+1):
        _fatorial *= n
        if show:
            print(f'{n} ', end='')

    return _fatorial


print(fatorial(5, True))
