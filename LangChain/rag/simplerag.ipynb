
#data ingestion steps (eg read frm txt file)
from langchain_community.document_loaders import TextLoader
loader= TextLoader("speech.txt")
text_document= loader.load()
text_document


# web based loader
from langchain_community.document_loaders import WebBaseLoader
from bs4 import SoupStrainer

# load, chunk and index the content of the html page
loader = WebBaseLoader(
    web_paths=("https://lilianweng.github.io/posts/2023-06-23-agent/",),
    bs_kwargs=dict(
        parse_only=SoupStrainer(
            class_=("post-title", "post-content", "post-header")
        )
    )
)

text_documents = loader.load()

print(len(text_documents))
print(text_documents[0].page_content[:500])




