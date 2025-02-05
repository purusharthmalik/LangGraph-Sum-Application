from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END

class Add(TypedDict):
    num1: int
    num2: int
    result: int

def add_numbers(state: Add) -> Add:
    num1 = state.get("num1")
    num2 = state.get("num2")
    return {"result": num1 + num2}

graph = StateGraph(Add)
graph.add_node("addition", add_numbers)
graph.add_edge(START, "addition")
graph.add_edge("addition", END)
app = graph.compile()

# inputs = {"num1": 5, "num2": 10}
# for num in app.stream(inputs, stream_mode=['values', 'updates', 'debug']):
#     print("Sum:", num)