import random
import os

os.system("clear")

possible_choices = ["Piedra", "Papel", "Tijera"]

def reset_game():
    is_user_want_reset = input("\n¿Quieres jugar otra vez? (s/n) ")

    if is_user_want_reset.lower().strip() == "s":
        rock_paper_scissors()
    else:
        print("\n¡Gracias por jugar! ¡Hasta la próxima!")

def results(user_choice, machine_choice):
    print("\n¡Resultados!")

    if user_choice == machine_choice:
        return f"{user_choice} vs {machine_choice} = Empate"
        
    elif user_choice == "Tijera" and machine_choice == "Piedra" or \
         user_choice == "Piedra" and machine_choice == "Papel" or \
         user_choice == "Papel" and machine_choice == "Tijera":
        return f"{user_choice} vs {machine_choice} = Perdiste :C"
    
    return f"{user_choice} vs {machine_choice} = ¡Ganaste Yujuuu!"
    
def rock_paper_scissors():
    print("\n---------------------------------------------")
    print("Bienvenido al juego de piedra, papel o tijera")
    print("---------------------------------------------")

    user_choice = ""
    machine_choice = random.choice(possible_choices)

    while True:
        user_choice = input("\nElige tu opción (piedra / papel / tijera): ").capitalize().strip()

        if user_choice not in possible_choices:
            print("\nDebes escoger una opción válida")
            continue
        
        break
    
    print(results(user_choice, machine_choice))
    reset_game()

rock_paper_scissors()