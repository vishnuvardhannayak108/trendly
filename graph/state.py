from typing import Annotated, Optional, TypedDict

from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages


class GraphState(TypedDict):
    """
    State shared between all LangGraph nodes.
    """

    # Complete conversation history
    messages: Annotated[list[BaseMessage], add_messages]

    # Chat session id
    session_id: str

    # Current order being processed
    order_id: Optional[str]

    # Output from the last executed tool
    tool_result: Optional[dict]

    # Whether the conversation has been escalated
    escalated: bool