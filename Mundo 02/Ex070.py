quer_continuar = 'S'
soma_total = 0
nomes = []
precos = []
indice = 0
produtos_caros = 0
indice_do_menor_preco = 0

print('-'*20, '\nLOJA SUPER BARATO\n', '-'*20)

while quer_continuar == 'S':
    nomes.insert(indice, str(input('Nome do produto: ')).strip())
    precos.insert(indice, float(input('Preço: R$')))

    soma_total += precos[indice]

    if precos[indice] > 1000:
        produtos_caros += 1

    if precos[indice] < precos[indice_do_menor_preco]:
        indice_do_menor_preco = indice

    quer_continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    indice += 1

print(f'O total da compra foi: R${soma_total:.2f}')
print(f'Temos {produtos_caros} produtos custando mais de R$1000,00')
print(
    f'O produto mais barato foi {nomes[indice_do_menor_preco]} que custa R$ {precos[indice_do_menor_preco]:.2f}')
