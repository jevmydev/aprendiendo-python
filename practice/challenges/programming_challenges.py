import re
import os

os.system("clear")

print("\n---------------------------------------")
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

print("\n---------------------------------------")
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

print("\n---------------------------------------")
print("Tercer ejercicio - Fibonacci")
print("---------------------------------------")

###
# * Escribe un programa que imprima los 50 primeros números de la sucesión
# * de Fibonacci empezando en 0.
# * - La serie Fibonacci se compone por una sucesión de números en
# *   la que el siguiente siempre es la suma de los dos anteriores.
# *   0, 1, 1, 2, 3, 5, 8, 13...
###

fibonacci = []

for i in range(51):
    if len(fibonacci) < 2:
        fibonacci.append(i)
        continue

    last_num = fibonacci[i - 1]
    second_to_last_num = fibonacci[i - 2]

    fibonacci_num = last_num + second_to_last_num
    fibonacci.append(fibonacci_num)

for num in fibonacci:
    print(f"{num}", end=", " if num != fibonacci[-1] else "\n")

print("\n---------------------------------------")
print("Cuarto ejercicio - Área de un polígono")
print("---------------------------------------")

###
# * Crea una única función (importante que sólo sea una) que sea capaz
# * de calcular y retornar el área de un polígono.
# * - La función recibirá por parámetro sólo UN polígono a la vez.
# * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
# * - Imprime el cálculo del área de un polígono de cada tipo.
###

def area_of_polygon(polygon, base, height):
    polygon = polygon.lower()
    
    pattern_square = "cuadrado"
    is_square = re.search(pattern_square, polygon)

    pattern_rectangle = "rect.ngulo"
    is_rectangle = re.search(pattern_rectangle, polygon)

    pattern_triangle = "tri.ngulo"
    is_triangle = re.search(pattern_triangle, polygon)

    area = base * height 

    if is_triangle:
        area /= 2
    
    if is_square or is_rectangle or is_triangle:
        return f"El área del {polygon} es: {area} u^2"

print(area_of_polygon("Triangulo", base=3, height=4))

print("\n---------------------------------------")
print("Quinto ejercicio - Invertir cadenas")
print("---------------------------------------")

###
# * Crea un programa que invierta el orden de una cadena de texto
# * sin usar funciones propias del lenguaje que lo hagan de forma automática.
# * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
###

def reverse_str(str):
    return str[::-1]

print(reverse_str("Hola mundo"))


print("\n---------------------------------------")
print("Sexto ejercicio - Contando palabras")
print("---------------------------------------")

###
# * Crea un programa que cuente cuantas veces se repite cada palabra
# * y que muestre el recuento final de todas ellas.
# * - Los signos de puntuación no forman parte de la palabra.
# * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
# * - No se pueden utilizar funciones propias del lenguaje que
# *   lo resuelvan automáticamente.
###

def count_words(text: str):
    dicc_words = {}
    list_text = text.split(" ")

    for word in list_text:
        parse_word = ""

        for char in word.lower():
            if char in ".,!¡?¿(){}[]":
                continue
            
            parse_word += char

        if parse_word in dicc_words:
            dicc_words[parse_word] += 1
        else:
            dicc_words[parse_word] = 1

    return dicc_words

# Genera test para count_words
print(count_words("Hola hola mundo. Mundo de pruebas, pruebas de código!"))
print(count_words("¡Pruebas, pruebas y más pruebas! ¿Por qué tantas pruebas?"))

print("\n---------------------------------------")
print("Séptimo ejercicio - Decimal a binario")
print("---------------------------------------")

###
# * Crea un programa se encargue de transformar un número
# * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
###

def decimal_to_binary(decimal):
    if decimal == 0:
        return "0"
    
    decimal = abs(int(decimal))
    binary = ""

    while decimal > 0:
        residue = decimal % 2
        decimal //= 2

        binary = str(residue) + binary

    return binary

print(decimal_to_binary(-100))