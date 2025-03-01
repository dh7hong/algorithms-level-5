def compute_gcd(a, b):
    """Finds the GCD of two numbers using the Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return a

def find_gcd(arr):
    """Finds the GCD of an array without using reduce or gcd."""
    result = arr[0]
    for num in arr[1:]:
        result = compute_gcd(result, num)
        if result == 1:  # Early exit: GCD is already at its minimum possible value
            return 1
    return result

def is_valid_divisor(divisor, arr):
    """Checks if divisor does NOT divide any element in arr."""
    for num in arr:
        if num % divisor == 0:
            return False
    return True

def solution(arrayA, arrayB):
    # Compute the GCD of each array manually
    gcdA = find_gcd(arrayA)
    gcdB = find_gcd(arrayB)
    
    # Check if gcdA satisfies the first condition
    validA = gcdA if is_valid_divisor(gcdA, arrayB) else 0
    # Check if gcdB satisfies the second condition
    validB = gcdB if is_valid_divisor(gcdB, arrayA) else 0
    
    # Return the maximum valid value, or 0 if neither is valid
    return max(validA, validB)

# Example test cases
print(solution([10, 17], [5, 20]))  # Output: 0
print(solution([10, 20], [5, 17]))  # Output: 10
print(solution([14, 35, 119], [18, 30, 102]))  # Output: 7
