import json
from settings import API_KEY
from urllib.request import urlopen, Request


# url = "https://api.openai.com/v1/chat/completions"
url = "https://api.deepseek.com/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

# Conversamos con la IA
# TODO guardar las preguntas y las respuestas como parte del contexto
while True:
    pregunta = input("habla con chatgpt: ")

    data = {
        "model": "deepseek-chat",
        # "model": "gpt-3.5-turbo",
        # "model": "gpt-5-nano",
        "messages": [
            {"role": "system", "content": "Eres un experto en ciudades de Cordoba en Argentina"},
            {"role": "user", "content": pregunta},
        ],
        "max_tokens": 200,
    }

    req = Request(
        url,
        data=json.dumps(data).encode("utf-8"),
        headers=headers
    )
    response = urlopen(req)
    result = json.load(response)
    print(f"\n\nresult: {result}\n")
    print("\n\nchatgpt dice:\n\n")
    print(result["choices"][0]["message"]["content"])
