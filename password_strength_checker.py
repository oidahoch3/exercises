# **Exercise: Password Strength Checker**
#
# Write a program that checks the strength of a password based on various criteria. The program should perform the
# following tasks:
#
# 1. Prompt the user to enter a password.
#
# 2. Define a set of rules for a strong password, such as:
#    - Minimum length of 8 characters.
#    - At least one uppercase letter.
#    - At least one lowercase letter.
#    - At least one digit (0-9).
#    - At least one special character (e.g., !, @, #, $, etc.).
#
# 3. Check the entered password against these rules and provide feedback to the user:
#    - If the password meets all the criteria, display a message indicating that it's a strong password.
#    - If the password doesn't meet one or more criteria, provide specific feedback about which criteria are not met.
#
# Example Output:
#
# Enter a password: MyP@ssw0rd
# Strong password!
#
# Enter a password: mypassword
# Password should contain at least one uppercase letter and one digit.
#
# Enter a password: !abc123
# Password should contain at least one uppercase letter and should have a minimum length of 8 characters.
#
# 4. You can go a step further and assign a "strength score" to the password based on how well it meets the criteria.
# For example, you could assign a score of 1 for each met criteria and then categorize the password based on the score.
#
# 5. Print the password's strength score and category (e.g., Weak, Moderate, Strong).
#
# Example Output:
#
# Enter a password: MyP@ssw0rd
# Password strength score: 5 (Strong)
#
# Enter a password: abc123
# Password strength score: 2 (Moderate)
#
# Enter a password: password
# Password strength score: 1 (Weak)
#
# Give it a try and see how well you can implement the password strength checking algorithm. If you have any questions
# or need further assistance, feel free to ask!

password = input('Enter a password:')

