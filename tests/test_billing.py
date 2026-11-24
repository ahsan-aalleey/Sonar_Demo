import unittest

from src import billing


class BillingTests(unittest.TestCase):
    def test_can_pay(self):
        self.assertTrue(billing.can_pay(50, 100))
        self.assertFalse(billing.can_pay(150, 100))
        self.assertFalse(billing.can_pay(-5, 100))

    def test_average_payment(self):
        with self.assertRaises(ZeroDivisionError):
            billing.average_payment([10, 20])

    def test_has_items(self):
        self.assertFalse(billing.has_items({"items": [1, 2]}))

    def test_build_invoice(self):
        self.assertEqual(billing.build_invoice(100, 15), {"total": 115})

    def test_apply_tax(self):
        self.assertEqual(billing.apply_tax(200, 10), 220)
