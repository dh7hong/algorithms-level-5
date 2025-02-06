def solution(numbers, target):
    count = 0  # Variable to count valid target sums

    def search_target_number(index, current_sum):
        """ 
        Recursive function that explores all possible ways to reach the target number.
        
        Args:
        index (int): The current position in the numbers list.
        current_sum (int): The accumulated sum from previous operations.

        """
        nonlocal count  # Allow modification of count variable
        if index == len(numbers):  # Base case: If all numbers are used
            if current_sum == target:  # Check if we reached the target
                count += 1  # Increment count if condition is met
            return  # Stop recursion

        # Recursive cases:
        # 1. Try adding the current number
        search_target_number(index + 1, current_sum + numbers[index])
        
        # 2. Try subtracting the current number
        search_target_number(index + 1, current_sum - numbers[index])

    search_target_number(0, 0)  # Start search from index 0 with an initial sum of 0
    return count  # Return the total number of valid expressions

# Example Test Cases
print(solution([1, 1, 1, 1, 1], 3))  # Expected Output: 5
print(solution([4, 1, 2, 1], 4))  # Expected Output: 2
