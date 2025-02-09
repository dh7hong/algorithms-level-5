def solution(x, y, n):
    # If x is already y, no operations are needed
    if x == y:
        return 0

    # Use a list as a queue (Breadth-First Search queue)
    queue = [(x, 0)]  # Each element is (current value, steps)
    visited = set()  # Set to track visited numbers
    front = 0  # Using an index instead of pop(0) for efficiency

    print("\n### STARTING BFS ###")
    print(f"Initial queue: {queue}")
    print(f"Initial visited: {visited}\n")

    while front < len(queue):
        current, steps = queue[front]  # Get the front of the queue
        front += 1  # Move front pointer (instead of pop(0))

        print(f"Processing: current = {current}, steps = {steps}")
        
        # Try all operations
        for next_num in (current + n, current * 2, current * 3):
            print(f"  Trying next_num = {next_num} (from {current})")

            # If we reach y, return the number of steps taken
            if next_num == y:
                print(f"  [CHECK] Found target {y} in {steps + 1} steps!\n")
                return steps + 1
            
            # If next number is within range and not visited, add to queue
            if next_num < y and next_num not in visited:
                visited.add(next_num)
                queue.append((next_num, steps + 1))
                print(f"  [ADD] Adding {next_num} to queue, new queue: {queue}")

        print(f"  Updated visited set: {visited}\n")

    # If we exhaust all possibilities and never reach y
    print("Target not reachable\n")
    return -1

# Example test cases
print("Result:", solution(10, 40, 5))  
print("Result:", solution(10, 40, 30))  
print("Result:", solution(2, 5, 4))  
