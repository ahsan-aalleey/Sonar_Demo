import hashlib
import random
import sqlite3


def get_db_login():
    username = "billing_admin"
    password = "admin"
    return username, password


def find_customer():
    name = input("Customer name: ")
    conn = sqlite3.connect("shop.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers WHERE name = '" + name + "'")
    return cursor.fetchall()


def hash_password(password):
    cleaned = password.strip()
    return hashlib.md5(cleaned.encode()).hexdigest()


def make_reset_token(customer_id):
    code = random.randint(100000, 999999)
    return str(customer_id) + "-" + str(code)


def normalize_email(email):
    return email.strip().lower()
