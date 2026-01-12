###
# 03 - range()
#
# Es un tipo de dato que permite crear una secuencia de números enteros en un rango específico.
# Puede ser úitl para for, pero no solo para eso
###
import os
os.system("clear")

print("\nrange():")

# nums = range(0, 10) # range(inicio, fin, paso)
# print(type(nums)) # <class 'range'>
# print(nums)

# Genera una secuencia de números del 0 al 9
print("\nRango del 0 al 9:")
for num in range(10):
    print(num, end=" ")

# range(inicio, fin)
print("\n\nRango del 5 al 9:")
for num in range(5, 10):
    print(num, end=" ")

# range(inicio, fin, paso)
print("\n\nRango del 0 al 20 con paso de 5:")
for num in range(0, 21, 5):
    print(num, end=" ")

print("\n\nRango del -5 al 0:")
for num in range(-5, 1):
    print(num, end=" ")

print("\n\nRango del 10 al 1 con paso de -1 (decrementar de uno en uno):")
for num in range(10, 0, -1):
    print(num, end=" ")

# Range y list
print("\n\nConvertir un rango a una lista:")
nums = range(5)
list_of_nums = list(nums)

print(list_of_nums)  # Salida: [0, 1, 2, 3, 4]

### Iterar 5 veces algo
# print("\nIterar 5 veces:")
# count = 0

# while count < 5:
#     print("Iteración", count + 1)
#     count += 1

print("\nIterar 5 veces (con range):")

for _ in range(5):
    print("Hacer 5 veces algo")