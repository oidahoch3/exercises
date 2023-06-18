# Certainly! Here's another exercise that builds on the previous one and introduces some additional complexity:
#
# Exercise: Palindrome Checker
#
# Write a program that checks a list of words and determines whether each word is a palindrome. A palindrome is a word
# that reads the same forwards and backwards. The program should perform the following tasks:
#
# 1. Create an empty list called `words`.
#
# 2. Prompt the user to enter a series of words, one word per line. The user should enter each word and press Enter.
# To indicate that they are done entering words, the user should enter a non-alphabetic value (such as "done" or an
# empty line).
#
# 3. Use a loop to read each input word and append it to the `words` list.
#
# 4. After the user finishes entering words, check each word in the list and determine whether it is a palindrome or
# not. Store the results in a new list called `palindromes`.
#
# 5. Print the list of palindromes.
#
# Example Output:
#
# Enter a word (or enter a non-alphabetic value to finish): radar
# Enter a word (or enter a non-alphabetic value to finish): level
# Enter a word (or enter a non-alphabetic value to finish): python
# Enter a word (or enter a non-alphabetic value to finish): done
#
# List of palindromes: ['radar', 'level']
#
# Note: The palindrome check should be case-sensitive. The program should only consider alphabetic characters when
# determining whether a word is a palindrome. Punctuation and spaces should be ignored.
#

words = []  # creating list

while True:
    word = input('Enter a word:')  # asking for input

    if word == '':  # breaking loop if no input
        break

    if not word.isdigit():  # adding word to words list if it is a string
        words.append(word)
    else:
        print('Invalid Input. Try again')  # if it is a digit, error message appears

palindromes = []

for word in words:
    if word[::-1] == word:  # checking if the reversed word is the same as word
        palindromes.append(word)  # if so, it is added to the palindrome list

print('List of palindromes:', ','.join(palindromes))  # pretty output
