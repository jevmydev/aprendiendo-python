###
# EJERCICIOS (for)
###
import os
os.system("clear")

# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
print("\nEjercicio 1:")

range_par_nums = range(2, 21, 2)
par_nums = list(range_par_nums)

for num in par_nums:
    print(num, end = " ")

# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.
print("\n\nEjercicio 2:")

numbers = [10, 20, 30, 40, 50]
sum = 0

for num in numbers:
    sum += num

average = sum / len(numbers)
print(average)

# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.
print("\nEjercicio 3:")

def compare_numbers(num, compare_num):
    """Esta función compara un número con una lista de números, verificando si es el mayor o no. Retorna True, en caso de ser el mayor y False en caso contrario."""
    for compare_num in numbers:
        if num < compare_num:
            return False
        
    return True

numbers = [15, 5, 25, 10, 20]
for num in numbers:
    is_max_number = compare_numbers(num=num, compare_num=numbers)

    if is_max_number:
        print(f"El número máximo es {num}")
        break

# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
print("\nEjercicio 4:")

words = ["casa", "arbol", "sol", "elefante", "luna"]
filter_words = [word for word in words if len(word) > 5]

print(filter_words)

# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
print("\nEjercicio 5:")

words = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
user_letter = input("Introduce una letra: ").lower()

count_coincidence = 0

for word in words:
    is_first_letter_match = word.startswith(user_letter)
    
    if is_first_letter_match:
        count_coincidence += 1

if count_coincidence == 1:
    print(f"Existe {count_coincidence} palabra que empieza por la letra {user_letter}")
else:
    print(f"Existen {count_coincidence} palabras que empiezan por la letra {user_letter}")
