# # 26) WAP to print numbers from 10 to 1
# n = 10
# while n >= 1:
#     print(n)
#     n -= 1

import random

print("Script is running...\n")

# List of famous Korean foods and drinks
foods = ["Kimchi", "Bibimbap", "Tteokbokki", "Bulgogi", "Samgyeopsal", "Jajangmyeon", "Sundae", "Gimbap", "Banchan", "Hotteok"]
drinks = ["Soju", "Makgeolli", "Bokbunja", "Omija", "Barley Tea", "Yuja Tea", "Peach Juice", "Rice Punch", "Citron Tea", "Ginger Tea"]

# Prices for food and drinks (Example prices in won)
food_prices = {
    "Kimchi": 5000, "Bibimbap": 8000, "Tteokbokki": 7000, "Bulgogi": 12000, "Samgyeopsal": 15000,
    "Jajangmyeon": 9000, "Sundae": 6000, "Gimbap": 5000, "Banchan": 4000, "Hotteok": 3000
}

drink_prices = {
    "Soju": 5000, "Makgeolli": 4000, "Bokbunja": 6000, "Omija": 5000, "Barley Tea": 3000,
    "Yuja Tea": 3500, "Peach Juice": 4000, "Rice Punch": 3000, "Citron Tea": 3500, "Ginger Tea": 3000
}

# Function to take an order
def take_order():
    print("\nWelcome to Kimchi Cafe! 🍽️")
    print("Here is our Menu:\n")

    print("🥘 Food Menu:")
    for index, food in enumerate(foods, start=1):
        print(f"{index}. {food} - {food_prices[food]} won")

    print("\n🥤 Drinks Menu:")
    for index, drink in enumerate(drinks, start=1):
        print(f"{index}. {drink} - {drink_prices[drink]} won")

    # Let customer choose food
    while True:
        try:
            food_choice = int(input("\nEnter the number of the food you want: "))
            if 1 <= food_choice <= len(foods):
                selected_food = foods[food_choice - 1]
                break
            else:
                print(" Invalid choice. Please select a valid number.")
        except ValueError:
            print(" Please enter a valid number.")

    # Let customer choose drink
    while True:
        try:
            drink_choice = int(input("Enter the number of the drink you want: "))
            if 1 <= drink_choice <= len(drinks):
                selected_drink = drinks[drink_choice - 1]
                break
            else:
                print("❌ Invalid choice. Please select a valid number.")
        except ValueError:
            print("❌ Please enter a valid number.")

    # Generate a random order number
    order_number = random.randint(1000, 9999)

    print("\n Your order has been placed!")
    print(f" Order Number: {order_number}")
    print(f" Food: {selected_food} - {food_prices[selected_food]} won")
    print(f" Drink: {selected_drink} - {drink_prices[selected_drink]} won")

    # Calculate total amount
    total_amount = food_prices[selected_food] + drink_prices[selected_drink]

    return order_number, selected_food, selected_drink, total_amount

# Function to process payment
def process_payment(total_amount):
    print("\n💳 Choose your payment method:")
    payment_type = input("Enter 'online' for online payment or 'cash' for cash: ").strip().lower()

    # Validate input
    while payment_type not in ["online", "cash"]:
        print("❌ Invalid payment method. Please choose 'online' or 'cash'.")
        payment_type = input("Enter 'online' for online payment or 'cash' for cash: ").strip().lower()

    # Apply discount for online payments
    if payment_type == "online":
        discount = total_amount * 0.2  # 20% discount
        total_amount -= discount
        print(f"\n💰 Thank you for paying online! You've received a 20% discount.")

    print(f"\n💵 Total amount to be paid: {total_amount} won")
    print("\n✅ Payment successful! Enjoy your meal! 🍽️")

# Main function to simulate customer experience
def main():
    order_number, food, drink, total_amount = take_order()  # Take order

    print("\n Generating your bill...")
    print(f" Order Number: {order_number}")
    print(f" Food: {food},  Drink: {drink}")
    print(f" Total Price: {total_amount} won")

    # Process payment
    process_payment(total_amount)

    # Prevent VS Code from closing immediately
    input("\nPress Enter to exit...")

# Run the main function
if __name__ == "__main__":
    main()