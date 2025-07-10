def checkout(cart, user=None):
    if not cart:
        print("Your Cart is empty")
        return

    total = sum(item["price"] * item['quantity'] for item in cart)
    print(f"Your Total is: ₹{total:.2f}")
    confirm = input("Confirm your order? (y/n): ")
    if confirm.lower() in ("y", "yes"):
        cart.clear()
        print(f"Order Placed, Thanks for Choosing us{f', {user}' if user else ''}")
    else:
        print("Checkout Cancelled")