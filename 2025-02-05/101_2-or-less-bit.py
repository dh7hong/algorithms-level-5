def solution(numbers):
    result = []  # Initialize an empty list to store results
    
    for num in numbers:
        # Step 1: Compute XOR to find differing bits between num and num + 1
        xor_value = num ^ (num + 1)

        # Step 2: Shift right by 2 to adjust changes 
        # (this effectively ensures at most 2 bit changes)
        adjustment = xor_value >> 2

        # Step 3: Compute the final result
        next_number = num + 1 + adjustment

        # Step 4: Append the computed value to the result list
        result.append(next_number)
    
    return result  # Return the final list of results

print(solution([2, 7]))