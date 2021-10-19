def leiaInt():
    while True:
        try:
            inteiro = int(input('Digite um número inteiro: '))
        except (ValueError, TypeError):
            print(f'\033[31mErro. Digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print(f'\033[31mUsuário não digitou valor.\033[m')
            return 0
        else:
            return inteiro


def leiaFloat():
    while True:
        try:
            real = float(input('Digite um número real: '))
        except (ValueError, TypeError):
            print(f'\033[31mErro. Digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print(f'\033[31mUsuário não digitou valor.\033[m')
            return 0
        else:
            return real


print(f'O número inteiro digitado foi {leiaInt()} e o real foi {leiaFloat()}')