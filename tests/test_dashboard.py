import unittest

from src import dashboard


class DashboardTests(unittest.TestCase):
    def test_daily_sales_report(self):
        self.assertEqual(dashboard.daily_sales_report([2, 3, 1]), 2)

    def test_weekly_sales_report(self):
        self.assertEqual(dashboard.weekly_sales_report([2, 3, 1]), 2)

    def test_monthly_sales_report(self):
        self.assertEqual(dashboard.monthly_sales_report([2, 3, 1]), 2)
