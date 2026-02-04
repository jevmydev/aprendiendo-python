###
# 01 - Dates

# Trabajando con fechas y horas en Python
###
import os
from datetime import datetime, timedelta
import locale 

os.system("clear")

# Obtener fecha y hora actual

now = datetime.now()
print(f"Fecha y hora actual: {now}")

# Crear una fecha y hora específica

specific_date = datetime(2026, 5, 1) # Parámetros: año - mes - día - hora - minuto - segundo...
print(f"\nFecha y hora específica: {specific_date}")

# Formatear fecha
# Método: strftime() para formatear fechas
# Pasarle el objeto datetime y el formato específico
# Formato: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes

format_date = now.strftime("%d %B %Y %p")
print(f"\nFecha formateada: {format_date}")
format_date = now.strftime("%d/%m/%Y %H:%M:%S %p")
print(f"Fecha formateada: {format_date}")

# Operaciones con fechas
# Sumar, restar: meses, días, horas, minutos 

yesterday = datetime.now() - timedelta(days=1)
tomorrow = datetime.now() + timedelta(days=1)

print(f"\nAyer: {yesterday} - Mañana: {tomorrow}")

# Obtener componentes individuales de una fecha
year = now.year
month = now.month
day = now.day

print(f"\n{day}-{month}-{year}")

# Calcular la diferencia entre dos fechas
difference = specific_date - now
print(f"\nDiferencia en días: {difference.days}")

# Fechas en otro idioma

locale.setlocale(locale.LC_TIME, "es_ES.UTF-8") # Los nombres de meses y de la semana en español van con minúsculas

format_date = now.strftime("%A %B %Y %H:%M:%S")
print(f"\nFecha formateada: {format_date}")
