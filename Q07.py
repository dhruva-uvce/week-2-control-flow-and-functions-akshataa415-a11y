# Q07. Reverse a Number (while loop)
#
# Ask the user for a positive integer.
# Print the reverse of the number using a while loop.
#
# Sample Input 1:   Enter a number: 1234
# Sample Output 1:  Reversed: 4321
#
# Sample Input 2:   Enter a number: 5000
# Sample Output 2:  Reversed: 5

# --- YOUR CODE HERE ---
# Ask the user for a positive integer
num = int(input("Enter a number: "))

reversed_num = 0

# Use a while loop to reverse the number
while num > 0:
    # Get the last digit using modulo
    digit = num % 10
    
    # Add digit to reversed_num (shifting existing digits to the left)
    reversed_num = (reversed_num * 10) + digit
    
    # Remove the last digit from num using integer division
    num = num // 10

# Print the result
print(f"Reversed : {reversed_num}")
