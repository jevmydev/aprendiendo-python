###
# 02 - Booleans

# Valores lógicos: True (verdadeiro) and False (falso)
# Fundamentales para el control de flujo y lógica en la programación.
###

import os
os.system("clear")

print("\nValores booleanos básicos:")
print("True:", True)
print("False:", False)

print("\nOperaciones de comparación: (devuelven un valor booleano)")
print("5 > 3:", 5 > 3)        # True (mayor que)
print("2 < 1:", 2 < 1)        # False (menor que)
print("4 == 4:", 4 == 4)      # True (igualdad)
print("3 != 3:", 3 != 3)      # False (desigualdad)
print("6 >= 5:", 6 >= 5)      # True (mayor o igual)
print("2 <= 2:", 2 <= 2)      # True (menor o igual)

print("\nComparación de cadenas:")
print("manzana < pera", "manzana" < "pera")  # True (orden lexicográfico, compara cada caracter según su orden en el alfabeto)
# print("Hola == hola", "Hola" == "hola")  # False (distingue mayúsculas y minúsculas)

print("\nOperadores lógicos:")
print("True and True:", True and True)    # True (ambos deben ser True)
print("True and False:", True and False)  # False (ambos deben ser True)
print("True or False:", True or False)    # True (al menos uno es True)
print("False or False:", False or False)  # False (ninguno es True)
print("not True:", not True)                # False (invierte el valor)
print("not False:", not False)              # True (invierte el valor)

print("\nTablas de verdad")

print("\nAnd:")
print("  A      B      A and B")
print("True   True     ", True and True)
print("True   False    ", True and False)
print("False  True     ", False and True)
print("False  False    ", False and False)

print("\nOr:")
print("  A      B      A or B")
print("True   True     ", True or True)
print("True   False    ", True or False)
print("False  True     ", False or True)
print("False  False    ", False or False)

print("\nNot:")
print("  A     not A")
print("True   ", not True)
print("False  ", not False)

#number = 5
#if number:
#    print("Recordar que solo sí el número es 0, se evalúa como False.")
#    print("Cualquier otro número se evalúa como True.")

#name = "Python"
#if name:
#    print("\nRecordar que una cadena vacía ('') se evalúa como False.")
#    print("Cualquier otra cadena con contenido se evalúa como True.")