print("\nWelcome to MnH! I'm Aahana, the chatbot that will be assisting you with your refund today.\n")
name = input("What is your name? ")

# Ensure a valid number of items is entered
while True:
    amount_str = input(f"\nHello {name}, what is the number of items you wish to return? ")
    if amount_str.isdigit():  # Check if input is a valid number
        amount = int(amount_str)
        if amount > 0:
            break
        else:
            print("\nYou must enter a number greater than 0.")
    else:
        print("\nPlease enter a valid number.")

# Ensure item names are correctly formatted
while True:
    item_names = input("\nGreat! What are the names of the items? Please separate each item name with a comma: ")
    items_list = [item.strip() for item in item_names.split(",")]  # Strip spaces
    if len(items_list) == amount:
        break
    else:
        print(f"\nThe number of items entered ({len(items_list)}) does not match the expected amount ({amount}). Please try again.")

# Ensure order numbers are correctly formatted
while True:
    order_numbers = input("\nAwesome! What is the order number of each item? Please separate each order number with a comma: ")
    order_list = [order.strip() for order in order_numbers.split(",")]  # Strip spaces
    if len(order_list) == amount:
        break
    else:
        print(f"\nThe number of order numbers entered ({len(order_list)}) does not match the number of items ({amount}). Please try again.")

# Ask for the reason for each return one by one
reasons = {}
for i in range(amount):
    reason = input(f"\nWhat is the reason for returning '{items_list[i]}'? ")
    reasons[items_list[i]] = reason  # Store reason for each item

print("\nThank you for providing the return reasons!\n")

# Proof of purchase selection with validation loop
while True:
    print("Lastly, please choose from the menu below by entering the number of your selected proof of purchase:\n")
    choice = input("1. Credit Card\n2. Debit Card\n3. Receipt\n4. Rewards Program\n\nYour choice: ")

    if choice == "1":
        credit = input("\nPlease enter the last 4 digits of the credit card used: ")
        break
    elif choice == "2":
        debit = input("\nPlease enter the last 4 digits of the debit card used: ")
        break
    elif choice == "3":
        receipt = input("\nPlease enter the receipt number: ")
        break
    elif choice == "4":
        program = input("\nPlease enter the email used for the rewards program: ")
        break
    else:
        print("\nThis is not a valid form of proof of purchase. Please try again.")

print("\nYour return has been processed. Have a good day!\n")
