### 
# 05 - Input

# Entrada del usuario (input()) - Versión simplificada
# Permite al usuario ingresar datos en la consola
###

# print("¿Cómo te llamas?")
# nombre = input()  # Captura la entrada del usuario

nombre = input("¿Cómo te llamas? ") # Espacio al final o salto de línea, para no dejar el texto pegado

print(f"Hola {nombre}, ¡bienvenido al mundo de Python!\n")
age = input("¿Cuántos años tienes? ") # Esto es una cadena de texto
age = int(age)
print(f"En 20 años más tendrás {age + 20} años.\n")

country, city = input("¿En qué ciudad y país vives? ").split()  # Divide la entrada en espacios
print(f"Vives en {city}, que está en {country}\n")