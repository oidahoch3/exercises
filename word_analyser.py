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
    word = input('Enter a word: ')  # asking for input

    if word == '':  # if the input equals '', the while loop breaks
        break

    words.append(word)  # the input is added to the words list

vowel_list = []  # creating a list where all the words that start with a vowel will be added
vowel = ['a', 'e', 'i', 'o', 'u']  # creating a list with all vowels to check the words against that
for index in words:  # checking all the words ind the words list
    if index[0].lower() in vowel:  # if the first letter (indicated by the [0]) is a vowel,
        # the word will be added to the list.
        # .lower() converts everything to lowercase
        vowel_list.append(index)

print('List of words:', ', '.join(words))  # printing the results
print('Longest word:', max(words, key=len))
print('Shortest word:', min(words, key=len))
print('Number of words starting with a vowel:', len(vowel_list))
