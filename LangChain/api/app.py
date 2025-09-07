from fastapi import FastAPI
from langchain.prompts import PromptTemplate
from langserve import add_routes
import uvicorn
from langchain_community.llms import Ollama

app = FastAPI(
    title="Langchain server",
    version="1.0",
    description="A simple API Server",
    openapi_url=None,   
    docs_url=None,     
    redoc_url=None      
)

# Use Ollama with gemma:2b
llm = Ollama(model="gemma:2b")

# Prompts
prompt1 = PromptTemplate.from_template(
    "Write me an essay about {topic} with 100 words"
)
prompt2 = PromptTemplate.from_template(
    "Write me a poem about {topic} with 100 words"
)

# Routes
add_routes(app, prompt1 | llm, path="/essay")
add_routes(app, prompt2 | llm, path="/poem")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
