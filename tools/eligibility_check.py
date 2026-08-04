from datetime import datetime

from models import ToolResult
from tools.order_lookup import OrderLookup


class EligibilityCheck:

    NON_RETURNABLE_CATEGORIES = {
        "innerwear",
        "jewellery",
        "beauty",
        "fragrance",
        "face masks",
        "gift cards",
        "socks",
    }

    def __init__(self, order_lookup: OrderLookup):
        self.order_lookup = order_lookup

    def check_eligibility(self, order_id: str) -> ToolResult:

        # Lookup Order
        order_result = self.order_lookup.lookup_order(order_id)

        if not order_result.status:
            return ToolResult(
                status=False,
                message="Order not found.",
                data=None
            )

        order = order_result.data

        
        # Status Checks
        
        if order.status == "cancelled":
            return ToolResult(
                status=False,
                message="Cancelled orders cannot be returned.",
                data=order
            )

        if order.status == "lost_in_transit":
            return ToolResult(
                status=False,
                message="Lost parcel claims must be handled by a human agent.",
                data=order
            )

        if order.status != "delivered":
            return ToolResult(
                status=False,
                message=f"Order cannot be returned because its current status is '{order.status}'.",
                data=order
            )

        
        # Delivery Date Check

        if order.delivered_at is None:
            return ToolResult(
                status=False,
                message="Delivery date not available.",
                data=order
            )

        days = (datetime.now().date() - order.delivered_at.date()).days

        if days > 30:
            return ToolResult(
                status=False,
                message="Return window has expired.",
                data=order
            )

        
        # Item Checks
        
        for item in order.items:

            # Final Sale
            if item.final_sale:
                return ToolResult(
                    status=False,
                    message="Final sale items are eligible for size exchange only.",
                    data=order
                )

            # Non-returnable Categories
            if item.category.lower() in self.NON_RETURNABLE_CATEGORIES:
                return ToolResult(
                    status=False,
                    message=f"{item.category.title()} items cannot be returned.",
                    data=order
                )

        
        # Eligible
        
        return ToolResult(
            status=True,
            message="Order is eligible for return.",
            data=order
        )