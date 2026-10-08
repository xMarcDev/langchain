"""11_structured_output_parser.py — Versión 2 del 10: respuesta estructurada con PydanticOutputParser (prompt | llm | parser)."""

import os
import sys

from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

MODEL_NAME = "gpt-4o-mini"
TEMPERATURE = 0.2
TEXT_TO_ANALYZE = "Me encantó la nueva película de acción, tiene efectos especiales increíbles."

PROMPT_TEMPLATE = """Analiza este texto cuidadosamente y proporciona un análisis estructurado:

{format_instructions}

TEXTO:
{text}

ANÁLISIS:"""


class TextAnalysis(BaseModel):
    summary: str = Field(description="Resumen breve del texto")
    sentiment: str = Field(description="Sentimiento: Positivo, Neutro o Negativo")
    keywords: list[str] = Field(description="3-5 palabras clave principales")


def build_chain():
    parser = PydanticOutputParser(pydantic_object=TextAnalysis)
    prompt = PromptTemplate(
        template=PROMPT_TEMPLATE,
        input_variables=["text"],
        partial_variables={"format_instructions": parser.get_format_instructions()},
    )
    llm = ChatOpenAI(model=MODEL_NAME, temperature=TEMPERATURE)
    return prompt | llm | parser


def main() -> None:
    if not os.getenv("OPENAI_API_KEY"):
        sys.exit("Falta la variable de entorno OPENAI_API_KEY.")

    chain = build_chain()

    print(f"Texto: {TEXT_TO_ANALYZE}")
    try:
        result = chain.invoke({"text": TEXT_TO_ANALYZE})
    except Exception as error:
        sys.exit(f"❌ Error: {error}")

    print("✅ Análisis exitoso:")
    print(result.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
