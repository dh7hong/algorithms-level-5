def solution(number, k):
    stack = []  # This will store our answer in progress

    for digit in number:  # Go through each digit in the number
        # Remove smaller digits if we still have deletions left (k > 0)
        while stack and k > 0 and stack[-1] < digit:
            stack.pop()  # Remove the last (smallest) digit
            k -= 1  # Reduce the count of deletions
        
        stack.append(digit)  # Add the current digit to the stack

    # If we still have deletions left, remove from the end
    return ''.join(stack[:-k] if k else stack)  
    # Return the final answer as a string

# Example test cases
print(solution("1924", 2))       # Output: "94"
print(solution("1231234", 3))    # Output: "3234"
print(solution("4177252841", 4)) # Output: "775841"