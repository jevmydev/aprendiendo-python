import re
import os

os.system("clear")

print("\n---------------------------------------")
print("1. FizzBuzz")
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
print("2 - ¿Es un anagrama?")
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
print("3 - Fibonacci")
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
print("4 - Área de un polígono")
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
print("5 - Invertir cadenas")
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
print("6 - Contando palabras")
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
print("7 - Decimal a binario")
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

print(decimal_to_binary(124))

print("\n---------------------------------------")
print("8 - Código morse")
print("---------------------------------------")

###
#  * Crea un programa que sea capaz de transformar texto natural a código
#  * morse y viceversa.
#  * - Debe detectar automáticamente de qué tipo se trata y realizar
#  *   la conversión.
#  * - En morse se soporta raya "—", punto "·, un espacio entre símbolo, dos espacios entre palabras "  ".
#  * - El alfabeto morse soportado será el mostrado en
#  *   https://es.wikipedia.org/wiki/Código_morse.
###

diccionary_to_morse = {
    "A": "·—",
    "B": "—···",
    "C": "—·—·",
    "D": "—··",
    "E": "·",
    "F": "··—·",
    "G": "——·",
    "H": "····",
    "I": "··",
    "J": "·———",
    "K": "—·—",
    "L": "·—··",
    "M": "——",
    "N": "—·",
    "O": "———",
    "P": "·——·",
    "Q": "——·—",
    "R": "·—·",
    "S": "···",
    "T": "—",
    "U": "··—",
    "V": "···—",
    "W": "·——",
    "X": "—··—",
    "Y": "—·——",
    "Z": "——··",
    "1": "·————",
    "2": "··———",
    "3": "···——",
    "4": "····—",
    "5": "·····",
    "6": "—····",
    "7": "——···",
    "8": "———··",
    "9": "————·",
    "0": "—————",
}
diccionary_to_text = {v: k for k, v in diccionary_to_morse.items()}

def morse_to_text(morse):
    text = ""
    words = morse.split("  ")

    for word in words:
        symbols = word.split(" ")

        for code_symbol in symbols:
            letter = diccionary_to_text[code_symbol]
            text += letter
        
        text += " "

    return text

def text_to_morse(text):
    morse = ""
    words = text.split(" ")

    for word in words:
        for letter in word:
            code_symbol = diccionary_to_morse[letter]
            morse += code_symbol + " "
        
        morse += "  "
    
    return morse

def conversion_morse_and_text(string):
    if string[0] in ["·", "—"]:
        return morse_to_text(string)
    
    return text_to_morse(string)

# =========================
# TESTS: text_to_morse
# =========================

print(conversion_morse_and_text("SOS"))
# Resultado esperado:
# "··· ——— ···  "

print(conversion_morse_and_text("HELLO"))
# Resultado esperado:
# "···· · ·—·· ·—·· ———  "

print(conversion_morse_and_text("HELLO WORLD"))
# Resultado esperado:
# "···· · ·—·· ·—·· ———   ·—— ——— ·—· ·—·· —··  "

print(conversion_morse_and_text("A1"))
# Resultado esperado:
# "·— ·————  "

# =========================
# TESTS: morse_to_text
# =========================

print(conversion_morse_and_text("··· ——— ···"))
# Resultado esperado:
# "SOS "

print(conversion_morse_and_text("···· · ·—·· ·—·· ———"))
# Resultado esperado:
# "HELLO "

print(conversion_morse_and_text("···· · ·—·· ·—·· ———  ·—— ——— ·—· ·—·· —··"))
# Resultado esperado:
# "HELLO WORLD "

print(conversion_morse_and_text("·— ·————"))
# Resultado esperado:
# "A1 "

print("\n---------------------------------------")
print("9 - Expresiones equilibradas")
print("---------------------------------------")

###
#  * Crea un programa que comprueba si los paréntesis, llaves y corchetes
#  * de una expresión están equilibrados.
#  * - Equilibrado significa que estos delimitadores se abren y cieran
#  *   en orden y de forma correcta.
#  * - Paréntesis, llaves y corchetes son igual de prioritarios.
#  *   No hay uno más importante que otro.
#  * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
#  * - Expresión no balanceada: { a * ( c + d ) ] - 5 }
###

