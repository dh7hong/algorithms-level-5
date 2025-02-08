def solution(x, y, n):
    # If x is already y, no operations are needed
    if x == y:
        return 0

    # Use a list as a queue (Breadth-First Search queue)
    queue = [(x, 0)]  # Each element is (current value, steps)
    visited = set()  # Set to track visited numbers
    front = 0  # Using an index instead of pop(0) for efficiency

    while front < len(queue):
        current, steps = queue[front]  # Get the front of the queue
        front += 1  # Move front pointer (instead of pop(0))

        # Try all operations
        for next_num in (current + n, current * 2, current * 3):
            # If we reach y, return the number of steps taken
            if next_num == y:
                return steps + 1
            
            # If next number is within range and not visited, add to queue
            if next_num < y and next_num not in visited:
                visited.add(next_num)
                queue.append((next_num, steps + 1))

    # If we exhaust all possibilities and never reach y
    return -1

# Example test cases
print(solution(10, 40, 5))   # Output: 2
print(solution(10, 40, 30))  # Output: 1
print(solution(2, 5, 4))     # Output: -1
