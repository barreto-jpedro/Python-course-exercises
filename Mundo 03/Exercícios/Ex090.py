alunos = dict()


alunos['nome'] = input('Nome: ')
alunos['media'] = int(input('Média: '))

if alunos['media'] >= 6:
    alunos['situação'] = 'Aprovado'
else:
    alunos['situação'] = 'Reprovado'


print('-='*20)
for k, v in alunos.items():
    print(f'\t- {k} é igual a {v}')

print()
