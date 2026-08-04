from langchain_core.tools import tool

from services.order_service import OrderService
from services.vector_store import VectorStoreService

from tools.order_lookup import OrderLookup
from tools.policy_search import PolicySearchTool
from tools.eligibility_check import EligibilityCheck
from tools.return_action import ReturnAction
from tools.escalate import Escalate


order_service = OrderService()
vector_store = VectorStoreService()

order_lookup = OrderLookup(order_service)

policy_search = PolicySearchTool(vector_store)

eligibility = EligibilityCheck(order_lookup)

return_action = ReturnAction()

escalate = Escalate()

@tool
def order_lookup_tool(order_id: str):
    """
    Tool to look up order details by order ID.
    """
    return order_lookup.lookup_order(order_id)

@tool
def policy_search_tool(query: str):
    """
    Tool to search for policy documents based on a query.
    """
    return policy_search.search_policy(query)   

@tool
def eligibility_check_tool(order_id: str):
    """
    Tool to check eligibility for a return based on order ID.
    """
    return eligibility.check_eligibility(order_id)

@tool
def create_return_tool(order_id: str):
    """
    Create a return request.
    """

    order = order_service.get_order(order_id)

    if not order:
        return "Order not found."

    return return_action.create_return(order)

@tool
def escalate_tool(issue_details: str):
    """
    Tool to escalate an issue based on provided details.
    """
    return escalate.escalate_issue(issue_details)


tools=[
    order_lookup_tool,
    policy_search_tool,
    eligibility_check_tool,
    create_return_tool,
    escalate_tool
]