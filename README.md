# langchain-basics

LangChain, LangGraph, RAG, GPT API, Streamlit, external tools 연동을 실습한 저장소입니다.

## Setup

Python 3.10+ 환경을 권장합니다.

```bash
pip install -r requirements.txt
```

일부 LangGraph 노트북과 tool 실습은 추가 패키지가 필요할 수 있습니다.

```bash
pip install -U langgraph langchain-openai langchain-chroma
pip install -U ddgs arxiv pymupdf
pip install -U "langchain-google-community[gmail]"
```

## Environment Variables

프로젝트 루트에 `.env` 파일을 만들고 필요한 API key를 넣습니다.

```env
OPENAI_API_KEY=your_openai_key_here
UPSTAGE_API_KEY=your_upstage_key_here
PINECONE_API_KEY=your_pinecone_key_here
TAVILY_API_KEY=your_tavily_key_here
```

모든 실습에 모든 key가 필요한 것은 아닙니다. 실행하는 노트북이나 앱에서 사용하는 provider에 맞춰 넣으면 됩니다.

## Run Streamlit App

세금 문서 기반 RAG 챗봇 앱은 아래 명령으로 실행합니다.

```bash
streamlit run llm_application/Streamlist.py
```

## Run Notebooks

Jupyter 또는 VS Code에서 원하는 노트북을 열어 위에서부터 순서대로 실행합니다.

주요 폴더:

- `langchain/`: LangChain 기본 예제
- `llm_application/`: RAG 앱과 관련 노트북
- `langgraph/`: LangGraph, tool calling, human-in-the-loop 실습
- `Huggingface-data/`: Hugging Face 기반 실습

## Gmail Tool

Gmail tool을 실행하려면 Google Cloud에서 Gmail API를 활성화하고 OAuth credential을 준비해야 합니다.

필요한 파일 예시:

```text
langgraph/google/gmail_credentials.json
langgraph/google/gmail_token.json
```

`langgraph/google/`, `.env`, token 파일은 개인 인증 정보이므로 커밋하지 않습니다.
