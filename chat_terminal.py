import os
from dotenv import load_dotenv
from openai import AzureOpenAI

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

def mini_chat(model: str):
    """
    Mini chatbot en modo consola. Mantiene historial de la conversación.
    """
    messages = [
        {
            "role": "system",
            "content": (
                "Eres un asistente experto en análisis de datos, estadística, "
                "valores faltantes y series de tiempo. Responde SIEMPRE en español."
            ),
        }
    ]

    print(f"=== Mini chatbot con Azure (modelo: {model}) ===")
    print("Escribe 'salir', 'exit' o 'quit' para terminar.\n")

    while True:
        user = input("Tú: ").strip()
        if user.lower() in ("salir", "exit", "quit"):
            print("Bot: ¡Hasta luego! 👋")
            break

        if not user:
            continue

        messages.append({"role": "user", "content": user})

        response = client.chat.completions.create(
            model=model,
            messages=messages,
            max_completion_tokens=300,  # límite de tokens de respuesta
        )

        answer = response.choices[0].message.content
        print(f"\nBot: {answer}\n")

        messages.append({"role": "assistant", "content": answer})

def main():
    mini_chat(deployment_name)

if __name__ == "__main__":
    main()
