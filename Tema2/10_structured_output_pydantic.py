"""10_structured_output_pydantic.py — Obtener una respuesta estructurada del modelo con with_structured_output y Pydantic."""

import os
import sys

from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

MODEL_NAME = "gpt-4o-mini"
TEMPERATURE = 0.6
TEXT_TO_ANALYZE = "Me encantó la nueva película de acción, tiene muchos efectos especiales y emoción."


class TextAnalysis(BaseModel):
    summary: str = Field(description="Resumen breve del texto.")
    sentiment: str = Field(description="Sentimiento del texto (Positivo, neutro o negativo)")


def main() -> None:
    if not os.getenv("OPENAI_API_KEY"):
        sys.exit("Falta la variable de entorno OPENAI_API_KEY.")

    llm = ChatOpenAI(model=MODEL_NAME, temperature=TEMPERATURE)
    structured_llm = llm.with_structured_output(TextAnalysis)

    print(f"Texto: {TEXT_TO_ANALYZE}")
    result = structured_llm.invoke(f"Analiza el siguiente texto: {TEXT_TO_ANALYZE}")
    print(f"Resultado: {result.model_dump_json()}")


if __name__ == "__main__":
    main()
