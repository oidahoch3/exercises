# Exercise: Word Frequency Counter
#
# Write a program that analyzes a paragraph of text and counts the frequency of each word. The program should perform
# the following tasks:
#
# 1. Prompt the user to enter a paragraph of text. The user should enter the entire paragraph and press Enter.
#
# 2. Split the paragraph into a list of words, excluding any punctuation marks and converting all words to lowercase.
#
# 3. Create an empty dictionary called `word_frequency`.
#
# 4. Iterate over each word in the list of words. If the word is already a key in the `word_frequency` dictionary,
# increment its value by 1. If the word is not a key, add it to the dictionary with an initial value of 1.
#
# 5. Sort the `word_frequency` dictionary in descending order based on the frequency of the words.
#
# 6. Print the word frequency in the following format:
#    - Each line should display a word followed by a colon and the frequency of that word.
#    - Words should be displayed in descending order based on frequency.
#
# Example Output:
#
# Enter a paragraph of text:
# "The cat and the dog are friends. The dog chases the cat."
#
# Word Frequency:
# the: 3
# cat: 2
# dog: 2
# and: 1
# are: 1
# chases: 1
# friends: 1
#
# Note: The program should treat words as case-insensitive, meaning "The" and "the" should be considered the same word.
# Punctuation marks should be excluded from word counting.

import string

paragraph = input('Enter a paragraph:').lower()  # asking for input and convert all to lowercase
stripped_paragraph = paragraph.translate(str.maketrans('', '', string.punctuation))  # removing punctuation
word_list = stripped_paragraph.split()  # adding the words from the input to a list

word_frequency = {}  # creating a dict

for word in word_list:  # checking if the word is not in the dict and then create that words with counter 0
    if word not in word_frequency:
        word_frequency[word] = 0

    word_frequency[word] += 1  # increasing the number by 1 if it appears again

for word in word_frequency:  # pretty output
    print(word + ':', word_frequency[word])
