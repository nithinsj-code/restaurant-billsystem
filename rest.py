print("Welcome to Nithin's Restaurant")
print("You can manage your bills here.")
print("------------------------------") 
print("You can add the items to your cart and generate the bill at the end.")
print("Let's get started!")
print("Choose item to add to cart or Type 'done' to generate bill.")
print("Here is the menu:")
menu = {
    "Idli": 20,
    "Dosa": 30,
    "Roast": 50,
    "Pongal": 40,
    "Biriyani": 120
}

for item, price in menu.items():
    print(f"{item}: Rs.{price}")
cart = {}
while True:
    item = input("Enter item name (or 'done' to finish): ")
    if item.lower() == 'done':
        break
    if item in menu:
        quantity = int(input(f"Enter quantity of {item}: "))
        if item in cart:
            cart[item] += quantity
        else:
            cart[item] = quantity
        print(f"Added {quantity} x {item} to cart.")
    else:
        print("Item not found in menu. Please try again.")
print("\nGenerating your bill...")
total = 0
print("\n--- BILL DETAILS ---")
for item, quantity in cart.items():
    price = menu[item]
    item_total = price * quantity
    total += item_total
    print(f"{item} x {quantity} @ Rs.{price} each: Rs.{item_total}")
print(f"Total Amount: Rs.{total}")
print("Thank you for dining with us!")

