# Analizador de números con un solo cambio de tendencia
# -----------------------------------------------------
# Un "Single Trend Change Number" es un entero positivo cuyos dígitos,
# leídos de izquierda a derecha, cambian de tendencia exactamente una vez:
# - puede subir y luego bajar, o
# - bajar y luego subir,
# siempre de forma estricta.
#
# Ejemplos:
# - 13421   -> sube y luego baja        -> válido
# - 211456  -> baja y luego sube        -> válido
# - 1234    -> solo sube               -> inválido
# - 4321    -> solo baja               -> inválido
# - 13241   -> sube, baja y sube        -> inválido
#
# Objetivo:
# Implementar la función is_single_trend_change_number(num: int) -> bool
#
# Restricciones:
# - No usar librerías externas.
# - Los números deben tener al menos 3 dígitos.
# - Las variaciones deben ser estrictas (sin dígitos iguales consecutivos).

import os
os.system("clear")

def is_single_change_num(num: int):
    iterable_num = str(num)
    len_iterable_num = len(iterable_num)

    if len_iterable_num < 3:
        return False

    was_increasing = None
    times_to_change_tendency = 0

    for i, iterable_digit in enumerate(iterable_num):
        if i == 0: continue

        digit = int(iterable_digit)
        last_digit = int(iterable_num[i - 1])

        if digit == last_digit:
            return False

        is_increment = last_digit < digit
        
        if i == 1: was_increasing = is_increment

        if is_increment:
            if was_increasing: continue

            times_to_change_tendency += 1
            was_increasing = True
        else:
            if not was_increasing: continue

            times_to_change_tendency += 1
            was_increasing = False

    return times_to_change_tendency == 1

tests = [
    (13421, True),    # sube y baja (caso clásico)
    (159631, True),   # sube y baja
    (1234, False),    # solo sube
    (4321, False),    # solo baja
    (13241, False),   # sube, baja, vuelve a subir
    (121, True),      # sube (1→2) y baja (2→1)
    (111, False),     # no es estrictamente creciente ni decreciente
    (10, False),      # menos de 3 dígitos
    (210, False),     # baja todo el tiempo
    (211456, False),  # baja, se mantiene igual y luego sube (al mantenerse igual no sigue la tendencia)
]

for num, expected in tests:
    result = is_single_change_num(num)
    print(f"{num}: esperado={expected}, obtenido={result}")