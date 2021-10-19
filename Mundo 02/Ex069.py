quer_continuar = 'S'
sum_mulheres_jovens = 0
sum_homens = 0
sum_adultos = 0

print('\nCADASTRE UMA PESSOA\n')

while quer_continuar == 'S':
    idade = int(input('\nIdade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()
    
    if idade > 18:
        sum_adultos += 1
    
    if sexo == 'M':
        sum_homens += 1

    if (sexo == 'F') and (idade < 20):
        sum_mulheres_jovens += 1

    quer_continuar = str(input('Quer continuar? [S/N] ')).strip().upper()

print(f'Total de pessoas com mais de 18 anos: {sum_adultos}')
print(f'Ao todo temos {sum_homens} homens cadastrados.')
print(f'E temos {sum_mulheres_jovens} mulheres com menos de 20 anos.')



