def is_safe(place):
    # Directions for checking adjacent and diagonal positions
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    diagonals = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    knights_moves = [(-2, 0), (2, 0), (0, -2), (0, 2)]
    
    # Iterate through the 5x5 grid
    for r in range(5):
        for c in range(5):
            if place[r][c] == 'P':  # Found a participant
                # Check adjacent positions
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < 5 and 0 <= nc < 5 and place[nr][nc] == 'P':
                        return 0  # Direct neighbor is a participant (violation)
                
                # Check diagonal positions
                for dr, dc in diagonals:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < 5 and 0 <= nc < 5 and place[nr][nc] == 'P':
                        # Ensure an 'X' is blocking the diagonal path
                        if not (place[r][nc] == 'X' and place[nr][c] == 'X'):
                            return 0  # No partition, violation
                
                # Check two-space distance (knight's move)
                for dr, dc in knights_moves:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < 5 and 0 <= nc < 5 and place[nr][nc] == 'P':
                        # Ensure the middle cell is an 'X' (partition)
                        if place[r + dr // 2][c + dc // 2] != 'X':
                            return 0  # No partition, violation
    
    return 1  # If all checks pass, the room is safe

def solution(places):
    return [is_safe(place) for place in places]
