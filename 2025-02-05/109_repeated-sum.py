def solution(sequence, k):
    left, right = 0, 0  # Two pointers to maintain the window
    current_sum = sequence[0]  # Initial sum with the first element
    best_range = None  # Store the best (start, end) range

    while right < len(sequence):
        if current_sum == k:  
            # Found a valid subarray
            if best_range is None or (right - left) < (best_range[1] - best_range[0]):
                best_range = (left, right)  # Update best range
            elif (right - left) == (best_range[1] - best_range[0]) and left < best_range[0]:
                best_range = (left, right)  # Prioritize the earlier one
            
        if current_sum >= k:
            # Shrink from the left to reduce the sum
            current_sum -= sequence[left]
            left += 1
        else:
            # Expand window to the right
            right += 1
            if right < len(sequence):  # Ensure right doesn't go out of bounds
                current_sum += sequence[right]

    return [best_range[0], best_range[1]]


print(solution([1, 2, 3, 4, 5], 7))  # Output: [2, 3]
print(solution([1, 1, 1, 2, 3, 4, 5], 5))  # Output: [6, 6]
print(solution([2, 2, 2, 2, 2], 6))  # Output: [0, 2]