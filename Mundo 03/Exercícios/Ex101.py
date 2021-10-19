def votar(ano):
    from datetime import date    

    idade = date.today().year - ano
    if idade > 65:
        return(f'O voto para quem tem mais de {idade} anos não é obrigatório.')
    elif idade > 18:
        return(f'O voto para quem tem {idade} anos é obrigatório. ')
    else:
        return(f'O voto para quem tem mais de {idade} é proibido. ')


print(votar(int(input('Em que ano você nasceu? '))))
