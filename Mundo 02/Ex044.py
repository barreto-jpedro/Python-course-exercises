preco = float(input('Digite o valor do produto: '))

print('[1] - Pagamento a vista DINHEIRO ou CHEQUE\n[2] - Pagamento a vista CARTÃO')
print('[3] - Pagamento 2x no CARTÃO\n[4] - Pagamento 3x ou mais no CARTÃO')

formaDePagamento = int(input('Escolha a forma de pagamento: '))

if formaDePagamento == 1:
    print(f'Com os 10% de desconto, o valor final fica: R${preco * 0.9}')
elif formaDePagamento == 2:
    print(f'Com os 5% de desconto, o valor final fica: R${preco * 0.95}')
elif formaDePagamento == 3:
    print(f'O valor final não muda. Fica: R${preco}')
elif formaDePagamento == 4:
    print(f'Com os 20% de juros, o valor final fica: R${preco * 1.2}')
else: 
    print('#$%¨&* METODO DE PAGAMENTO NÃO DISPONÍVEL! @#$%¨&*')
