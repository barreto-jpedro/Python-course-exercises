sexo = str(input('Digite qual é o seu sexo [M/F]: ')).strip().lower()

while sexo != 'm' and sexo != 'f':
    sexo = str(input('DADOS INVÁLIDOS. Por favor, digite qual é o seu sexo [M/F]: ')).strip().lower()


print(f'Sexo {sexo} registrado com sucesso.')
