### 
# 04 - Variables

# Las variables son contenedores para almacenar datos en memoria.

# En Python, no es necesario declarar el tipo de variable explícitamente; se asigna automáticamente según el valor que se le asigne.

# Python es un lenguaje de tipado dinámico. 
# Significa que puedes cambiar el tipo de dato de una variable simplemente asignándole un valor de otro tipo.

# Además, Python es un lenguaje de tipado fuerte.
# Significa que no se permiten operaciones entre tipos de datos incompatibles sin una conversión explícita.
###

my_name = "Jeremy" # Variable que guarda una cadena de texto (string)
print(my_name) # Imprime el valor de la variable my_name

age = 30
print(age)

age = 18 # Reasignación de la variable age a un nuevo valor en tiempo de ejecución
print(age)

# Tipado dinámico: el tipo de dato se asigna en tiempo de ejecución
age = "eighteen" # Ahora age es una cadena de texto
print(type(age))
# Otros lenguajes (EJ: Java) son tipado estático, donde el tipo de dato debe ser declarado explícitamente y no puede cambiarse.

# Tipado fuerte: Python no realiza conversiones de tipo autómaticas
# print("10" + 5) # Type Error
# Otros lenguajes (EJ: JavaScript) son tipado débil, donde se permiten conversiones automáticas entre tipos de datos.

print(f"My nombre es {my_name} y tengo {age} años.") # Uso de f-strings para formatear cadenas de texto (evaluando)

# Forma no recomendada de nombrar variables
city, country, continent = "Santiago", "Chile", "América" # Múltiples asignaciones en una sola línea
print(city, country, continent)

# Convenciones de nomenclatura de variables en Python:
snake_case_variable = "ok" # Uso de minúsculas y guiones bajos para separar palabras
name = "ok" 
nombre_de_variable_123 = "ok" # Pueden incluir números, pero no pueden comenzar con ellos 

MI_CONSTANTE = "valor" # UPPER_CASE -> Convención de constantes (valores que no cambian)

# camelCaseVariable = "valor" # No es común en Python, pero se usa en otros lenguajes como JavaScript
# PascalCaseVariable = "valor" # No es común en Python, pero se usa en otros lenguajes como C#
# kebab-case-variable = "valor" # No es válido en Python, ya que los guiones no son permitidos en nombres de variables

# Nombres de variables no permitidos:
# 1_variable = "valor" # No puede comenzar con un número
# my-variable = "valor" # No puede contener guiones
# True = "valor" # No puede ser una palabra reservada del lenguaje

# Todas las palabras reservadas son: 
# [False, None, True, and, as, assert, async, await, break, class, continue, 
# def, del, elif, else, except, finally, for, from, global, if, import, in, is,
# lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield]

is_user_logged_in: bool = False # Tipeo explícito (opcional en Python, "una anotación de tipo")
print(is_user_logged_in)

is_user_logged_in = "Texto" # Python se salta la anotación de tipo, aviso del editor 
print(is_user_logged_in)