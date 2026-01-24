import os
os.system("clear")

print("--------------------")
print("Bienvenido al cajero")
print("--------------------")

def check_balance(balance):
    print(f"\nTu balance es {balance}$")
    return balance

def deposit(balance):
    while True:
        try:
            money = float(input("\nIngresa tu cantidad para depositar: "))
            if money <= 0:
                raise ValueError("No puede depositar valores negativos")

            return balance + money
        except Exception:
            print("Debes ingresar un valor válido")

def withdraw(balance):
    while True:
        try:
            money = float(input("\nIngresa tu cantidad para retirar: "))
            if (money <= 0 and money != balance) or (money > balance):
                raise ValueError("No puede retirar valores negativos o valores mayores al total")

            return balance - money
        except Exception:
            print("Debes ingresar un valor válido")

def menu():
    balance = 0
    possible_options = ["1", "2", "3", "4"]

    while True:
        try:
            print("\nMenú")
            print("1. Revisa tu balance")
            print("2. Depositar")
            print("3. Retirar")
            print("4. Salir")

            option = input("\nSelecciona tu opción: ")

            if option not in possible_options:
                raise ValueError("Opción inválida")

            if option == "1": 
                balance = check_balance(balance)
            elif option == "2": 
                balance = deposit(balance)
            elif option == "3": 
                balance = withdraw(balance)
            else: break
        except Exception:
            print("Debes ingresar una opción válida, intenta de nuevo")    

    print("\n¡Gracias por usar nuestro servicio!")
    
menu()