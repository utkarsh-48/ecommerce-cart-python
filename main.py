from auth import login, register
from product_load import load_products
from cart import add_cart, remove_cart, view_cart, load_data, save_data
from checkout import checkout

def main():
    carts=load_data()
    print("Welcome to PythonCart ")
    products = load_products("prod.csv")
    user = None
    cart = []

    # Login/Sign Up
    while True:
        print("\n1.Login "
              "2. Create Account "
              "3. Exit")
        auth_option = int(input("Choose a option: "))
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
        try:
            cart=carts[user]
        except KeyError:
            carts[user] = cart
        print(f"\nLogged in as {user}")
        print("1. Add to Cart")
        print("2. Remove from Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Logout")

        choice = input("Enter option: ")

        if choice == "1":
            for p in products:
                print(f"{p['id']}: {p['name']} - ₹{p['price']} | {p['description']}")
            add_cart(cart,products)
        elif choice == "2":
            remove_cart(cart)
        elif choice == "3":
            view_cart(cart)
        elif choice == "4":
            checkout(cart)
        elif choice == "5":
            save_data(carts)
            print(f" Goodbye {user} ")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
