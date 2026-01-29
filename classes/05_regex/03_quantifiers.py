###
# 03 - Quantifiers

# Los cuantificadores se utilizan para especificar cuántas ocurrencias de un carácter o grupo de caracteres se deben encontrar en una cadena
###
import os
import re

os.system("clear")

# *: Puede aparecer 0 o más veces
print()

text = "aaaba"
pattern = "a*"

found = re.findall(pattern, text)
print(found) # ['aaa', '', 'a', ''] (los vacíos son que aparece 0 veces)

# Ejercicio 1
# ¿Cuántas palabras tienen de 0 a más "a" y después una b
print()

pattern = "a*b"
found = re.findall(pattern, text)

print(f"Hay {len(found)} palabras que tienen 0 a más 'a' y después una b")

# +: Puede aparecer 1 o más veces
print()

text = "dddd aaa ccc bb a aa casa"
pattern = "a+"
found = re.findall(pattern, text)
print(found)

# ?: Cero o una vez
print()

text = "aaabacb"
pattern = "a?b"
found = re.findall(pattern, text)
print(found)

# Ejercicio 2
# Haz opcional que aparezca un +34 en el siguiente texto
print()

phone = "+34 123123123 123123123"
pattern = r"(?:\+34 )?\d{9}"
matches = re.findall(pattern, phone)

print(matches)