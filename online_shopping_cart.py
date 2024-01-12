class ItemToPurchase:
    def __init__(self, item_name='none', item_price=0.0, item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        print("{} {} @ ${:.2f} = ${:.2f}".format(self.item_name, self.item_quantity, self.item_price, self.item_quantity * self.item_price))

    def print_item_description(self):
        print("{}: {}".format(self.item_name, self.item_description))

class ShoppingCart:
    def __init__(self, name="none", date="January 1, 2020"):
        self.cart_items = []
        self.name = name
        self.date = date

    def add_item(self, item_obj):
        self.cart_items.append(item_obj)

    def remove_item(self, item):
        count = 0
        for i in range(len(self.cart_items) - 1):
            if self.cart_items[i].item_name == item.item_name:
                del self.cart_items[i]
                count += 1
                break
        if count == 0:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, item_obj):
        for cart_item in self.cart_items:
            if cart_item.item_name == item_obj.item_name:
                if item_obj.item_price is not None:
                    cart_item.item_price = item_obj.item_price
                if item_obj.item_quantity is not None:
                    cart_item.item_quantity = item_obj.item_quantity
            else:
                print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total = 0
        for x in self.cart_items:
            total += x.item_quantity
        return total

    def get_cost_of_cart(self):
        total_cost = 0
        for i in self.cart_items:
            total_cost += i.item_price * i.item_quantity
        return total_cost

    def print_total(self):
        if len(self.cart_items) == 0:
            print("{}\'s Shopping Cart - {}".format(self.name, self.date))
            print("SHOPPING CART IS EMPTY")
        else:
            print("{}\'s Shopping Cart - {}".format(self.name, self.date))
            print("Number of Items: {}".format(self.get_num_items_in_cart()))
            for item in self.cart_items:
                item.print_item_cost()
            print("Total: ${:.2f}".format(self.get_cost_of_cart()))

    def print_descriptions(self):
        print("{}\'s Shopping Cart - {}".format(self.name, self.date))
        print()
        print("Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()