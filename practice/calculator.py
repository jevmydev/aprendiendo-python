import os
os.system("clear")

### Calculadora simple (propuesto con ChatGPT) ###

# Permite al usuario elegir una operación aritmética (suma, resta,
# multiplicación o división), ingresar los valores y obtener el resultado.
# El programa valida entradas incorrectas, maneja la división por cero
# y se ejecuta en un bucle hasta que el usuario decide salir.

###

print("\n-------------------------------------")
print("Bienvenido a la calculadora simple")
print("-------------------------------------")

def choice_two_numbers():
    return

def calculator_menu():
    print("\nMenú")
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Multiplicar dos números")
    print("4. Dividir dos números")

    option = input("\nElige una opción: ")

    if option not in ("1", "2", "3", "4"): 
        print("\nOpción no válida. Vuelve a intentarlo")
        calculator_menu()

    choice_two_numbers()

calculator_menu()