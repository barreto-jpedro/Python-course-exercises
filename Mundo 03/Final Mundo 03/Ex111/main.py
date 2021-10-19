from utilidadescev import moeda

valor = float(input(f'Digite o valor: R$'))
tx_aumento = float(input('Qual é a taxa de aumento? (%) '))
tx_reducao = float(input('Qual é a taxa de reducao? (%) '))

moeda.resumo(valor, tx_aumento, tx_reducao)
