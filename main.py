class ItemToPurchase:
    def __init__(self, name="none", price=0.0, quantity=0):
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity
    
    def print_item_cost(self):
        print(f"{self.item_name} x {self.item_quantity} @ {self.item_price} = {self.total_cost}")
    
    @property
    def total_cost(self):
        return self.item_price * self.item_quantity

item1 = ItemToPurchase()
item1.item_name = input("Please enter the name of the first item:")
item1.item_price = float(input("Please enter the price of the first item:"))
item1.item_quantity = int(input("Please enter the quantity of the first item:"))

item2 = ItemToPurchase()
item2.item_name = input("Please enter the name of the second item:")
item2.item_price = float(input("Please enter the price of the second item:"))
item2.item_quantity = int(input("Please enter the quantity of the second item:"))

print("\n")
print("TOTAL COST")
item1.print_item_cost()
item2.print_item_cost()
print(f"Total: ${item1.total_cost + item2.total_cost}\n")