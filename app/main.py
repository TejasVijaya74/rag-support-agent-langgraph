from fastapi import FastAPI
from app.graph import build_graph

app = FastAPI()
graph = build_graph()


@app.get("/")
def home():
    return {"message": "RAG Support Assistant Running"}


@app.post("/query")
def query_bot(query: str):
    print("Received query:", query)

    result = graph.invoke({"query": query})

    print("Final result:", result)

    return {"response": result["answer"]}