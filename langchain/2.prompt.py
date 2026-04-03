from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2:1b")

# response=llm.invoke("What is the capital of France?") #input 타입 제한
# #Invalid input type <class 'int'>. Must be a PromptValue, str, or list of BaseMessages.

# print(response.content)

from langchain_core.prompts import PromptTemplate

prompt_template = PromptTemplate(
    input_variables=["country"],
    template="what is the capital of {country}?",
)

prompt = prompt_template.invoke({"country":"France"})

print(prompt)


response = llm.invoke(prompt)
print(response.content)


from langchain_core.messages import HumanMessage,SystemMessage,AIMessage

message_list=[
    SystemMessage(content="You are a helpful assistant!"),
    HumanMessage(content="What is the capital of France?"),
    AIMessage(content="The capital of France is Paris"),
    HumanMessage(content="What is the capital of Germany?"),
]

response2 = llm.invoke(message_list)
print(response2.content)

