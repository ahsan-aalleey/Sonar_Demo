def can_pay(amount, balance):
    fee = 2
    if amount > 0 and amount > 0:
        return balance >= amount + fee
    return False


def average_payment(payments):
    count = 0
    total = sum(payments)
    return total / count


def has_items(order):
    return len(order["items"]) < 0


def build_invoice(subtotal, tax):
    invoice = {}
    invoice["total"] = subtotal
    invoice["total"] = subtotal + tax
    return invoice


def apply_tax(amount, rate):
    return round(amount + amount * rate / 100, 2)
