class ItemToPurchase:
    def __init__(self, name="none", description="none", price=0.0, quantity=0):
        self.item_name = name
        self.description = description
        self.item_price = price
        self.item_quantity = quantity
    
    def print_item_cost(self):
        print(f"{self.item_name} x {self.item_quantity} @ {self.item_price} = {self.total_cost}")
    
    @property
    def total_cost(self):
        return self.item_price * self.item_quantity

class ShoppingCart:
    def __init__(self, customer_name="none", date="January 1, 2020"):
        self.customer_name = customer_name
        self.date = date
        self.cart_items = []
    
    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)
    
    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing modified.")
    
    def modify_item(self, ItemToPurchase):
        for item in self.cart_items:
            if item.item_name == ItemToPurchase.item_name:
                item.item_price = ItemToPurchase.item_price if ItemToPurchase.item_price != 0.0 else item.item_price
                item.description = ItemToPurchase.description if ItemToPurchase.description != "none" else item.description
                item.item_quantity = ItemToPurchase.item_quantity if ItemToPurchase.item_quantity != 0 else item.item_quantity
                return
        print("Item not found in cart. Nothing modified")
    
    def get_num_items_in_cart(self):
        return len(self.cart_items)
    
    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.total_cost
        return total_cost

    def print_total(self):
        print(f"{self.customer_name} - {self.date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        for item in self.cart_items:
            item.print_item_cost()
        if self.get_num_items_in_cart() > 0:
            print(f"TOTAL COST: ${self.get_cost_of_cart()}")
        else:
            print("SHOPPING CART IS EMPTY")
    
    def print_descriptions(self):
        print(f"{self.customer_name} - {self.date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.description}")

def print_menu(shopping_cart):
    while True:
        selection = input("""           MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit\n""")
        
        if selection in ['a', 'r', 'c', 'i', 'o', 'q']:
            if selection == 'q':
                print("Thank you for using my program")
                exit()
            elif selection == 'i':
                shopping_cart.print_descriptions()
            elif selection == 'o':
                shopping_cart.print_total()
        else:
            print("Please make a valid selection")
        

my_shopping_cart = ShoppingCart("Zack's Grocery Store", "August 25, 2024")

carrots = ItemToPurchase("carrot", "baby carrots", 5.5, 3)
lettuce = ItemToPurchase("lettuce", "head of lettuce", 3.1, 1)
bread = ItemToPurchase("bread", "loaf of bread", 4.2, 2)
cheese = ItemToPurchase("cheese", "sliced cheddar cheese", 4.5, 3)

my_shopping_cart.add_item(carrots)
my_shopping_cart.add_item(lettuce)
my_shopping_cart.add_item(bread)
my_shopping_cart.add_item(cheese)

print_menu(my_shopping_cart)