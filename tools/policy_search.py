from services.vector_store import VectorStoreService
from models import ToolResult


class PolicySearchTool:

    def __init__(self, vector_service: VectorStoreService):
        self.vector_service = vector_service

    def search_policy(self, query: str) -> ToolResult:
        """
        Search the company policy using semantic search.

        Args:
            query: User's policy related question.

        Returns:
            ToolResult
        """

        results = self.vector_service.similarity_search(query)

        if not results:
            return ToolResult(
                status=False,
                message="No relevant policy found.",
                data=None
            )

        policy_chunks = [
            document.page_content
            for document in results
        ]

        return ToolResult(
            status=True,
            message="Relevant policy retrieved successfully.",
            data=policy_chunks
        )