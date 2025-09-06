from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st

# Define the prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries."),
        ("user", "Question: {question}")
    ]
)

# Streamlit UI
st.title("LangChain Demo with Gemma 2B")
input_text = st.text_input("Ask me anything")

# Call Gemma 2B through Ollama
llm = Ollama(model="gemma:2b")  # Open-source model
output_parser = StrOutputParser()
chain = prompt | llm | output_parser  # combine all

if input_text:
    response = chain.invoke({"question": input_text})
    st.write(response)
