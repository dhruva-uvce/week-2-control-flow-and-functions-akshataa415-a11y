# Q08. Sum of Digits (while loop)
#
# Ask the user for a positive integer.
# Print the sum of its digits using a while loop.
#
# Sample Input:   Enter a number: 9876
# Sample Output:  Sum of digits of 9876 = 30

# --- YOUR CODE HERE ---
#Ask the user for a positive integer
num_str = input("Enter a number: ")
num = int(num_str)
original_num = num

sum_digits = 0

# Use a while loop to process each digit
while num > 0:
    digit = num % 10      # Get the last digit
    sum_digits += digit   # Add it to the sum
    num = num // 10       # Remove the last digit using integer division

# Print the result matching the sample output format
print(f"Sum of digits of {original_num} = {sum_digits}")
