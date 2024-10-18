""" Check if a String is a Palindrome
- Write a function to check if a string reads the same forward and backward.
- Variation: Ignore spaces, punctuation, and case. """
import string


# Function to preprocess the string before checking palindrome
def preprocess_string(s):
    # Remove special characters and convert it to lower case
    return ''.join(char.lower() for char in s if char.isalnum())

def is_palindrome(s):
    cleaned_string = preprocess_string(s)

    # Step 1: Initialize two pointers
    left = 0
    right = len(cleaned_string) - 1 # Start at the last character of the string

    # Step 2: Loop until the two pointers meet or cross each other
    while left < right:
        # Step 3: Compare characters at left and right pointers
        if cleaned_string[left] != cleaned_string[right]:
            return False # If characters are different then it is not a palindrome
        
        # Step 4: Mobe the pointers inward
        left += 1 # Move the left pointer one step towards right
        right -= 1 #Move the right pointer one step towards left
    
    return True


# Test cases
""" test1 = "madam"
test2 = "race car"
test3 = "hello" """

test1 = "A man, a plan, a canal, Panama!"
test2 = "No lemon, no melon"
test3 = "Hello, World!"

print(f"Is '{test1}' a palindrome? {is_palindrome(test1)}")
print(f"Is '{test2}' a palindrome? {is_palindrome(test2)}")
print(f"Is '{test3}' a palindrome? {is_palindrome(test3)}")

