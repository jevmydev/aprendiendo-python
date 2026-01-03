### 
# 03 - Casting of types

# Transforma un valor de un tipo a otro
###

print("Conversión de tipos")

print(type(int("100")))       # De string a entero
print(int("100") + 2)

print("100" + str(2))   # De entero a string, el + concatena

print(int(3.1416))     # De float a entero (trunca)

print(bool(0))        # De entero a booleano (0 es False, cualquier otro valor es True)
print(bool(42))

print(bool(""))       # De string a booleano (string vacío es False, cualquier otro es True)
print(bool("Hola"))
print(bool("False"))

# print(int("Hola"))   # ValueError: no se puede transformar un texto a un número entero

# print(int(2.5)) # 2
print(round(2.5)) # 2
print(round(3.5)) # 4 -> Sí se encuentra en x.5 (en medio) redondea al par más cercano 