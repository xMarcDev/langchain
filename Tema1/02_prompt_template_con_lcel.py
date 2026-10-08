"""02_prompt_template_con_lcel.py — Encadenar un PromptTemplate con un modelo de OpenAI usando LCEL (prompt | llm)."""

import os
import sys

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

MODEL_NAME = "gpt-4o-mini"
TEMPERATURE = 0.7
USER_NAME = "David"

PROMPT_TEMPLATE = (
    "Saluda al usuario con su nombre.\n"
    "Nombre del usuario: {name}\n"
    "Asistente:"
)


def main() -> None:
    if not os.getenv("OPENAI_API_KEY"):
        sys.exit("Falta la variable de entorno OPENAI_API_KEY.")

    llm = ChatOpenAI(model=MODEL_NAME, temperature=TEMPERATURE)
    prompt = PromptTemplate(input_variables=["name"], template=PROMPT_TEMPLATE)

    chain = prompt | llm

    print(f"Nombre del usuario: {USER_NAME}")
    response = chain.invoke({"name": USER_NAME})
    print(f"Respuesta del modelo: {response.content}")


if __name__ == "__main__":
    main()
