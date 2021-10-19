nome = input('Digite seu nome completo: ')
print('Analisando seu nome...')

print('Seu nome em maiúsculas é: {}'. format(nome.upper()))
print('Seu nome em minúsculas é: {}'. format(nome.lower()))

print('Seu nome tem ao todo {} letras'. format(len(nome) - nome.count(' ')))

lista = nome.split()

print('Seu primero nome é {} e tem {} letras'. format(lista[0], len(lista[0])))