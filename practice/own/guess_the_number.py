import random
import os

os.system("clear")

print("\n¡Bienvenido a adivina el número, con pistas te irás guiando, hasta encontrar el número buscado!")
print("Procura no equivocarte tanto.")

def guess_the_number():
    program_number = random.randint(0, 100)
    tries = 0

    while True:
        try:
            user_number = int(input("\nEscoge tu número (entre 0 y 100, incluidos): "))
            diff = program_number - user_number

            if diff == 0:
                break

            if diff > 0:
                print("Más alto")
            else:
                print("Más bajo")
            tries += 1
            
        except ValueError:
            print("Debes escoger un valor entero.")

    print(f"\n¡Felicidades, lograste adivinar el número {program_number} en {tries} intentos!")

    reset_game = input("¿Deseas reiniciar el juego (s/n)?: ")
    if reset_game == "s":
        guess_the_number()
    
    return None
    
guess_the_number()
