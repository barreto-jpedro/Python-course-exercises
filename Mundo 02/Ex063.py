n_de_termos = int(input(('Quantos termos você quer ver? ')))

n = 2

termo_geral = 1
anterior = 1
aux = 1

print('0 -> 1 -> ', end='')

while n != n_de_termos:
    print(f'{termo_geral} -> ', end='')
    aux = termo_geral
    termo_geral += anterior
    anterior = aux
    n += 1
        
print('FIM')
    
