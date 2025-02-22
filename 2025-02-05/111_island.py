def solution(maps):
    # Determine the number of rows and columns in the grid
    rows = len(maps)
    cols = len(maps[0])
    
    # A 2D list to keep track of visited cells
    visited = [[False] * cols for _ in range(rows)]
    
    # Direction vectors for moving up, down, left, and right
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    def dfs(r, c):
        # Use a stack for DFS
        stack = [(r, c)]
        total = 0
        
        while stack:
            cur_r, cur_c = stack.pop()
            
            # Skip if this cell has been visited
            if visited[cur_r][cur_c]:
                continue
            
            # Mark the cell as visited
            visited[cur_r][cur_c] = True
            # Add the cell's food value to the total
            total += int(maps[cur_r][cur_c])
            
            # Check all adjacent cells
            for dr, dc in directions:
                nr, nc = cur_r + dr, cur_c + dc
                # Check boundaries and whether the adjacent cell is part of the island (i.e., not 'X')
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and maps[nr][nc] != 'X':
                    stack.append((nr, nc))
        
        return total
    
    island_food = []
    
    # Iterate over each cell in the grid
    for i in range(rows):
        for j in range(cols):
            # If the cell is not visited and is not sea ('X'), perform DFS to find the entire island
            if not visited[i][j] and maps[i][j] != 'X':
                island_sum = dfs(i, j)
                island_food.append(island_sum)
    
    # If no islands were found, return [-1]
    if not island_food:
        return [-1]
    
    # Return the sorted list of island food values (i.e., maximum days one can stay on each island)
    return sorted(island_food)

# Example test cases:
print(solution(["X591X","X1X5X","X231X", "1XXX1"]))  # Expected output: [1, 1, 27]
print(solution(["XXX","XXX","XXX"]))                 # Expected output: [-1]
