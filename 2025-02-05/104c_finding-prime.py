from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    return all(n % i for i in range(2, int(n**0.5) + 1))

def solution(numbers):
    num_set = {int("".join(p)) for i in range(1, len(numbers) + 1) 
               for p in permutations(numbers, i)}
    return sum(is_prime(num) for num in num_set)

# Example Test Cases
print(solution("17"))   # Output: 3 (Prime numbers: 7, 17, 71)
print(solution("011"))  # Output: 2 (Prime numbers: 11, 101)