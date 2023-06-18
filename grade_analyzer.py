# Write a program that analyzes a list of student grades and provides various statistics. The program should perform
# the following tasks:
#
# 1. Create an empty list called `grades`.
#
# 2. Prompt the user to enter a series of grades, one grade per line. The user should enter each grade as a numeric
# value and press Enter. To indicate that they are done entering grades, the user should enter a non-numeric value
# (such as "done" or an empty line).
#
# 3. Use a loop to read each input grade and append it to the `grades` list.
#
# 4. After the user finishes entering grades, analyze the list and provide the following information:
#    - Calculate and print the average grade.
#    - Find and print the highest grade.
#    - Find and print the lowest grade.
#    - Determine and print the number of students who passed (grades greater than or equal to 60).
#    - Determine and print the number of students who failed (grades below 60).
#    - Print a histogram representation of the grades using asterisks (*). Each asterisk represents 5 grades.
#
# 5. Print the list of grades.
#
# Example Output:
#
# Enter a grade (or enter a non-numeric value to finish): 85
# Enter a grade (or enter a non-numeric value to finish): 92
# Enter a grade (or enter a non-numeric value to finish): 78
# Enter a grade (or enter a non-numeric value to finish): 65
# Enter a grade (or enter a non-numeric value to finish): done
#
# Average grade: 80.0
# Highest grade: 92
# Lowest grade: 65
# Number of students passed: 3
# Number of students failed: 1
# Histogram of grades:
# *****
# *********
# ******
# **
#
# List of grades: [85, 92, 78, 65]
#
# Note: The grades entered should be treated as numeric values for accurate calculations and comparisons.

grades = []

while True:
    grade = input('Enter grade: ')

    try:
        grade = float(grade)
    except ValueError:
        break
    grades.append(grade)

avg_grade = sum(grades) / len(grades)
highest_grade = max(grades)
lowest_grade = min(grades)
passing_grades = [grade for grade in grades if grade >= 60]
failing_grades = len(grades) - len(passing_grades)

print('The average grade is:', avg_grade)
print('The highest grade is:', highest_grade)
print('The lowest grade is:', lowest_grade)
print('Number of students who passed: ', len(passing_grades))
print('Number of students who failed: ', failing_grades)
