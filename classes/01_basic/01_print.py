### 
# 01 - Print()

# Es un módulo para imprimir mensajes en la consola.

# Recordar:
# Los archivos serán escritos en snake case (usar guiones bajos para separar palabras).
# La extensión del archivo será .py
# Los strings o cadenas de texto se definen usando comillas dobles ("") o simples ('').
###

print("Hello World!")
print('También puedo usar comillas simples.')

print("Python", "es", "genial") # Por defecto separa los elementos con un espacio y salto de línea al final (\n) 
print("Python", "es", "brutal", sep="-") # Separamos los elementos con un guion

print("en una línea")
print ("Esto se imprime", end=" ") # Cambiamos el final del salto de línea (\n) a un espacio

print(42) # Podemos imprimir números