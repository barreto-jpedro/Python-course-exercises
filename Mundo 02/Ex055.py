print('Digite o peso de 5 pessoas: ')

pesos = []

for n in range(0, 5):
    pesos.insert(n, int(input('-> ')))


menor = pesos[0]
maior = pesos[0]


for i in range(0, 5):
    if pesos[i] > maior:
        maior = pesos[i]

for i in range(0, 5):
    if pesos[i] < menor:
        menor = pesos[i]

print('Dessas 5 pessoas, o maior peso é {}kg e o menor é {}kg.'.format(maior, menor))
