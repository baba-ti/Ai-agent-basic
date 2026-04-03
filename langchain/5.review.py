from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2:1b",
    temperature=0,
)


# 음식 이름 찾기
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

food_prompt = PromptTemplate(
    template= '''what is one of the most popular food in {country}?Please return the name of the food only''',
    input_variables= ['country']
)


food_chain = food_prompt | llm | StrOutputParser()

result =food_chain.invoke({'country': 'South korea'})

print(result)

from langchain_core.prompts import ChatPromptTemplate

recipe_prompt = ChatPromptTemplate.from_messages([
    ('system', '''Provide the recipe of the food that the user wants. Please return the recipe only as a numbered list'''),
    ('human', 'Can you give me the recipe for making {food}?')
])

recipe_chain = recipe_prompt | llm | StrOutputParser()

result2 =recipe_chain.invoke({'food':'bibimbap'})
print(result2)

final_chain = {'food' : food_chain} | recipe_chain

result3 = final_chain.invoke({'country':'France'})

print(result3)