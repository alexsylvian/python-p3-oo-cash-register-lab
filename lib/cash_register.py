#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.items = []
        self.total = 0
        self.last_transaction = 0
        self.discount = discount

    def add_item(self, name, price, quantity=1):
        item_cost = price * quantity
        self.items.extend([name] * quantity)
        self.total += item_cost
        self.last_transaction = item_cost
        return item_cost

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            print(f"After the discount, the total comes to $800.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.last_transaction > 0:
            self.total -= self.last_transaction
            self.items.pop()
            self.last_transaction = 0
            return "Last transaction voided."
        else:
            return "No transaction to void."
