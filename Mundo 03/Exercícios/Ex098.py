def contador(inicio, fim, pace):
    if fim < 0:
        fim += 1
    if pace < 0:
        pace *= -1
    if pace == 0:
        pace = 1
    print(f'Contagem de {inicio} até {fim} pulando {pace} em {pace}')
    if inicio <= fim:
        if pace < 0:
            pace -= (pace+pace)
        for cont in range(inicio, fim+1, pace):
            print(cont, end=' ')
        print()
        print('-'*30)
    else:
        if fim <= 0:
            fim -= 1
        for cont in range(inicio, fim-1, -pace):
            print(cont, end=' ')
        print()
        print('-' * 30)

def contagem_personalizada():
    print('Agora é a sua vez de personalizar a contagem! ')
    i = int(input('Início: '))
    f = int(input('Fim: '))
    p = int(input('Passo: '))
    print('-'*30)
    contador(inicio=i, fim=f, pace=p)

#programa principal
contador(1, 10, 1)
contador(10, 0, 2)
contagem_personalizada()
