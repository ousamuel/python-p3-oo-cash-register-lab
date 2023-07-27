#!/usr/bin/env python3


class CashRegister:
    

    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.food_dict = {}

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.food_dict.update({title: price})
        i = 0
        while i < quantity:
            self.items.append(title)
            i += 1

    def apply_discount(self):
        if self.discount > 0:
            self.total = int(self.total * ((100 - self.discount) / 100))
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        i = 0
        count = self.items.count(self.items[-1])
        while i < count:

            self.total -= self.food_dict[self.items.pop(-1)]
            i += 1

        # self.total = 0
        # for food in self.food_dict:
        #     self.total+= (self.food_dict[food] * self.items.count(food))
        # self.apply_discount()
        #assumed discount needed to be factored in
    pass


abc = CashRegister(20)
abc.add_item("apple", 0.99, 3)
abc.add_item("tomato", 1.76, 5)
print(abc.total)

print(abc.food_dict)
print(abc.items)
abc.void_last_transaction()
print(abc.items)
print(abc.total)
