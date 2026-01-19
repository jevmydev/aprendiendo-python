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

options = {
    "1": "+",
    "2": "-",
    "3": "x",
    "4": "/"
}

def sum_numbers(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError
    
    return a / b

def restart_calculator():
    while True:
        is_continue = input("\n¿Deseas realizar otra operación? (s/n): ").lower()
        
        if is_continue == "s":
            calculator_menu()
        elif is_continue == "n":
            print("\nGracias por usar la calculadora. ¡Hasta luego!") 
            exit() 
        else:
            print("\nOpción no válida. Vuelve a intentarlo")

def choice_two_numbers(option):
    try:
        num1 = float(input("\nDigite el primer número: "))
        num2 = float(input("Digite el segundo número: "))

        result = None
        
        if option == "1": result = sum_numbers(num1, num2)
        elif option == "2": result = subtract(num1, num2)
        elif option == "3": result = multiply(num1, num2)
        elif option == "4": result = divide(num1, num2)

        print(f"\nEl resultado de {num1} {options[option]} {num2} es: {result}")
        restart_calculator()
        
    except ValueError:
        print("\nDebes escribir un número válido. Vuelve a intentar")
        choice_two_numbers(option)
    except ZeroDivisionError:
        print("\nNo se puede dividir entre cero. Vuelve a intentar")
        choice_two_numbers(option)

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

    choice_two_numbers(option)

calculator_menu()