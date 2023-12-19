import os
import nltk
import PyPDF2
from docx import Document
from nltk.stem import PorterStemmer


def preprocess_text(text):
    # Tokenize the text into individual words
    words = nltk.word_tokenize(text)

    # Initialize a PorterStemmer for word stemming
    stemmer = PorterStemmer()

    # Perform stemming on each word
    stemmed_words = [stemmer.stem(word) for word in words]

    # Join the stemmed words back into a single string
    preprocessed_text = " ".join(stemmed_words)

    return preprocessed_text

def knuth_morris_pratt(text, pattern):
    # Preprocess the text and pattern
    text = preprocess_text(text)
    pattern = preprocess_text(pattern)

    # Calculate the longest proper suffix that is also a prefix for the pattern
    prefix_suffix_table = [0] * len(pattern)
    j = 0

    for i in range(1, len(pattern)):
        if pattern[i] == pattern[j]:
            j += 1
            prefix_suffix_table[i] = j
        else:
            if j != 0:
                j = prefix_suffix_table[j - 1]
                i -= 1
            else:
                prefix_suffix_table[i] = 0

    # Perform pattern matching using the Knuth-Morris-Pratt algorithm
    i = 0
    j = 0
    common_words = 0

    while i < len(text) and j < len(pattern):
        if text[i] == pattern[j]:
            i += 1
            j += 1
            common_words += 1
        else:
            if j != 0:
                j = prefix_suffix_table[j - 1]
            else:
                i += 1

    # Calculate the plagiarism level
    plagiarism_level = (common_words / len(pattern)) * 100

    return plagiarism_level



# Read the contents of file1
with open('mycode1.py', 'r') as file1:
    text1 = file1.read()

# Read the contents of file2
with open('mycode2.py', 'r') as file2:
    text2 = file2.read()

# Calculate the plagiarism level between file1 and file2
plagiarism_level = knuth_morris_pratt(text1, text2)
print(f"Plagiarism Level: {plagiarism_level}%")
