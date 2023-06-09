# Exercise: Temperature Analyzer
#
# Write a program that analyzes a list of temperatures and provides information about them. The program should perform the following tasks:
#
# 1. Create an empty list called `temperatures`.
#
# 2. Prompt the user to enter a series of temperatures, one temperature per line. The user should enter each temperature and press Enter. To indicate that they are done entering temperatures, the user should enter a non-numeric value (such as "done" or an empty line).
#
# 3. Use a loop to read each input temperature and append it to the `temperatures` list.
#
# 4. After the user finishes entering temperatures, analyze the list and provide the following information:
#    - Calculate and print the average temperature.
#    - Find and print the maximum temperature.
#    - Find and print the minimum temperature.
#    - Determine and print the number of temperatures above a certain threshold. Prompt the user to enter the threshold temperature.
#
# 5. Print the list of temperatures.
#
# Example Output:
#
# Enter a temperature (or enter a non-numeric value to finish): 25.5
# Enter a temperature (or enter a non-numeric value to finish): 20.3
# Enter a temperature (or enter a non-numeric value to finish): 18.9
# Enter a temperature (or enter a non-numeric value to finish): 23.1
# Enter a temperature (or enter a non-numeric value to finish): done
#
# Average temperature: 21.95
# Maximum temperature: 25.5
# Minimum temperature: 18.9
# Enter a threshold temperature: 22.0
# Number of temperatures above 22.0: 2
#
# List of temperatures: [25.5, 20.3, 18.9, 23.1]
#
# Note: The numbers entered should be treated as floating-point values for accurate calculations.

temperature = []  # creating a list

while True:
    add = input('Enter a temperature: ')  # asking for input -> entering temperatures

    try:
        temperature.append(float(add))  # added temps are added to the list and the string is converted to float
    except ValueError:  # if the input is no number, the loop stops
        break

sumOfTemp = sum(temperature)
countTemp = len(temperature)

aveTemp = sumOfTemp / countTemp  # calculating average temperature

print('The average Temperature is: ', aveTemp)
print('The highest Temperature is: ', max(temperature))  # finding the max value in the temp list
print('The lowest Temperature is: ', min(temperature))  # finding the min value in the temp list
