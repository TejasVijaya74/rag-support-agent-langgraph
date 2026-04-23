# rag-support-agent-langgraph

A Retrieval-Augmented Generation (RAG) based Customer Support Assistant built using LangGraph, ChromaDB, and LLMs.

## Features
- PDF-based knowledge ingestion
- Semantic search with embeddings
- Context-aware answer generation
- LangGraph workflow orchestration
- Conditional routing (answer vs escalation)
- Human-in-the-Loop (HITL) support

## Tech Stack
- FastAPI
- LangChain + LangGraph
- ChromaDB
- HuggingFace Embeddings
- OpenAI / LLM

## How it Works
1. Load and chunk PDF documents  
2. Store embeddings in vector database  
3. Retrieve relevant context for queries  
4. Generate answers using LLM  
5. Route responses or escalate to human  

## Run Locally
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Example
```bash
POST /query
{
  "query": "What is your refund policy?"
}
