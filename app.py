import streamlit as st
from rag.chatbot import ask_question

st.set_page_config(
    page_title="HBT AI Knowledge Assistant",
    page_icon="🤖"
)

st.title("HBT AI Knowledge Assistant")

question = st.text_input(
    "Ask a question about HBT"
)

if question:

    with st.spinner("Thinking..."):

        answer = ask_question(question)

    st.write(answer)