# from langchain_ollama import ChatOllama

# llm = ChatOllama(model="")

# response=llm.invoke("What is the capital of France?")

# print(response.content)

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

response=llm.invoke("What is the capital of France?") # OPEN_API_KEY

print(response.content)

