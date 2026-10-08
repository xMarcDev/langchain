"""01_invocar_chat_model.py — Ejemplo mínimo de LangChain: enviar una pregunta a un modelo de OpenAI."""

import os
import sys

from langchain_openai import ChatOpenAI

MODEL_NAME = "gpt-4o-mini"
TEMPERATURE = 0.7
QUESTION = "¿En qué año llegó el ser humano a la Luna por primera vez?"


def main() -> None:
    if not os.getenv("OPENAI_API_KEY"):
        sys.exit("Falta la variable de entorno OPENAI_API_KEY.")

    llm = ChatOpenAI(model=MODEL_NAME, temperature=TEMPERATURE)

    print(f"Pregunta: {QUESTION}")
    response = llm.invoke(QUESTION)
    print(f"Respuesta del modelo: {response.content}")


if __name__ == "__main__":
    main()
