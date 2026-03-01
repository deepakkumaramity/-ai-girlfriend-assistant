import requests

def ask_gf(message, history, personality):

    conversation = personality + "\n"

    for h in history:
        if h["role"] == "user":
            conversation += f"User: {h['content']}\n"
        else:
            conversation += f"Girlfriend: {h['content']}\n"

    conversation += f"User: {message}\nGirlfriend:"

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "phi3:mini",
            "prompt": conversation,
            "stream": False
        }
    )

    return response.json()["response"]