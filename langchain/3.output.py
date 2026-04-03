from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2:1b")

# response=llm.invoke("What is the capital of France?") #input 타입 제한
# #Invalid input type <class 'int'>. Must be a PromptValue, str, or list of BaseMessages.

# print(response.content)

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


prompt_template = PromptTemplate(
    input_variables=["country"],
    template="what is the capital of {country}? Return the name of the city only",
)

prompt = prompt_template.invoke({"country":"France"})

print(prompt)

ai_message = llm.invoke(prompt)
print(ai_message.content)

output_parser = StrOutputParser()

answer =output_parser.invoke(llm.invoke(prompt_template.invoke({"country":"France"})))

print(answer)

from langchain_core.output_parsers import JsonOutputParser

from pydantic import BaseModel, Field


