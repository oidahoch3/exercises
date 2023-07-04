# Exercise: Text Analyzer
#
# Write a program that analyzes a paragraph of text and provides various statistics about it. The program should
# perform the following tasks:
#
# 1. Prompt the user to enter a paragraph of text. The user should enter the entire paragraph and press Enter.
#
# 2. Analyze the text and provide the following information:
#    - Count and print the number of sentences in the paragraph.
#    - Count and print the number of words in the paragraph.
#    - Calculate and print the average word length.
#    - Calculate and print the average sentence length (in terms of the number of words).
#
# 3. Identify and print the most common words in the paragraph. Display the top N words, where N is a value provided
# by the user.
#
# 4. Identify and print the longest word in the paragraph.
#
# 5. Print the paragraph in reverse order, where each sentence is reversed.
#
# Example Output:
#
# Enter a paragraph of text:
# "The quick brown fox jumps over the lazy dog. The dog barks at the fox."
#
# Number of sentences: 2
# Number of words: 15
# Average word length: 3.727272727272727
# Average sentence length: 5.5
# Most common words (top 3):
# - the: 3
# - fox: 2
# - dog: 2
# Longest word: jumps
# Reversed paragraph:
# ".god yzal eht revo spmuj xof nworb eht ta skrab god eht .god yzal eht revo spmuj xof kciuq ehT"
#
# Note: The program should handle punctuation marks and consider them as part of words. Word lengths should be
# calculated excluding any punctuation marks. The program should consider sentences as a group of words separated
# by punctuation marks (., !, ?).

import re

text = input('Enter paragraph:')  # asking for input

nr_sentences = len(re.findall(r'[^?!.][?!.]', text))  # counting sentences by counting '.?!' if they follow NOT '.?!'

words = text.split()  # splitting the input into words
word_lengths = [len(w) for w in words]  # figuring out the length of each word

avg_word_length = sum(word_lengths) / len(words)  # calculating average word length

avg_sentence_length = len(words) / nr_sentences

print('Number of sentences:', nr_sentences)
print('Number of words:', len(words))
print('Average word length:', avg_word_length)
print('Average sentence length:', avg_sentence_length)
