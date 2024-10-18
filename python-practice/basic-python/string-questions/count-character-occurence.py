""" Count the Occurrences of a Character in a String
- Write a program to count how many times a specific character appears in a string.
- Variation: Count occurrences of multiple characters. """

def count_character_occurence(s, char):
    count = 0
    # Loop through each charcter of the string
    for c in s:
        if c == char:
            count += 1
        
    return count

# Test Case
test_string = "hello world"
character_to_count = "o"
print(f"The character '{character_to_count}' appears {count_character_occurence(test_string,character_to_count)} times in the string.")