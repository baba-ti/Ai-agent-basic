from langchain_upstage import UpstageEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_upstage import ChatUpstage
from langchain_classic import hub
from langchain_classic.chains import RetrievalQA
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

def get_ai_message(user_message):

    embedding = UpstageEmbeddings(model='solar-embedding-1-large')

    index_name ='tax-with-markdown' #'tax-table-index' #'tax-upstage-index'

    database = PineconeVectorStore.from_existing_index(embedding = embedding, index_name = index_name)

    llm = ChatUpstage()

    prompt = hub.pull("rlm/rag-prompt")
    retriever=database.as_retriever()


    retriever=database.as_retriever()

    qa_chain = RetrievalQA.from_chain_type(
        llm,
        retriever=retriever, 
        chain_type_kwargs={"prompt":prompt},
    )

    dictionary = ["사람을 나타내는 표현 -> 거주자"]

    prompt = ChatPromptTemplate.from_template(f"""
        사용자의 질문을 보고, 우리의 사전을 참고해서 사용자의 질문을 변경해주세요.
        만약 변경할 필요가 없다고, 판단된다면, 사용자의 질문을 변경하지 않아도 됩니다.
        사전: {dictionary}
        """)

    dictionary_chain = prompt | llm | StrOutputParser()

    tax_chain = {"query": dictionary_chain} | qa_chain
    ai_message = tax_chain.invoke({"question":user_message})
    return ai_message["result"]