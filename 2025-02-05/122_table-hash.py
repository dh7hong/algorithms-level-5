def solution(data, col, row_begin, row_end):
    # Step 1: Sort the data based on the col-th column (ascending)
    # If there is a tie, sort by the first column (descending)
    data.sort(key=lambda x: (x[col - 1], -x[0]))

    # Step 2: Compute S_i for each row from row_begin to row_end
    hash_value = 0  # Initialize hash value
    for i in range(row_begin, row_end + 1):
        S_i = sum(value % i for value in data[i - 1])  # Compute sum of remainders
        hash_value ^= S_i  # Apply bitwise XOR

    return hash_value  # Return final hash value

data = [[2,2,6], [1,5,10], [4,2,9], [3,8,3]]
col = 2
row_begin = 2
row_end = 3

print(solution(data, col, row_begin, row_end))  # Expected output: 4

