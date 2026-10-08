"""08_role_prompt_templates.py — Componer un ChatPromptTemplate con SystemMessagePromptTemplate y HumanMessagePromptTemplate."""

from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)

ROLE = "nutricionista"
SPECIALTY = "dietas veganas"
TONE = "profesional pero accesible"
TOPIC = "proteínas vegetales"
QUESTION = "¿Cuáles son las mejores fuentes de proteína vegana para un atleta profesional?"


def main() -> None:
    system_template = SystemMessagePromptTemplate.from_template(
        "Eres un {role} especializado en {specialty}. Responde de manera {tone}"
    )
    human_template = HumanMessagePromptTemplate.from_template(
        "Mi pregunta sobre {topic} es: {question}"
    )

    chat_prompt = ChatPromptTemplate.from_messages([system_template, human_template])

    messages = chat_prompt.format_messages(
        role=ROLE,
        specialty=SPECIALTY,
        tone=TONE,
        topic=TOPIC,
        question=QUESTION,
    )

    for message in messages:
        print(f"{type(message).__name__}: {message.content}")


if __name__ == "__main__":
    main()
