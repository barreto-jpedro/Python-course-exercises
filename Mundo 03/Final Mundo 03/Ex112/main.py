from utilidadescev import moeda, dado

valor = dado.leiaDinheiro('Digite o preço: ')
tx_aumento = float(input('Qual é a taxa de aumento? (%) '))
tx_reducao = float(input('Qual é a taxa de reducao? (%) '))

moeda.resumo(valor, tx_aumento, tx_reducao)
