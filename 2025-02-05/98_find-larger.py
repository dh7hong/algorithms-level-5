def solution(numbers):
    n = len(numbers)
    result = [-1] * n  
    # Initialize the result array with -1
    stack = []  
    # Stack to store indices
    
    for i in range(n):
        # While stack is not empty and the 
        # current number is greater than numbers[stack[-1]]
        while stack and numbers[stack[-1]] < numbers[i]:
            index = stack.pop()  
            # Get the last index from the stack
            result[index] = numbers[i]  
            # Update the result array with the next greater number
        
        stack.append(i)  
        # Store the index of the current number in the stack
    
    return result

# Example test cases
print(solution([2, 3, 3, 5]))  # Output: [3, 5, 5, -1]
print(solution([9, 1, 5, 3, 6, 2]))  # Output: [-1, 5, 6, 6, -1, -1]
