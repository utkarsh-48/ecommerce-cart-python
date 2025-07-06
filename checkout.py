def checkout(cart,username):
   if not cart:
       print("Your Cart is empty")
       return

   total = sum(item["price"] * item['quantity'] for item in cart)
   print(f"Your Total is: {total}")
   confirm = input("Confirm your order? (y/n): ")
   if confirm.lower() == "y":
       cart.clear()
       print("Order Placed, Thanks for Choosing us")
   else:
       print("Checkout Cancelled")
