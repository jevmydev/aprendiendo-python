###
# 01 - Expresiones regulares

# Las expresiones regulares son una secuencia de caracteres que forman un patrón de búsqueda.
# Se utilizan principalmente para la búsqueda de patrones en cadenas de texto y para la manipulación de texto.

# ¿Por qué aprender Regex?

# - Búsqueda avanzada: Encontrar patrones específicos en grandes volúmenes de texto.
# - Validación de datos: Verificar formatos como correos electrónicos, números de teléfono, etc.
# - Manipulación de texto: Reemplazar, dividir o extraer partes de cadenas de texto.
###
import os
os.system("clear")

# 1. Importar módulo de expresiones regulares (re)
import re

# 2. Crear un patrón, que es una cadena de texto que describe lo que queremos encontrar
pattern = "Hola"

# 3. El texto donde queremos buscar
text = "Hola, ¿cómo estás? Hola de nuevo."

# 4. Usar la función de búsqueda de "re"
result = re.search(pattern, text)

if result:
    print("\nPatrón encontrado")
else:
    print("\nPatrón no encontrado.")

# .group() devuelve la parte de la cadena que coincide con el patrón
print("Coincidencia:", result.group()) # type: ignore

# .start() devuelve el índice donde comienza la coincidencia
print("Inicio:", result.start()) # type: ignore

# .end() devuelve el índice donde termina la coincidencia
print("Fin:", result.end()) # type: ignore

# EJERCICIO 01
# Encuentra la primera ocurrencia de la palabra "IA" en el siguiente texto
# e indica en que posición empieza y termina la coincidencia.
text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero solo hace falta ver cómo la puede cagar con las Regex para ir con cuidado"

pattern = "IA"
found_ia = re.search(pattern, text)

if found_ia:
    print("\nPatrón encontrado")
    print("Inicio:", found_ia.start())
    print("Final:", found_ia.end())
else:
    print("\nPatrón no encontrado")

# -----------------------------------

# Encontrar todas las ocurrencias de un patrón en un texto
text = "Me gusta Pyhhon. Python es lo máximo. Aunque Python no es tan difícil, ojo con Python"
pattern = "Py.hon" # El punto (.) representa cualquier carácter. Algo como PyXhon, PyZhon, Py1hon, etc.

matches = re.findall(pattern, text)
print(f"\nTodas las coincidencias de {pattern}:", matches)
print("Número de coincidencias:", len(matches))

# -----------------------------------

# iter() devuelve un iterador con todas las coincidencias encontradas
text = "Me gusta Pyhhon. Python es lo máximo. Aunque Python no es tan difícil, ojo con Python"
pattern = "Py.hon" 

matches = re.finditer(pattern, text) # Devuelve un iterador

for match in matches:
    print(match.group(), "encontrado en la posición", match.start(), "-", match.end())

print()

# EJERCICIO 02
# Encuentra todas las ocurrencias de la palabra "midu" en el siguiente texto e indica en que posición empieza y termina cada coincidencia y cuantas veces se encontró.
text = "Este es el curso de Python de midudev. ¡Suscríbete a midudev si te gusta este contenido! midu"
pattern = "midu"

matches = re.finditer(pattern, text)
count_of_coincidences = len(re.findall(pattern, text))

for match in matches:
    coincidence = match.group()
    start = match.start()
    end = match.end()

    print(f"Se encontró la coincidencia: {coincidence}, en la posición: {start} - {end}")

print(f"Cantidad de coincidencias totales: {count_of_coincidences}")
print()

# -----------------------------------

# Modifadores, son opciones que se pueden agregar a un patrón para cambiar su comportamiento
# re.IGNORECASE: Ignora mayúsculas y minúsculas

text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero de todas maneras, la ia es el futuro, y la Ia es increíble."

pattern = "IA"
found = re.findall(pattern, text, re.IGNORECASE)

if found:
    print(found)

print()

# EJERCICIO 03
# Encuentra todas las ocurrencias de la palabra "python" en el siguiente texto, sin distinguir entre mayúsculas y minúsculas.

text = "Este es el curso de Python de midudev. ¡Suscríbete a python si te gusta este contenido! PYTHON"
pattern = "python"

found = re.findall(pattern, text, re.IGNORECASE)
print(found)