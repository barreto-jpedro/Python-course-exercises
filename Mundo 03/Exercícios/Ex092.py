from datetime import datetime
dados = dict()

dados['nome'] = input('Nome: ')
dados['idade'] = datetime.now().year - int(input('Ano de nascimento: '))
dados['ctps'] = int(input('Carteira de trabalho: (0 não tem) '))

if dados['ctps'] != 0: 
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: '))

print('-='*20)
for k, v in dados.items():
    print(f'\t- {k} tem o valor {v}')

print()
