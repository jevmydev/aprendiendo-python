import re
import os

os.system("clear")

def fibonacci_reverse(first, second):
    while first <= second:
        diff = second - first
        print(f"first: {first} second: {second} diff: {diff}")

        if diff > first:
            return first, second
        
        second = first
        first = diff

print(fibonacci_reverse(2440, 3948))

# -----------------------------

def reversed_str(string):
    return string[::-1]

print(reversed_str("worlds"))

# -----------------------------

def string_to_number(s):
    return int(s)    

# -----------------------------

def dna_to_rna(dna):
    pattern = "T"
    rna = re.sub(pattern, "U", dna)

    return rna    

print(dna_to_rna("TTTT"))