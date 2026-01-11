###
# 02 - Bucles for
# 
# Un bucle for se utiliza para iterar sobre una secuencia (como una lista, una tupla, un diccionario, un conjunto o una cadena).
###
import os
os.system("clear")

print("\nBucle for:")

# Iterar sobre una lista
fruits = ["manzana", "banana", "cereza", "durazno"]

for fruit in fruits:
    print(fruit)

# Iterar sobre cualquier secuencia
print("\nIterar sobre una cadena:")
text = "Hola"
for char in text:
    print(char)

# enumerate()
print("\nUso de enumerate:")

for index, fruit in enumerate(fruits):
    print(f"Índice {index}: {fruit}")

# Bucles anidados
print("\nBucle for anidado:")

letters = ['a', 'b', 'c']
numbers  = [1, 2, 3]

for letter in letters:
    for number in numbers:
        print(f"{letter}{number}")

# Break
print("\nUso de break:")
animals = ["perro", "gato", "pez", "pájaro", "hamster", "conejo"]

for i, animal in enumerate(animals):
    if animal == "pájaro":
        print(f"Índice de pájaro: {i}")
        break

# Continue
print("\nUso de continue:")
for animal in animals:
    if animal == "pájaro": continue

    print(animal)

# Comprensión de listas (List Comprehension)
print("\nComprensión de listas:")
animals = ["perro", "gato", "pez", "pájaro", "hamster", "conejo"]

animals_upper = [animal.upper() for animal in animals]
print(animals_upper)

# Muestra los números pares de un lista
print("\nMuestra los números pares de un lista")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

par_numbers = [num for num in numbers if num % 2 == 0]
print(par_numbers)