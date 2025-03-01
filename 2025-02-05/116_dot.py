import math

def solution(k, d):
    count = 0
    
    # Iterate over x values from 0 to d in steps of k
    for x in range(0, d + 1, k):
        # Compute the maximum possible y value that satisfies x^2 + y^2 ≤ d^2
        max_y = math.floor(math.sqrt(d**2 - x**2)) // k
        # Add the number of valid (x, y) points for this x value
        count += (max_y + 1)
    
    return count

# Test Cases
print(solution(2, 4))  # Expected output: 6
print(solution(1, 5))  # Expected output: 26