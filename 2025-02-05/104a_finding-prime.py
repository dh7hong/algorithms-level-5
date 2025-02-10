def is_prime(n):
    """Check if a number is a prime number."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  
        # Check divisibility up to sqrt(n)
        if n % i == 0:
            return False  
        # Not a prime number
    return True

def generate_permutations(s, path, used, num_set):
    """Recursively generate all possible number combinations."""
    if path:
        num_set.add(int("".join(path)))  
        # Convert the path to an integer and add it
    
    for i in range(len(s)):
        if not used[i]:  # If the digit is not used
            used[i] = True
            path.append(s[i])  # Add current digit to path
            generate_permutations(s, path, used, num_set)  
            # Recurse to add more digits
            path.pop()  
            # Backtrack
            used[i] = False  
            # Mark digit as unused

def solution(numbers):
    """Find how many unique prime numbers can be formed from the given digits."""
    num_set = set()  # To store unique numbers
    used = [False] * len(numbers)  # Keep track of used digits
    generate_permutations(list(numbers), [], used, num_set)  # Generate all numbers

    # Count how many of these numbers are prime
    return sum(1 for num in num_set if is_prime(num))

# Example Test Cases
print(solution("17"))   # Output: 3 (Prime numbers: 7, 17, 71)
print(solution("011"))  # Output: 2 (Prime numbers: 11, 101)

