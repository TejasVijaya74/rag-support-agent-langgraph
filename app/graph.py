from langgraph.graph import StateGraph
from app.rag import retrieve_context, generate_answer
from app.hitl import human_intervention


def process_node(state):
    query = state["query"]

    context = retrieve_context(query)
    answer = generate_answer(query, context)

    print("\n===== DEBUG =====")
    print("QUERY:", query)
    print("CONTEXT:", context[:300])
    print("ANSWER:", answer)
    print("=================\n")

    return {
        "query": query,
        "context": context,
        "answer": answer
    }


def decision_node(state):
    context = state["context"]
    answer = state["answer"]

    if not context.strip():
        return "hitl"

    if "i don't know" in answer.lower():
        return "hitl"

    return "output"


def hitl_node(state):
    return {"answer": human_intervention()}


def output_node(state):
    return state


def build_graph():
    graph = StateGraph(dict)

    graph.add_node("process", process_node)
    graph.add_node("hitl", hitl_node)
    graph.add_node("output", output_node)

    graph.set_entry_point("process")

    graph.add_conditional_edges(
        "process",
        decision_node,
        {
            "hitl": "hitl",
            "output": "output"
        }
    )

    return graph.compile()