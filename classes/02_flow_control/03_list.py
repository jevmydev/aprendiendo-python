###
# 03 - List

# Secuencia mutable de elementos
# Pueden contener elementos de diferentes tipos
###
import os
os.system("clear")

# Crear listas
print("Crear listas")
list_1 = [1, 2, 3, 4, 5] # Lista de enteros
list_2 = ["manzanas", "pera", "plátano"] # Lista de cadenas
list_3: list[int | str | float | bool] = [1, "b", 3.5, True] # Lista de tipos mixtos. Opcional el "tipeado"

list_4 = [] # Lista vacía
list_of_list = [[1, 2], [3, 4], [5, 6]] # Lista de listas
matrix = [[1, 2], [2, 3], [4, 5]] # Matriz (lista de listas)

print(list_1)
print(list_2)
print(list_3)
# print(list_4)
print(list_of_list)
print(matrix)

# Acceso a elementos por índice

print("\nAcceso a elementos por índice")
print(list_2[0]) # "a" = lust_[-3]
print(list_2[1]) # "b" = list_[-2]
print(list_2[-1]) # "c" (último elemento, cuenta del final hacia el inicio)

print(list_of_list[1][0]) # 3 (primer elemento de la segunda lista)

# Slicing (rebanado) de listas

print("\nSlicing de listas")

print(list_1[1:4]) # [2, 3, 4]
print(list_1[:3]) # [1, 2, 3]
print(list_1[3:]) # [4, 5]

print(list_1[:]) # Copia de la misma lista

list_1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(list_1[::2]) # list_1[desde:hasta:paso (cada cuanto cuenta)]
print(list_1[::-1]) # Invierte la lista (pasos al revés)

# Modificar una lista
print("\nModificando lista")

list_1[0] = 9
print(list_1)

# Añadir elementos
print("\nAñadir elementos a la lista")

# Forma larga y menos eficiente
list_1 = [1, 2, 3]
list_1 = list_1 + [4, 5, 6]
print(list_1)

# Forma más corta y más eficiente
list_1 += [7, 8, 9]
print(list_1)

# Recuperar longitud de una lista
print("\nLongitud de la lista:", len(list_1))