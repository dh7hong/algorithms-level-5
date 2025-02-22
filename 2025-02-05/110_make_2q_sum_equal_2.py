def solution(queue1, queue2):
    total = sum(queue1) + sum(queue2)
    if total % 2 != 0:
        return -1
    target = total // 2
    n = len(queue1)
    arr = queue1 + queue2  # Combined list of both queues.
    
    i = 0         # Pointer for removing elements from the "front" of queue1.
    j = n         # Pointer for adding elements from the "front" of queue2.
    current_sum = sum(queue1)
    
    cnt = 0
    max_ops = n * 3  # A safe upper bound on the number of operations.
    
    while cnt <= max_ops:
        if current_sum == target:
            return cnt
        # If current sum is too high, remove an element from the left 
        # (simulate pop from queue1).
        if current_sum > target:
            current_sum -= arr[i % (2 * n)]
            i += 1
        # If current sum is too low, add an element from the right 
        # (simulate pop from queue2 and push to queue1).
        else:
            current_sum += arr[j % (2 * n)]
            j += 1
        cnt += 1

    return -1

# Test Case
queue1 = [3, 2, 7, 2]
queue2 = [4, 6, 5, 1]
print(solution(queue1, queue2))