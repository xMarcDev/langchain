"""07_messages_placeholder_historial.py — Insertar un historial de conversación en un ChatPromptTemplate con MessagesPlaceholder."""

from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

SYSTEM_PROMPT = "Eres un asistente útil que mantiene el contexto de la conversación."
CURRENT_QUESTION = "¿Puedes decirme algo interesante de su arquitectura?"

# Simulamos un historial de conversación
CONVERSATION_HISTORY = [
    HumanMessage(content="Usuario: ¿Cuál es la capital de Francia?"),
    AIMessage(content="IA: La capital de Francia es París."),
    HumanMessage(content="Usuario: ¿Y cuántos habitantes tiene?"),
    AIMessage(
        content="IA: París tiene aproximadamente 2.2 millones de habitantes "
        "en la ciudad propiamente dicha."
    ),
]


def main() -> None:
    chat_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", SYSTEM_PROMPT),
            MessagesPlaceholder(variable_name="history"),
            ("human", "Usuario: {current_question}"),
        ]
    )

    messages = chat_prompt.format_messages(
        history=CONVERSATION_HISTORY,
        current_question=CURRENT_QUESTION,
    )

    for message in messages:
        print(f"{type(message).__name__}: {message.content}")


if __name__ == "__main__":
    main()
