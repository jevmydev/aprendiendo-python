###
# 02 - Metachars

# Los metacaracteres son caracteres con un significado especial o más específicos en las expresiones regulares.
###
import os
import re

os.system("clear")

# 1. El punto (.)
# El punto coincide con cualquier carácter excepto un salto de línea.

text = "Hola mundo, H0la 123 H$la hasta luego."
pattern = r"H.la" # r indica a python que es una expresión regular

found = re.findall(pattern, text)
print("\n",found)  # Salida: ['Hola', 'H0la', 'H$la']

text = "casa caasa cosa causa cisa cesa"
pattern = "c.sa" # Solo un carácter entre 'c' y 'sa'

found = re.findall(pattern, text)
print("\n",found)

# 2. Barra invertida \ 
# Se utiliza para darle un significado "literal", anulando un significado especial

text = "mi casa es blanca. Y el coche es negro."
pattern = r"\." 

found = re.findall(pattern, text)
print("\n", found)

# 3. Barra invertida d: \d
# Coincide con cualquier dígito (0-9)

text = "El número de teléfono es: +588123892"
# found = re.findall(r"\d\d\d\d\d\d\d\d\d", text) 
found = re.findall(r"\d{9}", text) 
print("\n", found)

# Ejercicio: Detectar si hay un num de España en el texto gracias al prefijo +34
text = "Mi número de teléfono es +34 691238183 apúntalo!"
pattern = r"\+34 \d{9}"

found = re.search(pattern, text)
if found: print("\n", found.group())

# 4. Barra invertida w: \w
# Coincide con cualquier carácter alfanumérico (a-z, A-Z, 0-9, _)

text = "@@@@el_rubius"
pattern = r"\w"

found = re.findall(pattern, text)
print("\n",found)

# 5. Barra invertida s: \s
# Coincide con cualquier espacio en blaco (espacio, tab, salto de línea)

text = "Hola \n Mundo, que tal\t hey!" # \t: tabulación
pattern = r"\s"

found = re.findall(pattern, text)
print("\n",found)
print()

# 6. ^
# Coincide con el principio de una cadena

username = "423_name%"
pattern = r"^\w" # Debe empezar solo con un alfanúmerico, no símbolos

valid = re.search(pattern, username)

if valid: print("Usuario válido")
else: print("Usuario no válido")

print()

phone = "+34 123131123"
pattern = r"^\+\d{2,3} \d{9}"

valid = re.search(pattern, phone)

if valid: print("El número es válido")
else: print("El número no es válido")