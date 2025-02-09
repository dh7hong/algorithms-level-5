def solution(numbers):
    # Convert numbers to strings so we can compare them
    str_numbers = list(map(str, numbers))

    # Custom sorting using a lambda function
    str_numbers.sort(key=lambda x: x * 3, reverse=True)

    # Join all sorted numbers into a single string
    answer = "".join(str_numbers)

    # If the result starts with "0" (like [0, 0, 0]), return "0"
    return "0" if answer[0] == "0" else answer

# Example test cases
print(solution([6, 10, 2]))  # Output: "6210"
print(solution([3, 30, 34, 5, 9]))  # Output: "9534330"
print(solution([0, 0, 0, 0]))  # Output: "0"
print(solution([1, 100, 1000, 10, 101]))  # Output: "11011001000"
