from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition

from graph.state import GraphState
from graph.langchain_tools import tools

from services.llm import LLMService
from app.prompt.system_prompt import SystemPrompt

from langchain_core.messages import SystemMessage


llm = LLMService().llm.bind_tools(tools)


def assistant(state: GraphState):

    messages = state["messages"]

    response = llm.invoke(
        [
            SystemMessage(content=SystemPrompt),
            *messages
        ]
    )

    return {
        "messages": [response]
    }

tool_node = ToolNode(tools)


builder = StateGraph(GraphState)

builder.add_node("assistant", assistant)

builder.add_node("tools", tool_node)

builder.add_edge(
    START,
    "assistant"
)

builder.add_conditional_edges(
    "assistant",
    tools_condition
)

builder.add_edge(
    "tools",
    "assistant"
)


graph = builder.compile()