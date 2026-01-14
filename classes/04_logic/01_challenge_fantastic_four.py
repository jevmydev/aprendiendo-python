"""
¿Está en Equilibrio la Alianza entre Reed Richards y Johnny Storm?

En el universo de los 4 Fantásticos, la unión y el equilibrio entre los poderes es fundamental para enfrentar cualquier desafío. En este problema, nos centraremos en dos de sus miembros:

Reed Richards (Mr. Fantastic), representado por la letra R.
Johnny Storm (La Antorcha Humana), representado por la letra J.

Objetivo:

Crea una función en Python que reciba una cadena de texto. Esta función debe contar cuántas veces aparece la letra R (para Reed Richards) y cuántas veces aparece la letra J (para Johnny Storm) en la cadena.

- Si la cantidad de R y la cantidad de J son iguales, se considera que la alianza entre la mente y el fuego está en equilibrio y la función debe retornar True.
- Si las cantidades no son iguales, la función debe retornar False.
- En el caso de que no aparezca ninguna de las dos letras en la cadena, se entiende que el equilibrio se mantiene (0 = 0), por lo que la función debe retornar True.
"""
import os
os.system("clear")

def check_balanced_alliance(str):
    str = str.upper()

    count_for_reed_richards = str.count("R") # Reed Richards
    count_for_johnny_storm = str.count("J") # Johnny Storm

    
    print(f"\nCount R: {count_for_reed_richards}. Count J: {count_for_johnny_storm}")
    return count_for_reed_richards == count_for_johnny_storm

print(check_balanced_alliance("RRjj"))
print(check_balanced_alliance("RRRRRjj"))
print(check_balanced_alliance("RRjjjj"))
print(check_balanced_alliance("ASDADUHAUODKPA"))
