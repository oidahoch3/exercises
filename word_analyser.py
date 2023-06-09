# Exercise: Word Analyzer
#
# Write a program that analyzes a list of words and provides information about them. The program should perform the following tasks:
#
# 1. Create an empty list called `words`.
#
# 2. Prompt the user to enter a series of words, one word per line. The user should enter each word and press Enter. To indicate that they are done entering words, the user should enter a non-alphabetic value (such as "done" or an empty line).
#
# 3. Use a loop to read each input word and append it to the `words` list.
#
# 4. After the user finishes entering words, analyze the list and provide the following information:
#    - Find and print the longest word.
#    - Find and print the shortest word.
#    - Determine and print the number of words that start with a vowel (a, e, i, o, u).
#
# 5. Print the list of words.
#
# Example Output:
#
# Enter a word (or enter a non-alphabetic value to finish): hello
# Enter a word (or enter a non-alphabetic value to finish): programming
# Enter a word (or enter a non-alphabetic value to finish): python
# Enter a word (or enter a non-alphabetic value to finish): done
#
# Longest word: programming
# Shortest word: hello
# Number of words starting with a vowel: 2
#
# List of words: ['hello', 'programming', 'python']
#
# Note: The words should be treated as case-sensitive, and only consider English alphabets for vowel identification.

words = []

while True:
    word = input('Enter a word: ')

    if word == '':
        break

    words.append(word)

print('Longest word', max(words, key=len))
