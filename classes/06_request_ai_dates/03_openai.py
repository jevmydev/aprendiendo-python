import os
import requests
import json

os.system("clear")

OPENAI_API_KEY = "Aquí va la api key"
prompt = "Aquí va el prompt"

def call_openai_gpt(api_key, prompt):
    url = "https://api.openai.com/v1/chat/completions"    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": "gpt-5-nano-2025-08-07",
        "messages": [
        {
            "role": "user",
            "content": prompt
        }]
    }

    response = requests.post(url, headers=headers, json=data)
    return response.json()

api_response = call_openai_gpt(OPENAI_API_KEY, prompt)
# print(json.dumps(api_response, indent=2))
print(api_response["choices"][0]["message"]["content"])

# Para hacer llamados a DeepSeek es absolutamente lo mismo que con OPENAI
# Pero cambiando la url y la api key respectiva