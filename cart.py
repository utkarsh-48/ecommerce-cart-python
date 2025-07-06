import json
import os
cart_file = "cart_data.json"

def load_cart_data():
    if os.path.exists(cart_file):
        with open("cart_file","r") as f:
            return json.load(f)
    return {}
def save_data(data):
    with open("cart_file","w") as f:
         json.dump(data,f,indent=2)



def add_cart(cart,products):
    try:
        prod_id = int(input("Enter Product Id: "))
        quantity = int(input("Enter the quantity "))
        if quantity == 0:
            print("Quantity can`t be less than 1")
            return
        product = next(p for p in products if p ["id"] == prod_id)
        if not product:
            print("Product not found")
            return
        for item in cart:
            if item["id"] == prod_id:
                item["quantity"]+=quantity
                print(f"Updated the {item("name")} to quantity {item['quantity']}")
        cart.append({
            "id": product["id"],
            "name": product["name"],
            "price": product["price"],
            "quantity": quantity
        })
        print(f" Added {product['name']} x{quantity} to cart.")

    except ValueError:
        print("Invalid Quantity")


def remove_cart(cart):
    try:
        prod_id = int(input("Enter the Product ID: "))
        for item in cart:
            if item["id"] == prod_id:
                cart.remove(item)
                print(f"Removed {item["name"]} from cart")
                return
            else:
                print("item not found in cart ")
    except  ValueError:
        print("hello")

def view_cart(cart):
    if not cart:
        print("Your cart is empty ")
        return
    else:
        print("\n Your Cart: ")
        total = 0
        for item in cart:
            subtotal = item['quantity'] * item['price']
            print(f"- {item['name']} x{item['quantity']} @ ₹{item['price']:.2f} = ₹{subtotal:.2f}")
            total += subtotal

        print(f"\n Total: ₹{total:.2f}\n")

