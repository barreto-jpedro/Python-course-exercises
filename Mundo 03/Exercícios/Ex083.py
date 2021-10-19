qnt_parenteses_abertos = 0
erro = False

expressao = str(input('Digite uma expressão: ')).strip().lower()

for letra in expressao:
    if letra == '(':
        qnt_parenteses_abertos += 1
    elif letra == ')':
        qnt_parenteses_abertos -= 1
    
    if qnt_parenteses_abertos < 0:
        erro = True
        break

if erro :
    print('\nEXPRESSÃO INVÁLIDA!\n')
else:
    print('\nSem problemas com a expressão digitada!\n')

