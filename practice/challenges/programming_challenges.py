import os
os.system("clear")

print("---------------------------------------")
print("Primer ejercicio - FizzBuzz")
print("---------------------------------------")

###
# * Escribe un programa que muestre por consola (con un print) los
# * números de 1 a 100 (ambos incluidos y con un salto de línea entre
# * cada impresión), sustituyendo los siguientes:
# * - Múltiplos de 3 por la palabra "fizz".
# * - Múltiplos de 5 por la palabra "buzz".
# * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
###

def extract_sum_of_digits(num):
    list_of_digits = [int(digit) for digit in str(num)]
    return sum(list_of_digits)

for num in range(1, 101):
    sum_of_digits = extract_sum_of_digits(num)
    
    if sum_of_digits % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    elif sum_of_digits % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)

print("---------------------------------------")
print("Segundo ejercicio - ¿Es un anagrama?")
print("---------------------------------------")

###
# * Escribe una función que reciba dos palabras (String) y retorne
# * verdadero o falso (Bool) según sean o no anagramas.
# * - Un Anagrama consiste en formar una palabra reordenando TODAS
# *   las letras de otra palabra inicial.
# * - NO hace falta comprobar que ambas palabras existan.
# * - Dos palabras exactamente iguales no son anagrama.
###

def is_anagram(str_1, str_2):
    str_1 = str_1.lower().strip()
    str_2 = str_2.lower().strip()

    if str_1 == str_2:
        return False
    
    list_1 = list(str_1)
    list_1.sort(key=str.lower)

    list_2 = list(str_2)
    list_2.sort(key=str.lower)

    return list_1 == list_2
    
# Test

print(is_anagram("roma", "amor"))          # True
print(is_anagram("listen", "silent"))      # True
print(is_anagram("anagram", "nagaram"))    # True
print(is_anagram("hola", "halo"))           # True
print(is_anagram("python", "typhon"))       # True
print(is_anagram("casa", "casas"))          # False
print(is_anagram("perro", "gato"))          # False
print(is_anagram("amor", "amores"))         # False
print(is_anagram("Roma", "amor"))           # True 
print(is_anagram("roma", "amor "))    # True 

print("---------------------------------------")
print("---------------------------------------")