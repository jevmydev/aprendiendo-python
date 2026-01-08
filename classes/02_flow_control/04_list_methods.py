###
# 04 - List methods

# Métodos más importantes para trabajar con listas

# Diferencia entre métodos y funciones: 
# Los métodos son funciones que "pertenecen" a un tipo de dato concreto (en este caso, las listas)
# Los métodos se llaman usando la sintaxis: nombre_lista.metodo()
# Las funciones son independientes del tipo de dato y se llaman usando la sintaxis: funcion(argumentos)
###
import os
os.system("clear")

# Añadir o insertar elemento/s a la lista
print("\nAñadir o insertar elemento/s a la lista")

list_1 = [1, 2, 3, 4, 5]
list_1.append(6) # Añade un elemento al final de una lista

print(list_1)

list_1 = ["a", "b", "c", "d", "e", "@", "@"]
list_1.insert(1, "@") # Inserta el "@" en la posición 1 (recordar que siempre empezamos desde el 0)

print(list_1)

list_1.extend(["f", "g", "h"]) # Añade múltiples elementos al final de la lista
print(list_1)

# Eliminar elemento/s a la lista
print("\nEliminar elemento/s a la lista")

list_1.remove("@") # Elimina la primera aparición del elemento "@"
print(list_1)

last = list_1.pop() # Elimina el último de la lista y lo devuelve
list_1.pop(1) # Elimina el indice que indicamos y lo devuelve

print(last, list_1)

# Eliminar de locos
del list_1[-1]
print(list_1)

# Eliminar todos los elementos
list_1.clear()
print(list_1)

# Eliminar un rango
list_1 = ["🎉", "❤️", "✨", "🐍", "👉", "🎯"]
del list_1[4:6]
print(list_1)

# Ordenar listas
print("\nOrdenar listas modificando la original")
numbers = [3, 10, 5, 2, 999, -4]
numbers.sort()
print(numbers)

print("\nOrdenar listas creando una nueva lista")
numbers = [3, 10, 5, 2, 999, -4]
sorted_numbers = sorted(numbers) # Ordenada
print(numbers) # Desordenada
print(sorted_numbers)

print("\nOrdenar listas de cadenas de texto (todo minúscula)")
frutas = ["manzana", "pera", "manzana", "kiwi", "pera", "arándanos"] 
sorted_fruits = sorted(frutas)
print(sorted_fruits)

print("\nOrdenar listas de cadenas de texto (mezcla mayúsculas y minúscula)")
frutas = ["manzana", "pera", "MANZANA", "kiwi", "Pera", "arándanos"] 
frutas.sort(key=str.lower)
print(frutas)

# Otros métodos y operadores útiles
animals = ["🐶", "😺", "🐒", "😺", "🦍", "🦊"]
print("\nOtros métodos útiles")
print(len(animals)) # Tamaño de la lista -> 5
print(animals.count("😺")) # Cuenta coincidencias -> 2
print("😺" in animals) # Comprueba si hay "😺" en la lista, devuelve booleano -> True
print("🦁" in animals) # -> False