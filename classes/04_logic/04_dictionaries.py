### 
# 04 - Diccionarios
#
# Los diccionarios en Python son estructuras de datos que almacenan pares clave-valor
# sirven para almacenar datos relacionados
###
import os
os.system("clear")

# Ejemplo
persona = {
    "nombre": "Juan",
    "edad": 30,
    "es_estudiante": True,
    "calificaciones": [6.5, 6.0, 7],
    "socials": {
        "twitter": "@juan",
        "facebook": "juan.fb"
    }
}

# Acceder a valores
print(persona["calificaciones"][1])
print(persona["nombre"])
print(persona["socials"]["twitter"], "\n")

# En JS es similar a los objetos, por ejemplo, para acceder al twitter: persona.socials.twitter

# Cambiar valores al acceder
persona["edad"] = 31
persona["calificaciones"][1] = 7
print(persona, "\n")

# Eliminar pares clave-valor
del persona["edad"]
print(persona, "\n")

# Si queremos recuperar el valor borrado
es_estudiante = persona.pop("es_estudiante")
print("Es estudiante:", es_estudiante)
print(persona, "\n")

# Sobreescribir un diccionario con otro diccionario
a = {"name": "Alice", "age": 25, "is_student": True}
b = {"name": "Bob", "age": 30, "city": "New York"}

a.update(b)
print(a, "\n")  # {'name': 'Bob', 'age': 30, 'city': 'New York'}

# Comprobar si una clave existe en un diccionario
print("name" in persona) # False
print("nombre" in persona, "\n") # True

# Obtener todas las claves
print(persona.keys(), "\n")

# Obtener todos los valores
print(persona.values(), "\n")

# Obtener todos los pares clave-valor
print(persona.items(), "\n")

for key, value in persona.items():
    print(f"{key}: {value}")