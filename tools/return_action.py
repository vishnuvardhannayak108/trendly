from models import ToolResult, Orders


class ReturnAction:

    def create_return(self, order: Orders) -> ToolResult:

        return_data = {
            "order_id": order.order_id,
            "customer_id": order.customer_id,
            "return_status": "initiated",
            "pickup_required": True,
            "reverse_pickup": True,
            "pickup_attempts": 2
        }

        return ToolResult(
            status=True,
            message="Return request initiated successfully.",
            data=return_data
        )