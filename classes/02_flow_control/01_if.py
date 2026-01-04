###
# 01 - Sentencias condicionales (if - elseif - else)
 
# Permiten ejecutar bloques de código solo si se cumple una condición específica.
###

import os
os.system("clear") # Importamos el módulo de operative system (os) para llamar al comando clear y limpiar la consola

print("\nSentencia simple condicional")

age = 18
if age >= 18:
    print("Eres mayor de edad")
    print("Felicidades")


print("\nSentencia condicional con else")

age = 15
if age >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

print("\nSentencia condicional con elif")

mark = 7
if mark >= 9:
    print("¡Sobresaliente!")
elif mark >= 7:
    print("Notable")
elif mark >= 5:
    print("Aprobado")
else:
    print("Desaprobado")

print("Condiciones múltiples con operadores lógicos")

age = 25
has_license = True

# JavaScript
# && -> And
# || -> Or

if age >= 18 and has_license:
    print("Puedes conducir")
else:
    print("Alto policía")

age = 18
has_carnet = True
did_bribe_police = False

if age >= 18 or has_carnet:
    print("Puedes conducir (rara la ley)")
else:
    if did_bribe_police:
        print("Puedes conducir (sobornó a la policia)")
    else:
        print("No puedes conducir y te multarán")

print("\nNegación de condiciones")

is_weekend = False

# JavaScript --> ! (negación)

if not is_weekend:
    print("¡A estudiar o trabajar!")

print ("\nCondiciones anidadas")

age = 20
has_money = True

if age >= 18:
    if has_money:
        print("Puedes salir de fiesta")
    else:
        print("No tienes dinero para salir de fiesta")
else: 
    print("Eres menor de edad, no puedes salir de fiesta")

# La idea es no abusar de las condiciones anidadas para mantener el código legible.

# Mejor usar operadores lógicos para combinar condiciones
#if age < 18:
#    print("Eres menor de edad")
#elif has_money:
#    print("Puedes salir de fiesta")
#else:
#    print("No tienes dinero para salir de fiesta")