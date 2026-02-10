###
# 04 - Classes

# Las clases son plantillas para crear objetos personalizados en Python. Nos permiten definir nuestras propias estructuras de datos y comportamientos.
# Nos permite agrupar datos y métodos relacionadas en una sola entidad. Esto facilita la organización y reutilización del código.
###
import os
import requests

os.system("clear")

# Ejemplo básico de una clase
class Car:
    type_of = "Vehículo de cuatro ruedas" # Atributo de clase (compartido por todas las instancias)

    # Método constructor (se llama al crear una instancia)
    # El self se refiere a sí mismo
    def __init__(self, make, model, color):
        self.make = make  # Atributo de instancia (específico para cada objeto)
        self.model = model
        self.color = color

    def start_engine(self):
        # ???
        return f"El coche {self.make} {self.model} arrancó."


my_car = Car("Toyota", "Corolla", "Rojo")
my_friend_car = Car("Ford", "Mustang", "Azul")

print(my_car.start_engine())  # El coche Toyota Corolla arrancó.
print(my_friend_car.start_engine())  # El coche Ford Mustang arrancó.

print(f"\n{my_car.type_of}")  # Vehículo de cuatro ruedas
print(my_friend_car.type_of)  # Vehículo de cuatro ruedas

print(f"\n{my_car.color}") # Rojo
print(my_friend_car.color) # Azul

# Encapsulación: Podemos ocultar los detalles internos de una clase y exponer solo lo necesario a través de métodos públicos.

# Crear una clase para llamar a una IA (OpenAI, DeepSeek)
class AIRequest:
    def __init__(self, api_key, url, model):
        self.api_key = api_key
        self.url = url
        self.model = model

    def call(self, prompt):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        data = {
            "model": self.model,
            "messages": [
            {
                "role": "user",
                "content": prompt
            }]
        }

        try:
            response = requests.post(self.url, headers=headers, json=data)
            response_json = response.json()

            return response_json["choices"][0]["message"]["content"]
    
        except Exception as e:
            return f"Error: {e}"
        
openai = AIRequest(
    api_key="Aquí va la api key de OpenAI",
    url="https://api.openai.com/v1/chat/completions",
    model="gpt-5-nano-2025-08-07"
)

deepseek = AIRequest(
    api_key="Aquí va la api key de DeepSeek",
    url="https://api.deepseek.com/chat/completions",
    model="deepseek-chat"
)

prompt = "¿Cuál es la integral de x^2?"

print("\nRespuesta de OpenAI:")
print(openai.call(prompt))

print("\nRespuesta de DeepSeek:")
print(deepseek.call(prompt))