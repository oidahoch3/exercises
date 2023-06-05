# Exercise: Number Classifier
#
# Write a program that classifies a list of numbers based on their properties. The program should perform the following tasks:
#
# 1. Create an empty list called `numbers`.
#
# 2. Prompt the user to enter a series of numbers, one number per line. The user should enter each number and press Enter. To indicate that they are done entering numbers, the user should enter a non-numeric value (such as "done" or an empty line).
#
# 3. Use a loop to read each input number and append it to the `numbers` list.
#
# 4. After the user finishes entering numbers, classify each number in the list according to the following rules:
#    - If the number is positive and divisible by 2, append it to a list called `even_numbers`.
#    - If the number is positive and not divisible by 2, append it to a list called `odd_numbers`.
#    - If the number is negative, append it to a list called `negative_numbers`.
#    - If the number is zero, append it to a list called `zero_numbers`.
#
# 5. Print the lists of numbers:
#    - Print the `even_numbers` list.
#    - Print the `odd_numbers` list.
#    - Print the `negative_numbers` list.
#    - Print the `zero_numbers` list.
#
# Example Output:
#
# Enter a number (or enter a non-numeric value to finish): 5
# Enter a number (or enter a non-numeric value to finish): -3
# Enter a number (or enter a non-numeric value to finish): 0
# Enter a number (or enter a non-numeric value to finish): 10
# Enter a number (or enter a non-numeric value to finish): done
#
# Even numbers: [10]
# Odd numbers: [5]
# Negative numbers: [-3]
# Zero numbers: [0]
#
# Note: The numbers should be classified and stored in the respective lists based on the given rules.

numbers = []
even_numbers = []
odd_numbers = []
negative_numbers = []
zero_numbers = []

while True:
    add = input('enter a number or done to finish: ')

    try:
        numbers.append(int(add))
    except ValueError:
        break

    if add == '0':
        zero_numbers.append(add)

print(zero_numbers)
