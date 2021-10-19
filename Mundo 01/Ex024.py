cidade = input('Digite a cidade que você nasceu e descubra se ela começa com a palavra "santo": ')

primeiraPalavra = cidade.split()
primeiraPalavra[0] = primeiraPalavra[0].lower()

print(primeiraPalavra[0] == 'santo')
    