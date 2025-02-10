from itertools import permutations

def is_prime(n):
    """Check if a number is a prime number."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  # Check divisibility up to sqrt(n)
        if n % i == 0:
            return False  # Not a prime number
    return True

def solution(numbers):
    """Find how many unique prime numbers can be formed from the given digits."""
    num_set = set()  # Use a set to avoid duplicate numbers
    
    # Generate all possible numbers using permutations
    for i in range(1, len(numbers) + 1):  # Try different lengths of permutations
        for perm in permutations(numbers, i):  # Get all orderings of length i
            num = int("".join(perm))  # Convert tuple to integer
            num_set.add(num)  # Store unique numbers

    # Count how many of these numbers are prime (expanded loop version)
    count = 0  # Initialize prime count
    for num in num_set:
        if is_prime(num):  # Check if the number is prime
            count += 1  # Increment count if prime
            
    return count  # Return the total count of prime numbers

# Example Test Cases
print(solution("17"))   # Output: 3 (Prime numbers: 7, 17, 71)
print(solution("011"))  # Output: 2 (Prime numbers: 11, 101)
