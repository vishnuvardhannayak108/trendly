import json
from models import Orders, Customer


class OrderService:
    def __init__(self):
        self.orders = {}
        self.customers = {}

        self.load_data()

    def load_data(self):
        with open("data/orders.json", "r") as file:
            data = json.load(file)

        # load customers
        for customer in data["customers"]:
            customer_obj = Customer(**customer)
            self.customers[customer_obj.customer_id] = customer_obj

        # load orders
        for order in data["orders"]:
            order_obj = Orders(**order)
            self.orders[order_obj.order_id] = order_obj

    def get_order(self, order_id: str):
        return self.orders.get(order_id)

    def get_customer(self, customer_id: str):
        return self.customers.get(customer_id)

    def get_orders_by_customer(self, customer_id: str):
        return [
            order
            for order in self.orders.values()
            if order.customer_id == customer_id
        ]