from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llm import Ollama #whenever we are int 3rd party, it is inside langchain_community

import stramlit as st
import os
from dotenv import load_dotenv

load_dotenv()


##feature for langsmith tracking
os.environ["LANG_TRACKING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]= os.getenv("LANGCHAIN_API_KEY")


##defining the prompt template:
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries")
        ("user", "Question:{question}")
    ]
)

##streamlit framework

st.title("Langchain Demo with Llama2")
input_text= st.text_input("Search the topic you want")

#calling llms, OLlama , llama2

llm= Ollama(model= "llama2")
output_parser= StrOutputParser()
chain= prompt|llm|output_parser ##here we just combine all these things

if input_text:
    st.write(chain.invoke({'question':input_text}))
