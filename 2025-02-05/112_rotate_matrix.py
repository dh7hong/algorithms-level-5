def solution(rows, columns, queries):
    # Step 1: Initialize the grid with numbers from 1 to rows * columns
    matrix = [[(i - 1) * columns + j for j in range(1, columns + 1)] for i in range(1, rows + 1)]
    result = []  # Store the minimum moved number for each query

    # Step 2: Process each query
    for x1, y1, x2, y2 in queries:
        # Convert to zero-based indices
        x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1

        # Step 3: Rotate the boundary clockwise
        prev_value = matrix[x1][y1]  # Store the top-left value
        min_value = prev_value  # Track minimum value in the rotated section

        # Move left edge upwards
        for i in range(x1, x2):
            matrix[i][y1] = matrix[i + 1][y1]
            min_value = min(min_value, matrix[i][y1])

        # Move bottom edge left
        for j in range(y1, y2):
            matrix[x2][j] = matrix[x2][j + 1]
            min_value = min(min_value, matrix[x2][j])

        # Move right edge downwards
        for i in range(x2, x1, -1):
            matrix[i][y2] = matrix[i - 1][y2]
            min_value = min(min_value, matrix[i][y2])

        # Move top edge right
        for j in range(y2, y1, -1):
            matrix[x1][j] = matrix[x1][j - 1]
            min_value = min(min_value, matrix[x1][j])

        # Restore the saved top-left value into its new position
        matrix[x1][y1 + 1] = prev_value

        # Step 4: Store the minimum value found
        result.append(min_value)

    return result

 