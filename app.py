import os
from dotenv import load_dotenv
from openai import AzureOpenAI
import streamlit as st

# 1. Cargar variables de entorno
load_dotenv()

endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
api_key = os.getenv("AZURE_OPENAI_API_KEY")
deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-5-chat")

if not endpoint or not api_key:
    raise ValueError("Faltan AZURE_OPENAI_ENDPOINT o AZURE_OPENAI_API_KEY en el .env")

# 2. Crear cliente de Azure OpenAI
client = AzureOpenAI(
    api_version="2024-12-01-preview",
    azure_endpoint=endpoint,
    api_key=api_key,
)

# 3. Configuración básica de la app
st.set_page_config(page_title="Chatbot analítico (Azure)", page_icon="📊")

st.title("📊 Chatbot analítico")
st.caption("Modelo de Azure: **{}**".format(deployment_name))

# 4. Inicializar historial en session_state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": (
                "Eres un asistente experto en análisis de datos, estadística, "
                "valores faltantes y series de tiempo. Responde SIEMPRE en español."
            ),
        }
    ]

# 5. Mostrar historial (solo user/assistant, no system)
for msg in st.session_state.messages:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.markdown(msg["content"])
    elif msg["role"] == "assistant":
        with st.chat_message("assistant"):
            st.markdown(msg["content"])

# 6. Entrada del usuario
user_input = st.chat_input("Escribe tu pregunta de análisis de datos...")

if user_input:
    # Mostrar mensaje del usuario
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Llamar al modelo y mostrar respuesta
    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            response = client.chat.completions.create(
                model=deployment_name,
                messages=st.session_state.messages,
                max_completion_tokens=400,
            )
            answer = response.choices[0].message.content
            st.markdown(answer)

    # Guardar respuesta en el historial
    st.session_state.messages.append({"role": "assistant", "content": answer})
