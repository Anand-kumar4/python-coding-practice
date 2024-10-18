# Reverse a string without using built-in functions.


# Function to reverse a string
def reverse_string(input_string):

# Create an empty string
    reversed_string = ""

#looping through the entire string starting from the last index. Appending the value to the empty string created
    for i in range(len(input_string) - 1, -1, -1):
        reversed_string += input_string[i]

# return the reverse string
    return reversed_string


input_str = 'Anand Kumar'
reversed_str = reverse_string(input_str)
print("Original String: ", input_str)
print("Reversed String: ", reversed_str)