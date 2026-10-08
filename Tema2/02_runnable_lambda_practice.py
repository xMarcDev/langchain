# Texto de entrada → Preprocesamiento → Análisis Completo → Resultado
#                                            ↙        ↘
#                                     Resumen    Sentimiento

import os
import sys
import json

from langchain_core.runnables import RunnableLambda
from langchain_openai import ChatOpenAI

MODEL_NAME = "gpt-4o-mini"
TEMPERATURE = 0
QUESTION = "¿En qué año llegó el ser humano a la Luna por primera vez?"


def main() -> None:
    if not os.getenv("OPENAI_API_KEY"):
        sys.exit("Falta la variable de entorno OPENAI_API_KEY.")

    llm = ChatOpenAI(model=MODEL_NAME, temperature=TEMPERATURE)

    # Preprocesador de Texto
    def preprocess_text(text):
        text = text.strip()[:500]  # Limita a 500 caracteres y elimina espacios extras
        return text

    # Convertir la función en un Runnable
    preprocessor = RunnableLambda(preprocess_text)

    # Generador de Resúmenes
    def generate_summary(text):
        """Genera un resumen conciso del texto"""
        prompt = f"Resume en una sola oración: {text}"
        response = llm.invoke(prompt)
        return response.content

    # Analizador de Sentimientos
    def analyze_sentiment(text):
        """Analiza el sentimiento y devuelve resultado estructurado"""
        prompt = f"""Analiza el sentimiento del siguiente texto.
        Responde ÚNICAMENTE en formato JSON válido:
        {{"sentimiento": "positivo|negativo|neutro", "razon": "justificación breve"}}
        
        Texto: {text}"""
        
        response = llm.invoke(prompt)
        try:
            return json.loads(response.content)
        except json.JSONDecodeError:
            return {"sentimiento": "neutro", "razon": "Error en análisis"}

    # Función de Combinación
    def merge_results(data):
        """Combina los resultados de ambas ramas en un formato unificado"""
        return {
            "resumen": data["resumen"],
            "sentimiento": data["sentimiento_data"]["sentimiento"],
            "razon": data["sentimiento_data"]["razon"]
        }

    # Función de Procesamiento Principal
    def process_one(t):
        resumen = generate_summary(t)              # Llamada 1 al LLM
        sentimiento_data = analyze_sentiment(t)    # Llamada 2 al LLM
        return merge_results({
            "resumen": resumen,
            "sentimiento_data": sentimiento_data
        })
    
    # Convertir en Runnable
    process = RunnableLambda(process_one)

    # La cadena completa
    chain = preprocessor | process

    # Prueba con diferentes textos
    textos_prueba = [
        "¡Me encanta este producto! Funciona perfectamente y llegó muy rápido.",
        "El servicio al cliente fue terrible, nadie me ayudó con mi problema.",
        "El clima está nublado hoy, probablemente llueva más tarde."
    ]
    
    for texto in textos_prueba:
        resultado = chain.invoke(texto)
        print(f"Texto: {texto}")
        print(f"Resultado: {resultado}")
        print("-" * 50)


if __name__ == "__main__":
    main()

