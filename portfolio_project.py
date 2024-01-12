from online_shopping_cart import ShoppingCart, ItemToPurchase

if __name__ == '__main__':
    def print_menu(cart):
        menu_options = {
            'a': "Add item to cart",
            'r': "Remove item from cart",
            'c': "Change item quantity",
            'i': "Output items' descriptions",
            'o': "Output shopping cart",
            'q': "Quit"
        }
        while True:
            print("\nMENU")
            for key, value in menu_options.items():
                print("{} - {}".format(key, value))
            print("\n")

            choice = input("Choose an option:\n")
            if choice == "q":
                break
            else:
                if choice in ["a", "r", "c", "i", "o", "q"]:

                    if choice == "a":
                        print("ADD ITEM TO CART")
                        item_name = input("Enter the item name:\n")
                        item_description = input("Enter the item description:\n")
                        item_quantity = int(input("Enter the item quantity:\n"))
                        item_price = float(input("Enter the item price:\n"))
                        item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
                        cart.add_item(item)

                    elif choice == "i":
                        print("OUTPUT ITEMS' DESCRIPTIONS")
                        cart.print_descriptions()

                    elif choice == "o":
                        print("OUTPUT SHOPPING CART")
                        cart.print_total()

                    elif choice == "r":
                        print("REMOVE ITEM FROM CART")
                        item_name = input("Enter name of item to remove:\n")
                        item = ItemToPurchase(item_name)
                        cart.remove_item(item)

                    elif choice == "c":
                        print("CHANGE ITEM QUANTITY")
                        item_name = input("Enter the item name:\n")
                        item_quantity = int(input("Enter the new quantity:\n"))
                        item = ItemToPurchase(item_name, None, item_quantity, None)
                        cart.modify_item(item)

                else:
                    choice = input("Choose an option:\n")

    name = input("Enter customer's name (ex. Abby Fleming):\n")
    date = input("Enter today's date (ex. December 23, 2023):\n")

    cart = ShoppingCart(name, date)

    print_menu(cart)