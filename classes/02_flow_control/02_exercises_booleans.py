import os
os.system("clear")

###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

### Solución ###
def compare_nums(num_1, num_2):
    if num_1 > num_2:
            print(f"El número {num_1} es mayor que el {num_2}")
    elif num_1 < num_2:
        print(f"El número {num_1} es menor que el {num_2}")
    else:
        print("Los números son iguales")

while True:
    try:
        num_1 = input("Escribe un número: ",)
        num_1 = float(num_1)

        num_2 = input("Escribe un segundo número: ")
        num_2 = float(num_2)

        compare_nums(num_1, num_2)
        break;
    except ValueError: 
        print("No puedes escribir letras o símbolos. Vuelve a intentarlo")
## Solución ###

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

## Solución ###
while True: 
    try:
        res = None

        num_1 = input("Escribe un número: ")
        num_1 = float(num_1)

        num_2 = input("Escribe otro número: ")
        num_2 = float(num_2)

        operation = input("Escribe una operación (+, -, * o /): ")

        if num_2 == 0 and operation == "/":
            raise ValueError("No se puede dividir entre 0")

        if operation == "+":
            res = num_1 + num_2
        elif operation == "-":
            res = num_1 - num_2
        elif operation == "*":
            res = num_1 * num_2
        elif operation == "/":
            res = num_1 / num_2
        else:
            raise ValueError("La operación no es válida")

        print(f"Tu operación {num_1} {operation} {num_2} es igual a {res}")
        break
    except ValueError as e:
        print(e)
## Solución ###

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

## Solución ###
year = input("Ingresa un año para determinar si es bisiesto: ")
year = int(year)

is_leap_year = year % 4 == 0

if (year % 100 == 0) and (year % 400 != 0):
    is_leap_year = False

print(f"El año {year} es bisiesto") if is_leap_year else print(f"El año {year} no es bisiesto")
## Solución ###

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

## Solución ###
try:
    age = input("Introduce una edad: ")
    age = int(age)

    if age >= 0 and age <= 2:
        print(f"Con {age} años, es un bebé")
    elif age >= 3 and age <= 12:
        print(f"Con {age} años, es un niño")
    elif age >= 13 and age <= 17:
        print(f"Con {age} años, es un adolescente")
    elif age >= 18 and age <= 64:
        print(f"Con {age} años, es un adulto")
    elif age >= 65:
        print(f"Con {age} años, es un adulto mayor")
    else:
        print("La edad no es válida")
except:
    print("La edad no es válida")
### Solución ###