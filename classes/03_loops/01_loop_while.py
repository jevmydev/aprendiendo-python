###
# 01 - Bucles while

# Permite ejecutar un bloque de código repetidamente mientras se cumple una condición
###
import os
os.system("clear")

print("\nBucle while")

# Bucle con una simple condición
contador = 0

while contador < 5: 
    contador += 1 # Super importante para evitar bucles infinitos
    print(contador)

# Utilizamos la palabra "break", para romper el bucle
print("\nBucle while con 'break'")

contador = 0
while True:
    contador += 1
    print(contador)

    if contador == 5:
        break

# Utilizamos la palabra "continue", para saltar una iteración específica
print("\nUsando bucle while con 'continue'")

contador = 0
while contador < 10:
    contador += 1
    if contador % 2 == 0: continue

    print(contador)

# El else, se utiliza cuando la condición del bucle se termina
print("\nUsando bucle while con 'else' cuando el bucle termina")

contador = 0

while contador < 5:
    contador += 1
    print(contador)
else:
    print("El bucle ha terminado")

# El else no se ejecuta solo en un caso, cuando el bucle para por el "break" 
print("\nCaso donde no se ejecuta el else: ")
contador = 0

while contador < 5:
    contador += 1
    print(contador)

    if contador == 2: break
else:
    print("El bucle ha terminado")

# Ejercicio práctico: pedirle al usuario un número que debe ser positivo

num = 0
while num <= 0:
    try:
        num = int(input("\nIngresa un número positivo para salir del bucle: "))

        if num <= 0:
            print("Oye! El número debe ser positivo, intenta de nuevo")
    except:
        print("Debes poner un número, sino explota el programa!")

print(f"Gracias! Has ingresado el número positivo: {num}")