fVerde, fAzul, fRoxo = "\033[1;30;42m", "\033[1;30;44m", "\033[1;30;45m"
normal = "\033[m"



def ajuda():
    while True:
        # Título
        print(fVerde, end="")
        print("~" * 30)
        print(" Sistema de ajuda para Python")
        print("~" * 30)
        print(normal)

        # Input
        comando = str(input("Comando ou biblioteca ('fim' para): "))

        # Condição de parada
        if comando.lower() == "fim":
            print(fRoxo, end="")
            print("~" * 16)
            print(" Até a próxima!")
            print("~" * 16)
            print(normal)
            break

        # Ajuda
        print(fAzul, end="")
        print(help(comando))
        print(normal)


ajuda()