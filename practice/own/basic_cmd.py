import os
os.system("clear")

DEFAULT_X = 0

def increase(x):
    print("Valor de x aumentado")
    return x + 1

def decrease(x):
    print("Valor de x disminuido")
    return x - 1

def print_x(x):
    print(f"Valor de x: {x}")

def reset():
    print("Valor de x reseteado")
    return DEFAULT_X

def cmd(x):
    print("-------------------------------")
    print("Bienvenido a Basic CMD")
    print("-------------------------------")

    while True:
        command = input("\n") # Idea: usar **kwargs para obtener parámetros y usar regex para identificar palabras claves

        if command == "inc": x = increase(x)
        elif command == "dec": x = decrease(x)
        elif command == "print": print_x(x)
        elif command == "reset": x = reset()
        elif command == "end": break
        else: print("\nComando no válido, si necesitas ayuda escribe: help")
    
cmd(DEFAULT_X)