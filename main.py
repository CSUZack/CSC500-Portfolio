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
    
    def modify_item(self, itemName, itemQuantity):
        for item in self.cart_items:
            if item.item_name == itemName:
                item.item_quantity = itemQuantity
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
            elif selection == 'a':
                print("ADD ITEM TO CART")
                itemName = input("Enter the item name:\n")
                itemDescription = input("Enter the item description:\n")
                itemQuantity = int(input("Enter the item quantity:\n"))
                itemPrice = float(input("Enter the item price:\n"))
                shopping_cart.add_item(ItemToPurchase(itemName, itemDescription, itemPrice, itemQuantity))
            elif selection == 'r':
                print("REMOVE ITEM FROM CART")
                itemName = input("Enter name of the item to remove:\n")
                shopping_cart.remove_item(itemName)
            elif selection == 'c':
                print("CHANGE ITEM QUANTITY")
                itemName = input("Enter name of the item to change:\n")
                itemQuantity = int(input("Enter the new quantity:\n"))
                shopping_cart.modify_item(itemName, itemQuantity)

        else:
            print("Please make a valid selection")
        


carrots = ItemToPurchase("carrot", "baby carrots", 5.5, 3)
lettuce = ItemToPurchase("lettuce", "head of lettuce", 3.1, 1)
bread = ItemToPurchase("bread", "loaf of bread", 4.2, 2)
cheese = ItemToPurchase("cheese", "sliced cheddar cheese", 4.5, 3)


shoppingCartName = input("Please enter your name:\n")
shoppingCartDate = input("Please enter the current date:\n")
print(f"Customer Name: {shoppingCartName}")
print(f"Current Date: {shoppingCartDate}")

myShoppingCart = ShoppingCart(shoppingCartName + "'s Shopping Cart", shoppingCartDate)

print_menu(myShoppingCart)