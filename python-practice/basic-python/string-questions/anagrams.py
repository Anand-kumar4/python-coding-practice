""" Check if Two Strings are Anagrams
- Write a function to check if two strings are anagrams.
- Variation: Consider case-insensitivity and ignore spaces/punctuation.""" 

import string

def preprocess_string(s):
    # Remove spaces and punctuations, and convert it to lower case
    return ''.join(char.lower() for char in s if char.isalnum())

def count_character_frequencies(s):
    # Create a dictionary to store character frequencies
    frequency = {}

    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

def are_anagrams(str1, str2):
    # Preprocess both strings
    str1 = preprocess_string(str1)
    str2 = preprocess_string(str2)

    # If the length of the processed strings are not equal, they are not anagrams
    if len(str1) != len(str2):
        return False
    
    # Count the frequencies of characters in both strings
    freq1 = count_character_frequencies(str1)
    freq2 = count_character_frequencies(str2)

    # Compare the frequency dictionaries
    return freq1 == freq2

# Test cases
str1 = "A man, a plan, a canal: Panama"
str2 = "A canal, a plan, a man: Panama"

if are_anagrams(str1, str2):
    print(f"'{str1}' and '{str2}' are anagrams.")
else:
    print(f"'{str1}' and '{str2}' are not anagrams.")


