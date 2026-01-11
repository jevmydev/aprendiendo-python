# ###
# # EJERCICIOS (while)
# ###
# import os
# os.system("clear")

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("\nEjercicio 1:")
count = 10

while count >= 1:
    print(count)
    count -= 1

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")

count = 0
sum = 0

while count <= 20:
    count += 1

    if count % 2 == 0:
        sum += count

print(f"La suma es: {sum}")

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3:")

num = int(input("Introduce un número entero positivo: "))
count = num
factorial = 1

while count != 1:
    factorial = factorial * count
    count -= 1

print(f"El factorial de {num} es: {factorial}")

# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4:")

while True:
    password = input("Introduce una contraseña válida (al menos 8 caracteres): ")
    lenght = len(password)

    if lenght >= 8:
        print("Contraseña válida")
        break
    else:
        print("Debes introducir una contraseña válida") 

# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5:")

num = int(input("Introduce un número entero: "))
count = 1

print(f"Tabla de multiplicar del {num}")
while count <= 10:
    res = num * count

    print(f"{num} x {count} = {res}")
    count += 1 

# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
print("\nEjercicio 6:")

num = int(input("Introduce un número entero positivo: "))
count = num
prime_numbers: list[int] = []

while count > 1:
    is_number_prime = True
    if count < 2:
        is_number_prime = False
    
    iterator = 2
    while iterator < (count - 1):
        if (count % iterator == 0):
            is_number_prime = False
            break
        
        iterator += 1
    
    if is_number_prime:
        prime_numbers.append(count)

    count -= 1
    

prime_numbers.sort()
print(f"El número {num} tiene los siguientes números primos: {prime_numbers}")