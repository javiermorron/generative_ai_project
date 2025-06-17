from utils.config_loader import Config
import requests

class OllamaClient:
    def __init__(self, model, endpoint):
        self.model = model
        self.endpoint = endpoint

    def complete(self, prompt):
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "stream": False
        }
        response = requests.post(self.endpoint, json=payload)

        if response.status_code == 200:
            return response.json()["message"]["content"]
        else:
            return f"❌ Error {response.status_code}: {response.text}"

# === PRUEBA LOCAL CON GEMMA ===
if __name__ == "__main__":
    config = Config()
    cfg = config.llms["local_ollama"]

    client = OllamaClient(model=cfg["model"], endpoint=cfg["endpoint"])
    respuesta = client.complete("¿Cuál es la capital de Cuba?")
    print("\n🧠 Respuesta de Gemma:\n", respuesta)

