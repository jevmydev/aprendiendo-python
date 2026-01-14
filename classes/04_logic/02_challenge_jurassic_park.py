"""
En Jurassic Park, se ha observado que los dinosaurios carnívoros, como el temible T-Rex, depositan un número par de huevos. Imagina que tienes una lista de números enteros en la que cada número representa la cantidad de huevos puestos por un dinosaurio en el parque.

Importante: Solo se consideran los huevos de los dinosaurios carnívoros (T-Rex) aquellos números que son pares.

Objetivo:
Escribe una función en Python que reciba una lista de números enteros y devuelva la suma total de los huevos que pertenecen a los dinosaurios carnívoros (es decir, la suma de todos los números pares en la lista).
"""
import os
os.system("clear")

# Para comprobar si un número es par
# siempre usamos el operador módulo (%)
# corresponde al resto de la división

def count_carnivore_dinosaur_eggs(eggs_list: list[int]) -> int:
    """
    Función que recibe una lista de números enteros (cantidad de huevos de dinosaurios jurásicos) y acumula los números pares (huevos de dinosaurios CARNÍVOROS) para finalmente devolver esa suma.
    """
    total_carnivore_eggs = 0

    for egg in eggs_list:
        if egg % 2 == 0:
            total_carnivore_eggs += egg
    
    print(f"\nNúmero de huevos de dinosaurio carnívoro: {total_carnivore_eggs}")
    return total_carnivore_eggs

egg_list = [3, 4, 5, 7, 8]
print(count_carnivore_dinosaur_eggs(egg_list))