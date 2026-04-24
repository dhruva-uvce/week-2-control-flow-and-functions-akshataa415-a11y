
    # Using an f-string to format the return val
    # The ** operator is used for exponentiation in P
    # Calling greet with only the required 'name' ar   # Output: Hello, Alice!
    
    # Calling greet with both argu  # Output: 1024# Q09. Functions with Default Parameters
#
# Write the following two functions:
#
#   greet(name, greeting="Hello")
#       Returns the string: "{greeting}, {name}!"
#
#   power(base, exp=2)
#       Returns base raised to exp.
#
# Then in the main block below, call and print:
#   greet("Alice")          → "Hello, Alice!"
#   greet("Bob", "Hi")      → "Hi, Bob!"
#   power(5)                → 25
#   power(2, 10)            → 1024


def greet(name, greeting="Hello"):
    # --- YOUR CODE HERE
    return f"{greeting},{name}!"
    pass


def power(base, exp=2):
    # --- YOUR CODE HERE ---
    return base ** esp
    pass


if __name__ == "__main__":
    # Call the functions and print results
    print(greet("Alice"))
    print(greet("Bob","Hi"))
    print(power(5))
    print(power(2,10))

    pass
