# Define the menu of the restaurant
menu = {
    # Appetizers
    'Salad': 7.99,
    'Soup': 6.99,
    'Wings': 9.99,

    # Main Courses
    'Pizza': 10.99,
    'Burger': 8.99,
    'Pasta': 12.99,
    'Steak': 24.99,
    'Fish': 18.99,
    'Chicken': 14.99,
    'Sandwich': 11.99,

    # Desserts
    'Ice Cream': 5.99,
    'Cake': 6.99,

    # Drinks
    'Coffee': 3.99,
    'Soda': 2.99
}

def display_menu():
    """Display the restaurant menu in a formatted way"""
    print("\n" + "="*50)
    print("           WELCOME TO OUR RESTAURANT")
    print("="*50)
    print("\n🍽️  APPETIZERS:")
    appetizers = ['Salad', 'Soup', 'Wings']
    for item in appetizers:
        if item in menu:
            print(f"   {item:<12} - ${menu[item]:>5.2f}")

    print("\n🍖 MAIN COURSES:")
    mains = ['Pizza', 'Burger', 'Pasta', 'Steak', 'Fish', 'Chicken', 'Sandwich']
    for item in mains:
        if item in menu:
            print(f"   {item:<12} - ${menu[item]:>5.2f}")

    print("\n🍰 DESSERTS:")
    desserts = ['Ice Cream', 'Cake']
    for item in desserts:
        if item in menu:
            print(f"   {item:<12} - ${menu[item]:>5.2f}")

    print("\n🥤 DRINKS:")
    drinks = ['Coffee', 'Soda']
    for item in drinks:
        if item in menu:
            print(f"   {item:<12} - ${menu[item]:>5.2f}")
    print("\n" + "="*50)

def take_order():
    """Handle customer ordering process"""
    order = {}
    total = 0.0

    while True:
        try:
            item = input("\nEnter menu item to order (or 'done' to finish): ").strip().title()

            if item.lower() == 'done':
                break

            if item in menu:
                quantity = input(f"How many {item}s would you like? ").strip()
                try:
                    qty = int(quantity)
                    if qty <= 0:
                        print("Please enter a positive quantity.")
                        continue
                except ValueError:
                    print("Please enter a valid number.")
                    continue

                if item in order:
                    order[item] += qty
                else:
                    order[item] = qty

                item_total = menu[item] * qty
                total += item_total
                print(f"Added {qty} x {item} = ${item_total:.2f}")

            else:
                print("Sorry, that item is not on the menu. Please choose from the menu above.")

        except KeyboardInterrupt:
            print("\n\nOrder cancelled. Thank you for visiting!")
            return {}, 0.0

    return order, total

def display_order(order, total):
    """Display the final order summary"""
    if not order:
        print("\nNo items ordered. Thank you for visiting!")
        return

    print("\n" + "="*50)
    print("              YOUR ORDER SUMMARY")
    print("="*50)

    for item, qty in order.items():
        item_total = menu[item] * qty
        print(f"   {item:<12} x{qty:<2} - ${item_total:>6.2f}")

    print("-"*50)
    print(f"   {'Total:':<15}    ${total:>6.2f}")
    print("="*50)
    print("Thank you for your order! Enjoy your meal! 🍽️")

# Main program
if __name__ == "__main__":
    display_menu()
    order, total = take_order()
    display_order(order, total)
