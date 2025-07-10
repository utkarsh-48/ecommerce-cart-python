import json
import os

cart_file = "cart_data.json"

def load_cart_data():
    if os.path.exists(cart_file):
        with open(cart_file, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(cart_file, "w") as f:
        json.dump(data, f, indent=2)

def add_cart(cart, products):
    try:
        prod_id = int(input("Enter Product Id: "))
        quantity = int(input("Enter the quantity: "))
        if quantity < 1:
            print("Quantity can't be less than 1")
            return False
        product = next((p for p in products if p["id"] == prod_id), None)
        if not product:
            print("Product not found")
            return False
        for item in cart:
            if item["id"] == prod_id:
                item["quantity"] += quantity
                print(f"Updated the {item['name']} to quantity {item['quantity']}")
                return True
        cart.append({
            "id": product["id"],
            "name": product["name"],
            "price": product["price"],
            "quantity": quantity
        })
        print(f"Added {product['name']} x{quantity} to cart.")
        return True
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return False

def remove_cart(cart):
    try:
        prod_id = int(input("Enter the Product ID: "))
        for item in cart:
            if item["id"] == prod_id:
                cart.remove(item)
                print(f"Removed {item['name']} from cart")
                return True
        print("Item not found in cart.")
        return False
    except ValueError:
        print("Invalid input. Please enter a numeric Product ID.")
        return False

def view_cart(cart):
    if not cart:
        print("Your cart is empty.")
        return
    print("\nYour Cart:")
    total = 0
    for item in cart:
        subtotal = item['quantity'] * item['price']
        print(f"- {item['name']} x{item['quantity']} @ ₹{item['price']:.2f} = ₹{subtotal:.2f}")
        total += subtotal
    print(f"\nTotal: ₹{total:.2f}\n")