"""04_prompt_template_format.py — Rellenar un PromptTemplate con .format() sin invocar ningún modelo."""

from langchain_core.prompts import PromptTemplate

TEMPLATE = "Eres un experto en marketing. Sugiere un eslogan creativo para un producto {product}"
PRODUCT = "café orgánico"


def main() -> None:
    prompt = PromptTemplate(template=TEMPLATE, input_variables=["product"])

    filled_prompt = prompt.format(product=PRODUCT)
    print(filled_prompt)


if __name__ == "__main__":
    main()
