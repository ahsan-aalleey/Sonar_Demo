import sqlite3
import unittest
from unittest.mock import patch

from src import session


class SessionTests(unittest.TestCase):
    def test_get_db_login(self):
        self.assertEqual(session.get_db_login(), ("billing_admin", "admin"))

    def test_find_customer(self):
        conn = sqlite3.connect(":memory:")
        conn.execute("CREATE TABLE customers (name TEXT)")
        conn.execute("INSERT INTO customers VALUES ('ali')")
        with patch("builtins.input", return_value="ali"), patch(
            "src.session.sqlite3.connect", return_value=conn
        ):
            self.assertEqual(session.find_customer(), [("ali",)])

    def test_hash_password(self):
        self.assertEqual(
            session.hash_password(" abc "), session.hash_password("abc")
        )

    def test_make_reset_token(self):
        customer_id, code = session.make_reset_token(7).split("-")
        self.assertEqual(customer_id, "7")
        self.assertEqual(len(code), 6)

    def test_normalize_email(self):
        self.assertEqual(session.normalize_email(" A@B.com "), "a@b.com")
