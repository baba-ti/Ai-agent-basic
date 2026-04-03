# langchain-basics

LangChain and Streamlit practice project for building a tax-focused RAG chatbot.

## Structure

- `langchain/`: basic LangChain example scripts
- `llm_application/`: Streamlit app and RAG application code
- `llm_application/Streamlist.py`: Streamlit chat UI entry point
- `llm_application/llm.py`: retrieval and LLM response pipeline

## Requirements

- Python 3.10+
- API keys configured in `.env`
- Required libraries for Streamlit, LangChain, Upstage, and Pinecone

## Environment Variables

Create a `.env` file in the project root and add the keys your environment requires.

Example:

```env
UPSTAGE_API_KEY=your_key_here
PINECONE_API_KEY=your_key_here
```

Do not commit `.env`. It is ignored by `.gitignore`.

## Run

Install dependencies, then start the Streamlit app:

```bash
streamlit run llm_application/Streamlist.py
```

## Notes

- The app loads environment variables with `python-dotenv`.
- The current retrieval pipeline uses Pinecone and Upstage models.
