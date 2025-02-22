def solution(queue1, queue2):
    # Convert lists to queues (using list operations)
    q1 = queue1[:]
    q2 = queue2[:]
    
    # Calculate the sum of both queues
    sum1 = sum(q1)
    sum2 = sum(q2)
    
    # Total sum of both queues
    total = sum1 + sum2
    
    # If total sum is odd, we can never split it evenly
    if total % 2 != 0:
        return -1
    
    target = total // 2  # The desired sum for each queue
    
    # Use two pointers to track movements
    count = 0  # Number of operations performed
    
    # Max operations allowed to avoid infinite loops (sum of both lengths * 2)
    max_operations = (len(q1) + len(q2)) * 2
    
    # Two pointers
    i, j = 0, 0  # Start from both queues
    
    # Process while within max operations
    while count <= max_operations and i < len(q1) + len(q2) and j < len(q1) + len(q2):
        if sum1 == target:
            return count  # Found the answer
        
        if sum1 > target:
            # Move element from queue1 to queue2
            if i < len(q1):
                val = q1[i]  # Access element directly
                sum1 -= val
                sum2 += val
                q2.append(val)
                i += 1
        else:
            # Move element from queue2 to queue1
            if j < len(q2):
                val = q2[j]  # Access element directly
                sum2 -= val
                sum1 += val
                q1.append(val)
                j += 1
        
        count += 1  # Increase operation count
    
    return -1  # If no solution is found
