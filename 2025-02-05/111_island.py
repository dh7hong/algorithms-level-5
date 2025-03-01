from collections import deque

def solution(maps):
    # Determine the number of rows and columns in the grid
    rows = len(maps)
    cols = len(maps[0])
    
    # A 2D list to keep track of visited cells
    visited = [[False] * cols for _ in range(rows)]
    
    # Direction vectors for moving up, down, left, and right
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    def bfs(r, c):
        """Performs BFS to find connected components (islands) and their food values."""
        queue = deque([(r, c)])  # Use deque for BFS
        total = 0  # Track total food in the island
        
        while queue:
            cur_r, cur_c = queue.popleft()  # Pop from the left for BFS
            
            if visited[cur_r][cur_c]:  # Skip if already visited
                continue
            
            # Mark the cell as visited
            visited[cur_r][cur_c] = True
            # Add the cell's food value to the total
            total += int(maps[cur_r][cur_c])
            
            # Check all adjacent cells
            for dr, dc in directions:
                nr, nc = cur_r + dr, cur_c + dc
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and maps[nr][nc] != 'X':
                    queue.append((nr, nc))  # Add to queue for further exploration
        
        return total
    
    island_food = []
    
    # Iterate over each cell in the grid
    for i in range(rows):
        for j in range(cols):
            # If the cell is not visited and is not sea ('X'), perform BFS to find the entire island
            if not visited[i][j] and maps[i][j] != 'X':
                island_sum = bfs(i, j)
                island_food.append(island_sum)
    
    # If no islands were found, return [-1]
    return sorted(island_food) if island_food else [-1]

# Example test cases:
print(solution(["X591X","X1X5X","X231X", "1XXX1"]))  # Expected output: [1, 1, 27]
print(solution(["XXX","XXX","XXX"]))                 # Expected output: [-1]
