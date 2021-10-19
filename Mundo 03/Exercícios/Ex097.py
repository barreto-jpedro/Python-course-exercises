def titulo(palavra):
    intervalo = len(palavra) + 6
    print('~'*intervalo)
    print(f'   {palavra.strip().upper()}')
    print('~'*intervalo)


titulo('mais que exatas')
titulo('joao pedro barreto costa almeida')
titulo('teste')
