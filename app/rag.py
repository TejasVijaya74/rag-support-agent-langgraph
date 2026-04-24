from groq import Groq
from app.config import GROQ_API_KEY, MODEL_NAME
from app.retriever import get_retriever

client = Groq(api_key=GROQ_API_KEY)
retriever = get_retriever()


def retrieve_context(query):
    docs = retriever.invoke(query)
    
    if not docs:
        return ""
    
    text = docs[0].page_content.replace("\n", " ")
    return text


def generate_answer(query, context):
    if not context.strip():
        return "I don't know"

    prompt = f"""
You are a customer support assistant.

Answer ONLY using the provided context.

Rules:
- Provide the COMPLETE answer from the context
- Include all important details
- Do NOT shorten to a single word
- Do NOT add explanations or notes
- Keep answer natural and user-friendly

Context:
{context}

Question:
{query}

Answer:
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}]
    )

    answer = response.choices[0].message.content.strip()

    #  Remove unwanted explanations
    if "Note:" in answer:
        answer = answer.split("Note:")[0].strip()

    return answer
