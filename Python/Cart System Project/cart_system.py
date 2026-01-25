# cart_system.py

cart = {}

print("Welcome to the Cart System")
print("===========================\n")


def add_to_cart():
    product = input("Enter product name to add in the cart: ")
    qty = int(input("Enter quantity: "))
    cart[product] = qty
    print(f"{product} has been added to the cart.")


def update_cart():
    product = input("Enter the product to update: ")
    qty = int(input("Enter new quantity: "))
    cart[product] = qty
    print(f"{product} updated successfully.")


def remove_from_cart():
    product = input("Enter product to remove: ")
    if product in cart.keys():
        cart.pop(product)
        print(f"{product} has been removed.")
    else:
        print("Product not found in the cart.")


def view_cart():
    if cart:
        print("\nCurrent items in the cart:")
        for p, q in cart.items():
            print(f"{p}: {q}")
    else:
        print("The cart is empty.")


def main():
    Flag = True
    while Flag:
        print("====================")
        print("Cart menu:")
        print("====================")
        print("1. Add item to cart")
        print("2. Update item in cart")
        print("3. Remove item from cart")
        print("4. View cart")
        print("5. Buy and Exit")
        print("====================\n")

        user_choice = int(input("\nEnter your choice (1-5): "))

        if user_choice == 1:
            add_to_cart()
        elif user_choice == 2:
            update_cart()
        elif user_choice == 3:
            remove_from_cart()
        elif user_choice == 4:
            view_cart()
        elif user_choice == 5:
            print("Buy Successfully! Thank you for shopping.")
            Flag = False
        else:
            print("Invalid option, try again!")


main()
print("Exiting the Cart System. Goodbye!")
