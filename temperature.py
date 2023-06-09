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

temperatures = []  # creating a list

while True:
    add = input('Enter a temperature: ')  # asking for input -> entering temperatures

    try:
        temperatures.append(float(add))  # added temps are added to the list and the string is converted to float
    except ValueError:  # if the input is no number, the loop stops
        break

threshold = None  # creating threshold variable

while threshold is None:  # starting loop to ask for valid threshold input
    try:
        threshold = float(input('Enter a threshold for the temperatures: '))  # asking for threshold input
    except ValueError:  # if its not valid input, it starts the loop again
        pass

above_threshold = []  # creating a list for temps that are above the threshold

for temp in temperatures:  # checking if temps in temperatures list are above threshold
    if temp > threshold:
        above_threshold.append(temp)  # if they are, they get added to the list

sum_of_temp = sum(temperatures)  # getting the sum of all the entered temps
count_of_temp = len(temperatures)  # getting the amount of how many values are in the list

avg_temp = sum_of_temp / count_of_temp  # calculating average temperature

print('The average Temperature is:', avg_temp)
print('The highest Temperature is:', max(temperatures))  # finding the max value in the temp list
print('The lowest Temperature is:', min(temperatures))  # finding the min value in the temp list
print('Number of temperatures above', str(threshold) + ':',
      len(above_threshold))  # printing the length of my above_threshold list
