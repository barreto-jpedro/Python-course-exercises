alunos = list()
dados = list()
continuar = 'S'


while continuar == 'S':
    dados.append(input('Nome: '))
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))

    alunos.append(dados[:])
    dados.clear()

    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()


print('-='*25)
print(f'{"nº":<4}', f'{"NOME":<20}', f'{"MÉDIA":>8}')
print('-'*40)

for n in range(0, len(alunos)):
    print(f'{n:<4}{alunos[n][0]:<20}{(alunos[n][1] + alunos[n][2])/2 :>8}')



while True:
    indice = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if indice == 999:
        break
    print(f'Notas de {alunos[indice][0]} são: {alunos[indice][1:]}')

print('FIM DO PROGRAMA')
