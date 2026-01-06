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
list_2 = ["a", "b", "c"] # Lista de cadenas
list_3: list[int | str | float | bool] = [1, "b", 3.5, True] # Lista de tipos mixtos. Opcional el "tipeado"

list_4 = [] # Lista vacía
list_of_list = [[1, 2], [3, 4], [5, 6]] # Lista de listas
matrix = [[1, 2], [2, 3], [4, 5]] # Matriz (lista de listas)

print(list_1)
print(list_2)
print(list_3)
print(list_4)
print(list_of_list)
print(matrix)

# Acceso a elementos por índice

print("\nAcceso a elementos por índice")
print(list_2[0]) # "a" = lust_[-3]
print(list_2[1]) # "b" = list_[-2]
print(list_2[-1]) # "c" (último elemento, cuenta del final hacia el inicio)

print(list_of_list[1][0]) # 3 (primer elemento de la segunda lista)