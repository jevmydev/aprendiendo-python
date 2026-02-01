import os
import re

os.system("clear")

states = {}

def print_help():
    print()
    print("Comandos disponibles:")
    print("---------------------")
    print(" help        - Muestra esta ayuda")
    print(" echo txt    - Imprime un texto en pantalla")
    print(" clear       - Limpia la pantalla y el estado")
    print(" exit        - Finaliza la consola")
    print()
    print("Utilidades:")
    print(" add a b     - Suma dos números")
    print(" sub a b     - Resta dos números")
    print(" mul a b     - Multiplica dos números")
    print(" div a b     - Divide dos números")
    print()
    print("Estado:")
    print(" set k v     - Guarda una variable")
    print(" get k       - Obtiene el valor de una variable")
    print(" vars        - Lista las variables guardadas")
    print()

def clear():
    os.system("clear")
    states.clear()

    print("Consola y estado limpiados correctamente.")

def echo(command):
    pattern = r"^(echo )"
    text = re.sub(pattern, "", command, flags=re.IGNORECASE)

    print(text)

def calculator(command):
    prompt = command.split(" ")
    operation, num1, num2 = prompt

    try:
        num1 = float(num1)
        num2 = float(num2)

        if operation == "add": print(f"La suma de {num1} y {num2} es: {num1 + num2}")
        elif operation == "sub": print(f"La resta de {num1} y {num2} es: {num1 - num2}")
        elif operation == "mul": print(f"La multiplicación de {num1} y {num2} es: {num1 * num2}")
        elif operation == "div": 
            if num2 == 0: raise ZeroDivisionError("No se puede dividir entre 0.")
            
            print(f"La división de {num1} y {num2} es: {num1 / num2}")

    except ValueError:
        raise ValueError("No es posible realizar la operación con esos valores. Vuelve a intentarlo.")

def state(command):
    prompt = command.split()
    operation = prompt[0].lower()

    if operation == "set":
        key = prompt[1]
        value = prompt[2]

        states[key] = value
        print(f"Variable '{key}' guardada con valor '{value}'.")
    elif operation == "get":
        key = prompt[1]

        if key in states:
            print(f"{key} = {states[key]}")
        else:
            print(f"La variable '{key}' no existe.")
    elif operation == "vars":
        if not states:
            print("No hay variables guardadas.")
        else:
            for key, value in states.items():
                print(f"{key} = {value}")

def interpreter(command):
    parse_command = command.lower().strip()

    pattern_calculator = r"^(add|sub|mul|div) -?\d+(\.\d+)? -?\d+(\.\d+)?$"
    is_calculator_command = re.match(pattern_calculator, parse_command)

    pattern_state = r"^(set \w+ \w+|get \w+|vars)$"
    is_state_command = re.match(pattern_state, parse_command)

    # Basic comands
    if parse_command == "help": print_help()
    elif parse_command.startswith("echo "): echo(command)
    elif parse_command == "clear": clear()
    elif parse_command == "exit": exit()
    # Calculator
    elif is_calculator_command: calculator(parse_command) 
    # State
    elif is_state_command: state(command)
    # Error
    else: raise SyntaxError("El comando escrito no es válido. Vuelve a intentarlo.")

def cmd():
    print("=====================================")
    print("              BASIC CMD              ")
    print("=====================================")
    print()
    print("Bienvenido a la consola interactiva.")
    print("Escribe un comando y presiona Enter.")
    print()
    print("Comandos básicos:")
    print("  help     - Mostrar lista de comandos")
    print("  exit     - Salir de la consola")
    print()
    print("Consejo: escribe 'help' para comenzar.")
    print("------------------------------------")

    while True:
        try:
            command = input("\n>> ")
            interpreter(command)
        except Exception as err:
            print(err)

cmd()