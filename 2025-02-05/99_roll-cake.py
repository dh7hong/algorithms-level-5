def solution(topping):
    # Use a set to track unique toppings on both sides
    left_toppings = set()  
    # Unique toppings on the left side
    right_toppings = {}  
    # Dictionary to count occurrences of 
    # toppings on the right side

    # Initialize right_toppings with full topping list
    for t in topping:
        if t in right_toppings:
            right_toppings[t] += 1
        else:
            right_toppings[t] = 1

    count = 0  
    # Count of valid splits

    # Iterate through the topping list to make splits
    for i in range(len(topping) - 1):  # Exclude last index to ensure a split
        t = topping[i]

        # Add topping to left side
        left_toppings.add(t)

        # Remove topping from right side (decrease count)
        right_toppings[t] -= 1
        if right_toppings[t] == 0:  
            # If no more of that topping in right side, remove from dictionary
            del right_toppings[t]

        # If both sides have the same number of unique toppings, 
        # it's a valid split
        if len(left_toppings) == len(right_toppings):
            count += 1

    return count

# Example test cases
print(solution([1, 2, 1, 3, 1, 4, 1, 2]))  # Output: 2
print(solution([1, 2, 3, 1, 4]))  # Output: 0