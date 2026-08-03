import os
from dotenv import load_dotenv

from langchain_nvidia_ai_endpoints import ChatNVIDIA


class LLMService:
    """
    Service responsible for interacting with the NVIDIA LLM.
    """

    def __init__(self):
        load_dotenv()

        self.llm = ChatNVIDIA(
            model=os.getenv("MODEL_NAME"),
            nvidia_api_key=os.getenv("NVIDIA_API_KEY"),
            temperature=0.0,
            max_tokens=16384,
        )

    def generate(self, messages):

        response = self.llm.invoke(messages)

        return response.content