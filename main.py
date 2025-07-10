from auth import login, register
from product_load import load_products
from cart import add_cart, remove_cart, view_cart
from checkout import checkout

def main():
    print("Welcome to PythonCart ")
    products = load_products("prod.csv")
    user = None
    cart = []

    # Login/Sign Up
    while True:
        print("\n1. Login "
              "2. Create Account "
              "3. Exit")
        try:
            auth_option = int(input("Choose an option: "))
        except ValueError:
            print("Invalid input. Try again.")
            continue
        if auth_option == 1:
            user = login()
            if user:
                break
        elif auth_option == 2:
            user = register()
            break
        elif auth_option == 3:
            print("Goodbye!")
            exit()
        else:
            print("Invalid input. Try again.")

    # Shopping
    while True:
        print(f"\nLogged in as {user}")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. Remove from Cart")
        print("4. View Cart")
        print("5. Checkout")
        print("6. Logout")

        choice = input("Enter option: ")

        if choice == "1":
            for p in products:
                print(f"{p['id']}: {p['name']} - ₹{p['price']:.2f} | {p['description']}")
        elif choice == "2":
            add_cart(cart, products)
        elif choice == "3":
            remove_cart(cart)
        elif choice == "4":
            view_cart(cart)
        elif choice == "5":
            checkout(cart, user)
        elif choice == "6":
            print(f"Goodbye {user}")
            cart.clear()
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()