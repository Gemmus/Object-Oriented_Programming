class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity


item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 1000, 3)

print(f'Total value of Phone : {item1.calculate_total_price()}')
print(f'Total value of Laptop: {item2.calculate_total_price()}')