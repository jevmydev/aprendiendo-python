### 

# 02 - types

# Python tiene varios tipos de datos incorporados que nos permiten almacenar y manipular diferentes tipos de información.
# Como son: int, float, complex, str, bool, NoneType, list, tuple, dict, set, range, entre otros.

### -> Comentarios (#)

"""
    Podemos hacer una cadena de texto multilínea
    o usar la triple comilla para documentar nuestro código.
"""

print("Integer (enteros):")

print(10)
print(type(10)) # Imprime el tipo de dato
# print(type(-5))
# print(type(1023109313910))
# print(1293091039018391831)
# print(1293091039018391831 + 1) # En JS se desborda el manejo de números grandes, en Python no.

print("\nFloat (decimales):")
print(10.0) # Los floats pueden representar números enteros también.
print(type(10.0))
# print(-409.123)

print("\nComplex (complejos):")
print(3 + 4j)
print(type(3 + 4j)) # 3 es la parte real, 4j es la parte imaginaria representada en Python.

print("\nString (cadenas de texto):")
print("Esto es una cadena de texto.")
print(type("Esto es una cadena de texto."))
# print("123")
# print("""
#    Multilínea
#    cadena de texto.
#""")

