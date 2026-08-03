from services.order_service import OrderService
from models import ToolResult



class OrderLookup:
    def __init__(self, order_service: OrderService):
        self.order_service = order_service

    def lookup_order(self, order_id: str) -> ToolResult:
        order = self.order_service.get_order(order_id)
        if order:
            return ToolResult(status=True,
                              message="Order found",
                              data=order
                              )
        else:
            return ToolResult(status=False,
                              message="Order not found",
                              data=None
                              )