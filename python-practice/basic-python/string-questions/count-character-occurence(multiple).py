def count_multiple_characters(s, characters):
    # Initialize a dictionary to store the counts for each character.
    count_dict = {char: 0 for char in characters}

    # Loop through the string and update the counts for specified characters
    for c in s:
        if c in count_dict:
            count_dict[c] += 1
        
    return count_dict

# Test case
test_string = "hello world"
characters_to_count = ['l', 'o', 'h']
counts = count_multiple_characters(test_string, characters_to_count)

# Print the results
for char, count in counts.items():
    print(f"The character '{char}' appears {count} times in the string.")