def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_numbers(numbers, num_set, current=""):
    if current:
        num_set.add(int(current))
    for i in range(len(numbers)):
        generate_numbers(numbers[:i] + numbers[i+1:], num_set, current + numbers[i])

def solution(numbers):
    num_set = set()
    generate_numbers(list(numbers), num_set)
    return sum(is_prime(num) for num in num_set)

# Example Test Cases
print(solution("17"))   # Output: 3 (Prime numbers: 7, 17, 71)
print(solution("011"))  # Output: 2 (Prime numbers: 11, 101)
