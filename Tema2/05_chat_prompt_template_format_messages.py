"""05_chat_prompt_template_format_messages.py — Construir mensajes de chat (system/human) con ChatPromptTemplate."""

from langchain_core.prompts import ChatPromptTemplate

SYSTEM_PROMPT = "Eres un traductor del español al inglés muy preciso."
TEXT = "Hola mundo, ¿cómo estás?"


def main() -> None:
    chat_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", SYSTEM_PROMPT),
            ("human", "{text}"),
        ]
    )

    messages = chat_prompt.format_messages(text=TEXT)

    for message in messages:
        print(f"{type(message).__name__}: {message.content}")


if __name__ == "__main__":
    main()
