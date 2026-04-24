from langchain_community.document_loaders import PyPDFLoader


def ingest_pdf():
    print("Loading PDF...")

    loader = PyPDFLoader("data/knowledge.pdf")
    docs = loader.load()

    full_text = "\n".join([doc.page_content for doc in docs])

    # Split by questions
    qa_pairs = full_text.split("Q:")

    chunks = []
    for qa in qa_pairs:
        qa = qa.strip()
        if qa:
            chunks.append("Q: " + qa)

    print(f"Created {len(chunks)} Q&A chunks")

    from langchain_huggingface import HuggingFaceEmbeddings
    from langchain_chroma import Chroma

    embedding = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    vectordb = Chroma.from_texts(
        texts=chunks,
        embedding=embedding,
        persist_directory="vectorstore"
    )

    print("Vector DB created ")