"""cv_evaluator.py — Evaluador de CVs: prompt de reclutador | LLM con salida estructurada (AnalisisCV)."""

from functools import lru_cache
from typing import Callable

from langchain_openai import ChatOpenAI

from models.cv_model import AnalisisCV
from prompts.cv_prompts import crear_sistema_prompts

MODEL_NAME = "gpt-4o-mini"
TEMPERATURE = 0.7
MAX_TOKENS = 1500


@lru_cache(maxsize=1)
def crear_evaluador_cv() -> Callable[[str, str], AnalisisCV]:
    """Crea un evaluador de CVs con LangChain y OpenAI.

    Devuelve una función `evaluar_cv(texto_cv, descripcion_puesto)` que retorna un AnalisisCV.
    """
    llm = ChatOpenAI(model=MODEL_NAME, temperature=TEMPERATURE, max_tokens=MAX_TOKENS)
    structured_llm = llm.with_structured_output(AnalisisCV)

    chain = crear_sistema_prompts() | structured_llm

    def evaluar_cv(texto_cv: str, descripcion_puesto: str) -> AnalisisCV:
        """Evalúa un CV frente a la descripción de un puesto y devuelve un análisis estructurado."""
        return chain.invoke(
            {"descripcion_puesto": descripcion_puesto, "texto_cv": texto_cv}
        )

    return evaluar_cv


def evaluar_candidato(texto_cv: str, descripcion_puesto: str) -> AnalisisCV:
    """Evalúa un CV reutilizando un único evaluador (se crea la primera vez que se llama)."""
    return crear_evaluador_cv()(texto_cv, descripcion_puesto)
