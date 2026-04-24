# Q10. Call by Reference — List Mutations
#
# Write the following two functions:
#def add_element(lst, element):
    # .append() modifies the list in-place and returns None
    lst.append(element)

def double_elements(lst):
    # We use a loop with range and len to modify each index directly
    for i in range(len(lst)):
        lst[i] *= 2

if __name__ == "__main__":
    # 1. Create the initial list
    numbers = [1, 2, 3]
    print(f"Initial list: {numbers}")

    # 2. Add an element and print
    add_element(numbers, 4)
    print(f"After add_element(4): {numbers}")

    # 3. Double all elements and print
    double_elements(numbers)
    print(f"After double_elements: {numbers}")
#   add_element(lst, elements)

 
