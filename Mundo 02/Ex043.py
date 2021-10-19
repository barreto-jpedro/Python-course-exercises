print('Vamos calcular o seu IMC? ')

altura = float(input('Digite a sua altura: '))
massa = float(input('Digite a sua massa: '))

imc = massa / (altura**2)

imc = round(imc, 2)

if imc <= 18.5:
    print('Você está ABAIXO do seu peso ideal')

elif 18.5 < imc and imc <= 25:
    print('Você está no seu PESO IDEAL')

elif 25 < imc and imc <= 30:
    print('Você está com SOBREPESO')

elif 30 < imc and imc <= 40:
    print('Você está com OBESIDADE')

else:
    print('Você está com OBESIDADE MORBIDA')

print(f'Seu IMC é: {imc}')
