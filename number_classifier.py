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

numbers = []  # creating a list

while True:
    add = input('Enter a number or done to finish: ')  # asking for input

    try:
        numbers.append(int(add))  # if the input is an int, it will be added to the lsit
    except ValueError:  # if it is not an int, the loop breaks
        break

even_numbers = []  # creating lists
odd_numbers = []
negative_numbers = []
zero_numbers = []

for number in numbers:  # going through all the numbers in the numbers list to check for certain parameters
    if number > 0:  # checking if number is bigger than 0
        if (number % 2) == 0:  # checking if number is even (if it is dividable by 2 without 'rest')
            even_numbers.append(str(number))
        else:
            odd_numbers.append(str(number))
    elif number < 0:  # checking if the number is below 0
        negative_numbers.append(str(number))
    else:  # number is 0
        zero_numbers.append(str(number))

print('Even numbers:', ', '.join(even_numbers))  # printing results
print('Odd numbers:', ', '.join(odd_numbers))
print('Negative numbers:', ', '.join(negative_numbers))
print('Zero numbers:', ', '.join(zero_numbers))
