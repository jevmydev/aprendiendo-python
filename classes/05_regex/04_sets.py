###
# 03 - Sets

# Los sets son conjuntos que definen una lista de caracteres permitidos para una sola posición en una búsqueda de texto.
###
import os
import re

os.system("clear")

# [: Coincide con cualquier caracter dentro de los corchetes
username = "rub.$ius_69+"
pattern = r"^[\w._+-]+$"

match = re.search(pattern, username)

if match: print("Nombre de usuario válido: ", match.group())
else: print("Nombre de usuario inválido")

# Ejercicio:
# Buscar todas las vocales de una palabra
print()

text = "Hola mundo"
pattern = r"[aeiou]"

matches = re.findall(pattern, text)
print(matches)

# Ejercicio:
# Usa regex para encontrar las palabras man, fan y ban
# Pero ignora el resto
print()

text = "man fan ñan"
pattern = r"[mfb]an"

matches = re.findall(pattern, text)
print(matches)

# Ejercicio:
# Se nos complicó el asunto, resulta que hay palabras que encajan, pero no empiezan por esas letras.
# Solo buscamos las palabras man, fan y ban (no omniman)
print()

text = "omniman fantástico man fan bandana"
pattern = r"\b[mfb]an\b"

matches = re.findall(pattern, text)
print(matches)

# ---------------------------------------------
print()

text = "22"
pattern = r"[1-2]"

matches = re.findall(pattern, text)
print(matches)

# ---------------------------------------------
r"[a-z]"
r"[A-Za-z0-9áéíóúñàèìòù]+"

# ---------------------------------------------
print()

# [^]: Coincide con cualquier caracter que NO esté dentro de los corchetes
text = "Hola mundo"
pattern = r"[^aeiou]" # Que no sea vocal

matches = re.findall(pattern, text)
print(matches)