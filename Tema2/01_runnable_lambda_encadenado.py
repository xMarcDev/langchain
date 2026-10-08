"""01_runnable_lambda_encadenado.py — Encadenar dos RunnableLambda con el operador | (LCEL)."""

from langchain_core.runnables import RunnableLambda

INPUT_NUMBER = 43


def format_number(number: int) -> str:
    return f"Numero {number}"


def duplicate_text(text: str) -> list[str]:
    return [text] * 2


def main() -> None:
    format_step = RunnableLambda(format_number)
    duplicate_step = RunnableLambda(duplicate_text)

    chain = format_step | duplicate_step

    print(f"Entrada: {INPUT_NUMBER}")
    result = chain.invoke(INPUT_NUMBER)
    print(f"Resultado: {result}")


if __name__ == "__main__":
    main()
