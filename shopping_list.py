# Exercise: Shopping List Organizer

# Write a program that helps organize a shopping list based on categories. The program should perform the following tasks:

# Create an empty dictionary called categories.
# Create an empty list called items.
# Prompt the user to enter items for the shopping list. The user should enter each item followed by its category, separated by a comma. For example: "Apples, Fruits".
# Split the input entered by the user into an item and its corresponding category using the comma as a delimiter.
# Add the item to the items list.
# If the category already exists in the categories dictionary, append the item to the existing list. Otherwise, create a new key-value pair in the categories dictionary, where the category is the key and the value is a list containing the item.
# Repeat steps 3-6 until the user enters "done" as the item.
# Print the sorted shopping list organized by categories. For each category, print the items in that category on a separate line.
# Example Output:

# Enter an item and its category (or enter "done" to finish): Apples, Fruits
# Enter an item and its category (or enter "done" to finish): Bread, Bakery
# Enter an item and its category (or enter "done" to finish): Carrots, Vegetables
# Enter an item and its category (or enter "done" to finish): Milk, Dairy
# Enter an item and its category (or enter "done" to finish): done

# Categories:
# Bakery: Bread
# Dairy: Milk
# Fruits: Apples, Oranges
# Vegetables: Carrots

# Note: The final output should be sorted alphabetically by category.


shopping_list = {

}

while True:
    add = input('Enter item, category or done to finish:')
    if add == 'done':
        break

    item, category = add.split(', ')

    if category not in shopping_list:
        shopping_list[category] = []

    shopping_list[category].append(item)

for category in shopping_list:
    print(category, ':', ', '.join(shopping_list[category]))
