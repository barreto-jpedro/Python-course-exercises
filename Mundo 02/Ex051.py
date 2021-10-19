print('Vamos calcular a soma dos 10 primeiros termos de uma PA. ')

razao = int(input('Qual é a razão PA? '))
primeiro_termo = int(input('Qual é o primeiro termo? '))
soma = 0
decimo = primeiro_termo + (9 * razao)

for primeiro_termo in range(primeiro_termo, decimo + razao, razao):
    print(f'{primeiro_termo}', end=' -> ')
    soma += primeiro_termo

print('A soma da sua PA é: {}'. format(soma))
