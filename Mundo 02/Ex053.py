# Uniformiza as letras e tira espaços
frase = str(input('Digite uma frase: ')).strip().lower()
palavras = frase.split()
novaFrase = ''.join(palavras)


tamanho = len(novaFrase)
soma = 0


for i in range(0, tamanho):  # percorre a palavra da esquerda para a direita
    for j in range(tamanho-1, -1, -1):  # percorre a palavra da direita para a esquerda
        # Compara as letras da palavras.
        if novaFrase[i] == novaFrase[j] and i + j == tamanho-1:
            soma += 1  # soma 1 unidade se as letras forem iguais

if soma == tamanho:
    print('É UM PALINDROMO')
else:
    print('NÃO É UM PALINDROMO')
