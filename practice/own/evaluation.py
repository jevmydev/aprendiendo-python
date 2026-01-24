import os
os.system("clear")

# Evaluación: Programación en Python (Práctica)
#
# Nivel: Primer año universitario
# Duración: 90 minutos
# Puntaje total: 100 puntos
# Lenguaje: Python 3
#
# Instrucciones generales
#
# Escriba código claro, correctamente indentado y funcional.
# Cada ejercicio es independiente.
# No se permite el uso de librerías externas.
# No use Programación Orientada a Objetos.
# Se evaluará principalmente la lógica, no solo que el código “corra”.
#
# --------------------------------------------------
# Ejercicio 1 – Función básica (15 pts)
#
# Implemente una función llamada es_par(n) que:
# - Reciba un número entero n
# - Retorne True si el número es par, False en caso contrario
#
# --------------------------------------------------
# Ejercicio 2 – Uso de ciclos (15 pts)
#
# Escriba una función suma_hasta(n) que:
# - Reciba un entero positivo n
# - Retorne la suma de todos los números desde 1 hasta n
#
# Ejemplo:
# suma_hasta(5)  # retorna 15
#
# --------------------------------------------------
# Ejercicio 3 – Manejo de listas (20 pts)
#
# Implemente una función mayor_de_lista(lista) que:
# - Reciba una lista de números enteros
# - Retorne el mayor elemento de la lista
# - No puede usar la función max()
#
# --------------------------------------------------
# Ejercicio 4 – Listas y condicionales (20 pts)
#
# Implemente una función filtrar_positivos(lista) que:
# - Reciba una lista de enteros
# - Retorne una nueva lista con solo los números mayores que 0
# - Mantenga el orden original
#
# Ejemplo:
# filtrar_positivos([-3, 5, 0, 2, -1])  # retorna [5, 2]
#
# --------------------------------------------------
# Ejercicio 5 – Programa completo (30 pts)
#
# Desarrolle un programa que:
# 1. Pida al usuario cuántos números ingresará
# 2. Lea esa cantidad de números enteros
# 3. Guarde los números en una lista
# 4. Muestre por pantalla:
#    - La suma total
#    - El promedio
#    - La cantidad de números pares
#    - El mayor número ingresado
#
# Restricciones:
# - No usar funciones predefinidas que resuelvan directamente el problema
#   (sum, max, etc.)
# - El programa debe funcionar correctamente para cualquier cantidad ≥ 1
###

# Ejercicio 1 – Función básica (15 pts)
def es_par(n):
    return n % 2 == 0

# Ejercicio 2 – Uso de ciclos (15 pts)
def suma_hasta(n):
    suma = 0
    for sumandos in range(n + 1): # Debe ser range(n + 1) para incluir el valor "n"
        suma += sumandos
    
    return suma

# Ejercicio 3 – Manejo de listas (20 pts)
def mayor_de_lista(lista):
    max_num = None

    for num in lista:
        if max_num == None:
            max_num = num
            
        if num > max_num:
            max_num = num

    return max_num

# Ejercicio 4 – Listas y condicionales (20 pts)
def filtrar_positivos(lista):
    lista_de_positivos = []

    for num in lista:
        if num > 0:
            lista_de_positivos.append(num)
    
    return lista_de_positivos

# Ejercicio 5 – Programa completo (30 pts)
def calcular_suma(numeros):
    suma = 0
    for num in numeros:
        suma += num
    return suma

def cantidad_pares(numeros):
    cantidad = 0
    for num in numeros:
        if num % 2 == 0:
            cantidad += 1
    return cantidad

numeros = []
cantidad_iteraciones = int(input("Ingresa la cantidad de números que deseas: "))

for i in range(cantidad_iteraciones):
    num = int(input(f"Ingresa el número {i + 1}°: "))
    numeros.append(num)

suma_total = calcular_suma(numeros)
promedio = suma_total / len(numeros)
cantidad_par = cantidad_pares(numeros)
numero_max = mayor_de_lista(numeros)

print("\nResultados:")
print(f"Suma total: {suma_total}")
print(f"Promedio: {promedio}")
print(f"Cantidad de números pares: {cantidad_par}")
print(f"Mayor número ingresado: {numero_max}")