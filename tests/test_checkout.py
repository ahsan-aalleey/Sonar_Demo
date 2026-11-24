import unittest

from src import checkout


def make_order(status, items=None, urgent=False):
    return {"status": status, "items": items or [], "urgent": urgent}


class CheckoutTests(unittest.TestCase):
    def test_paid_orders(self):
        items = [
            {"qty": 1, "price": 200},
            {"qty": 1, "price": 60},
            {"qty": 1, "price": 10},
            {"qty": 0, "price": 10},
        ]
        result = checkout.process_orders([make_order("paid", items)])
        self.assertEqual(result, ["big", "medium", "small", "empty"])

    def test_pending_and_other_orders(self):
        orders = [make_order("pending", [1], True), make_order("cancelled")]
        self.assertEqual(checkout.process_orders(orders), ["rush", "skip"])

    def test_order_total(self):
        items = [{"qty": 2, "price": 10}, {"qty": 1, "price": 5}]
        self.assertEqual(checkout.order_total(items), 25)
