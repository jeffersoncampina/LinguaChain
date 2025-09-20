from dotenv import load_dotenv
import os
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
chave_api = os.getenv("OPENAI_API_KEY")

mensagens = [
    SystemMessage("Traduza o texto à seguir para inglês"),
    HumanMessage("Se inscrevam no canal para aprender Python")
]

modelo = ChatOpenAI(model = "gpt-3.5-turbo")
parser = StrOutputParser()
chain = modelo | parser

template_mensagem = ChatPromptTemplate.from_messages([
    ("system", "Traduza o texto para {idioma}"),
    ("user", "{texto}"),
])

# template_mensagem.invoke({"idioma": "francês", "texto": "Dê like no vídeo e comente o que você tá achando"})

chain = template_mensagem | modelo | parser

# texto = chain.invoke({"idioma": "francês", "texto": "Dê like no vídeo e comente o que você tá achando"})

# print(texto)