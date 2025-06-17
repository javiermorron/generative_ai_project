# 🧠 Generative AI Project Template

Una plantilla profesional y lista para producción para proyectos de Inteligencia Artificial Generativa en Python.

Estructurada, mantenible, y con soporte para texto, imagen y audio usando modelos como GPT, Claude, Stable Diffusion y ElevenLabs.

---

## 📁 Estructura del Proyecto

```plaintext
generative_ai_project/
├── app/                  # Lógica de la aplicación
│   ├── main.py           # Entrada principal del proyecto
│   ├── prompts/          # Prompts estáticos o plantillas base
│   ├── agents/           # Agentes LLM (CrewAI, LangChain, etc.)
│   └── services/         # Lógica de negocio generativa (texto, imagen, audio)
│
├── models/               # Wrappers de modelos (OpenAI, Claude, SD, etc.)
├── config/               # Archivos YAML con configuraciones de modelo y logging
├── prompt_engineering/   # Plantillas y manipulación avanzada de prompts
├── utils/                # Utilidades comunes: logger, rate limiter, loader de config
├── handlers/             # Manejo de errores
├── data/                 # Datos de entrada, salida, caché y embeddings
├── examples/             # Ejemplos de código listos para usar
├── notebooks/            # Análisis exploratorio y pruebas rápidas
├── requirements.txt      # Dependencias del proyecto
├── setup.py              # Configuración para empaquetado
├── Dockerfile            # Imagen para contenerización (opcional)
├── README.md             # Este archivo
└── .env.example          # Variables de entorno necesarias (API keys)
```

---

## 🚀 Primeros pasos

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu_usuario/generative_ai_project.git
cd generative_ai_project
```

### 2. Crear entorno virtual e instalar dependencias

```bash
python -m venv venv
source venv/bin/activate  # en Linux/macOS
venv\Scripts\activate     # en Windows
pip install -r requirements.txt
```

### 3. Copiar archivo `.env.example` como `.env`

```bash
cp .env.example .env
```

Reemplazar las claves API correspondientes.

### 4. Ejecutar ejemplo básico de generación de texto

```bash
python examples/basic_completion.py
```

---

## 🪄 Chat Local con Gemma (vía Ollama)

Este proyecto incluye un ejemplo funcional de chatbot local usando [Ollama](https://ollama.com) y el modelo `gemma:2b`.

### 🚩 Requisitos

* Windows 10/11 o Linux/macOS
* Python 3.10+
* Al menos 4 GB de RAM libre (modelo ligero recomendado)

### 🛠️ Instalar Ollama

1. Descargar desde: [https://ollama.com](https://ollama.com)
2. Instalar y verificar:

```bash
ollama --version
```

### 🪨 Descargar modelo Gemma 2b

```bash
ollama run gemma:2b
```

Esto descargará y ejecutará el modelo en background.

### 🔄 Ejecutar el chatbot local (Streamlit UI)

```bash
streamlit run examples/chat_streamlit.py
```

Se abrirá en: `http://localhost:8501`

Podrás chatear localmente con el modelo **sin conexión a Internet**.

---

## 🔮 Ejemplo básico (examples/basic\_completion.py)

```python
from utils.config_loader import Config
from models.gpt import GPTClient

config = Config()
gpt_cfg = config.llms['gpt']

client = GPTClient(api_key=gpt_cfg['api_key'], model=gpt_cfg['model'])

respuesta = client.complete("Contame un chiste corto.")
print(respuesta)
```

---

## 📌 Buenas prácticas

* Separar prompts y lógica generativa en `services/` y `prompt_engineering/`
* Usar `config_loader.py` para no hardcodear claves
* Incluir ejemplos ejecutables
* Excluir `.env` y carpetas `data/` del repositorio con `.gitignore`

---

## 🧠 Modelos Soportados

* **Texto:** OpenAI GPT, Claude, Gemma (Ollama)
* **Imagen:** Stable Diffusion (Automatic1111)
* **Audio:** ElevenLabs TTS

---

## 📜 Licencia

Este proyecto está licenciado bajo la **Apache License 2.0**, una licencia permisiva que permite usar, modificar y redistribuir el código con fines personales o comerciales, con protección frente a reclamaciones de patentes.

* ✅ Uso personal y comercial permitido
* ✅ Se puede modificar y distribuir
* ✅ No obliga a publicar el código modificado
* ⚠️ Es necesario incluir el aviso de licencia original

Podés ver el texto completo en el archivo [`LICENSE`](LICENSE).

---

## 📧 Contacto

Si tienes preguntas o sugerencias, no dudes en contactarme a través de [mi web](https://javiermorron.com).

