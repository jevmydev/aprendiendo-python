###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
if system("clear") != 0: system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí
print("Soy Jeremy Díaz")
print("Vivo en Santiago de Chile")

print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí

def print_types(*data):
    for var in data:
        print(type(var))

print_types(a, b, c, d, e)

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí

print(int("12345"))
print(float("12345"))
print(int(3.99)) # Trunca el número (3)

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

### Completa aquí

def describe_person(**info):
    for adjective, value in info.items():
        print(f"Mi {adjective} es {value}")

name = "Jeremy Díaz"
age = 18
height = 1.70

describe_person(nombre=name, edad = age, altura = height)

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

result = int(round(3.1416) / 2) 

print("Valor aproximado de PI:", 3.1416)
print("Valor redondeado de PI:", round(3.1416))
print("Valor redondeado de PI / 2, de forma entera:", result)
