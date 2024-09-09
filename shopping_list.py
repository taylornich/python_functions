# question 2 task 1

shopping_list = []

choice = input("Would you like to add an item to your shopping list? yes or no ")
while choice == "yes":
    item = input("What would you like to add to your shopping list? (type quit to exit)")
    if item != "quit":
        shopping_list.append(item)
    else:
        break


# question 2 task 2

choice2 = input("Would you like to remove items from your shopping list? (yes or no)")

while choice == "yes":
    item = input("What would you like to remove?")
    if item != "quit":
        if item in shopping_list:
            shopping_list.remove(item)
        else:
            print(f"{item} not in shopping list.")
    else:
        break

# question 2 task 3
print("Current shopping list: ")
for item in shopping_list:
    print(item)
    print()