def is_balanced(expression):
    open_symbols = []

    for symbol in expression:
        if symbol == "(" or symbol == "[" or symbol == "{":
            open_symbols.append(symbol)

        elif symbol == ")" or symbol == "]" or symbol == "}":
            if len(open_symbols) == 0:
                return False

            last_open = open_symbols.pop()

            if (last_open == "(" and symbol != ")" or
                last_open == "[" and symbol != "]" or
                last_open == "{" and symbol != "}"):
                return False

    return len(open_symbols) == 0
    

print(is_balanced("{ [ a * ( c + d ) ] - 5 }"))  # True
print(is_balanced("{ a * ( c + d ) ] - 5 }"))    # False 
print(is_balanced("[ ( a + b ) * { c + d } ]")) # True
print(is_balanced("[ ( a + b ) * { c + d } "))   # False
print(is_balanced("{ ( [ ] ) }"))                  # True
print(is_balanced("{ ( [ ) ] }"))                  # False
print(is_balanced("{ ( [ ] { } ) }"))                  # True

print("\n---------------------------------------")
print("10 - Eliminando caracteres")
print("---------------------------------------")

###
#  * Crea una función que reciba dos cadenas como parámetro (str1, str2)
#  * e imprima otras dos cadenas como salida (out1, out2).
#  * - out1 contendrá todos los caracteres presentes en la str1 pero NO
#  *   estén presentes en str2.
#  * - out2 contendrá todos los caracteres presentes en la str2 pero NO
#  *   estén presentes en str1.
###

def deleting_chars(str1, str2):
    out1 = ""
    out2 = ""

    for char1 in str1:
        if char1 not in str2:
            out1 += char1

    for char2 in str2:
        if char2 not in str1:
            out2 += char2

    return (out1, out2)

# =========================
# TESTS: deleting_chars
# =========================

print(deleting_chars("abc", "bcd")) # ("a", "d")
print(deleting_chars("abc", "xyz")) # ("abc", "xyz")
print(deleting_chars("", "abc")) # ("", "abc")
print(deleting_chars("", "")) # ("", "")
print(deleting_chars("aabbcc", "abc")) # ("", "")
print(deleting_chars("AbC", "abc")) # ("AC", "ac")
print(deleting_chars("a b!c", "b c?")) # ("a!", "?")
print(deleting_chars("python", "python")) # ("", "")

print("\n---------------------------------------")
print("10 - Es un palíndromo")
print("---------------------------------------")

###
#  * Escribe una función que reciba un texto y retorne verdadero o
#  * falso (Boolean) según sean o no palíndromos.
#  * Un Palíndromo es una palabra o expresión que es igual si se lee
#   * de izquierda a derecha que de derecha a izquierda.
#  * NO se tienen en cuenta los espacios, signos de puntuación y tildes.
#  * Ejemplo: Ana lleva al oso la avellana.
###

def is_palindrome(text):
    parse_text = ""

    pattern = r"\w"
    alfa_numerics_text = re.findall(pattern, text)

    for char in alfa_numerics_text:
        char = char.lower()

        if char == "á": char = "a"
        elif char == "é": char = "e"
        elif char == "í": char = "i"
        elif char == "ó": char = "o"
        elif char == "ú": char = "u"

        parse_text += char

    return parse_text == parse_text[::-1]

print(is_palindrome("ana"))                           # True
print(is_palindrome("Ana"))                           # True
print(is_palindrome("Ana lleva al oso la avellana"))  # True
print(is_palindrome("¿Acaso hubo búhos acá?"))        # True
print(is_palindrome("La ruta nos aportó otro paso natural."))  # True
print(is_palindrome("Esto no es un palíndromo"))      # False
print(is_palindrome(""))                              # True
print(is_palindrome("a"))                             # True
print(is_palindrome("12321"))                         # True
print(is_palindrome("A1b2b1a"))                       # True