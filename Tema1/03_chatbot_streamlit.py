"""04_chatbot_streamlit_mensajes_directos.py — Chatbot con LangChain + Streamlit: historial construido
con AIMessage/HumanMessage/SystemMessage, sin PromptTemplate (se pasa la lista de mensajes directo al modelo)."""

import os

import streamlit as st
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

AVAILABLE_MODELS = ["gpt-4o-mini", "gpt-3.5-turbo", "gpt-4"]
DEFAULT_TEMPERATURE = 0.5
HISTORY_KEY = "messages"

SYSTEM_PROMPT = (
    "Eres un asistente útil y amigable llamado ChatBot Pro. "
    "Responde de manera clara y concisa."
)


def build_model(model_name: str, temperature: float) -> ChatOpenAI:
    return ChatOpenAI(model=model_name, temperature=temperature)


def render_history(messages: list[BaseMessage]) -> None:
    for message in messages:
        role = "assistant" if isinstance(message, AIMessage) else "user"
        with st.chat_message(role):
            st.markdown(message.content)


def stream_answer(chat_model: ChatOpenAI, question: str, history: list[BaseMessage]):
    """Genera la respuesta fragmento a fragmento (lo consume st.write_stream)."""
    messages = [SystemMessage(content=SYSTEM_PROMPT), *history, HumanMessage(content=question)]
    for chunk in chat_model.stream(messages):
        yield chunk.content


def main() -> None:
    st.set_page_config(page_title="Chatbot Básico", page_icon="🤖")
    st.title("🤖 Chatbot Básico con LangChain")
    st.markdown(
        "Este es un *chatbot de ejemplo* construido con LangChain + Streamlit. "
        "¡Escribe tu mensaje abajo para comenzar!"
    )

    if not os.getenv("OPENAI_API_KEY"):
        st.error("Falta la variable de entorno OPENAI_API_KEY.")
        st.stop()

    with st.sidebar:
        st.header("Configuración")
        temperature = st.slider("Temperatura", 0.0, 1.0, DEFAULT_TEMPERATURE, 0.1)
        model_name = st.selectbox("Modelo", AVAILABLE_MODELS)

    chat_model = build_model(model_name, temperature)

    if HISTORY_KEY not in st.session_state:
        st.session_state[HISTORY_KEY] = []
    history: list[BaseMessage] = st.session_state[HISTORY_KEY]

    render_history(history)

    if st.button("🗑️ Nueva conversación"):
        st.session_state[HISTORY_KEY] = []
        st.rerun()

    question = st.chat_input("Escribe tu mensaje:")
    if not question:
        return

    with st.chat_message("user"):
        st.markdown(question)

    try:
        with st.chat_message("assistant"):
            answer = st.write_stream(stream_answer(chat_model, question, history))
    except Exception as error:
        st.error(f"Error al generar respuesta: {error}")
        st.info("Verifica que tu API Key de OpenAI esté configurada correctamente.")
        return

    history.append(HumanMessage(content=question))
    history.append(AIMessage(content=answer))


main()
