def solution(arr):
    # Get the size of the matrix
    n = len(arr)
    
    # This function checks if all elements in the square are the same
    def check_same(x, y, size):
        first = arr[x][y]  # The first value in the section
        for i in range(x, x + size):
            for j in range(y, y + size):
                if arr[i][j] != first:
                    return False  # Found a different number, can't compress
        return True  # All numbers are the same

    # This function recursively compresses the matrix
    def compress(x, y, size):
        # If all numbers in this part of the matrix are the same, count them
        if check_same(x, y, size):
            if arr[x][y] == 0:
                return (1, 0)  # One compressed 0, no 1s
            else:
                return (0, 1)  # One compressed 1, no 0s
        
        # Otherwise, split into 4 smaller sections and process them
        half = size // 2
        top_left = compress(x, y, half)
        top_right = compress(x, y + half, half)
        bottom_left = compress(x + half, y, half)
        bottom_right = compress(x + half, y + half, half)

        # Sum up all the 0s and 1s from the 4 parts
        zeros = top_left[0] + top_right[0] + bottom_left[0] + bottom_right[0]
        ones = top_left[1] + top_right[1] + bottom_left[1] + bottom_right[1]

        return (zeros, ones)

    # Start from the entire matrix
    return list(compress(0, 0, n))

print(solution([[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]))
print(solution([[1, 1, 1, 1, 1, 1, 1, 1], 
                [0, 1, 1, 1, 1, 1, 1, 1], 
                [0, 0, 0, 0, 1, 1, 1, 1], 
                [0, 1, 0, 0, 1, 1, 1, 1], 
                [0, 0, 0, 0, 0, 0, 1, 1], 
                [0, 0, 0, 0, 0, 0, 0, 1], 
                [0, 0, 0, 0, 1, 0, 0, 1], 
                [0, 0, 0, 0, 1, 1, 1, 1]]))