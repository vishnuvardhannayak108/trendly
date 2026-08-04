from fastapi import APIRouter, HTTPException
from langchain_core.messages import HumanMessage

from models import ChatRequest, ChatResponse
from graph.graph import graph

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.post(
    "",
    response_model=ChatResponse
)
def chat(request: ChatRequest):

    try:

        state = {
            "messages": [
                HumanMessage(
                    content=request.message
                )
            ],
            "session_id": request.session_id,
            "order_id": None,
            "tool_result": None,
            "escalated": False
        }

        result = graph.invoke(state)

        ai_message = result["messages"][-1]

        return ChatResponse(
            reply=ai_message.content,
            escalated=result.get("escalated", False)
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )