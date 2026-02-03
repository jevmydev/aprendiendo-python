import os
import re

os.system("clear")

# Ejercicio final:
# Mejorar esto: https://www.computerhope.com/jargon/r/regular-expression.png
# Buscar corner cases que no pasa y arreglarlo:

pattern = r"^[\w._%+-/=]{1,64}@([\w.-]+\.[a-zA-Z]+){1,255}$"

def is_valid_email(email):
    match = re.search(pattern, email)
    return True if match else False

### TEST ###
emails = [
    "Jeremy@gmail.com",
    "lo.que+sea@shopping.online",
    "michael@gov.co.uk",
    "a@b.co",
    "user@domain.museum",
    "user@domain.travel",
    "user@domain.technology",
    "user@sub.subdomain.com",
    "user+tag+sorting@example.com",
    "user.name+tag@example.co.uk",
    "customer/department=shipping@example.com",
    "user_name@example-domain.com",
    "x@example.com",
]

for email in emails:
    print(email, is_valid_email(email))
### TEST ###