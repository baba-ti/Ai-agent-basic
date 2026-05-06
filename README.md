## Setup

Python 3.10++

```bash
pip install -r requirements.txt
```

```bash
pip install -U langgraph langchain-openai langchain-chroma
pip install -U ddgs arxiv pymupdf
pip install -U "langchain-google-community[gmail]"
```

## Environment Variables

```env
OPENAI_API_KEY=your_openai_key_here
UPSTAGE_API_KEY=your_upstage_key_here
PINECONE_API_KEY=your_pinecone_key_here
TAVILY_API_KEY=your_tavily_key_here
```

## Run Streamlit App

세금 문서 기반 RAG 챗봇 앱은 아래 명령으로 실행합니다.

```bash
streamlit run llm_application/Streamlist.py
```

## Run Notebooks

주요 폴더:

- `langchain/`: LangChain 기본 예제
- `llm_application/`: RAG 앱
- `langgraph/`: LangGraph, tool calling, human-in-the-loop
- `Huggingface-data/`: Hugging Face 기반

## Gmail Tool

Gmail tool을 실행하려면 Google Cloud에서 Gmail API를 활성화하고 OAuth credential을 준비

```text
langgraph/google/gmail_credentials.json
langgraph/google/gmail_token.json
```
