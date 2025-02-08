
#Question 2 Task 1
def add_item(shopping_list):
    item = input("What would you like to add to your shopping list? (type 'quit' to stop adding): ").strip()
    while item != "quit":
        shopping_list.append(item)
        item = input("What else would you like to add? (type 'quit' to stop adding): ").strip()

# Question 2 Task 2
def remove_item(shopping_list):
    item = input("What would you like to remove from your shopping list? (type 'quit' to stop removing): ").strip()
    while item != "quit":
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} has been removed from the shopping list.")
        else:
            print(f"{item} is not in the shopping list.")
        item = input("What else would you like to remove? (type 'quit' to stop removing): ").strip()

# Question 2 Task 3
def print_list(shopping_list):
    if shopping_list:
        print("\nYour shopping list:")
        for item in shopping_list:
            print(f"- {item}")
    else:
        print("Your shopping list is empty.")


def shopping_list_program():
    shopping_list = []  

    while True:
        print("\nShopping List Menu:")
        print("1. Add an item")
        print("2. Remove an item")
        print("3. Print shopping list")
        print("4. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_item(shopping_list)
        elif choice == "2":
            remove_item(shopping_list)
        elif choice == "3":
            print_list(shopping_list)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose a valid option.")

shopping_list_program()