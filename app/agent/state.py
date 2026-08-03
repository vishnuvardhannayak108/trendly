from langchain_core.messages import (
    BaseMessage,
    HumanMessage,
    AIMessage,
)

from typing import Dict, List


class ConversationState:
    """
    Manages conversation history for each user session.
    """

    def __init__(self):
        self.sessions: Dict[str, List[BaseMessage]] = {}

    def create_session(self, session_id: str):
        """
        Create a new session if it doesn't already exist.
        """
        if session_id not in self.sessions:
            self.sessions[session_id] = []

    def get_messages(self, session_id: str) -> List[BaseMessage]:
        """
        Return all messages for a session.
        """
        self.create_session(session_id)
        return self.sessions[session_id]

    def add_user_message(self, session_id: str, message: str):
        """
        Add a user message to the conversation history.
        """
        self.create_session(session_id)

        self.sessions[session_id].append(
            HumanMessage(content=message)
        )

    def add_ai_message(self, session_id: str, message: str):
        """
        Add an AI message to the conversation history.
        """
        self.create_session(session_id)

        self.sessions[session_id].append(
            AIMessage(content=message)
        )

    def clear_session(self, session_id: str):
        """
        Remove a conversation session.
        """
        if session_id in self.sessions:
            del self.sessions[session_id]

    def session_exists(self, session_id: str) -> bool:
        """
        Check whether a session exists.
        """
        return session_id in self.sessions