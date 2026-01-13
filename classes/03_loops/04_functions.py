###
# 04 - Funciones
# 
# Bloques de código reutilizables y parametrizables para realizar tareas específicas.
###
import os
os.system("clear")

"""
Definición de funciones

def nombre_de_la_funcion(parametro1, parametro2, ...):
    # Docstring opcional
    # Cuerpo de la función
    return valor_de_retorno  # Opcional

"""

print("Función simple:")

def saludar():
    print("¡Hola!")

saludar()

print("\nFunción con parámetros:")

def saludar_a(nombre):
    print(f"¡Hola, {nombre}!")

saludar_a("Ana")
saludar_a("Luis")
saludar_a("María")

# Parámetro es lo que acepta la función
# Argumento es lo que se le pasa a la función

print("\nFunción con múltiples parámetros:")

def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print(f"La suma de 5 y 3 es: {resultado}\n")

# Documentar funciones con docstrings
def restar(a, b):
    """Resta de dos números y devuelve el resultado."""
    return a - b    

# print(restar.__doc__)
# help(restar)

print("Función con parámetros por defecto:")

def multiplicar(a, b=2):
    return a * b

print(multiplicar(3))
print(multiplicar(3, 4))

print("\nArgumentos por posición y por clave:")

def describir_persona(nombre, edad, ciudad):
    print(f"Soy {nombre} tengo {edad} años y vivo en {ciudad}.")

# Los parámetros son posicionales
describir_persona("Carlos", 28, "Madrid")
describir_persona("Barcelona", 22, "Lucía")

# Argumentos por clave
# Parámetros nombrados
describir_persona(edad=30, ciudad="Sevilla", nombre="Ana")

print("\nArgumentos de longitud variable (*args):")

def sumar_numeros(*args):
    suma = 0
    for num in args:
        suma += num

    return suma
 
print(sumar_numeros(1, 2, 3, 4, 5))

print("\nArgumentos de clave-valor variable (**kwargs):")

def mostrar_info(**kwargs):
    print ("\nInformación recibida:")

    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Luis", edad=35, ciudad="Valencia")
mostrar_info(nombre="Marta", profesion="Ingeniera", pais="Argentina", is_rich=True)

### Ejercicios (Cumplido)
#
# Volver a ejercicios anteriores y convertir el código en funciones reutilizables
# e intentar utilizar todos los casos y conceptos aprendidos
# que se han visto
###