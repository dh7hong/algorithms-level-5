def solution(numbers):
    result = []  # Initialize an empty list to store results
    
    print("\n### STARTING COMPUTATION ###\n")
    
    for num in numbers:
        print(f"Processing num = {num} (binary: {bin(num)})")

        # Step 1: Compute XOR to find differing bits between num and num + 1
        xor_value = num ^ (num + 1)
        print(f"  XOR with (num+1): {xor_value} (binary: {bin(xor_value)})")

        # Step 2: Shift right by 2 to adjust changes 
        adjustment = xor_value >> 2
        print(f"  Adjustment after >> 2: {adjustment} (binary: {bin(adjustment)})")

        # Step 3: Compute the final result
        next_number = num + 1 + adjustment
        print(f"  Computed next_number: {next_number} (binary: {bin(next_number)})\n")

        # Step 4: Append the computed value to the result list
        result.append(next_number)
    
    print("### COMPUTATION FINISHED ###\n")
    
    return result  # Return the final list of results

# Example test case
print("Final Result:", solution([2, 7]))
