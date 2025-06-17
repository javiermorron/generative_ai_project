import streamlit as st
import sys
import os
import requests

# === Importar la configuración del modelo ===
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.config_loader import Config

# === CONFIGURACIÓN DE PÁGINA (debe ir antes de cualquier otro st.xxx) ===
st.set_page_config(page_title="🧠 Chat con Gemma (Ollama)")

# === Cargar configuración del modelo ===
config = Config()
cfg = config.llms["local_ollama"]

# === Inicializar estado de la conversación ===
if "messages" not in st.session_state:
    st.session_state.messages = []

# === Sidebar con botón para reiniciar ===
with st.sidebar:
    st.title("⚙️ Opciones")
    if st.button("🔄 Reiniciar conversación"):
        st.session_state.messages = []
        st.rerun()  # ✅ función moderna para recargar

# === Cliente simple para Ollama ===
def chat_with_model(prompt, model=cfg["model"], endpoint=cfg["endpoint"]):
    payload = {
        "model": model,
        "messages": st.session_state.messages + [{"role": "user", "content": prompt}],
        "stream": False
    }
    response = requests.post(endpoint, json=payload)
    if response.status_code == 200:
        content = response.json()["message"]["content"]
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.session_state.messages.append({"role": "assistant", "content": content})
        return content
    else:
        return f"❌ Error {response.status_code}: {response.text}"

# === Interfaz principal ===
st.title("💬 Chat Local con Gemma")
st.markdown("Interactuá con el modelo `gemma:2b` desde tu PC — sin conexión, sin costo.")

# === Input del usuario ===
user_input = st.chat_input("Escribí tu mensaje...")

# === Mostrar historial ===
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# === Procesar mensaje nuevo ===
if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        response = chat_with_model(user_input)
        st.markdown(response)

